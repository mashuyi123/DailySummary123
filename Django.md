**pip install Django==2.1.1  安装**

## 1、创建项目 ##
### 创建项目命令 ###
	django-admin startproject myblog

### 项目目录结构及简介 ###
**1、manage.py** 与项目进行交互的命令行工具集入库（项目管理器）

	python manage.py
	python manage.py runserver
	python manage.py runserver 9999
**2、myblog目录**

	项目的一个容器
	包含项目最基本的一些配置
	目录名称不建议修改
	
	wsgi.py:(wsgi python服务器网关接口），python应用于web服务器之间的接口
	urls.py:url配置文件，python中所有地址（页面）都需要自己去配置URL
	settings.py:项目总配置文件，包含数据库，web应用，时间等各种配置
	init.py:python中声明模块的文件，内容默认为空

![](https://i.imgur.com/7UkL2NV.png)

**3、创建应用**

进入项目manage.py同级目录，命令行输入：python manage.py startapp blog;添加用用名到settings.py中的installed_apps里

	migrations
		数据迁移模块
	admin.py
		该应用的后台管理系统配置
	apps.py
		该应用的一些配置
	models.py
		数据模块，使用ORM框架
	tests.py
		自动化测试模块
		Django提供了自动化测试功能，在这里编写测试脚本
	views.py
		执行响应的代码所在模块
		代码逻辑处理的主要地点
		项目中大部分代码再次编写

![](https://i.imgur.com/fgkJnjq.png)

![](https://i.imgur.com/jDXXb8V.png)

**4、查看python包的路径**

![](https://i.imgur.com/u6ZpM4L.png)

**5、创建一个页面（响应）**

	编辑blog.views
		每个响应对应一个函数，函数必须返回一个响应
		函数必须存在一个参数，一般约定为request
		每一个响应（函数）对应一个URL
	配置URL
		编辑urls.py
		每个URL都以url的形式写出来
		url函数放在urls.py的urlpatterns列表中
		url函数三个参数：URL（正则），响应方法，名称
	启动服务查看效果
		python manage.py runserver
	