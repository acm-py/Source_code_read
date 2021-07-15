# hashlib库的使用指南
## 三个问题
### Why
为了安全！
为了加密！
我们在实际开发中，用户的登录口令，敏感信息容易受到攻击，这时候我们就应该加密。
此外，消息的摘要处理也可以用hash
### What
Hash也称散列、哈希，对应的英文都是Hash。基本原理就是把任意长度的输入，通过Hash算法变成固定长度的输出。这个映射的规则就是对应的Hash算法，而原始数据映射后的二进制串就是哈希值。活动开发中经常使用的MD5和SHA都是历史悠久的Hash算法。

一个优秀的hash算法，需要什么样的要求呢？

a)、从hash值不可以反向推导出原始的数据这个从上面MD5的例子里可以明确看到，经过映射后的数据和原始数据没有对应关系b)、输入数据的微小变化会得到完全不同的hash值，相同的数据会得到相同的值echo md5("这是一个测试文案");
// 输出结果：2124968af757ed51e71e6abeac04f98decho 
md5("这是二个测试文案");
// 输出结果：bcc2a4bb4373076d494b2223aef9f702
可以看到我们只改了一个文字，但是整个得到的hash值产生了非常大的变化。
c)、哈希算法的执行效率要高效，长的文本也能快速地计算出哈希值
d)、hash算法的冲突概率要小由于hash的原理是将输入空间的值映射成hash空间内，而hash值的空间远小于输入的空间
。根据抽屉原理，一定会存在不同的输入被映射成相同输出的情况。那么作为一个好的hash算法，就需要这种冲突的概率尽可能小。
### How
#### hashlib库的使用方法
##### 2.1、md5()加密算法
``` python
import hashlib
# 创建了一个md5算法的对象
hash = hashlib.md5()
# 对字节'password' 进行加密
hash.update(bytes('password', encoding='utf8'))
# 拿到16进制加密字符串
print(hash.hexdigest())
>>> 5f4dcc3b5aa765d61d8327deb882cf99
# 可以看到输出是一个32位的16进制字符。
# 1个16进制是4位2进制 == 4字节
# 32*4 == 128位字节
```
##### 2.2、sha1()加密算法
``` python
# sha1 算法
hash2 = hashlib.sha1()
hash2.update(bytes('passowrd', encoding='utf8'))
print(hash2.hexdigest())
>>> 6c526d10729e6cb117d5fe310b80673ad5e8dd70
# sha1 是40位16进制字符串
# 40*4 == 160字节
```
##### 2.3、sha256()算法
上同

### 总结
虽然sha256要比sha1安全很多
但是更慢
万物皆有代价
Valar Morghulis
Valar Dohaeris