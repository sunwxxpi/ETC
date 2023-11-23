# print('1')
# print('안녕하세요')

'''
a = 1
b = 2.2
c = '1'

print(a, b, c) 
'''






'''
아이스크림 = 2000
초코칩 = 1700
사탕 = 300

print(아이스크림*3+초코칩*2+사탕*4)
'''

#거북이 모듈 불러오기 
import turtle
#거북이 생성하기
tedi = turtle.Turtle()
tedi.shape("turtle") 
tedi.color("green") # 거북이 색상 정하기
tedi.speed(0) # 거북이 속도 : 0이 제일 빠름

# turtle.bgcolor("black") # 배경 색상 정하기
'''
# 사각형
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(90) # 오른쪽으로 90도 회전
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(90) # 오른쪽으로 90도 회전
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(90) # 오른쪽으로 90도 회전
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(90) # 오른쪽으로 90도 회전 
'''

'''
# 삼각형
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(120) # 오른쪽으로 90도 회전
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(120) # 오른쪽으로 90도 회전
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(120) # 오른쪽으로 90도 회전

'''
# 별그리기
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(144) # 오른쪽으로 90도 회전
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(144) # 오른쪽으로 90도 회전
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(144) # 오른쪽으로 90도 회전
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(144) # 오른쪽으로 90도 회전
tedi.forward(100) # 앞으로 100만큼 이동
tedi.right(144) # 오른쪽으로 90도 회전


# 연습문제

# 1. 책 2페이지 참조
#2.
a = 2
b = 8
print(a+b)
print(a**3)

#3.
a = 'pine'
b = 'apple'
print(a + b)

#4.
print("="* 20)

#5.
import turtle as t
t.forward(100)
t.right(144)
t.forward(100)
t.right(144) 
t.forward(100)
t.right(144) 
t.forward(100)
t.right(144) 
t.forward(100)
t.right(144) 

# 6.
icecream = 1700
cookie = 1500
cake = 4500
bread = 2100
money = 10000

total = icecream + cookie + bread + money
extra = money - total
print("총 금액은", total , "원입니다")
print("거슮돈은", extra, "원입니다") 

# 7.
second = 10000
hour = second // 3600
minute = second % 3600 // 60
sec = second % 60
print(hour, "시", minute, "분", sec, "초")





