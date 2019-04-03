##网络访问和管理
1. 通过网络获取资源-**wget**

	* `-b` 后台下载模式
	* `-O` 下载到指定目录
	* `-r` 递归下载

2. 显示/操作网络配置（旧） -**ifconfig**
 
		AdministratordeiMac:etc administrator$ ifconfig en0
		en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
				options=10b<RXCSUM,TXCSUM,VLAN_HWTAGGING,AV>
				ether 98:5a:eb:e1:12:0f 
				nd6 options=201<PERFORMNUD,DAD>
				media: autoselect (none)
		status: inactive
3. 显示/操作网配置（新window下）-**ip**

		[root@iZwz97tbgo9lkabnat2lo8Z ~]# ip address
		1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1
    		link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    		inet 127.0.0.1/8 scope host lo
       		valid_lft forever preferred_lft forever
		2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP qlen 1000
    			link/ether 00:16:3e:02:b6:46 brd ff:ff:ff:ff:ff:ff
    		inet 172.18.61.250/20 brd 172.18.63.255 scope global eth0
       		valid_lft forever preferred_lft forever
4. 网络可达性检查 -**ping**

		AdministratordeiMac:etc administrator$ ping www.baidu.com
		PING www.a.shifen.com (14.215.177.39): 56 data bytes
		64 bytes from 14.215.177.39: icmp_seq=0 ttl=52 time=10.037 ms
		64 bytes from 14.215.177.39: icmp_seq=1 ttl=52 time=7.587 ms
		64 bytes from 14.215.177.39: icmp_seq=2 ttl=52 time=8.018 ms
		64 bytes from 14.215.177.39: icmp_seq=2 ttl=52 time=49.398 ms (DUP!)
		......
		
5. 查看网络服务和端口 -**netstat**

		AdministratordeiMac:etc administrator$ netstat -nap | grep nginx
		netstat: option requires an argument -- p
		Usage:	netstat [-AaLlnW] [-f address_family | -p protocol]
			netstat [-gilns] [-f address_family]
			netstat -i | -I interface [-w wait] [-abdgRtS]
			netstat -s [-s] [-f address_family | -p protocol] [-w wait]
			netstat -i | -I interface -s [-f address_family | -p protocol]
			netstat -m [-m]
			netstat -r [-Aaln] [-f address_family]
			netstat -rs [-s]
6. 安全文件拷贝-**scp**

		[root@iZwz97tbgo9lkabnat2lo8Z ~]# scp root@1.2.3.4:/root/guido.jpg hellokitty@4.3.2.1:/
		home/hellokitty/pic.jpg
7. 安全文件传输 - **sftp**

		[root@iZwz97tbgo9lkabnat2lo8Z ~]# sftp root@120.77.222.217
		root@120.77.222.217's password:
		Connected to 120.77.222.217.
		sftp>
	
	* `help`:显示帮助信息
	* `ls / lls`：显示远端/ 本地目录列表
	* `cd / lcd`: 切换远端/ 本地路径
	* `mkdir / lmkdir`：创建远端/ 本地目录
	* `pwd / lpwd`:显示远端/ 本地当前工作目录
	* `get`:下载文件
	* `put`:上传文件
	* `rm`：删除远端文件
	* `bye / exit / quit`: 退出sftp
	
##进程管理
1. 进程查询 -**ps**

		AdministratordeiMac:img administrator$ ps -ef
  		UID   PID  PPID   C STIME   TTY           TIME CMD
    	0     1     0   0 一11上午 ??         3:26.43 /sbin/launchd
    	0    41     1   0 一11上午 ??         0:28.07 /usr/sbin/syslogd
    	0    42     1   0 一11上午 ??         0:15.52 /usr/libexec/UserEventAgent (System)
		.......
    	0    47     1   0 一11上午 ??         0:25
    	
2. 终止进程-**kill**

		AdministratordeiMac:img administrator$ kill 1234
		AdministratordeiMac:img administrator$ kill -9 1234
		
3. 将进程至于后台运行
	* `Ctrl+Z`
	* `&`
	
			[root@iZwz97tbgo9lkabnat2lo8Z ~]# mongod &
			[root@iZwz97tbgo9lkabnat2lo8Z ~]# redis-server
			...
			^Z
			[4]+  Stopped                 redis-server
			
4. **jobs** --查询后台进程

 		AdministratordeiMac:img administrator$ jobs
 		
5. **bg** -让进程在后台运行

		AdministratordeiMac:img administrator$ bg %4
		
6. **fg** --将后台进程置于前台

	AdministratordeiMac:img administrator$ fg %4
	> 说明：置于前台的进程可以用`Ctrl+C`来终止它。
7. **top**-进程健康

		AdministratordeiMac:img administrator$ top
		
		Processes: 340 total, 2 running, 338 sleeping, 1369 threads                                                          		14:46:30
		Load Avg: 2.65, 1.93, 1.61  CPU usage: 4.83% user, 3.38% sys, 91.78% idle
		SharedLibs: 339M resident, 72M data, 105M linkedit. MemRegions: 54087 total, 3898M resident, 	211M private, 1274M shared.
		PhysMem: 8785M used (1842M wired), 7598M unused. VM: 1505G vsize, 1110M framework vsize, 0(0) swapins, 0(0) swapouts.
		Networks: packets: 1725240/1049M in, 688716/124M out. Disks: 161639/5099M read, 1113060/8508M 		written.

		PID    COMMAND      %CPU TIME     #TH   #WQ  #PORT MEM    PURG   CMPR PGRP  PPID  STATE    BOOSTS          %CPU_ME %CPU_OTHRS
		30229  top          2.6  00:00.76 1/1   0    23    3192K  0B     0B   30229 5094  running  *0[1]           0.00000 0.00000
		30228  quicklookd   0.0  00:00.08 4     1    88    4404K  28K    0B   30228 1     sleeping  0[0]           0.00000 0.00000
		.......
		
		
##系统性能

1. 查看系统活动消息 --**sar**
2. 查看内存使用情况 --**free**
3. 查看进程使用内存状况-**pmap**
4. 报告设备CPU和I/O统计信息 -**iostat**

		 AdministratordeiMac:img administrator$ iostat
              disk0               disk2       cpu    load average
    		KB/t  tps  MB/s     KB/t  tps  MB/s  us sy id   1m   5m   15m
   			10.94    7  0.07     9.15    0  0.00   1  1 98  1.55 1.79 1.64