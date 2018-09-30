**pip install Django==2.1.1  安装**

## 一、创建项目 ##
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
	
**6、第二种URL配置**
	
	在根urls.py中引入include
	在APP目录下创建urls.py文件，格式与根urls.py相同
	根urls.py中url函数第二个参数改为include（'blog.urls')

	注意事项：
		根urls.py针对APP配置的URL名称，是该APP所有URL的总路径
		配置URL时注意正则表达式结尾符号$和/

## 二、Templates ##
### Templates介绍 ###
template即html文件，使用了django模板语言（DTL），可以使用第三方模板如Jinja2
### 开发一个template ###
**1、步骤：**

	在APP根目录下创建一个Template目录
	在该目录下创建Html文件
	在views.py中返回render（）
**2、DTL使用方法**

	rander（）函数支持一个dict类型的参数，后台传递数据到前端，键为参数名，在模板中使用{{参数名}}来直接使用
**3、Templates注意点**

	Django查找Template，按照installed_apps中添加的顺序查找templates
	不用APP下templates目录中的同名.html文件会造成冲突
**4、解决Templates冲突方案**
	
	在APP的Templates目录下创建以APP名为名称的目录
	将html文件放入新创建的目录下
### Models介绍 ###
一个model对应数据库的一张数据表，Django中models以类的形式表现，包含一些基本字段及数据行为，ORM对象关系映射（object Relation Mapping):实现了对象和数据库之间的映射，隐藏了数据访问的细节，不需要编写SQL语句。
### 编写model ###
1、步骤：

	在应用跟目录下创建models.py,并引入model模块
	创建类，继承models.Model,该类即使一张数据表
	在类中创建字段
2、字段创建：
	
	字段即类里面的属性（变量）
	attr = models.CharField(max_lenth=64)
	类及类的字段官网：https://docs.djangoproject.com/en/2.1/ref/models/fields/
3、生成数据表（将模型映射成数据表）
	
	命令行进入manage.py同级目录
	执行python manage.py makemigrations app名（可选）
	再执行python manage.py migrate
	Django会自动再app/migrations/目录下生成移植文件
	执行python manage.py sqlmigrate 应用名 文件id 查看SQL语句
	默认sqlit3的数据库在项目根目录下db.sqlite3（可使用SQLLite Expert Personal打开，下载地址：http://www.sqliteexpert.com/download.html)
![](https://i.imgur.com/LUSDkXK.png)
![](https://i.imgur.com/dlWCf4A.png)
4、页面数据呈现
	后台步骤：
		views.py中import models
		article = models.Article.obkects.get(pk=1) //取出主键等于1的数据
		render(request,page,{'article' :article} //通过render将数据传递给前端
	前端步骤：
		模板可以直接使用对象以及对象的" ."操作，{{article.title}}