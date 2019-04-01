####实用程序

#####文件和文件夹操作

1、创建/删除目录-**mkdir / rmdir**

	AdministratordeiMac:test administrator$ mkdir abc
	AdministratordeiMac:test administrator$ mkdir -p xyz/abc
	AdministratordeiMac:test administrator$ rmdir abc

2、创建/删除文件 -- **touch / rm**

	AdministratordeiMac:test administrator$ touch readme.text
	AdministratordeiMac:test administrator$ touch error.ext
	AdministratordeiMac:test administrator$ rm -rf error.ext
	AdministratordeiMac:test administrator$ rm error.txt
	
* touch命令用于创建空白文件或者修改文件时间。在Linux系统中一个文件有三种时间：
	* 更改内容的时间 --mtime
	* 更改权限的时间 - ctime
	* 最后访问时间 -- atime
* rm的几个重要参数：
	* -i：交互是删除 
	* -r：删除目录并递归目录中的文件和目录
	* -f：强制删除，忽略不存在的文件，没有任何提示

3、切换和查看当前工作目录 - **cd / pwd**
> 说明： `cd`命令后面可以跟相对路径（以当前路径作为参考）或绝对路径（以/开头）来切换到指定目录，也可以用 `cd ..`来返回上一级目录

4、查看目录内容 -**ls**

* -l：以长格式查看文件和目录
* -a：显示以点开头的文件和目录（隐藏文件）
* -R：遇到目录需要进行递归展开（继续列出目录下面的文件和目录）
* -d：只列出目录，不列出其他内容
* -S / -t：按大小/时间排序

5、查看文件内容-**cat / head / tail / more / less**

	AdministratordeiMac:test administrator$ wget http://www.baidu.com/
	--2019-04-01 15:43:11--  http://www.baidu.com/
	正在解析主机 www.baidu.com (www.baidu.com)... 14.215.177.39, 14.215.177.38
	正在连接 www.baidu.com (www.baidu.com)|14.215.177.39|:80... 已连接。
	已发出 HTTP 请求，正在等待回应... 200 OK
	长度：2381 (2.3K) [text/html]
	正在保存至: “index.html”

	index.html          100%[===================>]   2.33K  --.-KB/s  用时 0s      

	2019-04-01 15:43:11 (162 MB/s) - 已保存 “index.html” [2381/2381])

	AdministratordeiMac:test administrator$ cat index.html
	
	<!DOCTYPE html>
	<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/	html;charset=utf-8><meta http-equiv=X-UA-Compatible 	content=IE=Edge><meta content=always name=referrer><link rel=stylesheet 
	.......
	
	AdministratordeiMac:test administrator$ less index.html
	.....
	AdministratordeiMac:test administrator$ cat -n index.html | more
	.....
6、移动和拷贝文件 -**cp / mv**
	
	AdministratordeiMac:test administrator$ mkdir backuo
	AdministratordeiMac:test administrator$ cp index.html backuo/
	AdministratordeiMac:test administrator$ cd backuo
	AdministratordeiMac:backuo administrator$ ls
	index.html
	AdministratordeiMac:backuo administrator$ mv index.html readme.text
	AdministratordeiMac:backuo administrator$ ls
	readme.text
	AdministratordeiMac:backuo administrator$ 
7、查找文件和查找内容 -**find / grep**

	[root@iZwz97tbgo9lkabnat2lo8Z ~]# find / -name "*.html"
	/root/sohu.html
	/root/backup/sohu_index.html
	[root@izwz97tbgo9lkabnat2lo8z ~]# find . -atime 7 -type f -print
	[root@izwz97tbgo9lkabnat2lo8z ~]# find . -type f -size +2k
	[root@izwz97tbgo9lkabnat2lo8z ~]# find . -type f -name "*.swp" -delete
	[root@iZwz97tbgo9lkabnat2lo8Z ~]# grep "<script>" sohu.html -n
	20:<script>
	[root@iZwz97tbgo9lkabnat2lo8Z ~]# grep -E \<\/?script.*\> sohu.html -n
	20:<script>
	22:</script>
	24:<script src="//statics.itc.cn/web/v3/static/js/es5-
	...
>说明：grep在搜索字符串时可以使用正则表达式，如果需要使用正则表达式可以`grep -E`或则使用`egrep`

8、链接 -**ln**

	AdministratordeiMac:test administrator$ ls -l index.html
	-rw-r--r--@ 1 administrator  staff  2381  1 23  2017 index.html
	AdministratordeiMac:test administrator$ ln -s /ect/centos-release sysinfo
	AdministratordeiMac:test administrator$ ls -l sysinfo
	lrwxr-xr-x  1 administrator  staff  19  4  1 16:00 sysinfo -> /ect/	centos-release
> 说明：链接可以分为硬链接和软链接（符号链接）。硬链接可以认为是一个指向文件数据的指针，就像python中对象的引用计数，每添加一个硬链接，文件的对应链接数就增加1，只有文件的链接数为0时，文件所对应的存储空间才有可能被其他文件覆盖。

> 我们平常删除文件时其实并没有删除硬盘上的数据，我们**删除的只是一个指针**，或者说是数据的一条使用记录，所以类似于“文件粉碎机”之类的软件在“粉碎”文件时删除文件的指针，还会在文件对应的存储区域填入数据来保证文件无法再恢复。

> 软链接类似于Window系统下的快捷方式，当软链接链接的文件删除时候，软链接也就失效了

9、压缩、解压缩、和归档、解归档-**gzip / gunzip / xz / tar**

	AdministratordeiMac:test administrator$ wget http://download.redis.io/	releases/redis-4.0.10.tar.gz
	--2019-04-01 16:17:41--  http://download.redis.io/releases/	redis-4.0.10.tar.gz
	正在解析主机 download.redis.io (download.redis.io)... 109.74.203.151
	正在连接 download.redis.io (download.redis.io)|109.74.203.151|:80... 已连接。
	已发出 HTTP 请求，正在等待回应... 200 OK
	长度：1738465 (1.7M) [application/x-gzip]
	正在保存至: “redis-4.0.10.tar.gz”

	redis-4.0.10.tar.gz             100%	
	[=====================================================>]   
	1.66M  44.1KB/s  用时 1m 48s  

	2019-04-01 16:19:29 (15.7 KB/s) - 已保存 	“redis-4.0.10.tar.gz” [1738465/1738465])

	AdministratordeiMac:test administrator$ ls redis*
	redis-4.0.10.tar.gz
	AdministratordeiMac:test administrator$ gunzip redis-4.0.10.tar.gz
	AdministratordeiMac:test administrator$ ls redis*
	redis-4.0.10.tar
	AdministratordeiMac:test administrator$ tar -xvf redis-4.0.10.tar
	x redis-4.0.10/
	x redis-4.0.10/.gitignore
	x redis-4.0.10/00-RELEASENOTES
	x redis-4.0.10/BUGS
	x redis-4.0.10/CONTRIBUTING
	......
	AdministratordeiMac:test administrator$ ls redis*
	redis-4.0.10.tar

	redis-4.0.10:
	00-RELEASENOTES		INSTALL			deps			runtest-sentinel	utils
	BUGS			MANIFESTO		redis.conf		sentinel.conf
	CONTRIBUTING		Makefile		runtest			src
	COPYING			README.md		runtest-cluster		tests
10、其它工具 - **sort / uniq /diff / tr / cut / paste / file / wc**


	AdministratordeiMac:test administrator$ cat readme.text
	grape
	apple
	pitaya
	AdministratordeiMac:test administrator$ cat bar.txt
	100
	200
	300
	400
	AdministratordeiMac:test administrator$ paste readme.text bar.txt
	grape	100
	apple	200
	pitaya	300
		400
	AdministratordeiMac:test administrator$ paste readme.text bar.txt > 	hello.txt
	AdministratordeiMac:test administrator$ cat hello.txt
	grape	100
	apple	200
	pitaya	300
		400
	AdministratordeiMac:test administrator$ cut -b 4-8 hello.txt
	pe	10
	le	20
	aya	3
	0
	AdministratordeiMac:test administrator$ cat hello.txt | tr '\t' ','
	grape,100
	apple,200
	pitaya,300
	,400

	AdministratordeiMac:test administrator$ wget https://www.baidu.com/img/
	bd_logo1.png
	--2019-04-01 16:33:51--  https://www.baidu.com/img/bd_logo1.png
	正在解析主机 www.baidu.com (www.baidu.com)... 14.215.177.39, 14.215.177.38
	正在连接 www.baidu.com (www.baidu.com)|14.215.177.39|:443... 已连接。
	已发出 HTTP 请求，正在等待回应... 200 OK
	长度：7877 (7.7K) [image/png]
	正在保存至: “bd_logo1.png”

	bd_logo1.png                    100%
	[=====================================================>]   
	7.69K  --.-KB/s  用时 0.006s  

	2019-04-01 16:33:51 (1.19 MB/s) - 已保存 “bd_logo1.png” [7877/7877])

	AdministratordeiMac:test administrator$ file bd_logo1.png
	bd_logo1.png: PNG image data, 540 x 258, 8-bit colormap, non-interlaced
	AdministratordeiMac:test administrator$ wc index.html
       2     162    2381 index.html
	AdministratordeiMac:test administrator$ wc - l index.html
	wc: -: open: No such file or directory
	wc: l: open: No such file or directory
       2     162    2381 index.html
       2     162    2381 total 
####管道和重定向
1、管道的使用 -**l**
示例：查找当前目录下文件个数

	AdministratordeiMac:test administrator$ find ./ | wc -l
     666
示例：列出当前路径下的文件和文件夹，给每一项加一个编号。

	AdministratordeiMac:test administrator$ ls | cat -n
     1	backuo
     2	bar.txt
     3	bd_logo1.png
     4	foo.txt
     5	hello.txt
     6	index.html
     7	readme.text
     8	redis-4.0.10
     9	redis-4.0.10.tar
    10	sysinfo
    11	xyz

示例：查找bar.txt中包含的apple，但不包含100的总数

	AdministratordeiMac:test administrator$ cat hello.txt | grep apple | grep -v 100 |  wc -l
       1
2、输入重定向和错误重定向-**> / >> / 2>**

	AdministratordeiMac:test administrator$ cat fruit.txt
	banana
	apple
	grape
	apple
	grape
	watermelon
	pear
	pitaya
	AdministratordeiMac:test administrator$ cat fruit.txt | sort | uniq > 	end.txt
	AdministratordeiMac:test administrator$ cat end.txt
	apple
	banana
	grape
	pear
	pitaya
	watermelon
3、输入重定向-**<**

	AdministratordeiMac:test administrator$ echo 'hello,world!' > hello.txt
	AdministratordeiMac:test administrator$ wall < hello.txt
                                                                               
	Broadcast Message from administrator@AdministratordeiMac.local                 
        (/dev/ttys000) at 17:15 CST...                                         
                                                                               
	hello,world!                                                                   
                                                                               
	AdministratordeiMac:test administrator$ echo 'I will show you world! ' 	>> hello.txt
	AdministratordeiMac:test administrator$ wall < hello.txt
                                                                               
	Broadcast Message from administrator@AdministratordeiMac.local                 
        (/dev/ttys000) at 17:16 CST...                                         
                                                                               
	hello,world!                                                                   
	I will show you world!

####别名

1、alias

	AdministratordeiMac:test administrator$ alias ll='ls -l'
	AdministratordeiMac:test administrator$ ll
	total 15072
	drwxr-xr-x   3 administrator  staff       96  4  1 15:50 backuo
	-rw-r--r--@  1 administrator  staff       16  4  1 16:29 bar.txt
	-rw-r--r--@  1 administrator  staff     7877  9  3  2014 bd_logo1.png
	-rw-r--r--   1 administrator  staff       42  4  1 17:11 end.txt
	drwxr-xr-x   2 administrator  staff       64  4  1 16:28 foo.txt
	-rw-r--r--@  1 administrator  staff       54  4  1 17:12 fruit.txt
	-rw-r--r--   1 administrator  staff       37  4  1 17:16 hello.txt
	-rw-r--r--@  1 administrator  staff     2381  1 23  2017 index.html
	-rw-r--r--@  1 administrator  staff       19  4  1 16:27 readme.text
	...                       
2、unalias

	AdministratordeiMac:test administrator$ unalias ll
	AdministratordeiMac:test administrator$ ll
	-bash: ll: command not found

####其他程序
1、时间和日期-**date / cal**	                                

	AdministratordeiMac:test administrator$ date
	2019年 4月 1日 星期一 17时25分41秒 CST
	AdministratordeiMac:test administrator$ cal
    	  四月 2019         
	日 一 二 三 四 五 六  
    	1  2  3  4  5  6  
	 7  8  9 10 11 12 13  
	14 15 16 17 18 19 20  
	21 22 23 24 25 26 27  
	28 29 30              
                      
	AdministratordeiMac:test administrator$ cal 9 2020
     	 九月 2020         
	日 一 二 三 四 五 六  
       	1  2  3  4  5  
 	6  7  8  9 10 11 12  
	13 14 15 16 17 18 19  
	20 21 22 23 24 25 26  
	27 28 29 30           
2、录制操作脚本 -**script**

3、给用户发送消息 -**-mesg / write / wall / mail**
                                                       