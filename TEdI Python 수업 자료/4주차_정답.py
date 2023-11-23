""" # number_list = ["one", "two", "three"]

# for number in number_list:
    # print(number)
    
for _ in range(3):
    print("hello") """
    
# a = list(range(10)) # 0 ~ x-1
# print(a)
    
""" def get_three_character():
    str1 = "hello"

    return str1[0], str1[1], str1[2]

x, y, _ = get_three_character()
print(x, y) """

""" for i in range(1, 11, 3):
    print(i) """

""" test1 = ["a", "b", "c", "d"]
test2 = [[1, 2], [3, 4], [5, 6]]
# for (x, y) in test2:
    # print(x + y)
    
for (x, y) in zip(test1, test2):
    print(f"x is {x} and y is {y}") """

""" for number, upper, lower in zip("12345", "ABC", "abcd"):
    print(number, upper, lower) """

""" list1 = [[1, 2], [3, 4], [5, 6, 7], [8], [9, 10]]
print(len(list1)) # 5
a = list1[3]
print(a) """

# for name in enumerate(name_list):
    # print(name)

""" name_list = ["sunwoopi", "yangjaewon", "hanseojang]
for index, name in enumerate(name_list, start=3):
    print(f"{index}번 : {name}") """
    
# print(list(range(5)))

""" num=[1, 2, 3, 4]
result=[] # 3, 6, 9, 12

for x in num:
    result.append(x * 3)
print(str(num) + " 변수에 3을 곱한 값은?", result)
print(num, "변수에 3을 곱한 값은?", result)
print(f"{num} 변수에 3을 곱한 값은? {result}") """

""" num = [4, 8, 12, 24]
# results = [x * 3 for x in num] # List Comprehension
results = [x * 2 for x in num if x % 6 == 0] # [24, 48]
print(results) """

# x = 8
# print("haha" if x < 6 else "hello")

""" import numpy as np

# list1 = [1, 2, 3]
str1 = "hello"
# array1 = np.array(list1)
# print(list1)
# print(array1)
# print(array1 * 3)
print(str1 * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3] """

""" # list1 = [[0] for _ in range(10)]
# print(list1) # [[0], [0], [1] ...]
# list1[3][0] = 1
# print(list1)

list2 = [[0]] * 10
print(list2)
list2[3][0] = 1
print(list2) """

# a, b = map(int, input().split())



















""" # 연습문제
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
    print(a[:x]) """