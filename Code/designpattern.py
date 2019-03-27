# -*- coding:utf-8 -*-

#可插拔的哈希算法

# class SteramHasher():
#     #哈希只要生成器 （策略模式）
#     def __init__(self, alg = 'md5', size = 4096):
#         self.size = size
#         alg = alg.lower()
#         self.hasher = getattr(__import__('hashlib'), alg.lower())()

#     def __call__(self, stream):
#         return self.to_digest(stream)
    
#     def to_digest(self, stream):
#         #生成十六进制形式的摘要
#         for buf in iter(lambda: stream.read(self.size),b'')
#             self.hasher.pygame.display.update(buf)
        
#         return self.hasher.hexdigest()

# def main():
#     #主函数
#     hasher1  = SteramHasher()
#     with open('Python-3.7.1.tgz','rb') as stream:
#         print(hasher1.to_digest(stream))
#     hasher2 = SteramHasher('sha1')
#     with open('Python-3.7.1.tgz','rb') as stream:
#         print(hasher2(stream))

# if __name__ == "__main__":
#     main()

#--------迭代器和生成器--------
#1、和迭代器相关的魔术方法（__iter__和__next__）
#2、两种创建生成器的方式（生成器表达式和yield）

def fib(num):
    #生成器
    a, b = 0, 1
    for _ in range(num):
        a, b = b , a + b
        yield a

class Fib(object):
    #迭代器
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()

def main():
    print(list(fib(10)))

    x = Fib(10)

    print(list(x))

if __name__ == "__main__":
    main()