# 연습문제
#1
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

s = 0
for x in range(len(a)) :
    s += x

print("A학급의 평균점수는 %s 입니다" % (s))

for x in range(len(a)) :
    if a[x] >= 70 :
        print(a[x])

'''
다른 버전
for x in a:
    if x >= 70 :
        print(x)

'''

#2
a = int(input("수를 입력하세요 "))
b = []
for x in range(1, a+1) :
    b.append(x**2)
print(b)


''' 다른 답
c = [ x**2 for x in range(1, a+1) ]
'''

# 3

a = int(input('첫번째 수를 입력하세요 '))
b = int(input('두번째 수를 입력하세요 '))

for x in range(a, b+1) :
    for y in range(1, 10) :
        print("%d x %d = %d" % (x, y, x*y))

# 4

s = 0
for x in range(1, 101) :
    if x % 3 == 0 :
        s += x

print(s)

#5
a = int(input()) 
for x in range(1, a + 1) :
    print(' '*(a-x) + '*' *x) 
    

# 6
rsp = ["가위", "바위", "보"]
for x in rsp:
    for y in rsp :
        print(x + "VS" + y)
# 7
color = ["white", "red", "pink", "yellow"]
flower = ["rose", "lily", "anemone", "camellia"]
for x in color:
    for y in flower:
        print(x, y)

# 8
c = 0
a = input()
for x in a :
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        c += 1
print("모음의 개수는 %d개입니다" % c)

# 9
a = input()
for x in range(1, len(a)+1) :
    print(a[:x])



