# PyMySQL库的基本使用
## 三个问题
### Why
为了使用python语言连接数据库
### What
一个数据库连接模块，同时有着其他强大的功能，便于Python 开发者的开发
### How
#### 1、连接
``` python
import pymysql # pymysql为第三方库，使用之前请确保安装过.
db = pymysql.connect(host='localhost', port=3306, user='bing', passwd='123456',db='TESTDB', charset='utf8')
# 各个参数的释义
# host: str -> MySQL 服务器地址
# port: int -> MySQL服务端端口号
# user: str -> MySQL的用户名
# passwd: str -> MySQL用户的密码（注意是passwd!）
# charset: str -> MySQL连接编码

# connect() -> 返回一个connect对象
# 所以db变量支持如下的操作
# 1、cursor -> 使用该连接创建并返回游标
# 2、commit -> 提交当前事务
# 3、rollback -> 回滚当前事务
# 4、close() -> 关闭连接
```
#### 使用cursor()方法创建一个游标对象
##### What
游标对象：使用执行查询和获取结果
cursor对象支持的方法：
1、execute(op, [args]) -- 执行一个数据库查询和命令
2、fetchone() -- 取的结果集的下一行，结果集是一个对象
3、fetchall() -- 取的结果集的剩下所有
4、rowcount -- 最近一次execute返回数据的行数或者影响的行数，只读属性。
5、close() -- 关闭游标对象

#### 实践
##### 2.1、使用execute()方法执行sql查询
``` Python
cursor.execute("SELECT VERSION()")
```
##### 2.2、使用fetchone()方法获取单条数据
``` Python
data = cursor.fetchone()
print("%s",data)
db.close()
```
##### 2.3、创建数据库
``` python
# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='bing', passwd='123456',db='TESTDB', charset='utf8')

#使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYMENT")

# 使用预处理语句创建表
sql = """
	CREATE TABLE EMPLOYEE(
		FIRST_NAME CHAR(20) NOT NULL,
		LAST_NAME CHAR(20),
		AGE INT,
		SEX CHAR(1),
		INCOME FLOAT
	)
"""

cursor.execute(sql)

# 关闭数据库连接
db.close()
```
##### 2.4 数据库插入操作
``` python
cursor = db.cursor()

# SQL 插入语句
sql = """
	INSERT INFO EMPLOYEE(
		FIRST_NAME,
		LAST_NAME,
		AGE,
		SEX,
		INCOME)
	VALUES('Mac', 'Mohan', 20, 'M', 2000)
"""
try:
	# 执行sql 语句
	cursor.execute(sql)
	db.commit()
except:
	# 如果发生错误则回滚
	db.rollback()

db.close()
```

##### 2.5 数据库查询
``` Python
# sql 查询语句
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s" % (1000)
try:
	# 执行sql语句
	cursor.execute(sql)
	# 获取所有记录列表
	results = cursor.fetchall()
	for row in results:
		fname = results[0]
		lname = row[1]
		age =row[2]
		sex = row[3]
		income = row[4]
		print("fname={0},lanme={1},age={2},sex={3},income={4}".format(fname,lanme,age,sex,income))
except:
	print('Error: unable to fetch data")
# 关闭数据库连接
db.close()
```
	
