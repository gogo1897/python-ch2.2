#한 줄 문자열 정의
s = ''
str1 ='hello world'
str2 ='hello world'
print(type(s), type(str1), type(str2))

# 여러줄 문자열 정의
str3 ="""ABC
DEF
가나다라마바사
아자차카타파하
"""

print(str3)

#여러줄 주석
#여러줄 문자열 사용
"""
주석1
주석2
주석3
"""

# escape
print("hello\nworld\n| say 'Hello World'")
print("hello\nworld\n| say \"Hello World\"")

#
#문자열 연산
#
str1 = "First String"
str2 = "Second String"

# 1. 인덱싱
print(str1[0], str1[2], str1[4])

#2. 슬라이싱
str3 = str2[2:5]
print(str3)
print(str2[2:])

#3. 연결(+) +는 생략 가능하다 단, 리터럴일때
print(str1 + " " + str2)
print("Frist String"" ""Second String")

# 문자열 객체와 정수형 객체는 + 연결 연산을 할 수 없다
name = "길동"
age = 40
#print(name + 40) <ㅡ 오류
print(name +str(age))

#반복(*) 연산
print(str1*3)

#len함수
print(len(str2))

#in, not in
print("S" in str2)
print("S" not in str2)

#문자열 객체는 변경할 수 없다(immutable)
#str1[0] = "F"

#서식(formating) - format()함수
print("name: " + name + " age :" + format(age, "d"))
print("name: " + format(name, "s") + " age :" + format(age, "d"))

#튜플을 이용한 서식
f = "name:%s, age:%d"
print(f)
print(f % (name, age))
print("name:%s, age:%d" % (name, age))

#cf C스타일
#printf("name:%s, age:%d" , name, age)

#서식 - 딕셔너리를 이용한 포매팅
f = "name:%(name)s, age:%(age)d"
print(f % {"name": "둘리", "age" : 30})
print(f % {"name": "마이콜", "age" : 20})
























