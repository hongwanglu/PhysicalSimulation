# 该项目主要用于AI辅助的计算物理学习及案例分享

## 使用的工具

项目采用Python语言（<https://www.python.org/>）开发，UI使用PySide6（<https://pypi.org/project/PySide6/>），包管理和项目管理使用的工具是uv（An extremely fast Python package and project manager, written in Rust，<https://docs.astral.sh/uv>）

## 文件目录结构

fig 用于存放图片

ui 用于存放图形界面ui文件及pyside6-uic编译生成的_ui.py文件。注意：部分_ui.py文件是直接写的，没有对应的.ui文件。

每个具体例子都对应一个或多个python文件（在工作目录下）+相应的ui目录下的ui文件。

## 使用教程

1. 从 master 分支拉取最新代码，创建一个新分支。

   步骤 1）：Fork 仓库到你的 GitHub 账户

    打开浏览器，访问项目地址：<https://github.com/hongwanglu/PhysicalSimulation>点击右上角的 Fork 按钮。选择 Fork 到你自己的账户（默认就是你的账户）。等待几秒，Fork 完成后会跳转到你的 Fork 仓库：<https://github.com/你的用户名/PhysicalSimulation>

    现在你对自己的 Fork 有完整读写权限。

    步骤 2）：克隆你的 Fork 到本地（使用 VS Code）

    打开 VS Code。
    按快捷键 Cmd + Shift + P 打开命令面板，输入并选择 Git: Clone。
    输入你的 Fork 仓库地址：
    <https://github.com/你的用户名/PhysicalSimulation.git>
    （或者点击仓库页面绿色的 Code 按钮复制 HTTPS 地址）
    选择本地保存文件夹，点击 Clone。

    VS Code 会问是否打开克隆的仓库，点击 Open。

    步骤 3）：添加原仓库作为远程上游（upstream，便于同步最新代码）

    在 VS Code 中打开终端（Terminal > New Terminal），执行以下命令（把 hongwanglu 替换成原作者用户名）：

    git remote add upstream https://github.com/hongwanglu/PhysicalSimulation.git

    验证是否添加成功：

    git remote -v

    你会看到 origin（你的 Fork）和 upstream（原仓库）。

    步骤 4）：拉取最新代码并创建新分支

    先确保主分支是最新的：

    git checkout master # 拉取最新代码

    git pull upstream master # 从原仓库拉取最新代码

    git push origin master   # 把最新代码同步到你的 Fork（可选但推荐）

    创建并切换到新分支（建议用有意义的名字）：

    git checkout -b feature/你的功能描述

    示例：textgit checkout -b feature/add-gravity-calculation

    VS Code 图形化方式：

    左下角点击当前分支名（master）。

    输入新分支名，如 feature/add-gravity-calculation，回车创建并切换。

2. 配置开发环境安装必要的软件包。
3. 使用python运行Physical_Simulation.py(也可以运行单独的例子，测试开发环境搭建是否成功)。
4. 在自己的分支上加入自己的代码、文档、保证代码能独立运行。
5. 在新分支上正常编辑、添加、修改 Python 文件，commit 并 push 到 GitHub。


    步骤1）：更新Physical_Simulation.py文件中力、热、光、电相应位置，让主程序能在相应模块中索引自己的代码。

    步骤2）：在 VS Code 左侧 Source Control 视图：

    Stage 修改的文件（点击 + 或 Stage All）。

    输入 commit 消息（清晰描述你做了什么）。

    提交（点击 ✓ 或 Cmd + Enter）。

    步骤3）：推送你的分支到自己的 Fork：

    git push origin feature/你的更新功能描述

    或在 VS Code：点击底部状态栏的上传箭头（↑），或选择 Publish Branch。

6. 提交 Pull Request（PR）

    打开浏览器，访问你的 Fork 仓库：<https://github.com/你的用户名/PhysicalSimulation>，你会看到刚推送的分支，旁边有Contribute > Open pull request 按钮，点击它。（或者直接访问原仓库，GitHub 会提示 “Compare & pull request”）

    PR 页面：

    base repository：hongwanglu/PhysicalSimulation ← base: master（或 main）

    head repository：你的用户名/PhysicalSimulation ← compare: 你的分支

    填写 PR 标题和详细描述：

    标题：简洁描述功能（如 “添加重力计算模块”）

    描述：说明做了什么、为什么、如何测试等（越详细越好）

    点击 Create pull request。

    完成！原仓库拥有者（hongwanglu）会收到通知，审查你的代码。

    如果需要修改，你可以在本地继续在同一分支 commit 并 push，PR 会自动更新。
7. 由管理者审查 PR：查看变化、评论、请求修改。批准并 合并 (Merge) PR 到 master。
8. 后续常见操作

如果需要同步原仓库最新代码（持续开发中定期做）：

git checkout master

git pull upstream master

git checkout 你的分支

git rebase master   # 或 git merge master，把最新代码合并到你的分支

git push --force-with-lease origin 你的分支  # 更新远程分支

## TODO Lists

1. 整理文档，每个案例相关的文档/说明
2. 加入更多优秀案例
3. ...
