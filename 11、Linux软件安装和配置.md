##软件安装和配置
####使用包管理工具
1. **yum** --Yellowdog Updater Modified
	* `yum search`:搜索软件包，例如` yum search nginx`.
	* `yum list installed`:列出已经安装的软件包，例如`yum list installed | grep zlib`.
	* `yum install`: 安装软件包，例如`yum install nginx`
	* `yum remove`:删除软件包，例如：`yum remove ngnix`
	* `yum update`:更新软件包，例如`yum update`可以更新所有软件包，而`yum update tar`只会更新tar
	* `yum check-update`: 检查有哪些可以更新的软件包
	* `yum info`:显示软件包相关信息，例如`yum info nginx`
2. **rpm** - Redhat Package Manager
	* 安装软件包：`rpm -ivh <packagename>.rpm`.
	* 移除软件包：`rpm -e <packagename>`
	* 查询软件包：`rpm -qa`,例如可以用`rpm -qa | grep mysql`来检查是否安装了MySQL相关软件包

下面以Nginx为例，演示如何使用yum安装软件。

	[root@iZwz97tbgo9lkabnat2lo8Z ~]# yum -y install nginx
	...
	Installed:
  	nginx.x86_64 1:1.12.2-2.el7
	Dependency Installed:
 	 nginx-all-modules.noarch 1:1.12.2-2.el7
  	nginx-mod-http-geoip.x86_64 1:1.12.2-2.el7
  	nginx-mod-http-image-filter.x86_64 1:1.12.2-2.el7
  	nginx-mod-http-perl.x86_64 1:1.12.2-2.el7
  	nginx-mod-http-xslt-filter.x86_64 1:1.12.2-2.el7
  	nginx-mod-mail.x86_64 1:1.12.2-2.el7
  	nginx-mod-stream.x86_64 1:1.12.2-2.el7
	Complete!
	[root@iZwz97tbgo9lkabnat2lo8Z ~]# yum info nginx
	Loaded plugins: fastestmirror
	Loading mirror speeds from cached hostfile
	Installed Packages
	Name        : nginx
	Arch        : x86_64
	Epoch       : 1
	Version     : 1.12.2
	Release     : 2.el7
	Size        : 1.5 M
	Repo        : installed
	From repo   : epel
	Summary     : A high performance web server and reverse proxy server
	URL         : http://nginx.org/
	License     : BSD
	Description : Nginx is a web server and a reverse proxy server for HTTP, SMTP, POP3 and
            : IMAP protocols, with a strong focus on high concurrency, performance and low
            : memory usage.
	[root@iZwz97tbgo9lkabnat2lo8Z ~]# nginx -v
	nginx version: nginx/1.12.2
移除Ngnix

	[root@iZwz97tbgo9lkabnat2lo8Z ~]# nginx -s stop
	[root@iZwz97tbgo9lkabnat2lo8Z ~]# yum -y remove nginx
	
> MacOS下安装用 **Homebrew**