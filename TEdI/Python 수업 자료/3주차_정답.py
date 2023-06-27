""" a, b = input().split(' ')
print(type(a), type(b))

a, b = map(float, input().split())
print(type(a), type(b)) """

# print(type("123"))

""" a = 1, 2, 2
print(a) """

""" a, b = 1, 2
print(a, b) """

# a = list1
# print(a)

""" str1 = "psw"

a, b = str1
print(a, b) """

# print(bool(1))
# print(bool(213))
# print(bool(0))
# print(bool("hi"))
# print(bool(""))
# print(bool([1]))
# print(bool([]))
# print(bool({3}))
# print(bool({}))


""" if bool(condition):
    print("True")
else:
    print("False") """
    
# condition = [1, 2]
# condition = []
# condition = "hello"
# condition = ""

""" if bool(condition == True):
    print("True")
else:
    print("False") """

""" x = 5
if x < 3:
    print("x < 3")
elif x < 7: # 3 <= x < 7
    print("x < 7")
elif x < 10:
    print("x < 10")
else: # x >= 10
    print("else") """

""" y = int(input())

print(2 if y>0 else 3) """

""" x = round(1.8 + 2.1, 1)
if x == 3.9:
    print(True)
else:
    print(False)
    print(x) """

""" a = round(123.456, -1) # Default
print(a) """

"""
<and>
T T T
T F F
F T F
F F F

<or>
T T T
T F T
F T T
F F F

<not>
T F
F T
"""

""" for(i=4; i<10; i=i+3){
    printf(i);
} """

""" list1 = [1, 2, 3, 5]
# str1 = "pisunwoo"
for hello in list1[::-1]:
    print(hello) """

""" my_list = [1, 2, 3, 4, 5]
new_list = [x+3 for x in my_list[::-1] if x > 3]

print(new_list) """

""" my_list = [1, 2, 3, 4, 5]
new_list = []
for x in my_list:
    if x > 3:
        new_list.append(x+3)

print(new_list) """

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [1, 3, 5, 6]

""" str1 = "pisunwoo"
str2 = "pihyunwoo"

result = [i for i in str1 if i in str2]
print(result) """

""" my_str = "Hello My Name is"
# if "hello" in my_str:
if "hello" not in my_str:
    print(True)
else:
    print(False) """

""" if type(123) is int:
    print("It's int")
    
if isinstance(123, int):
    print("It's int") """
    
str1 = "pi"
str2 = "sun"
print(str1, end='')
print(str2, end='')


""" import turtle as t

t.shape("turtle")
t.color("#fcba03")
t.speed(0)
t.bgcolor("blue")
t.pensize(3)

t.forward(100) """





























""" # 연습문제
# 1. 
a = int(input("하나의 정수를 입력하세요"))
if a % 3 == 0 or a % 5 == 0 :
    print("%d 는 3의 배수이면서 5의 배수입니다"% a)
elif a % 5 == 0 :
    print("%d 는 5의 배수입니다"% a)
elif a % 3 == 0  :
    print("%d 는 3의 배수입니다"% a)
else :
    print("%d 는 3의 배수이면서 5의 배수입니다"% a)

#2. 
a = int(input("정수를 입력하게요 : "))
if a >= 100 and a <= 1000 :
    print("입력된 정수 500은 100~1000사이에 있습니다")

#3. 
a = input("영어 소문자 하나 입력하세요 :")
if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print("%s는 자음입니다"%a)
else :
    print("%s는 모음입니다"%a)

#4
a = int(input("점수를 입력하세요 "))
if a >= 90 :
    print("당신의 등급은 A등급 입니다")
elif a >= 80 :
    print("당신의 등급은 B등급 입니다")
elif a >= 70 :
    print("당신의 등급은 C등급 입니다")
elif a >= 60 :
    print("당신의 등급은 D등급 입니다")
else :
    print("당신의 등급은 F등급 입니다")

#5
a = input()
if 'a' in a or 'e' in a  or 'i' in a or 'o' in a or 'u' in a:
    print("문자에 모음이 있습니다")
else :
    print("문자에 모음이 없습니다")

#6
a = int(input("첫 번째 수를 입력하세요"))
b = int(input("두 번째 수를 입력하세요"))
o = input("연산자를 입력하세요(+,-,*,/)")

if o == '+' :
    print(a + b)
elif o == '-' :
    print(a - b)
elif o == '*' :
    print(a * b)
elif o == '/' :
    print(a / b)


#7
a = int(input("해를 입력하세요 :"))
if (a % 4 == 0 and a % 100 != 0 ) or a % 400 == 0:
    print("%d년은 윤년입니다" % a)
else :
    print("%d년은 윤년이 아니다" % a)
    

#8
x1 = int(input('큰원 x좌표')) 
y1 = int(input('큰원 y좌표'))
r1 = int(input("큰원 반지름 :"))
x2 = int(input('작은원 x좌표'))
y2 = int(input('작은원 y좌표'))
r1 = int(input("작은원 반지름 :"))

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2 ) ** 0.5 
r = r1 - r2
if d < r :
    print("큰 원이 작은 원 내부 안에 있습니다")
else :
    print("큰 원이 작은 원 내부 안에 없습니다") """