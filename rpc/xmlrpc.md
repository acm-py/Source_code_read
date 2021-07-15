# Rpc的入门和使用
## 三个问题
### Why
由定义可以知道，服务之间通过APi的方式走HTTP不也可以实现通过网络通信调用不同服务的目的。那么为什么还需要使用RPC呢？
必然相比API调用方式有着很大的优势
优势在何处？
- 系统内部APi调用之间交互很少，接口少的情况下，很有效。但是在一个大系统中，子系统的交互很多，如果要使用API，需要定义很多接口，难以维护。
- rpc是远程过程调用，其调用协议通常包含传输协议和序列化协议。远程调用和本地调用一样简单，还会自动进行数据序列化，协议编码，网络传输等过程。
### What
**RPC（Remote Procedure Call）– 远程过程调用，通过「网络通信」调用不同的服务，共同支撑一个软件系统，是分布式系统中的基石技术。**
### How
一个RPC框架其核心功能可以分成5个主要部分，分别是：客户端、客户端 Stub、网络传输模块、服务端 Stub、服务端等，之间的关系如下图。
![rpc原理图](https://i.loli.net/2021/07/14/zL9SdZx7t3NpInC.png)
- 客户端（Client）: 服务调用方
- 客户端存根(Client Stub): 存放服务端地址信息，将客户端的请求参数打包成网络信息，再通过网络传输发送给服务端.
- 服务器存根（Server Stub）: 接受客户端发送过来的请求，并将请求消息解包，然后调用本地服务(local call)进行处理
- 服务端（Server）: 服务的真正提供者。
- Network service: 底层传输：可以是tcp,也可以是Http
## 首先通过对python的xmlrpc简单使用，加深一下rpc概念的理解
**首先是服务端**
``` Python
# 服务端
from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
	return n % 2 == 0

# 创建RPC Server实例
server = SimpleXMLRPCServer('127.0.0.1', 5000)
print('Listening on port 5000')
server.register_function(is_even, 'is_even')# 注册服务
# 轮训监听5000端口
server.serve_forever()
```
**客户端**
``` Python
import xmlrpc.client

with xmlrpc.client.ServerProxy('http://127.0.0.1:5000/') as proxy:
	res1 = proxy.is_even(3) # 调用服务端的is_even方法
	print('res1:', res1)
	res2 = proxy.is_even(100)
	print('res2:', res2)
```
从下图可以看到Client的两次调用，其实就是POST请求，走的是HTTP/1.1.
说明Python的xmlrpc基于HTTP/1.1作为网络传输协议
![http协议post请求](https://i.loli.net/2021/07/14/dwjyQHE7puCfbWP.png)

## xmlrpc源码分析
通过我们自己写的client.py一点点分析。
1、可以使用with语法，说明内部类肯定实现了__enter__和__exit__方法
在IDE中使用快捷键ctrl + 鼠标左键进入ServerProxy类中
看到
``` python
# Lib/xmlrpc/Client/ServerProxy

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.__close()
```
和我们预想的相同
该类本身并没有is_even(方法)，但是我们运行代码没有报错，那就证明重写了__getattr__方法
果不其然
``` Python
# Lib/xmlrpc/Client/ServerProxy

    # 调用属性
    def __getattr__(self, name):
        # magic method dispatcher
        return _Method(self.__request, name)
```
_Method这个类点进去看。
``` Python
# Lib/xmlrpc/Client

class _Method:
    # some magic to bind an XML-RPC method to an RPC server.
    # supports "nested" methods (e.g. examples.getStateName)
    def __init__(self, send, name):
        self.__send = send
        self.__name = name
    def __getattr__(self, name):
        return _Method(self.__send, "%s.%s" % (self.__name, name))
    def __call__(self, *args):
        return self.__send(self.__name, args)
```
看到了__call__方法，这个方法的最终作用就是self.__request(name, args)，对应到proxy.is_even(3)，就是
self.___request(is_even, 3)。
重点就是__request方法。

我们来看下__request方法
``` Python
# Lib/xmlrpc/Client/ServerProxy

    def __request(self, methodname, params):
        # call a method on the remote server
        
        # dumps方法最终会返回一个具有XML格式的字符串
        request = dumps(params, methodname, encoding=self.__encoding,
                        allow_none=self.__allow_none).encode(self.__encoding, 'xmlcharrefreplace')
        # 请求
        response = self.__transport.request(
            self.__host, # self.__host, self.__handler = urllib.parse.splithost(uri)，在ServerProxy类实例化时获取了对应的值
            self.__handler,
            request, # xml格式数据
            verbose=self.__verbose # 是否显示详细的debug信息，默认为False
            )

        if len(response) == 1:
            response = response[0]
        # 返回相应结果
        return response
```
__request方法的关键就是调用了self.__transport.request方法进行请求，该方法的调用过程__transport.request --> __transport.single_request --> __transport.send_request。