
a = 1.2
print(a, type(a))
print(isinstance(a, float))

b=2.000
print(b, type(b))
#객체함수 is_integer()는 값이 정수 인지 실수 인지 확인하는 함수
#타입을 확인하는 함수가 아니다
print(b.is_integer())

#다른 언어와 마찬가지로 e, E사용한 부동소수점 표기 가능
b = 2e3
c = 0.2e-4
print(b, c)

#complex
p = 2.5
q = -3
print(complex(p,q))