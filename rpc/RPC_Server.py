from xmlrpc.server import SimpleXMLRPCServer

def is_even(n):
	return n % 2 == 0

# 创建RPC Server实例
server = SimpleXMLRPCServer(('127.0.0.1', 5000))
print('Listening on port 5000')
server.register_function(is_even, 'is_even')# 注册服务
# 轮训监听5000端口
server.serve_forever()