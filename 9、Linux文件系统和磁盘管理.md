##文件系统
####文件和路径
1. 命名规则：文件的最大长度与文件系统类型有关，一般情况下，文件名不应该超过255个字符，虽然绝大多数的字符都可以用于文件名，但是最好使用英文大小写字母、数字、下划线、点这样的符号。文件名中虽然可以使用空格，但应该尽可能避免使用空格，否则在输入文件名是需要将文件名放在双引号中或者通过`\`对空格进行转义
2. 扩展名：在Linux系统下文件的扩展名是可选的，但是使用扩展名有助于对明见内容的理解。有些应用程序要通过扩展名来识别文件，但是更多的应用程序并不依赖文件的扩展名，就像`file`命令在识别文件时候并不是依据扩展名来判定文件的类型
3. 隐藏文件：以点开头的文件在Linux系统中是隐藏文件（不可见文件）

####目录结构
1. **/bin -基本命令的二进制文件。**
2. /boot -引导加载程序的静态文件。
3. **/dev - 设备文件**
4. **/ect - 配置文件**
5. /home - 普通用户主目录的父目录
6. **/lib - 共享文件**
7. /lib64 -共享64位库文件
8. /lost+found - 存放未连接文件
9. /media - 自动识别设备的挂载目录
10. /mnt - 临时挂载文件系统的挂载点
11. /opt - 可选插件软件包安装位子
12. /proc - 内科和进程信息
13. **/root  -超级管理员用户主目录**
14. /run  - 存放系统运行时需要的东西
15. /sbin - 超级用户的二进制文件
16. **/sys - 设备的伪文件系统**
17. **/tmp - 临时文件夹**
18. **/usr - 用户应用目录**
19. /var - 变量数据目录

##访问权限
###1、chmod --改变文件模式比特

	AdministratordeiMac:test administrator$ ls -l

	total 15072
	drwxr-xr-x   3 administrator  staff       96  4  1 15:50 backuo
	-rw-r--r--@  1 administrator  staff     2381  1 23  2017 index.html
	...
	AdministratordeiMac:test administrator$ chmod g+w,o+w index.html
	AdministratordeiMac:test administrator$ ls -l
	total 15072
	drwxr-xr-x   3 administrator  staff       96  4  1 15:50 backuo
	-rw-rw-rw-@  1 administrator  staff     2381  1 23  2017 index.html
> 说明：通过上面的示例可以看出，用chmod改变文件模式比特有两种方式：
 
> * 一种是字符设定法
> * 另一种是数字设定法
> 
> 除了chmod之外，可以通过umask来设定哪些权限将在新文件的默认权限中被删除

长格式查看目录或者文件时显示结果及其对应权限的数值如下图所示。
       
![](https://github.com/jackfrued/Python-100-Days/blob/master/Day31-35/res/file-mode.png?raw=true)


       
### 2、chown --改变文件所有者

	[root@iZwz97tbgo9lkabnat2lo8Z ~]# ls -l
	...
	-rw-r--r--  1 root root     54 Jun 20 10:06 readme.txt
	...
	[root@iZwz97tbgo9lkabnat2lo8Z ~]# chown hellokitty readme.txt
	[root@iZwz97tbgo9lkabnat2lo8Z ~]# ls -l
	...
	-rw-r--r--  1 hellokitty root     54 Jun 20 10:06 readme.txt
	...     
##磁盘管理

1、列出文件系统的磁盘使用情况-**df**

	AdministratordeiMac:test administrator$ df -h
	Filesystem      Size   Used  Avail Capacity iused               ifree %iused  	Mounted on
	/dev/disk1s1   234Gi  133Gi   98Gi    58% 2236430 9223372036852539377    0%   /
	devfs          186Ki  186Ki    0Bi   100%     645                   0  100%   /dev
	/dev/disk1s4   234Gi  2.0Gi   98Gi     2%       1 9223372036854775806    0%   /private/var/vm
	map -hosts       0Bi    0Bi    0Bi   100%       0                   0  100%   /net
	map auto_home    0Bi    0Bi    0Bi   100%       0                   0  100%   /home

2、磁盘分区表操作 -**fdisk**

	AdministratordeiMac:test administrator$ fdisk -l
	fdisk: illegal option -- l
	usage: fdisk [-ieu] [-f mbrboot] [-c cyl -h head -s sect] [-S size] [-r] [-a style] disk
	-i: initialize disk with new MBR
	-u: update MBR code, preserve partition table
	-e: edit MBRs on disk interactively
	-f: specify non-standard MBR template
	-chs: specify disk geometry
	-S: specify disk size
	-r: read partition specs from stdin (implies -i)
	-a: auto-partition with the given style
	-d: dump partition table
	-y: don't ask any questions
	-t: test if disk is partitioned
	`disk' is of the form /dev/rdisk0.
	auto-partition styles:
 	boothfs     8Mb boot plus HFS+ root partition (default)
 	hfs         Entire disk as one HFS+ partition
  	dos         Entire disk as one DOS partition
  	raid        Entire disk as one 0xAC partition
  	
  3、格式化文件系统 --**mkfs**
  
  4、文件系统检查 -**fsck**
  
  5、挂载/卸载 --**mount / umout**
  