#2진, 8진 , 10진, 16진 Literal

a = 23
print(type(a))

b = 0b1101
o = 0o46
h = 0x23
print(b, o, h)


#3.x 에서는 int와 long이 합쳐졌다. 표현범위는 무한대
e = 2**1024
print(e, type(e))
print(e.bit_length())

#변환 함수
print(oct(38))
print(hex(38))
