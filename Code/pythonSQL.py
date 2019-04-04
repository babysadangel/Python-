# -*- coding:utf-8 -*-

# ----------python访问MySQL数据库-----------

drop database if exists hrs;
creare dabase hrs default charaset utf8;

use hrs;

drop table if exists tb_emp;
drop table if exists tb_dept;

create table tb_dept
(
    dno int not null comment '编号',
    dname varchar(10) not null comment '名称',
    dloc varchar(20) not null comment '所在地',
    primary key (dno)
);

insert into tb_dept values
        (10, '会计部', '北京'),
	    (20, '研发部', '成都'),
	    (30, '销售部', '重庆'),
	    (40, '运维部', '深圳');

create table tb_emp
(
    eno int not null comment '员工编号',
    ename varchar(20) not null comment '员工姓名',
    job varchar(20) not null comment '员工职位',
    mgr int comment '主管编号',
    sal int not null comment '员工底薪',
    comm int comment '每月补贴',
    dno int comment '所在部门编号',
    primary key (eno)
);

alert table tb_emp add constraint fk_emp_dno foreign key (dno)  references tb_dept (dno);

insert into tb_emp values
    (7800, '张三丰', '总裁', null, 9000, 1200, 20),
	(2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
	(3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
	(3211, '张无忌', '程序员', 2056, 3200, null, 20),
	(3233, '丘处机', '程序员', 2056, 3400, null, 20),
	(3251, '张翠山', '程序员', 2056, 4000, null, 20),
	(5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
	(5234, '郭靖', '出纳', 5566, 2000, null, 10),
	(3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
	(1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
	(4466, '苗人凤', '销售员', 3344, 2500, null, 30),
	(3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
	(3577, '杨过', '会计', 5566, 2200, null, 10),
	(3588, '朱九真', '会计', 5566, 2500, null, 10);

# 在Python3中，我们通常使用纯三方库PyMySQL来访问数据库，他因该是目前最好的选择。

# 1、安装pymysql
    # pip install pymysql
# 2.添加一个部门

import pymysql

def main():
    no = int(input('编号：'))
    name = input('名字：')
    loc = input('所在地：')

    #1、创建书看了链接对象

    con = pymysql.connect(host='localhost',port=3036,
                            database='hrs',charset='utf8',
                            user='root',password='123456'
                            )
    try:
        #2.通过链接对象获取游标
    
        with con.cursor() as cursor:
            #3.通过游标执行SQL并获得执行结果
            result = cursor.execute(
                'insert into tb_dept values(%s, %s, %s)',
                (no, name, loc)
            )
        if result == 1:
            #4.造作成功提交事务
            con.commit()
            print('添加成功')
    finally:
        #5.关闭链接资源
        con.close()
if __name__ == "__main__":
    main()


# 3.是删除一个部门

import pymysql

def main():
    no = int(input('编号：'))
    con = pymysql.connect(
        host='localhost',port=8987,
        database='hrs',charset='utf8',
        user='root', password='1234556',
        autocommit=True
    )

    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'delete from tb_dept where dno=%s',
                (no,)
            )
            if result == 1:
                print('删除成功！')
    finally:
        con.close()

if __name__ == "__main__":
    main()