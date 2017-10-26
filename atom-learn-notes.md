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

# 第二章：使用Atom

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
