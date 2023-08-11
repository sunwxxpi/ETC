""" several_line_str = '''꿀꽈배기는
너무
맛있어요'''
print(several_line_str) """

""" str = '...나도..고등학교...'
str_strip = str.strip('.')
print(str_strip) """

""" python = '파이썬'
java = '자바'
print('개발언어에는 {1}, {0} 등이 있다.'.format(python, java))
print(f'개발언어에는 {python}, {java} 등이 있다.') """

""" my_list = ['오예스', '몽쉘']
del my_list[1]
my_list.append('초코파이')
my_list.remove('오예스')
print(my_list) """

""" my_list = ['오예스', '몽쉘']
a = my_list.pop()
print(a) """

""" numbers = (1, 2, 3, 4, 5)
one, two, *others = numbers
print(others) """

""" my_list = [1, 2, 3, 4, 5]
new_list = [x+3 for x in my_list if x > 3]
print(new_list) """

""" def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer)

visit('2023년 1월 1일', '장발장', '이남수') """

""" message = '나는야 전역변수'
print(message)
list1 = []
print(list1)

def no_secret():    
    global message
    message = '바꿀 수 있을까요?' # global 선언을 해야 수정 가능
    
    list1.append('hello')
    list1[0] = 'impossible' # global 선언 없이도 수정 가능
    
no_secret()
print(message)
print(list1) """

""" print(1, 2, 3, sep='HaHa')
print('1'+'2'+'3', sep='HaHa')
print(1, 2, 3, end='HaHa')
print('AAAAAAAAA') """

""" f = open('list.txt', 'w', encoding='utf8')
f.write('김선우\n')
f.write('피선우\n')
f.close() """

""" f = open('list.txt', 'r', encoding='utf8')
for line in f:
    print(line.rstrip())
    # print(line, end='')
f.close()

f = open('list.txt', 'r', encoding='utf8')
# f.seek(0)
contents = f.read()
# contents = f.readline().rstrip()
# contents = f.readlines()
print(contents)
f.close() """

""" with open('list2.txt', 'w', encoding='utf8') as f:
    f.write('김선우\n')
    f.write('피선우\n')
    f.write('김선우\n')
    f.write('피선우\n') """
    
""" import pickle

gameOption = {
    "Sound": 8,
    "VideoQuality": "HIGH", 
    "Money": 100000,
    "WeaponList": ["gun", "missile", "knife"]
    }

with open("game.txt", "wb" ) as file:
    pickle.dump(gameOption, file) # Dict를 pickle File에 저장

with open("game.txt", "rb") as f:
    data = pickle.load(f)
    print(data) """
    
""" # class BlackBox:
class BlackBox():
    def __init__(self, name, price): # 객체가 생성될 때
        self.name = name
        self.price = price
    
    def set_travel_mode(self, min):
        print(self.name, str(min) + '분 동안 여행 모드 ON')

b1 = BlackBox('까망이', 200000)
# print(b1.name)
# print(b1.price)

# b1.set_travel_mode(20) # 같은 것
# BlackBox.set_travel_mode(b1, 20) # 같은 것 """

""" class SpecialBlackBox(BlackBox): # 상속(Inheritance)
    def special_mode(self):
        print('This is Special Mode')
        
s1 = SpecialBlackBox('하양이', 300000)
# print(s1.name)
# print(s1.price)

# s1.special_mode()
# b1.special_mode()

class SDBlackBox(BlackBox):
    def __init__(self, name, price, sd):
        # BlackBox.__init__(self, name, price)
        super().__init__(name, price)
        self.sd = sd """

""" class VideoMaker():
    def make(self):
        print('추억용 여행 영상 제작')
        
class AdvancedBlackBox(BlackBox, VideoMaker):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd
        
a = AdvancedBlackBox('검정이', 24234, 64)
a.make() """

""" class VideoMaker():
    def make(self):
        print('추억용 여행 영상 제작')

class BestBlackBox(BlackBox, VideoMaker):
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd

    def make(self): # Method Overriding
        print('추억용 여행 영상을 보정해서 제작')
        
h1 = BestBlackBox("피선우", 500000, 256)
h1.make() """

""" class Calculate:
    def __init__(self, a, b) :
        self.a = a
        self.b = b

    def __str__(self) : 
        return f'add 함수를 사용해서 {self.a}과 {self.b}을 더할 수 있습니다'
    
cal = Calculate(3, 7)
print(cal) """
    
""" num1 = 3
num2= 0
try:
    result = num1 / num2
    print(f'연산 결과는 {result}입니다.')
except ZeroDivisionError:
    print('0으로 나눌 수 없어요.')
except Exception as err:
    print('에러가 발생했어요. :', err)
else:
    print('정상 동작했어요.')
finally:
    print('수행 종료') """
    
""" list = input().split()
print(list)
list_list = [input().split()]
print(list_list) """

""" white_chess_num = map(int, input().split())
chess_num = [1, 1, 2, 2, 2, 8]

black_chess_num = [chess_num - white_chess_num for white_chess_num, chess_num in zip(white_chess_num, chess_num)]
for i in black_chess_num:
    print(i, end=' ') """
    
""" first_num = int(input())
second_num = input()

for i in second_num[::-1]:
    print(first_num * int(i))
    
print(first_num * int(second_num)) """

""" x = int(input())
y = int(input())

if x > 0:
    print(1 if y>0 else 4)
else:
    print(2 if y>0 else 3) """
    
""" a, b = map(int, input().split())

print(format(a/b, '.2f'))
print('{:.2f}'.format(a/b)) 
print(f'{a/b:.2f}') # Main
print('%.2f' %(a/b)) """

""" a = map(int, input().split())
a = list(a)

print(sum(a), f'{sum(a)/len(a):.2f}') """
    
""" print(type(123))

if type(123) is int:
    print("It's int")
    
if isinstance(123, int):
    print("It's int") """
    
""" if 3 == 3.0:
    print(True)
else:
    print(False)

if 3 is 3.0:
    print(True)
else:
    print(False) """
    
""" a = input()
a = int(a, 16)

for i in range(1, 16):
    # print("%X"%a, "*%X" %i, "=%X" %(a*i), sep='')
    # print("%X*%X=%X" %(a, i, a*i))
    print(f"{a:X}*{i:X}={a*i:X}") """
    
""" a = int(input())

for i in range(1, a+1):
    # if ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)):
    # if any((one_char in ['3', '6', '9']) for one_char in str(i)):
    if any((one_num in str(i)) for one_num in ['3', '6', '9']):
        print('X', end=' ')
        continue

    print(i, end=' ') """
    
""" import numpy as np

print(any([False, True, False]))
print(all([False, True, False]))
print(all(np.array([20, 40, 50]) < 45)) """

""" print(round(12343.123, -1))
print(round(12343.123, 0))
print(round(12343.123, 1))
print(round(12343.125, 2)) # round()에서는 반올림할 때, 5는 내림 처리. 왜냐? 사실 4988877이기 때문. NumPy에서는 올림 처리.
# 소수 첫 째 자리가 기준 (0) """

""" for number, upper, lower in zip("12345", "ABC", "abcd"):
    print(number, upper, lower) """
    
""" list1 = [1, 2, 3]
print(list1)
print(list1.reverse())
print(list1)

print('-----------')

list1 = [1, 2, 3]
print(list(reversed(list1)))

print('-----------')

print(range(3))
print(list(range(3))) """

""" import numpy as np

list1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

array1 = np.array(list1)
print(list(array1)) # List 안에 담긴 Array
print(array1.tolist()) # List

y = array1[:, 1] # List가 아닌 Array에서만 가능
print(list(y)) # List
print(y.tolist()) # List """

""" list1 = [1, 2, 3]
print(list1 * 3)

string1 = 'String' # String 객체는 Immutable(불변), string1[3] = 'a' 불가능
print(string1 * 3)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print(list1 + list2) """

""" import numpy as np

index_array = np.array([2, 4, 5])
array1 = np.array([11, 12, 13, 14, 15, 16])

print(array1[index_array]) """

""" a, b, c = 1e9, 75.25e1, 3954e-3 # 지수 표현 방식은 실수 자료형으로 처리
print(a, b, c) """

""" a = 0.3 + 0.6
print(a)
print(f'{a:.1f}') """

""" array1 = [[0] * 2 for _ in range(3)] # 올바른 List 초기화 방식
print(array1)
array1[1][1] = 1
print(array1)
print()
array2 = [[0] * 2] * 3 # 잘못된 List 초기화 방식
print(array2)
array2[1][1] = 1
print(array2) """

""" list1 = [3, 1, 2, 5, 6, 8, 2, 5]
print(list1)

list1.append(12)
print(list1)

list1.reverse()
print(list1)

list1 = list(reversed(list1))
print(list1)

list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.insert(3, 43)
print(list1)

print(list1.count(5))

list1.remove(2) # 원소 1개만 제거
print(list1)

set = {2, 5} # List : [], Tuple : (), Set : {}, Dictionary : {: }
result = [i for i in list1 if i not in set]
print(result)

list2 = [1, 2, 3]
list2.append('TikTok')
print(list2)
list2.extend('TikTok')
print(list2) """

""" a, b = 3, 1

dict1 = {'사과': 'Apple',
         '바나나': 'Banana',
         '코코넛': 'Coconut',
         a: b}

print(dict1.keys())
print(list(dict1.keys()))
print(dict1.values())
print(list(dict1.values()))

for key in dict1.keys():
    print(dict1[key]) """
    
""" data1 = set([1, 2, 3, 3, 4, 4, 5])
print(data1)
data2 = {1, 2, 3, 3, 4, 4, 5}
print(data2)
data2.add(12)
data2.update([15, 16])
data2.update({22, 25})
data2.remove(15)
print(data2)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a | b)
print(a & b)
print(a - b) """

""" from sys import stdin

data_1 = stdin.readline().rstrip()
print(data_1)

data_2 = stdin.readlines() # EOF : ctrl + d (UNIX), ctrl + z (Windows)
print(data_2)

a, b, c = map(int, stdin.readline().rstrip().split())
print(a, b, c) """

""" string1 = '135'
a = ['3' in string1, '2' in string1]
print(a) """

""" print((lambda a, b: a + b)(3, 7))

array1 = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array1, key=my_key)) # .sort() != sorted()
print(sorted(array1, key=lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10, 15, 20]
print(list1 + list2)
print(list(map(lambda a, b: a + b, list1, list2))) # map() : 각각의 원소 like iterate~ """

""" result = eval("(3+5)*7")
print(type(result))
print(result) """

""" result = sorted([9, 1, 8, 5, 4]) # .sort() != sorted()
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

array1 = [['홍길동', 50], ['이순신', 32], ['아무개', 74]]
result = sorted(array1, key=lambda x: x[1], reverse=True)
print(result) """

""" # {'A', 'B', 'C'}
# 순열(nPr) : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열
#   3P2 : 3 * 2 : AB AC BA BC CA CB
# 조합(nCr) : 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택
#   3C2 : 3 * 2 / 2! : AB AC BC

from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

permu = list(permutations(data, 2)) # 순열
print(permu)
combi = list(combinations(data, 2)) # 조합
print(combi)
produ = list(product(data, repeat=2)) # 중복 순열 : 2개를 뽑는 모든 순열 (중복 허용)
print(produ)
combi_repl = list(combinations_with_replacement(data, 2)) # 중복 조합 : 2개를 뽑는 모든 조합 (중복 허용)
print(combi_repl) """

""" from collections import Counter

list1 = ['red', 'blue', 'red', 'green', 'blue', 'blue']
counter = Counter(list1)
print(counter['red'], counter['green'], counter['blue'])
print(dict(counter))
print(list(counter)) # list(dictionary 객체) >> [dictionary key값] """

""" from math import gcd, lcm

a, b = 21, 14
print(gcd(a, b)) # Greatest Common Divisor (최대 공약수)
print(lcm(a, b)) # Least Common Multiple (최소 공배수)
print((lambda a, b: gcd(a, b) * (a // gcd(a, b)) * (b // gcd(a, b)))(a, b)) """

""" result = [x * y for x in range(2,10) for y in range(1,10)]
print(result) """

""" print("\\\\\'")
print(r"\\'") """

""" from collections import Counter

lst = [2, 2, 3, 3, 3, 1, 1, 1]

# 리스트에서 가장 많이 등장한 수의 개수를 구합니다
counts = Counter(lst)
max_count = max(counts.values())

if list(counts.values()).count(max_count) >= 2:
    print("가장 많이 등장한 수의 종류는 2종류 이상입니다")
else:
    print("가장 많이 등장한 수의 종류는 1종류입니다")

# 가장 많이 등장한 수의 종류를 리스트에 저장합니다
most_common = [num for num, count in counts.items() if count == max_count]

# 리스트를 정렬하고 출력합니다
most_common.sort()
print(f"가장 많이 등장한 수의 종류 : {most_common}") """

""" import os, sys

# 1.현재 파일의 이름 & 경로
print(__file__)
print(os.path.realpath(__file__)) # __file__ 실제 경로 
print(os.path.abspath(__file__)) # __file__ 절대 경로

# 2. Directory 경로
print(os.getcwd()) # Terminal상 현재 작업 Directory 경로
print(os.path.dirname(os.path.realpath(__file__))) # __file__의 Directory 경로

# 3.Terminal상 현재 작업 Directory의 File 리스트
print(os.listdir(os.getcwd()))

# 4.작업 디렉토리 변경
os.chdir("../")
print(os.getcwd())

# 5. sys.path에 import 가능한 Module 경로를 추가
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) """

""" name = ['psw', 'phw', 'No Haha']
yearning = [3, 6]

dictionary = dict(zip(name, yearning))
print(dictionary) """

""" def solution(names, yearning, photos):
    return [sum(yearning[names.index(name)] for name in photo if name in names) for photo in photos]

names = ['psw', 'phw']
yearning = [3, 8]
photos = [['psw']]

print(yearning[names.index('psw')]) """

""" str_list = ['There', 'is', 4, "items"]
result = ' '.join(map(str, str_list))
print(result) """

""" list1 = ["a", "b", "c"]
list2 = list1
list3 = list1.copy()
list1.append("d")
print(list2)
print(list3) """

""" cards1 = []
if len(cards1) > 0 and "haha" in cards1[0]:
# if "haha" in cards1[0] and len(cards1) > 0:
    del cards1[0]
    print("if")
else:
    print("else") """
    
""" import numpy as np

list = [[0, 23], [1, 21], [2, 22]]
list.sort(key=lambda x: x[1])
print(list)

print(list[-1:-3])
print(list[-1:]) # 착각하지 말자. 역순으로 처음부터 끝까지가 아니라 마지막 것부터 끝까지이다. """

""" import math

print(math.trunc(7.14))
print(math.trunc(-7.14)) # 소수 부분만 제거 """

""" a = None
b = "Hello"
result = a or b
print(result)  # 출력: Hello

a = [1, 2, 3]
b = [4, 5, 6]
result = a or b
print(result)  # 출력: [1, 2, 3] """

""" small = b if a > b else a """

""" num = int(input("정수 1개를 입력하시오: "))
for x in range(1, num+1):
    if '3' in str(x) or '6' in str(x) or '9' in str(x):
    # if any([True for i in ['3', '6', '9'] if i in str(x)]): # if만
    # if any([True if i in str(x) else False for i in ['3', '6', '9']]): # if, else
    # if any((one_num in str(x)) for one_num in ['3', '6', '9']):
        print("X", end=' ')
    else:
        print(x, end=' ') """
        
""" input_list = [1, 3, 5, 6, 10, 15]
output_list = ["A" if x % 3 == 0 else ("B" if x % 5 == 0 else "C") for x in input_list]

print(output_list)  # 출력: ['C', 'A', 'B', 'A', 'B', 'A'] """
        
""" def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(is_even, numbers))

print(even_numbers)  # 출력: [2, 4, 6, 8]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # 출력: [2, 4, 6, 8]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)  # 출력: [2, 4, 6, 8] """

""" for x in range(1, 11, 2):
    # print(f"{'*'*x:^11}")
    # print(f"{'*'*x:>11}")
    # print(f"{'*'*x:<11}")
    
    print(f"{'*'*x:-^11}") """
    
""" num = 0.12347
print(f"{num:.4f}") # 0.1235

print(f"{num:10.3f}")
print(f"{num:^10.3f}")
print(f"{num:<10.3f}")

print(f"{num:a>10.3f}")
print(f"{num:a^10.3f}")
print(f"{num:a<10.3f}") """

""" print(int(float("4.2")))
print(int("4.2")) # 오류 """