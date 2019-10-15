Ubuntu 18.04, 19.04

* 安装Python3</br>
`sudo apt install python3`

* 查看python版本</br>
```
   ~ $ python3
   Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
```

* 安装pip3</br>
`sudo apt install python3-pip`

* 创建虚拟环境 .env</br>
`python3 -m venv .env`

* 激活虚拟环境</br>
`source .env/bin/activate`

* 安装需要的python模块</br>
`pip install *`

* 退出虚拟环境</br>
`deactivate`


Windows 10
* 安装Python3</br>
自定义 勾选 配置环境变量path 和 所有用户安装，默认会安装pip

* 创建虚拟环境</br>
`python -m venv .env`

* 激活虚拟环境</br>
`.env\Scripts\activate.bat`

* Windows 10下PowerShell提示权限错误</br>
错误信息：</br>
无法加载文件 .env\scripts\activate.ps1，因为在此系统上禁止运行脚本。有关详细信息，请参
阅 http://go.microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。</br>
以管理员身份打开PowerShell，执行命令：</br>
`set-executionpolicy remotesigned`

```
网易pypi镜像使用帮助

一、临时使用
使用pip的时候在后面加上-i参数，指定pip源：

pip install xxx -i https://mirrors.163.com/pypi/simple/
替换“xxx”为你需要安装的模块名称。

二、永久修改使用
Linux/Unix中使用：

~/.pip/pip.conf
添加或修改pip.conf（如果不存在，创建一个）

[global]
index-url = https://mirrors.163.com/pypi/simple/

Windows中使用：

%APPDATA%/pip/pip.ini
1.打开此电脑，在最上面的的文件夹窗口输入：%APPDATA%

2.按回车跳转进入目录，并新建一个文件夹：pip

3.创建文件：pip.ini

添加或修改pip.ini（如果不存在，创建一个）

[global]
index-url = https://mirrors.163.com/pypi/simple/
```




* 常用Visual Studio Code扩展</br>
```
Name: Trailing Spaces
Id: shardulm94.trailing-spaces
Description: Highlight trailing spaces and delete them in a flash!
Version: 0.3.1
Publisher: Shardul Mahadik
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=shardulm94.trailing-spaces
```

```
Name: Beautify
Id: hookyqr.beautify
Description: Beautify code in place for VS Code
Version: 1.4.11
Publisher: HookyQR
```

```
Name: Bracket Pair Colorizer 2
Id: coenraads.bracket-pair-colorizer-2
Description: A customizable extension for colorizing matching brackets
Version: 0.0.28
Publisher: CoenraadS
```

```
Name: Diff
Id: fabiospampinato.vscode-diff
Description: Diff 2 opened files with ease. Because running `code --diff path1 path2` is too slow.
Version: 1.4.0
Publisher: Fabio Spampinato
```

```
Name: Partial Diff
Id: ryu1kn.partial-diff
Description: Compare (diff) text selections within a file, across files, or to the clipboard
Version: 1.4.0
Publisher: Ryuichi Inagaki
```

```
Name: Git History
Id: donjayamanne.githistory
Description: View git log, file history, compare branches or commits
Version: 0.4.6
Publisher: Don Jayamanne
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory
```

```
Name: GitLens — Git supercharged
Id: eamodio.gitlens
Description: Supercharge the Git capabilities built into Visual Studio Code — Visualize code authorship at a glance via Git blame annotations and code lens, seamlessly navigate and explore Git repositories, gain valuable insights via powerful comparison commands, and so much more
Version: 9.6.3
Publisher: Eric Amodio
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens
```

```
Name: Markdown All in One
Id: yzhang.markdown-all-in-one
Description: All you need to write Markdown (keyboard shortcuts, table of contents, auto preview and more)
Version: 2.3.1
Publisher: Yu Zhang
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one
```

```
Name: Python
Id: ms-python.python
Description: Linting, Debugging (multi-threaded, remote), Intellisense, code formatting, refactoring, unit tests, snippets, and more.
Version: 2019.4.11987
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python
```

```
Name: Python for VSCode
Id: tht13.python
Description: Python language extension for vscode
Version: 0.2.3
Publisher: Thomas Haakon Townsend
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=tht13.python
```

```
Name: Python Extension Pack
Id: donjayamanne.python-extension-pack
Description: Popular Visual Studio Code extensions for Python
Version: 1.4.0
Publisher: Don Jayamanne
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack
```

```
Name: Python Extended
Id: tushortz.python-extended-snippets
Description: Python Extended is a vscode snippet that makes it easy to write codes in python by providing completion options along with all arguments.
Version: 0.0.1
Publisher: Taiwo Kareem
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=tushortz.python-extended-snippets
```

```
Name: AREPL for python
Id: almenon.arepl
Description: real-time python scratchpad
Version: 1.0.14
Publisher: Almenon
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=almenon.arepl
```

```
Name: Python Preview
Id: dongli.python-preview
Description: Provide Preview for Python Execution.
Version: 0.0.4
Publisher: dongli
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=dongli.python-preview
```

```
Name: Python Path
Id: mgesbert.python-path
Description: Python imports utils.
Version: 0.0.11
Publisher: Mathias Gesbert
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=mgesbert.python-path
```

```
Name: vscode-icons
Id: vscode-icons-team.vscode-icons
Description: Icons for Visual Studio Code
Version: 8.6.0
Publisher: VSCode Icons Team
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons
```

```
Name: shellcheck
Id: timonwong.shellcheck
Description: An extension to use shellcheck in vscode
Version: 0.6.0
Publisher: Timon Wong
```

```
Name: shell-format
Id: foxundermoon.shell-format
Description: shellscript、Dockerfile、properties、gitignore、dotenv、hosts、jvmoptions... DocumentFormat
Version: 4.0.5
Publisher: foxundermoon
```

```
Name: Robot Framework Intellisense
Id: tomiturtiainen.rf-intellisense
Description: Robot Framework Intellisense
Version: 2.5.0
Publisher: Tomi Turtiainen
```
