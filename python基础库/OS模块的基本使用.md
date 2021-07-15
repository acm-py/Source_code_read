# OS模块的使用
## 三个问题
### why
我们经常需要查找文件和路径，这就依赖OS模块
### what
OS-> 也就operating system 的缩写，顾名思义，即代表着系统模块。
### how
``` python
import os
os.getcwd()#-> 获取当前工作路径
>>> Out[4]: 'C:\\Users\\bing'
os.listdir()# -> 获取当前工作文件夹内的文件夹或文件
>>> Out[2]:
['.3T',
 '.android',
 '.AndroidStudio3.6',
 '.bash_history',
 '.BookxNotePro',
 '.cache',
 '.codeintel',
 '.conda',
 ...

os.scandir()# -> 获取当前工作文件夹的文件
>>> Out[3]: <nt.ScandirIterator at 0x4083a60> 
# 返回的是一个可迭代对象
# 可以使用for循环获得结果
for i in os.scandir():
	if not f.is_file(): # is_file判断 这个路径是否是一个文件
		print('yes')
	else:
		print('no')

# 题外话，python3.5之前用的是os.walk() 后来我翻到了一个博主，它写了一个scandir()模块，经过测试性能是walk()函数的二十倍以上，然后就被收录到python3.5+的官方模块了。

os.makedir() # -> 创建文件夹

os.chdir() # -> 改变当前工作目录（以传递的参数为目录，且参数需要是绝对目录，无返回值）

os.path.join() # -> 路径拼接

os.path.abspath(path) # -> 返回path的绝对路径

os.system(command) # -> 运行shell命令