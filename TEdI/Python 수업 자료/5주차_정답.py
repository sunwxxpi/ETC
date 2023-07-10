""" print("기능을 선택하세요")
print("1. 더하기", "2. 빼기", "3. 곱하기", "4. 나누기", sep='\n')
feature = int(input("계산기 기능을 선택하세요(1, 2, 3, 4): "))

num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

if feature == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif feature == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif feature == 3:
    print(f"{num1} x {num2} = {num1 * num2}")
elif feature == 4:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("오류입니다.") """


'''num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))
num3 = int(input("세 번째 정수를 입력하세요: "))

my_list = [num1, num2, num3]

""" largest = num1 # 1번이 제일 크다고 가정
if num1 < num2: 
    largest = num2
    if num2 < num3:
        largest = num3
else: # num1 >= num2
    if num1 < num3:
        largest = num3 """

"""
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i """
      
""" my_list = [num1, num2, num3]
largest = max(my_list) """

print(f"입력된 세 수 {num1}, {num2}, {num3}중에서 가장 큰수는 {largest}입니다.")'''


""" ################################ pass ################################
unit = input("단위를 입력해 주세요(섭씨 또는 화씨): ")
temp = int(input("온도를 입력해 주세요: "))

if unit == '섭씨':
    pass
elif unit == '화씨':
    temp = (temp - 32) * (5 / 9)

if temp < 0:
    state = '고체'
elif temp >= 100:
    state = '기체'
else:
    state = '액체'
        
print(f"물의 섭씨 온도: {round(temp, 0):.0f}도, 상태는 {state}") """

'''num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))
x = int(input("원하는 배수를 입력하세요: "))
sum = 0

""" for num in range(num1, num2 + 1):
    if num % x == 0:
        sum += num """
        
""" for num in range(num1, num2 + 1, 5):
    sum += num """
        
print(f"{num1}에서 {num2}까지의 정수 중 {x}의 배수 합계는 {sum}입니다.")
################################ Complexity ################################'''


'''year = int(input("년도를 입력하세요: "))

""" if year % 4 == 0:
    if year % 100 != 0:
        year_type = '윤년o'
    else:
        if year % 400 == 0:
            year_type = '윤년o'
        else:
            year_type = '윤년x'
else:
    year_type = '윤년x' """
    
""" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    year_type = '윤년o'
else:
    year_type = '윤년x' """
    
# print(year_type)

# print('윤년o' if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) else '윤년x')'''
    

""" import random

# a = random.randint(1, 5)
# print(a)

# my_list = [1, 2, 3]
# b = random.choice(my_list)
# print(b)

random.seed(12983712897321)
your_list = [1, 2, 3]
random.shuffle(your_list)
print(your_list) """


stage = 1
sum = 0

""" while stage <= 5:
    sum += stage
    stage += 1 """
    
while True:
    sum += stage
    stage += 1
    
    if stage > 5:
        break
    
print(sum)










""" # 연습문제

# 1 
import random
com = random.randint(1, 100)

while True :
    m = input("숫자를 입력하세요")
    if com > m :
        print("숫자가 너무 작습니다. 다시 입력하세요")
    elif com < m :
        print("숫자가 너무 큽니다. 다시 입력하세요")

    else :
        print("정답입니다")
        break

# 2
# import random
count = 1
while True :
    print("주사위 던지기 : %s" % (count))
    me = random.randint(1, 6)
    computer = random.randint(1, 6)
    print("나 : %d" % (me))
    print("컴퓨터 : %d" % (computer))
    if me > computer :
        print("나의 승리!")
    elif me < computer :
        print("컴퓨터의 승리!")
    else :
        print("동점!")
    count += 1
    again = input("계속하려면 y를 입력하세요")
    if not(again == 'y' or again == "Y") :
        break

#3
# import random
option = ["왼쪽", "중앙", "오른쪽"]
while True :
    me = input("어디를 수비하시겠어요?(왼쪽, 중앙, 오른쪽) :")
    computer = random.choice(option)
    if me == computer :
        print("패널티 킥이 성공하였습니다")
    else :
        print("패널티 킥이 실패하였습니다") 

    
# 4
flower=["rose","sunflower","peony","cherryblossom"]
n = 0
while n < len(flower) :
    print(flower[n])
    n += 1

# 5
# sum 4
# sum 7
# sum 9
# sum 10

# 6
bus = 5000
w = bus * 0.05
while True :
    a = int(input("충전 또는 사용한 액수를 +/- 기호화 함께 입력하세요 :"))
    print("현재 잔액은 %d원입니다" % (bus))
    bus = bus + a
    if bus <= w :
        print("[경고] 잔액을 충전해주세요.")

# 7
mx = 0
mn = 0
while True :
    a = int(input())
    if a > mx :
        mx = a
    if a < mn:
        mn = a
    if a == -1 :
        print("3개의 숫자 중에 %d가 제일 크고, %d가 제일 작습니다" % (mx, mn))
        break


# 8

while True :
    a = input()
    if a == '-1' :
        break
    
    flag = True 
    for x in range(len(a)) :
        if a[x] != a[len(a) - 1 - x]:
            flag = False

    if flag :
        print("%s은 거꾸로 정수입니다"% a)
    else :
        print("%s은 거꾸로 정수가 아닙니다" %a ) """