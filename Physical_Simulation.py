# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Copyright (C) 2026 HongwangLu

from PySide6 import QtWidgets
from PySide6.QtCore import Qt, QThread, Signal, QTimer, QSize
from PySide6.QtGui import QFont, QTextCursor, QIcon
import subprocess
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 导入其他模块
from ui.Physical_Simulation_ui import Ui_Simulation
from Three_Body_Frame import three_body_frame
from movement_air_frame import movement_air_frame
from spinning_top_frame import spinning_top_frame
from wavefunction_superposition import wavefunction_superposition_frame
from ui.SchBlack_Hole_ui import schblack_hole_frame
from Michelson_Equal_Path_Interference import michelson_equal_path_interference_frame
from Michelson_Equal_Thickness_Interference import michelson_equal_thickness_interference_frame
from Heat_Conduction_in_a_2D_Plate import heat_conduction_in_a_2D_plate_frame

def clean_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    text = ansi_escape.sub('', text)

    # 移除可能的进度指示符（如 ⠋ ⠙ ⠹ 等）
    spinner_chars = re.compile(r'[⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏]')
    text = spinner_chars.sub('', text)

    return text.strip()


# 调用 ollama 处理 AI 回复
def get_ai_response(prompt, model="codellama:latest"):
    try:
        # 使用 subprocess 调用 ollama run
        process = subprocess.Popen(
            ["ollama", "run", model],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,  # 确保文本模式
            encoding="utf-8"  # 设置编码为 UTF-8
        )

        # 将用户输入传递给命令行工具，同时捕获 stdout 和 stderr
        stdout, stderr = process.communicate(input=prompt)

        # 清理 stderr 的控制字符并移除多余空格
        stderr_cleaned = clean_ansi_codes(stderr).strip()
        if stderr_cleaned:  # 仅在 stderr 有有效内容时打印错误信息
            print("错误信息:", stderr_cleaned)

        # 清理 stdout 的控制字符并返回
        return clean_ansi_codes(stdout.strip())
    except UnicodeDecodeError as e:
        print("编码错误:", e)
        return "AI 回复时发生编码错误"
    except Exception as e:
        print("发生错误:", e)
        return "AI 生成失败"


# AI 交流窗口类
class AIChatDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AI 交流")
        self.setMinimumSize(700, 600)

        # 布局
        layout = QtWidgets.QVBoxLayout(self)

        # 聊天显示区域
        self.chat_display = QtWidgets.QTextBrowser(self)
        layout.addWidget(self.chat_display)

        # 用户输入区域
        self.input_field = QtWidgets.QTextEdit(self)
        self.input_field.setPlaceholderText("请输入你的问题...")
        self.input_field.setFixedHeight(100)
        layout.addWidget(self.input_field)

        # 发送按钮
        self.send_button = QtWidgets.QPushButton("发送", self)
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        # 创建 AI 处理线程
        self.ai_worker = None

        # 动态显示旋转的圆圈
        self.spinner_characters = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']  # 旋转动画
        self.thinking_dots = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_thinking_message)

    def send_message(self):
        user_message = self.input_field.toPlainText().strip()
        if user_message:
            # 显示用户消息
            self.chat_display.append(f"<b>你:</b> {user_message}")
            self.input_field.clear()

            # 显示旋转的圆圈提示
            self.chat_display.append("")  # 初始为空行

            # 启动定时器进行动态显示旋转的圆圈
            self.thinking_dots = 0
            self.timer.start(200)  # 每 200 毫秒更新一次

            # 启动 AI Worker 线程
            self.start_ai_worker(user_message)

    def update_thinking_message(self):
        try:
            # 使用旋转动画的字符
            spinner = self.spinner_characters[self.thinking_dots % len(self.spinner_characters)]

            # 获取文本游标并更新文本
            cursor = self.chat_display.textCursor()

            # 移动到最后一行的开始位置
            cursor.movePosition(QTextCursor.EndOfBlock)
            cursor.movePosition(QTextCursor.StartOfBlock, QTextCursor.KeepAnchor)

            # 删除上一行的内容，并插入新的字符
            cursor.removeSelectedText()  # 清除上一行的内容
            cursor.insertText(f"{spinner}")  # 插入当前的旋转字符

            self.thinking_dots += 1
        except Exception as e:
            print(f"动态更新错误: {e}")  # 捕获动态更新中的任何错误


    def start_ai_worker(self, user_message):
        self.ai_worker = AIWorker(user_message)
        self.ai_worker.response_ready.connect(self.display_ai_response)
        self.ai_worker.error_occurred.connect(self.display_error)
        self.ai_worker.start()

    def display_ai_response(self, response):
        try:
            # 停止定时器并清理旋转的圆圈提示
            self.timer.stop()

            # 删除旋转的圆圈提示并显示 AI 回复
            cursor = self.chat_display.textCursor()
            cursor.movePosition(QTextCursor.StartOfBlock)
            cursor.movePosition(QTextCursor.Down, QTextCursor.KeepAnchor)
            cursor.removeSelectedText()

            self.chat_display.append(f"<b>AI:</b> {response}")
        except Exception as e:
            print(f"显示响应错误: {e}")

    def display_error(self, error_message):
        try:
            # 停止定时器并清理旋转的圆圈提示
            self.timer.stop()

            # 删除旋转的圆圈提示并显示错误信息
            cursor = self.chat_display.textCursor()
            cursor.movePosition(QTextCursor.StartOfBlock)
            cursor.movePosition(QTextCursor.Down, QTextCursor.KeepAnchor)
            cursor.removeSelectedText()

            self.chat_display.append(f"<b>AI:</b> 出现错误：{error_message}")
        except Exception as e:
            print(f"显示错误信息时发生问题: {e}")

    def closeEvent(self, event):
        # 确保关闭时正确清理和终止
        if self.ai_worker and self.ai_worker.isRunning():
            self.ai_worker.terminate()
        event.accept()


# AI 处理线程类
class AIWorker(QThread):
    response_ready = Signal(str)  # AI 回复信号
    error_occurred = Signal(str)  # 错误信号

    def __init__(self, user_message):
        super().__init__()
        self.user_message = user_message

    def run(self):
        try:
            # 获取 AI 回复
            response = get_ai_response(self.user_message)
            self.response_ready.emit(response)
        except Exception as e:
            self.error_occurred.emit(str(e))



class SimulationApp(QtWidgets.QMainWindow, Ui_Simulation):
    def __init__(self):
        super().__init__()

        # 领域及选项配置
        self.simulation_options = {
            "力学": ["三体运动", "抛体运动", "旋转运动"],
            "热学": ["二维板材导热展示（差分法）", "2", "3"],
            "光学": ["迈克尔逊干涉仪等倾干涉", "迈克尔逊干涉仪等厚干涉", "3"],
            "电动力学": ["选项 1", "选项 2", "选项 3"],
            "量子力学": ["一维无限深势阱波函数态叠加", "选项 2", "选项 3"],
            "统计力学": ["史瓦西黑洞下的引力透镜效应", "选项 2", "选项 3"]
        }

        self.setupUi(self)  # 先调用 UI 设置

        # 设置中央小部件
        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        # 创建一个垂直布局
        main_layout = QtWidgets.QVBoxLayout(self.central_widget)

        # 创建标题部分，显示“计算物理实验展示平台”
        self.title_label = QtWidgets.QLabel("计算物理实验学习及优秀案例展示平台", self)
        self.title_label.setAlignment(Qt.AlignCenter)  # 居中显示
        font = QFont("Arial", 38, QFont.Bold)  # 设置字体为 Arial，大小为 24，加粗
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("padding: 20px;")  # 减少padding以确保文字可见
        main_layout.addWidget(self.title_label)
        # 设置大小策略 
        self.title_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # 创建一个垂直间隔，保证标题和按钮之间的空间
        main_layout.addSpacerItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # 创建按钮并添加到布局
        self.create_simulation_buttons(main_layout)

        # 创建“AI 交流”按钮
        ai_button = QtWidgets.QPushButton("AI 交流", self.central_widget)
        ai_button.setMinimumSize(250, 80)
        ai_button.setText("AI 交流")
        ai_button.setToolTip("点击与AI进行交流")
        ai_button.clicked.connect(self.open_ai_chat)
        ai_button.setStyleSheet("""
            QPushButton {
                border-radius: 15px;
                background-color: #f0f0f0;
                font-size: 16px;
                color: #333;
                border: 2px solid #B0B0B0;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #c0c0c0;
            }
        """)
        main_layout.addWidget(ai_button)

        # 设置窗口大小
        self.setGeometry(500, 100, 1000, 900)  # 设置窗口的大小和位置

    def create_simulation_buttons(self, layout):
        domain_icons = {
            "力学": "./fig/mechanics_icon.png",
            "热学": "./fig/thermodynamics_icon.png",
            "光学": "./fig/optics_icon.png",
            "电动力学": "./fig/electrodynamics_icon.png",
            "量子力学": "./fig/quantum_icon.png",
            "统计力学": "./fig/statistics_icon.png"
        }

        for domain in self.simulation_options.keys():
            button = QtWidgets.QPushButton(self.central_widget)
            button.setMinimumSize(250, 80)
            button.setText(domain)
            button.setToolTip(f"点击选择{domain}模拟")
            icon_path = domain_icons.get(domain, "path/to/default_icon.png")  # 获取领域的图标路径
            icon = QIcon(icon_path)
            button.setIcon(icon)
            button.setIconSize(QSize(40, 40))  # 设置图标大小
            button.clicked.connect(lambda _, d=domain: self.show_simulation_options(d))
            button.setStyleSheet("""
            QPushButton {
                border-radius: 15px;
                background-color: #f0f0f0;
                font-size: 16px;
                color: #333;
                border: 2px solid #B0B0B0;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
            QPushButton:pressed {
                background-color: #c0c0c0;
            }
        """)
            layout.addWidget(button)

    def show_simulation_options(self, domain):
        options = self.simulation_options[domain]
        dialog = QtWidgets.QInputDialog(self.central_widget)
        dialog.resize(500, 500)
        dialog.setWindowTitle(f"选择{domain}模拟")
        dialog.setLabelText(f"请选择{domain}模拟")
        dialog.setComboBoxItems(options)
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        result = dialog.exec()
        selected_option = dialog.textValue()
        if result == QtWidgets.QDialog.Rejected or selected_option == "":
            return
        self.add_simulation_frame(selected_option)

    def add_simulation_frame(self, selected_option):
        tab_mapping = {
            "三体运动": self.add_three_body_tab,
            "抛体运动": self.add_movement_in_air_tab,
            "旋转运动": self.add_spinning_top_tab,
            "一维无限深势阱波函数态叠加": self.add_wavefunction_superposition_tab,
            "史瓦西黑洞下的引力透镜效应": self.add_schblack_hole_tab,
            "迈克尔逊干涉仪等倾干涉": self.add_michelson_equal_path_interference_tab,
            "迈克尔逊干涉仪等厚干涉": self.add_michelson_equal_thickness_interference_tab,
            "二维板材导热展示（差分法）": self.add_heat_conduction_in_a_2D_plate_tab,
        }

        if selected_option in tab_mapping:
            tab_mapping[selected_option]()

    def add_simulation_window(self, frame_class, tab_name):
        # Create a new QDialog window for the simulation
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle(tab_name)

        dialog.adjustSize()  # 自动调整大小为内容的大小

        # 设置最小尺寸以避免过小
        dialog.setMinimumSize(900, 700)
        dialog.setWindowFlags(dialog.windowFlags() | Qt.WindowMinMaxButtonsHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)  # 移除问号按钮

        # Create the simulation frame and add it to the dialog
        frame = frame_class(dialog)
        layout = QtWidgets.QVBoxLayout(dialog)
        layout.addWidget(frame)

        dialog.show()  # Show the dialog window

    # 这些方法用于打开具体的模拟框架
    def add_three_body_tab(self):
        self.add_simulation_window(three_body_frame, "三体运动")

    def add_movement_in_air_tab(self):
        self.add_simulation_window(movement_air_frame, "抛体运动")

    def add_spinning_top_tab(self):
        self.add_simulation_window(spinning_top_frame, "旋转运动")

    def add_wavefunction_superposition_tab(self):
        self.add_simulation_window(wavefunction_superposition_frame, "一维无限深势阱波函数态叠加")

    def add_schblack_hole_tab(self):
        self.add_simulation_window(schblack_hole_frame, "史瓦西黑洞下的引力透镜效应")

    def add_michelson_equal_path_interference_tab(self):
        self.add_simulation_window(michelson_equal_path_interference_frame, "迈克尔逊干涉仪等倾干涉")

    def add_michelson_equal_thickness_interference_tab(self):
        self.add_simulation_window(michelson_equal_thickness_interference_frame, "迈克尔逊干涉仪等厚干涉")

    def add_heat_conduction_in_a_2D_plate_tab(self):
        self.add_simulation_window(heat_conduction_in_a_2D_plate_frame, "二维板材导热展示（差分法）")


    def open_ai_chat(self):
        # 打开 AI 聊天窗口并启动后台进程
        self.chat_dialog = AIChatDialog(self)
        self.chat_dialog.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = SimulationApp()
    main_window.show()
    sys.exit(app.exec())









