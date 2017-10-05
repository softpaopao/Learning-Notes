openSUSE：Tumbleweed 升级
--------------

translated by softpaopao

2017-08-15 翻译 

本页中的“升级”的意思就是：从一个旧的openSUSE发行版（比如 openSUSE 13.2 或者 Leap）迁移至 Tumbleweed。

官方支持两种升级方式：

* `离线升级` —— 通过使用DVD来启动系统，并进行升级
* `在线升级` —— 通过变更已经安装的 openSUSE 系统的软件源来实现在线安装和升级

离线升级相对来说更加安全，因为在此升级过程中没有已经运行的应用干扰。

在线升级相对来说更加方便一些，因为此升级过程可以在系统运行时进行，并且不需要下载完整的 DVD 镜像。

===离线升级===

离线升级只需要以下几步：
* 下载相应的 DVD 镜像，烧录到 DVD 光盘或者 USB 记忆棒
* 启动 DVD 光盘或者 USB 记忆棒
* 选择升级
* 按照向导操作，升级向导会检测你的安装设备并进行升级。

===在线升级===

通过以下三个步骤来实现从任何版本到 Tumbleweed 版本的升级：
* 在现有的系统中安装在线更新，如果有的话。（对于 openSUSE 13.2 来说，通常需要在升级之前修复内核问题，并且会在系统重启后继续。）
* 变更软件源到 Tumbleweed 的软件源
* 执行 `zypper dup` （这是命令 `zypper dist-upgrade` 的简写形式）来升级全部的包文件

====软件源 ====

首先移除现有的软件源（备份现有软件源至 `etc/zypp/repos.d/old` 路径下）：

```
 mkdir /etc/zypp/repos.d/old
 mv /etc/zypp/repos.d/*.repo /etc/zypp/repos.d/old
```

然后添加新的软件源：

 ```
 zypper ar -f -c http://download.opensuse.org/tumbleweed/repo/oss repo-oss
 zypper ar -f -c http://download.opensuse.org/tumbleweed/repo/non-oss repo-non-oss
 zypper ar -f -c http://download.opensuse.org/tumbleweed/repo/debug repo-debug
 zypper ar -f -c http://download.opensuse.org/update/tumbleweed/ repo-update
```

你也可以选择性的添加 sources 软件源，当然也可以添加要使用的 OBS 源。
 
 ```
 zypper ar -f -d -c http://download.opensuse.org/tumbleweed/repo/src-oss repo-src-oss
 zypper ar -f -d -c http://download.opensuse.org/tumbleweed/repo/src-non-oss repo-src-non-oss
```

最终你会看到如下的软件源列表：

```
 # zypper lr -u
  # | Alias             | Name              | Enabled | Refresh | URI
  --+-------------------+-------------------+---------+---------+--------------------------------------------------------
  1 | repo-debug        | repo-debug        | Yes     | Yes     | http://download.opensuse.org/tumbleweed/repo/debug
  2 | repo-non-oss      | repo-non-oss      | Yes     | Yes     | http://download.opensuse.org/tumbleweed/repo/non-oss
  3 | repo-oss          | repo-oss          | Yes     | Yes     | http://download.opensuse.org/tumbleweed/repo/oss
  4 | repo-src-non-oss  | repo-src-non-oss  | No      | Yes     | http://download.opensuse.org/tumbleweed/repo/src-non-oss
  5 | repo-src-oss      | repo-src-oss      | No      | Yes     | http://download.opensuse.org/tumbleweed/repo/src-oss
  6 | update            | repo-update       | Yes     | Yes     | http://download.opensuse.org/update/tumbleweed/
```

update 源通常是空的，仅在当下一个版本的 Tumbleweed 快照延期同时又有重要的安全漏洞需要尽快修复的时候使用。

==== 运行升级命令 ====

当你完成了软件源的配置，就可以使用 `zypper dup` 来进行升级。

{{Warning | 尽量使用控制台来执行命令，以避免 '''zypper dup''' 命令在执行时被终止，比如X dies 。尽量不要使用 Tmux 这样的终端来执行命令，以避免同样的问题}}

```
 zypper dup
```

现在可以放松一下等待升级完成，愉快的使用我们的滚动更新版本。

同时不要忘了订阅 [ http://lists.opensuse.org/opensuse-factory/mailinglist ] 来了解开发的最新信息。

====如果升级失败：请刷新zypper源 ====

有时 zypper 升级失败是因为找不到类似这样的文件：

```
 Retrieving: monitoring-tools-1.14.0-4.2.x86_64.rpm ......................................................................................................[error]
 File './x86_64/monitoring-tools-1.14.0-4.2.x86_64.rpm' not found on medium 'http://download.opensuse.org/repositories/server:/monitoring/openSUSE_Tumbleweed/'
```

当你进入 `http://download.opensuse.org/repositories/server:/monitoring/openSUSE_Tumbleweed/x86_64/` 时，你会发现存在多个版本的 `monitoring-tools-*.x86_64.rpm` 文件。

上述错误通常意味着你的 `zypper` 本地配置与软件源不同步。 通过 `zypper refresh` 来解决, 使用如下的命令组合来正确升级:

```
 zypper refresh
 zypper dist-upgrade
```
来源：https://zh.opensuse.org/openSUSE:%E5%8D%87%E7%BA%A7_Tumbleweed
