树莓派使用记录
----
* 烧录镜像 raspbian ，默认用户：pi ，默认密码：raspberry 。
* 开启SSH，须在 /boot 目录下，添加文件名为 ssh 的空文件。
* 连接SSH命令
  * ssh pi@raspberrypi.local
  * 查到 ip 的话，使用 ssh pi@x.x.x.x
* 启用 wifi
  * 须在 /boot 目录下，添加文件名为 wpa_supplicant.conf 的文件。
  * 文件内容：
  
  ```markdown
  country=GB
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1
  
  netwrok = {
    ssid="wifi名称"
    psk="wifi密码"
    priority="5"   #代表优先级，数字越大，优先级越高
  } 
  ```
* 开启 VNC 服务
 * 通过 raspberrypi 配置工具，开启VNC
   * sudo raspi-config
 * vncserver list > 列出 VNC 会话
 * vncserver kill :2 > 结束 VNC 会话
 * 如果使用 windows 连接 VNC 服务，需要安装 xrdp 软件包。
   * systemctl start xrdp
   * systemctl enable xrdp
* 使用中文界面
  * 安装中文字体包，如：tty-wqy-zenhei
  
* 无密码ssh登录
  * 生成公钥和私钥
  * cat id_rsa.pub >> ~/.ssh/authorized_keys（也就是SSH客户端使用私钥，服务端使用公钥）
----
参考文章：
[《树莓派入门指南》](https://sspai.com/post/38542)
[《如果没有显示器如何愉快玩树莓派》](https://sspai.com/post/38780)
