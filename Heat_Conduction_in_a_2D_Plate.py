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

import sys
import numpy as np
from PySide6 import QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import cm
from scipy import interpolate

class heat_conduction_in_a_2D_plate_frame(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(heat_conduction_in_a_2D_plate_frame, self).__init__(parent)

        k = 1000      # 导热系数
        q = 500e3     # 西侧边界通量
        T_top = 100   # 北侧边界温度

        L = 0.3  # 长度
        H = 0.4  # 高度

        nx = 50  # x方向网格个数，列数
        ny = 50  # y方向网格个数，行数

        dx = L / nx  # 网格大小
        dy = H / ny

        A = np.zeros((nx * ny, nx * ny))  # 构造系数矩阵
        B = np.zeros((nx * ny))           # 构造源项矩阵

        grad_e = grad_w = dy / dx
        grad_n = grad_s = dx / dy

        for i in range(nx * ny):  # 填充nx * ny行系数矩阵
            # 内部单元（去除底部、左侧、顶部以及右侧单元）
            if np.floor(i / nx) != 0 and i % nx != 0 and np.floor(i / nx) != ny - 1 and (i + 1) % nx != 0:
                A[i, i - 1] = -k * grad_w  # 西侧面
                A[i, i + 1] = -k * grad_e  # 东侧面
                A[i, i + nx] = -k * grad_n  # 北侧面
                A[i, i - nx] = -k * grad_s  # 南侧面
                A[i, i] = -(A[i, i-1] + A[i, i+1] + A[i, i+nx] + A[i, i-nx])

            # 底部单元，不考虑角点  
            elif np.floor(i / nx) == 0 and i != 0 and i != nx - 1:
                A[i, i - 1] = -k * grad_w  # 西侧面
                A[i, i + 1] = -k * grad_e  # 东侧面
                A[i, i + nx] = -k * grad_n  # 北侧面
                A[i, i] = -(A[i, i-1] + A[i, i+1] + A[i, i+nx])  
            # 因为底部边界是绝热边界所以fluxCb=0 fluxV_b=0（第二类边界条件）

            # 右侧单元,不考虑角点
            elif (i+1) % nx == 0 and i != nx - 1 and i != nx * ny - 1:
                A[i, i - 1] = -k * grad_w  # 西侧面
                A[i, i + nx] = -k * grad_n  # 北侧面
                A[i, i - nx] = -k * grad_s  # 南侧面
                A[i, i] = -(A[i, i - 1] + A[i, i + nx] + A[i, i - nx])  
                # 因为右侧边界是绝热边界所以fluxCb=0 fluxVb=0（第二类边界条件）

            # 左侧单元， 不考虑角点
            elif i % nx == 0 and i != 0 and i != (ny - 1) * nx:
                A[i, i + 1] = -k * grad_e  # 东侧面
                A[i, i + nx] = -k * grad_n  # 北侧面
                A[i, i - nx] = -k * grad_s  # 南侧面
                A[i, i] =-(A[i, i + 1] + A[i, i + nx] + A[i, i - nx])
                # （第二类边界条件）源项多了fluxVb = q*dy
                B[i] = q * dy

            # 顶部，不考虑角点
            elif np.floor(i / nx) == ny - 1 and i != nx * ny -1 and i != (ny - 1) * nx:
                A[i, i - 1] = -k * grad_w  # 西侧面
                A[i, i + 1] = -k * grad_e  # 东侧面
                A[i, i - nx] = -k * grad_s  # 南侧面
                A[i, i] =- (A[i, i - 1] + A[i, i + 1] + A[i, i - nx]) + 2 * k * grad_n   
                # 第一类边界条件 边界项为k*dx/(dy/2)
                B[i] = 2 * k * grad_n * T_top

            # 左下角
            elif i == 0:
                A[i, i + 1] = -k * grad_e  # 东侧面
                A[i, i + nx] = -k * grad_n  # 北侧面
                A[i, i] = -(A[i, i + 1] + A[i, i + nx])
                B[i] = q * dy

            # 右下角
            elif i == nx - 1:
                A[i, i - 1] = -k * grad_w  # 西侧面
                A[i, i + nx] = -k * grad_n  # 北侧面
                A[i, i] = -(A[i, i - 1] + A[i, i + nx])

            # 左上角
            elif i == nx * (ny - 1):
                A[i, i + 1] = -k * grad_e  # 东侧面
                A[i, i - nx] = -k * grad_s  # 南侧面
                A[i, i] = -(A[i, i + 1] + A[i, i - nx]) + 2 * k * grad_n
                B[i] = q * dy + 2 * k * grad_n * T_top

            # 右上角
            elif i == nx * ny - 1:
                A[i, i - 1] =- k * grad_w  # 西侧面
                A[i, i - nx] = -k * grad_s  # 南侧面
                A[i, i] = -(A[i, i - 1] + A[i, i - nx]) + 2 * k * grad_n
                B[i] = 2 * k * grad_n * T_top

        T = np.linalg.solve(A,B)  # LU分解法
        #print(T)

        # 创建数组用于存储各单元体心坐标
        cellC = np.ones((nx * ny, 2))
        for i in range(len(cellC)):
            cellC[i, 0] = dx / 2 + (i % nx) * dx
            cellC[i, 1] = dy / 2 + (np.floor(i / nx)) * dy
        x = cellC[:, 0]
        y = cellC[:, 1]

        # 绘制图形并将其嵌入PyQt5窗口
        self.figure = Figure(figsize=(6, 8))
        self.canvas = FigureCanvas(self.figure)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

        self.plot_contour(x, y, T, 0, 0.3, 0, 0.4)
        self.canvas.draw()

    def plot_contour(self, Coordx, Coordy, T, minX, maxX, minY, maxY):
        X = np.linspace(minX, maxX, 1000)
        Y = np.linspace(minY, maxY, 1000)
        X1, Y1 = np.meshgrid(X, Y)

        fig = self.figure
        ax = fig.add_subplot(111)
        levels = range((int)(T.min()), (int)(T.max()) + 5, 1)
        Z = interpolate.griddata((Coordx, Coordy), T, (X1, Y1), method="cubic")
        cset1 = ax.contourf(X1, Y1, Z, levels, cmap=cm.jet)

        ax.set_xlim(minX, maxX)
        ax.set_ylim(minY, maxY)
        ax.set_xlabel("X(mm)", size=15)
        ax.set_ylabel("Y(mm)", size=15)

        cbar = fig.colorbar(cset1)
        cbar.set_label('T', size=18)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = heat_conduction_in_a_2D_plate_frame()
    window.setWindowTitle('Heat Conduction in 2D Plate')
    window.show()
    sys.exit(app.exec())
