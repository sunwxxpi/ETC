# 연습문제

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
        print("%s은 거꾸로 정수가 아닙니다" %a )
    
            
