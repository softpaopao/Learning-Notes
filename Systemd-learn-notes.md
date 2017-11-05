Systemed--学习笔记
----
## Systemed 主要用途：分析系统状态
* systemctl status > 显示系统状态
* systemctl
* systemctl list-units > 输出激活的单元
* systemctl --failed > 显示运行失败的单元
* /usr/lib/systemed/system > 软件包安装的单元
* /etc/systemed/system > 系统管理员安装的单元
* systemctl list-unit-files > 显示所有已安装的服务

## 单元（Units）配置文件
* .service
* .mount
* .sokets
* .device
* .swap
* .path
* .target
* .timer

## 电源管理
* systemctl
  * reboot > 重启
  * poweroff > 退出并关闭电源
  * suspend > 待机
  * hibernate > 休眠
  * hybrid-sleep > 混合休眠（同时休眠到硬盘并待机）

## 配置文件
* /etc/systemed/system/~ <-- 优先级高
* /usr/lib/systemed/system/~ 
* systemd-delta > 查看哪些单元被覆盖或被修改

## Systemctl 命令
* systemctl
  * start > 激活
  * stop > 停止
  * restart > 重启
  * reload > 重新加载配置
  * status > 显示运行状态
  * is-enable > 检查是否配置为自启动
  * enable > 开机自启
  * disable > 取消开机自启
  * mask > 禁用单元
  * unmask > 取消禁用
  * help
  * daemon-reload > 重载 systemd ，扫描新的或变动单元
  * show > 所有底层参数
  * show -p cpushares ... 特定属性
  * set-property http-service cpushares = 500 > 设定属性
  * kill > 杀死进程

## 目标（Target）
* systemctl list-units --type=target > 获取当前目标

Systemd 目标

  |int level|target|含义|
  |-|---------------|-------|
  |0|poweroff.target|中断系统|
  |1|rescue.target|单用户模式|
  |2、4|    |自定义|
  |3|multi-user.target|多用户模式（无图形界面，可以使用终端、网络登陆）|
  |5|graphical.target|多用户模式（图形界面，继承 3 的服务）|
  |6|reboot.target|重启|
  |emergency|emergency.target|救援模式|
  
* systemctl isolate graphical.target > 切换运行级别（对下次启动没有影响）
* 修改默认启动
  * systemctl set-default mult-user.target （可使用参数 -f 进行覆盖）
  * systemctl get-default > 获取默认 target

## 日志（Journal）
* /etc/systemd/journal-conf > 配置文件
* 过滤输出
  * journalctl
    * -b > 本次启动之后（-0）
    * -1 > 上次
    * -2 > 上上次


日志级别

|level|含义|
|-----|----|
|0    |emery   |
|1   |alert   |
|2   |crit   |
|3   |err   |
|4   |warning   |
|5   |notice   |
|6   |info   |
|7   |debug   |


* journalctl
  * -p err..alert > 显示错误、冲突、警告
  * --since="2012-10-30 18:17:16"
  * --since="20 min ago"
  * -f > 显示最新信息（实时滚动刷新）
  * /usr/lib/systemd/system 特定程序
  * -u netcfg 指定单元 （-- since today）
  * -K 内核缓存
  * -PID=1 指定PID
  * -n 显示尾部行数（-n 10）（-n 20）
  * --disk-usage 显示日志占用的空间
  * --vancum-size = 1G 设定最大占用空间
  * --vancum-time = 1years 设定最大占用时间

## 相关命令

* systemd-analyze 查看启动耗时
      * blame 每个服务的启动耗时
      * critical-chain 瀑布状的启动耗时
      * critical-chain atd.service 制定服务的启动流


* hotnamectl 显示当前主机信息
      * sudo hostnamectl set-hostname softpaopao 设置主机名


* loginctl 查看当前登陆用户
      * loginctl list-session
      * loginctl list-user
      * loginctl show-user


* timectl 查看当前时区
      * timectl set-timezone ...
      * timectl set-time YYYY-MM-DD
      * timectl set-time HH:MM:SS
      * timectl list-timezone


* systemctl list-units
      * --all 列出所有，包括启动失败
      * --all --state=inactive 没有运行的
      * --faild 加载失败的
      * --type=service 类型为 service 的 units


* systemctl status 查看系统状态和单元状态
      * is-active
      * is-failed
      * is-enable
      * -H pi@ip status http.service 远程主机的某个服务


* systemctl list-dependenices 列出一个 unit 的依赖
      * -all 展开 target


* unit
      * /etc/systemd/system  --> /usr/lib/systemd/system （真正的存放目录）
      * sudo systemctl enable ssh.service 
      相当于： 
      sudo ln -s '/usr/lib/systemd/system/ssh.service' '/etc/systemd/system/ssh.service'


* systemctl list-unit-files 列出所有（配置文件）
  * --type=service
    * enable 启动链接
    * disable 没建立启动链接
    * static 没有 [Install] 部分，仅作为依赖
    * mask 禁止


* 配置文件做出修改后
  * systemctl daemon-reload
  * systemctl restart ssh.service


## Systemd 配置

[Unit]
* Description 简述
* Documentation 文档位置
* After 在...之后
* Before 在...之前 （只涉及启动顺序，不涉及依赖）
* Wants 弱依赖
* Requires 强依赖 （默认同时启动，不涉及顺序）

[Service]
* Environment 指定环境参数文件
* ExecStart 定义启动进程时执行的命令
* ExecReload 重启服务时执行的命令
* ExecStop 停止服务时执行的命令
* ExecStartPre 启动服务之前执行
* ExecStartPost 启动服务之后执行
* ExecStopPost 停止服务之后执行

Exextart=/-bin ....
空值，则为取消上一行设置，“-” 抑制错误，即使不存在，也不会错误。
