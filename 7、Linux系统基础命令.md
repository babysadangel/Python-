###基础命令

Linux系统的命令通常都是如下所示的格式：

		命令名称 [命令参数] [命令对象]
	
1、获取登录信息 - w/who/last

	AdministratordeiMac:~ administrator$ w
	11:52  up 19 mins, 2 users, load averages: 1.43 1.63 1.83
	USER     TTY      FROM              LOGIN@  IDLE WHAT
	administrator console  -                11:33      18 -
	administrator s000     -                11:52       - w
	AdministratordeiMac:~ administrator$ who
	administrator console  Apr  1 11:33 
	administrator ttys000  Apr  1 11:52 
	AdministratordeiMac:~ administrator$ who am i
	administrator ttys000  Apr  1 11:52 
2、查看自己使用的Shell - **ps**
   
  Shell也被称为‘壳’，它是用户与内核交流的翻译官，简单来说就是人与计算机交互的接口。目前很多Linux系统默认的Shell都是bash（Bourne Again SHell），因为他可以使用Tab键进行补全命令，可以保存历史命令、可以方便的配置环境变量以及执行批处理操作等。
  
  	AdministratordeiMac:~ administrator$ ps
  	PID TTY           TIME CMD
 	779 ttys000    0:00.13 -bash
	
3、查看命令说明-- **whatis**

	AdministratordeiMac:~ administrator$ whatis ps
	ps(1)                    - process status
	AdministratordeiMac:~ administrator$ whatis python
	python(1)                - an interpreted, interactive, object-oriented 	programming language
	Inline::Python(3pm)      - Write Perl subs and classes in Python
	pydoc(1)                 - the Python documentation tool
	python(1)                - an interpreted, interactive, object-oriented 	programming language
	pythonw(1)               - run python script allowing GUI

4、查看命令的位子 --**which/whereis**

	AdministratordeiMac:~ administrator$ whereis ps
	/bin/ps
	AdministratordeiMac:~ administrator$ whereis python
	/usr/bin/python
	AdministratordeiMac:~ administrator$ which python3
	/usr/local/bin/python3
	
5、查看帮助文档- **man / info / apropos**

	AdministratordeiMac:~ administrator$ ps --help
	ps: illegal option -- -
	usage: ps [-AaCcEefhjlMmrSTvwXx] [-O fmt | -o fmt] [-G gid[,gid...]]
          [-g grp[,grp...]] [-u [uid,uid...]]
          [-p pid[,pid...]] [-t tty[,tty...]] [-U user[,user...]]
       ps [-L]
	AdministratordeiMac:~ administrator$ man ps

     For the processes which have been selected for display, the information
     to display is selected based on a set of keywords (see the -L, -O, and -o
     options).  The default output format includes, for each process, the
     process' ID, controlling terminal, CPU time (including both user and sys-
     tem time), state, and associated command.

     The options are as follows:

     -A      Display information about other users' processes, including those
             without controlling terminals.

     -a      Display information about other users' processes as well as your
             own.  This will skip any processes which do not have a control-
             ling terminal, unless the -x option is also specified.

     -C      Change the way the CPU percentage is calculated by using a
             ``raw'' CPU calculation that ignores ``resident'' time (this nor-
             mally has no effect).
             
             AdministratordeiMac:~ administrator$ info ps
             ......
6、切换用户-**su**
	
	AdministratordeiMac:~ administrator$ su hellokitty
	
7、以管理员的身份执行命令--**sudo**

	AdministratordeiMac:~ administrator$ sudo xxxxxx
>说明：如果希望用户能够以管理员身份执行命令，用户必须被添加到sudoers名单中，该文件在 /etc目录下。

8、登入登出相关-**logout / exit / adduser / userdel / passwd / ssh**

	[root@izwz97tbgo9lkabnat2lo8z ~]# adduser hellokitty
	[root@izwz97tbgo9lkabnat2lo8z ~]# passwd hellokitty
	Changing password for user jackfrued.
	New password:
	Retype new password:
	passwd: all authentication tokens updated successfully.
	[root@izwz97tbgo9lkabnat2lo8z ~]# ssh hellokitty@1.2.3.4
	hellokitty@1.2.3.4's password:
	Last login: Thu Apr 12 23:05:32 2018 from 10.12.14.16
	[hellokitty@izwz97tbgo9lkabnat2lo8z ~]$ logout
	Connection to 1.2.3.4 closed.
	[root@izwz97tbgo9lkabnat2lo8z ~]#
9、查看系统和主机名称--**uname / hostname**
	AdministratordeiMac:~ administrator$ uname
	Darwin
	AdministratordeiMac:~ administrator$ hostname
	AdministratordeiMac.local

10、重启和关机 -**reboot / init 6/ shutdown / init 0**

11、查看历史命令 -**history**

	AdministratordeiMac:~ administrator$ history
   	37  /usr/local/opt/python/bin/python3.7
   	38  pwd
   	39  cd /Users/administrator/Documents/Python学习笔记2019年3月6日/Code
  	40  python object.pyy
  	42  python object2.py
  	......
  	

