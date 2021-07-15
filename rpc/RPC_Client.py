import xmlrpc.client

with xmlrpc.client.ServerProxy('http://127.0.0.1:5000/') as proxy:
	res1 = proxy.is_even(3) # 调用服务端的is_even方法
	print('res1:', res1)
	res2 = proxy.is_even(100)
	print('res2:', res2)