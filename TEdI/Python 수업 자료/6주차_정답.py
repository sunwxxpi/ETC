""" def hello():
    print("Hello")

hello() """

""" def hello(name):
    print("Hello", name)

hello("yangjewon")
hello("janghanseo") """

""" def return_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    
    return sum

print(f"합계는 {return_sum(1, 5)}이다.") """

""" def order():
    print("주문하실 음료를 알려주세요.")
    drink = input()
    print(drink, "주문하셨습니다.")

order() """

""" def price(num_drink):
    price_drink = 2500
    total_price = num_drink * price_drink
    
    return total_price

num_drink = input()
# num_drink = int(input())
total_price = price(num_drink) # 지역 변수, 전역 변수
print(f"총 가격은 {total_price}입니다.") """

""" def gugudan(num):
    for i in range(1, 10):
        print(f"{num} x {i} = {num * i}")

gugudan(3) """

""" def my_gcd(a, b):
    small = b if a > b else a

    for i in range(1, small+1):
        if (a % i == 0) and (b % i == 0):
            result = i
            
    return result

num1 = int(input("첫 번째 수: "))
num2 = int(input("두 번째 수: "))

gcd_of_num = my_gcd(num1, num2)
print(f"{num1}과 {num2}의 최대공약수는 {gcd_of_num}입니다.") """

""" from math import gcd, lcm

a, b = 20, 25
print(gcd(a, b)) # Greatest Common Divisor (최대 공약수)
print(lcm(a, b)) # Least Common Multiple (최소 공배수) """

""" def return_sum(start=1, end=10, jump=1):
    sum = 0
    for i in range(start, end+1, jump):
        sum += i
    
    return sum

# print(return_sum())
# print(return_sum(9))
# print(return_sum(3, 5))
# print(return_sum(3, 5, 2))
# print(return_sum(end=8, jump=2, start=3)) """

""" def visit(today, *customers):
# def visit(today, *customers, last):
    print(today)
    print(customers)
    # today(last)
    for customer in customers:
        print(customer)

visit('2023년 1월 1일', '장발장', '이남수', '피선우') """

""" numbers = 1, 2, 3, 4, 5
# print(numbers)

# numbers : (1, 2, 3, 4, 5)
# one, two, three, four, five = numbers
# print(one, two, three, four, five)

one, two, *others = numbers
print(one, two, others) """

def return_sum(start=1, end=10):
    sum = 0
    for i in range(start, end+1):
        sum += i
    
    return sum

""" def return_first(start=1, end=10):
    first = list(range(start, end+1))[0]

    return first

# my_func_list = [return_sum(), return_first()]
# print(my_func_list)

my_func_list = [return_sum, return_first]
print(my_func_list)
print(my_func_list[0]()) # return_sum()
print(my_func_list[1]()) # return_first()
print(f"합계는 {my_func_list[0]()}이다.") """

""" def my_func():
    list1.append('hello2')
    list1[0] = 'impossible' # global 선언 없이도 전역 변수 접근 가능 (List)
        
    global message
    message = 'message 변수를 바꿔보자' # global 선언 있어야 전역 변수 접근 가능 (String)
    
message = '나는야 전역변수' # 전역 변수
list1 = ['hello1'] # 전역 변수
print(message)
print(list1)
    
my_func()
print(message)
print(list1)
################## List : mutable, Tuple, String : immutable ################## """

""" str1 = 'abc'
str1 = 'hello'
print(str1) """

""" str1 = 'abc'
str1[1] = 'h'
print(str1) """

""" str1 = 'abc'
print(list(str1)) # ['a', 'b', 'c']
list(str1)[1] = 'h'
print(list(str1)) # ['a', 'b', 'c']
final_str = ''.join(str1)
print(final_str) """

""" str1 = 'abc'
list1 = list(str1)
list1[1] = 'h'
final_str = ''.join(list1)
print(final_str) """

""" list1 = [1, 2, 3]
list2 = list1.copy()

list1[1] = 5
print(list2) """

""" def hello(n):
    if n < 1:
        return

    print("안녕")
    return hello(n - 1)

hello(3) """

""" # 출발 기둥에서 도착 기둥으로 보조 기둥을 이용하여 n개의 원판을 옮긴다.
def hanoi_tower(n, 출발, 도착, 보조):
    if n > 0:
        # 출발 기둥에서 보조 기둥으로 도착 기둥을 이용하여 n - 1개의 원판을 옮긴다.
        hanoi_tower(n - 1, 출발, 보조, 도착)

        # 출발 기둥에서 도착 기둥으로 n번째 원판을 옮긴다.
        print(f"{n} 번 원판을 {출발} 기둥에서 {도착} 기둥으로 옮긴다.")
        
        # 보조 기둥에 놓인 n - 1개의 원판을 도착 기둥으로 옮긴다.
        hanoi_tower(n - 1, 보조, 도착, 출발)

원판_개수 = 4
hanoi_tower(원판_개수, 'A', 'C', 'B') """















""" # 연습문제
# 1

def even_odd(n) :
    if n % 2 == 0 :
        print("%d는 홀수 입니다" % n)
    else :
        print("%d는 짝수 입니다" % n)


# 2
def Number(num) :
    list_new = []
    for x in range(1, num + 1) :
        list_new.append(x**2)
    return list_new
n = int(input("n 값을 입력하세요:"))
num_list = Number(n)
print(num_list)

# 3

def payment(pay, hour) :
    return pay * hour * 0.97

pay = int(input('시급을 입력하시요 :'))
hour = int(input('근무 시간을 입력하시오 :'))
p = payment(pay, hour)
print("월급은 :", p)


#4

def prime(n) :
    if n < 2 :
        print("1 이상의 수 입력해주세요")
        return 0
    for x in range(2, n) :
        if n % x == 0 :
            return False
    return True

def p(n) :
    for x in range(2, n+1) :
        if prime(x):
            print("%d 소수 입니다"% x)

# 5
def s(n) :
    if n < 1:
        return n 
    return s(n-1) + n

# 6
def isValid(p):
    if len(p)<10:
        return False
    is_num=False
    is_upper=False
    for x in p:
        if x.isupper() :
            is_upper = True
        if x.isdigit():
            is_num = True 
    
    return is_upper and is_num

print("▶ 비밀번호는 10자리 이상, 영문 대문자를 포함하여야 합니다.")
pw = input("비밀번호 입력 :")
if isValid(pw):
    print("유효한 비밀번호입니다")
else: 
    print("비밀번호가 잘못되었습니다! 다시 입력해 주세요") """