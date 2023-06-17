# 연습문제
# 1
weather = [('9월', 26), ('10월', 20), ('11월', 12), ('12월', 4)]

max_tem = 0
min_tem = 10000000
min_month = 0
max_month = 0 
for x in range(len(weather)):
    month, temperature = x
    if temperature > max_tem :
        max_tem = temperature
        max_month = month
    if temperature < min_tem :
        min_tem = temperature
        min_month = month

print("최고온도 : %s %d도" % (max_month, max_tem))
print("최저온도 : %s %d도" % (min_month, min_tem))

# 2

row = (1,2,3,4)
col = ('A','B','C','D','E')
seat = []
for c in col :
    for r in row :
        s = c + str(r)
        seat.append(s) 
print(seat) 

# 3
a = {'a' :1, 'b' : 2, 'c' :3}
print(a)

# 4
a = {'alice':11, 'bob':22, 'tedi':33, 'sooaa':44}
for x in a.values() :
    print(x)

# 5
a = {'t':10, 'e':20, 'd':30, 'i':40}
a['t'] = 100
a['e'] = 200

print(a)

#6
a = int(input())
k = {}
for x in range(a) :
    k[x] = x
print(k)

# 7
a = {'a':0, 'e':0, 'i':0, 'o':0, 'u' :0 }
s = input()
key = list(a.keys())
for x in s :
    if x in key:
        a[x] += 1

print(a)

# 8

a = {'국어' : 100, '수학' : 85, '사회' : 90 , '과학' : 77}
m = 0
n = 0 
for x, y  in a.items() :
    if m > y :
        m = y
        n = x
print(x)

# 9
item = {}
while True :
    n = input(' 1) 재고 조회 2) 입고 3) 출고 4) 종료 :')
    if n == '1':
        i = input('재고조회할 물건의 이름을 입력하시오')
        if i in item.keys():
            print(item[i])
    elif n == '2' :
        i = input("입고할 물건을 입력하시오")
        c = int(input("입고할 물건의 수량을 입력하시오"))
        if i in item.keys():
            item[i] += c
        else :
            item[i] = c 
    elif n == '3':
        i = input("출고할 물건을 입력하시오")
        c = int(input("출고할 물건의 수량을 입력하시오"))
        if i in item.keys():
            item[i] -= c
        else :
            print("아이템이 없습니다") 
    elif n == '4' :
        print("프로그램 종료!") 
        break 
