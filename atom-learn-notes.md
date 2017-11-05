Atom飞行手册--学习笔记
----
原文链接：http://flight-manual.atom.io

# 第一章：入门（Getting started）

## Why Atom？

Atom 使用了最新版本的 Chromium 的变种，用来对页面进行本地渲染。所有的 API 都可以在 Node.js 程序上运行。

作为一个长期持续进行的项目，开源是必须的。就像是已经持续了三十多年的 Vim 和 Emacs 一样。

## Atom Basics

* `Ctrl+Shift+P` > Command Palette 命令板
* `Ctrl+O` > 打开文件
* 通过cmd，使用 `atom` 或 `apm` 命令。e.g. `atom [files]` （ atom 命令已经被自动安装）
* `Ctrl+S` > 保存文件
* `Ctrl+Shift+S` > 另存为 ...
* `Ctrl+Shift+A` > 打开文件夹
* 使用 `atom` 命令 `atom [folder2] [folder2]` ，可以同时打开多个文件夹。
* `Crl+\` > 显示或隐藏目录树
* `Alt+\` > 在工作窗口与目录树之间，切换聚焦。在目录树窗口下，可以使用 `A` , `M` , `Delete` 进行创建，移动，删除文件。
* 使用 `Ctrl+T` 或 `Ctrl+P` ，快速搜索并打开项目内的文件。

# 第二章：使用 Atom

## Atom Packages

* 切换聚焦，或则点击窗口标签栏，使用 `Ctrl+,` 可以调出设置视图（setting view）。
* 使用 apm 命令，例如
  + `apm install <package_name>` 安装包
  + `apm install <package_name>@<package_version>`
  + `apm search` 搜索包
  + `apm view` 查看包的详细信息
 
## Moving in Atom

* `Ctrl+Left` 或 `Ctrl+Right` 用来移动至文字的开头或末尾。
* `Home` 或 `End` 用来移动至当前所在行的开头或末尾。
* `Ctrl+Home` 或 `Ctrl+End` 用来移动至文件内容的开头或末尾。
* 使用 `Ctrl+G` 并输入 `行:列` ，直接定位到特定位置。
* `Ctrl+R` 使用符号导航（symbols-view）。
* Bookmarks
  + `Ctrl+Alt+F2` 在当前行添加书签
  + `F2` ，`Shift+F2`用来从上到下或者从下到上的在书签中循环切换
  + `Ctrl+F2` 列出所有的书签
  + 在书签位置再次使用 `Ctrl+Alt+F2` 可以取消书签 

## Atom Selections

* `Shift`+`UP`/`Down`/`Left`/`Right` 
* `Ctrl`+`Shift`+`Left`/`Right` > 选择光标位置到文字的开头或末尾
* `Shift`+`Home`/`End` > 选择光标位置到所在行的开头或末尾
* `Ctrl`+`Shift`+`Home`/`End` > 选择光标位置到文件内容的开头或结尾
* `Ctrl`+`A` > 全选
* `Ctrl`+`L` > 选择光标所在行

## Editing and Deleting Text 

* Basic Manipulation
  * `Ctrl+J` > 将下一行移动到当前行末
  * `Ctrl+Up/Down` > 向上或向下移动当前行
  * `Ctrl+Shift+D` > 重复当前行
  * `Ctrl+K` `Ctrl+U` > 大写光标所在单词
  * `Ctrl+K` `Ctrl+L` > 小写光标所在单词

* Deleting and Cutting
  * `Ctrl+Shift+K` > 删除当前光标所在行
  * `Ctrl+Backspace` > 删除光标所在单词之前的字母
  * `Ctrl+Delete` > 删除光标所在单词之后的字母

* Multiple Cursors and Selections （多重光标与选择）
  * `Ctrl+Click` > 在鼠标点击的位置添加光标
  * `Ctrl+D` > 选择当前光标位置之后的一个词
  * `Alt+F3` > 从文中同时选中所有与光标所在词相同的词

* Whitespace （空白）

* Encoding （编码）
  * `Ctrl+Shift+U` > 文件编码菜单

## Find and Replace

* `Ctrl+F` > 在缓冲区查找 
* `Ctrl+Shift+F` > 在整个项目中查找 

在查找的结果中，可以使用 `F3` 或 `Enter` 键进行切换。
使用 `ESC` 退出查找。

## Panes （窗格）

* `Ctrl+K` `Up/Down/Left/Right` > 在 上/下/左/右 划分窗格
* `Ctrl+W` > 关闭当前窗格

在 树视图 中双击文件，会以新的标签形式打开文件。

## Grammar

* `Ctrl+Shift+L` > 打开语法选择菜单

## Version Control in Atom

Atom 的版本控制集成了基本的 Git 和内建的 GitHub。

要使用版本控制，项目的根目录需要连接到 Git 仓库。

* Open on GitHub
  * `Alt+G` `O` > 在 GitHub 中打开文件
  * `Alt+G` `B` > 在 GitHub 中打开文件以 Blame 视图
  * `Alt+G` `H` > 在 GitHub 中打开文件以 History 视图
  * `Alt+G` `C` > 复制当前文件的 GitHub 超链接地址到剪切板
  * `Alt+G` `R` > 在 GitHub 中比较分支

## GitHub Packages

* `Ctrl+9` > 打开 Git 面板
* `Ctrl+8` > 打开 GitHub 面板
