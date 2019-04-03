##关系数据库入门
###关系数据库概述
1. 数据持久化 --将数据保存到（在掉电情况下）能够长久保存数据的存储介质中
2. 数据库发展史 -网状数据库、层次数据库、关系数据库
 
	>1970年，IBM研究员E.F.Codd在Communication of the ACM上发表名为A Relation Model of Data for Large Shared Data Banks的论文，提出了关系模型的概念，奠定了关系模型的理论基础。后来Codd又陆续发表多篇，论述范式理论和衡量关系系统的12条标准，用书序理论奠定了数据关系库的基础。
	
3. 关系数据特点。
	* 理论基础：集合论和关系代数
	* 具体表象：用二维表（有行和列）组织数据
	* 编程语言：结构化查询语言（SQL）
4. E-R图
	* 实体：矩形框
	* 属性：椭圆框
	* 关系:菱形框
	* 重数：-1：1 / 1：N / M:N
5. 关系数据库产品
	* [Oracle](https://www.oracle.com/index.html)-目前世界上使用最为广泛的数据库管理系统。
		* 作为一个通用的数据库系统，它具有完整的数据库管理功能；
		* 作为一个关系数据库，它是一个完备关系的产品；
		* 作为分布式数据库，它实现了分布处理的功能。
		* 在新的版本中，还引入了多承租方架构，使用该架构氪轻松部署和管理数据库云
	* [DB2](https://www.ibm.com/analytics/us/en/db2/) -IBM公司开发，主要运行与Unix（包括IBM自家的AIX）、Linux以及Window服务器版等系统的关系数据库。DB2历史悠久且被认为是最早使用SQL的数据库产品，他拥有较为强大的商业智能功能。
	* [SQL Server](https://www.microsoft.com/en-us/sql-server/)-有Microsoft开发和推广的关系型数据库产品，最初适用于中小企业的数据库管理，但是近年来他的应用范围有所扩展，部分大企业甚至跨国公司也开始基于它来构建自己的数据库系统。
	* [MySQL](https://www.mysql.com/) -MySQL是开放源代码的，任何人都可以在GPL（General Publish License）的许可下下载，并根据个性化的需求对其进行修改。MySQL因为速度、可靠性和适应性而备受关注。
	* [PostgreSQl](https://github.com/jackfrued/Python-100-Days/blob/master/Day36-40)--在BSD（Berkeley Software Distribution license）许可证下发行的开发源代码的关系数据库产品。

##MySQL简介
1. 安装和配置
2. 常用命令

###SQL详解
1. DDL (Data Definition Language 数据库定义语言)

	```
	-- 创建数据库SRS
	drop databse if exists SRS;
	create database SRS default charset utf8;
	
	-- 切换到SRS
	use SRS;
	
	-- 创建学院表
	create table tb_college
	(
	 collid int not null auto_increatement comment '学院编号',
	 collname varchar(50) not  null comment '学院名称',
	 collmaster varchar(20) not null comment '院长姓名',
	 collweb varchar(511) default '' comment '学院网站',
	 primary key (collid)
	);
			
	-- 添加唯一性约束
	alert table tb_collage add constraint uni_college_collname unique(collname);
	-- alert table tb_collage drop index uni_collage_cllname
	
	-- 创建学生表
	create table tb_student
	(
	stuid int not null comment '学号',
	stuname varchar(20) not null comment '学生姓名',
	stusex bit default 1 comment '性别',
	stubirth date not null comment '出生日期',
	stuaddr varchar(255) default '' comment '籍贯',
	collid int not null comment '所属学院',
	primary key (stuid)
	);
	
	-- 添加外键约束
	alert table tb_student add constraint fk_student_collid foreign key (collid) references tb_college (collid);
	
	-- 创建教师表
	create table tb_teacher
	(
	teacherid int not null comment '教师工号',
	tname varchar(20) not null comment '教师名称',
	ttitle varchar(10) default '' comment '职称',
	collid int not null comment '所属学院编号'
	);
	
	-- 添加主键约束
	alert table tb_teacher add constraint pk_teacher primary key (teacherid);
	
	-- 添加外键约束
	alert table tb_teacher add constraint fk_teacher_collid foreign key  (collid) references tb_college(collid);
	
	-- 创建课程表
	create table tb_course
	(
	courseid int not null comment '课程编号',
	cname varchar(50) not null comment '课程名称',
	ccredit tinyiny not null comment '学分'
	tid int not null comment '教师工号',
	primary key (courseid)
	);
	
	-- 添加外键约束
	alert table tb_course add constraint fk_course_tid foreign key (tid) refercences tb_teacher (teacherid);
	
	
	-- 创建学生选课程表
	create table tb_score
	(
	scid int not null auto_increment comment '选课编号',
	sid int not null comment '学号',
	cid int not null commtn '课程编号',
	selectdate datetime comment '选课时间日期',
	score decimal(4,1) comment '考试成绩',
	primary key (scid)
	);
	
	-- 检测添加约束（MySQL中检测约束不生效）
	alert table tb_score add constraint ck_score_score check (score bwtween 0 and 100);
	
	-- 添加外键约束
	alert table tb_score add constraint fk_score_sid foreign key (sid) references tb_student (stuid);
	alert table tb_score add constraint fk_score_cid foreign key (cid) references tb_course(courseid);
			
	```
2.DML (Data Manipulation Language）数据操纵语言

	```
	-- 插入学院数据
	inset into tb_college
	(collname,collmaster, collweb) values
	('计算机学院'，‘左冷禅’, 'http://www.abc.com'),
	('外国语学院', '岳不群', 'http://www.xyz.com'),
	('经济管理学院', '风清扬', 'http://www.foo.com');
	
	-- 插入学生数据
	insert into tb_student
	(stuid, stuname, stusex, stubrith, stuaddr, collid) values
	(1001, '向问天', 1, '1990-3-3','四川成都'，1),
	(1002, '任我行', 1, '1992-2-2', '湖南长沙', 1),
	(1033, '任盈盈', 0, '1989-12-3', '湖南长沙', 1),
	(1572, '余沧海', 1, '1993-7-19', '四川成都', 1),
	(1378, '岳灵珊', 0, '1995-8-12', '四川绵阳', 1),
	(1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
	(2035, '令狐冲', 1, '1988-6-30', '陕西咸阳', 2),
	(3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
	(3755, '龙傲天', 1, '1993-1-25', '广东东莞', 3),
	(3923, '向天问', 0, '1985-4-17', '四川成都', 3),
	(2177, '隔壁老王', 1, '1989-11-27', '四川成都', 2);
	
	-- 插入老师数据
	insert into tb_teacher
	(teacherid, tname, ttitle, collid) values
	(1122,'张三丰','教授', 1 ),
	(1133, '宋远桥', '副教授', 1),
	(1144, '杨逍', '副教授', 1),
	(2255, '范遥', '副教授', 2),
	(3366, '韦一笑', '讲师', 3); 
	
	-- 插入课程数据
	insert into tb_course
	(courseid, cname, ccredit, tid) values
	(1111, 'Python程序设计', 3, 1122),
	(2222, 'Web前端开发', 2, 1122),
	(3333, '操作系统', 4, 1122),
	(4444, '计算机网络', 2, 1133),
	(5555, '编译原理', 4, 1144),
	(6666, '算法和数据结构', 3, 1144),
	(7777, '经贸法语', 3, 2255),
	(8888, '成本会计', 2, 3366),
	(9999, '审计', 3, 3366);
	
	-- 插入选课数据
	inset into tb_score
	(sid ,cid ,selectdate, score) values
	(1001, 1111, now(), 96),
	(1001, 2222, now(), 87.5),
	(1001, 3333, now(), 100),
	(1001, 4444, now(), null),
	(1001, 6666, now(), 100),
	(1002, 1111, now(), 65),
	(1002, 5555, now(), 42),
	(1033, 1111, now(), 92.5),
	(1033, 4444, now(), 78),
	(1033, 5555, now(), 82.5),
	(1572, 1111, now(), 78),
	(1378, 1111, now(), 82),
	(1378, 7777, now(), 65.5),
	(2035, 7777, now(), 88),
	(2035, 9999, now(), 70),
	(3755, 1111, now(), 72.5),
	(3755, 8888, now(), 93),
	(3755, 9999, now(), null);
	
	
	-- 删除数据
	delete from tb_student where stuid=2177;
	
	-- 更新数据
	update tb_score set score=null where sid=1002 and cid=111
	
	```
3. DQL （Data Query Language）数据查询语言

	```
	-- 查询所有学生信息
	select * from tb_student;
	select stuid, stuname, stusex, stubirth, stuaddr, collid
	from tb_student;
	
	-- 查询所有课程名称及学分（投影和别名）
	select cname as 课程名称 , ccredit as 学分 form tb_course;
	
	-- 查询所有女学生的姓名和出生日期（筛选）
	select stuname, stubirth from tb_student where stusex=0;
	
	-- 查询所有80后女学生的姓名、性别（显示性别‘女’）和出生日期（筛选）
	select stuname,'女' as stusex,stubirth from tb_student
	where stubirth between '1909-1-1' and '1990-1-0' and stusex=0;
	
	-- 查询姓‘林’的学生姓名和性别（模糊）
	select stuname ,if(stusex,'男', '女') as stusex
	from tb_student where stuname like '林%';
	
	-- 查询姓‘张’名字总共两个字的老师姓名和职称（模糊）
	select tname from tb_teacher where taname like '张_';
	
	-- 查询‘张’民资总共三个字的老师姓名和职称（模糊）
	select tname ,ttitle from tb_teacher where tname like '张__';
	
	-- 查询名字中有‘天’字学生的姓名（模糊）
	select tname from tb_student where stuname like '%天%'
	
	-- 查询学生籍贯（去重）
	select distinct stuaddr from tb_student 
	where stuaddr<>'' and stuaddr is not null;
	
	-- 查询男学生的姓名和生日按年龄从大到小排序
	select stuname, srubirth from tb_student
	where stusex=1 order by stubirth asc;
	
	-- 查询年龄最大/最小的学生的出生日期（聚合函数）
	select min(stubirth) from tb_student;
	select max(stubirth) from tb_student;
	
	-- 查询学生/男学生/女学生的总人数
	select count(stuid) from tb_student;
	select count(stuid) from tb_student where stusex=1;
	select conut(stuid) from tb_student where setsex=0;
	
	-- 查询1111课程的平均分/最低分/最高分/选课人数/考试人数
	select avg(score) from tb_score where cid=1111;
	select min(score) from tb_score where
	
	-- 查询男女学生人数（分组和聚合函数）
	select if(stusex, '男', '女') as 性别, count(stussex) as 人数
	
 	
	```
			