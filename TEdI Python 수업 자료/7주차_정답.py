""" my_tuple = (1, 2, 3)
print(type(my_tuple))
print(isinstance(my_tuple, tuple)) """


""" my_tuple = (1, 2, 3)
my_tuple[1] = 8 """


""" a, b, c = [1, 2, 3]
print(f"a is {a}, b is {b}, c is {c}")

a, b, c = (1, 2, 3)
print(f"a is {a}, b is {b}, c is {c}")

a = [1, 2, 3]
b = (1, 2, 3)
c = 1, 2, 3
print(f"a is {a}, b is {b}, c is {c}")

d = 1, 2, 3
a, b, c = d
print(f"a is {a}, b is {b}, c is {c}") """

""" x = 10
y = 25

z = x
x = y
y = z
print(x, y)

# x, y = 10, 25
# x, y = y, x
# print(x, y) """


""" # 논리 표현식의 단축 평가(Short-circuit Evaluation)
x = 25
# x = 10
if x == (10 or 25):
    print(True)
else:
    print(False)
    
# True -> or : 왼, and : 오
# False -> or : 오, and : 왼
print(3 or 5)
print(3 and 5) """


""" def fc_layer(in_features, hidden_features=None):
    hidden_features = hidden_features or in_features

def example_function_1(arg1=5, arg2):
    pass

def example_function_2(arg1, arg2=5):
    pass

example_function_1(3)
example_function_2(3) """


""" x = 25
if x == (10 or 25):
    pass

if x == 10 or x == 25:
    pass

if x in [10, 25]:
    pass

if any((x == value) for value in [10, 25]):
    pass

x = 25
print((x == value) for value in [10, 25])
print(list((x == value) for value in [10, 25]))
print([(x == value) for value in [10, 25]])

print(any((x == value) for value in [10, 25]))

print(any([False, True, False])) # or
print(all([False, True, False])) # and """

# my_list = [value - 3 for value in [1, 3, 6, 7]]
# print(my_list)


""" # scores = {'국어': 50, '수학': 90, '생명과학': 95, 200: 100, 'a': my_list} # {key : value}
my_list = [4, 5, 6]
pi_scores = {
    '국어': 50,
    '수학': 90,
    '생명과학': 95,
    200: 100,
    'a': my_list
    }
print(pi_scores)

print(pi_scores['a'][1]) """


""" pi_scores = {
    '국어': 50,
    '수학': 90,
    '생명과학': 95,
    }

pi_scores['수학'] = 40 # Value 변경
print(pi_scores)

del pi_scores['생명과학'] # Key : Value 삭제
print(pi_scores)

pi_scores['사회'] = 25 # Key : Value 추가
print(pi_scores) """


""" pi_scores = {
    '국어': 50,
    '수학': 90,
    '생명과학': 95,
    }

print(pi_scores.keys())
print(pi_scores.values())
print(list(pi_scores.keys()))
print(list(pi_scores.values())) """


""" pi_scores = {
    '국어': 50,
    '수학': 90,
    '생명과학': 95,
    }

print(list(pi_scores.items()))

# for item in pi_scores.items():
    # print(item)

# for item in pi_scores.items():
    # print(f"key is {item[0]}")
    # print(f"key is {item[1]}")
    # print()
    
# for key, value in pi_scores.items():
    # print(key, 'and', value) """

    
""" my_list = [
    [1, 2, 3],
    [4, 5, 6]
    ]
for a, b, c in my_list:
    print(a, b, c)

# for a, b in my_list:
    # print(a, b) """
    

""" name = ['psw', 'phw', 'No Haha']
yearning = [3, 6, 'hello', 4]

dictionary = dict(zip(name, yearning))
print(dictionary) """



















""" # 연습문제
# 1-1
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

# 1-2
max, min = 0, 50
mm, nn = 'a', 'b'
weather =  [('9월', 26), ('10월', 20), ('11월', 12), ('12월', 4)]

for x, y in weather:
  if(max < y):
    mm, max = x, y
  if(y < min):
    nn,min = x, y
print("최고 온도 : %s %d도"%(mm,max))
print("최저 온도 : %s %d도"%(nn,min))

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
        break  """