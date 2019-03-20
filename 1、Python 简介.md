###Python简介

* 1994年1月：Python 1.0正式发布。

* 2000年10月16日：Python 2.0发布，增加了实现完整的垃圾回收，提供了对Unicode的支持。与此同时，Python的整个开发过程更加透明，社区对开发进度的影响逐渐扩大，生态圈开始慢慢形成。
* 2008年12月3日：Python 3.0发布，它并不完全兼容之前的Python代码，不过因为目前还有不少公司在项目和运维中使用Python 2.x版本，所以Python 3.x的很多新特性后来也被移植到Python 2.6/2.7版本中。

###Python的应用领域

目前Python在云基础设施、DevOps、网络爬虫开发、数据分析挖掘、机器学习等领域都有着广泛的应用，因此也产生了Web后端开发、数据接口开发、自动化运维、自动化测试、科学计算和可视化、数据分析、量化交易、机器人开发、图像识别和处理等一系列的职位。


####其他工具介绍

* IDLE - 自带的集成开发工具IDLE是安装Python环境时自带的集成开发工具，如下图所示。但是由于IDLE的用户体验并不是那么好所以很少在实际开发中被采用。
* Sublime - 文本编辑神器
* 首先可以通过官方网站下载安装程序安装Sublime 3或Sublime 2。

安装包管理工具。通过快捷键Ctrl+`或者在View菜单中选择Show Console打开控制台，输入下面的代码。

* Sublime 3
`import  urllib.request,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler()));open(os.path.join(ipp,pf),'wb').write(urllib.request.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read())`

* Sublime 2
`import  urllib2,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();os.makedirs(ipp)ifnotos.path.exists(ipp)elseNone;urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler()));open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read());print('Please restart Sublime Text to finish installation')`
* 安装插件。通过Preference菜单的Package Control或快捷键Ctrl+Shift+P打开命令面板，在面板中输入Install Package就可以找到安装插件的工具，然后再查找需要的插件。推荐大家安装以下几个插件：

		1。SublimeCodeIntel - 代码自动补全工具插件。
	
		2.Emmet - 前端开发代码模板插件。
	
		3.Git - 版本控制工具插件。
	
		4.Python PEP8 Autoformat - PEP8规范自动格式化插件。
	
		5.ConvertToUTF8 - 将本地编码转换为UTF-8。

* **PyCharm - Python开发神器**
* 使用turtle在屏幕上绘制图形。

		import turtle

		turtle.pensize(4)
		
		turtle.pencolor('red')
		
		turtle.forward(100)
		
		turtle.right(90)
		
		turtle.forward(100)
		
		turtle.right(90)
		
		turtle.forward(100)
		
		turtle.right(90)
		
		turtle.forward(100)
		
		turtle.mainloop()