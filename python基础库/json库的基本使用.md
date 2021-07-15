# Json库的使用指南
## 三个问题
### Why
json是一种数据格式，一种最为通用的数据格式。
在开发中，我们常常需要将某个语言的特定数据格式（列表、数组等）转为为通用的数据格式，以便协同。
例如后端传给前端的数据，我们从其他网站或者自己爬取的数据（如csv,txt）等
我们需要将它处理成本语言对应的数据结构才能够对其进行处理操作。
### What
json是一种轻量级数据交换格式。
json的Key只能是字符串（Python中的字典，key可以使任何可以hash的对象（比如元组））
、且Key和Value 都由双引号包裹
### How
#### loads
##### 2.1、json.loads()方法解码json 数据，返回Python类型数据（不一定是字典）
```python
#定义一个json数据
office_worker = '''
[{
    "name": "jack",
    "gender": "male",
    "birthday": "1966-06-66",
	"company": "Alibaba"
}, {
     "name": "rose",
    "gender": "female",
    "birthday": "1988-08-88",
	"company": "Alibaba"
}]
'''
print(type(office_worker))
>>> <class 'str'>
data = josn.loads(office_worker)
>>> Out[9]:
[{'name': 'jack',
  'gender': 'male',
  'birthday': '1966-06-66',
  'company': 'Alibaba'},
 {'name': 'rose',
  'gender': 'female',
  'birthday': '1988-08-88',
  'company': 'Alibaba'}]
# 可以看到它是一个列表
# 之后就按照列表进行数据的提取就行了。
```

#### dumps
用法同上