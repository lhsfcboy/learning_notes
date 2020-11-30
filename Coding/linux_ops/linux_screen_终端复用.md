
## 参考

- [IBM: 使用 screen 管理你的远程会话](https://www.ibm.com/developerworks/cn/linux/l-cn-screen/index.html)
- [Screen User’s Manual](https://www.gnu.org/software/screen/manual/screen.html)
## 安装与版本检查
    apt-get -y install screen
    yum -y install screen
    
    
    rpm -qa|grep screen
    screen -v

## 开始使用Screen

    screen #新建并进入一个不具名screen会话的窗口
    screen -S name #新建并进入一个名为name的screen会话的窗口
    screen vi test.c #新建并进入一个不具名screen会话的窗口, 并执行命令
    screen -ls #查看现有会话
    
    screen -r xxxx #连接到名为xxxx, 或screen_pid为xxxx的会话
    C-a, c #在当前会话内生成一个新的窗口并切换到该窗口
    C-a, d #中断当前会话 
    
## 分屏
    C-a, S-s #上下分屏
    C-a, Tab #切换屏幕
    C-a, c   #创建新的终端
    C-a, x   #关闭终端, 也就是exit

## 常用的键绑定

    C-a ?	显示所有键绑定信息
    C-a w	显示所有窗口列表
    C-a C-a	切换到之前显示的窗口
    C-a c	创建一个新的运行shell的窗口并切换到该窗口
    C-a n	切换到下一个窗口
    C-a p	切换到前一个窗口(与C-a n相对)
    C-a 0..9	切换到窗口0..9
    C-a a	发送 C-a到当前窗口
    C-a d	暂时断开screen会话
    C-a k	杀掉当前窗口
    C-a [	进入拷贝/回滚模式
    
##     
