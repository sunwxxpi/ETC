""" num = int(input("정수 1개를 입력하시오: "))

for x in range(1, num+1):
    if '3' in str(x) or '6' in str(x) or '9' in str(x):
    # if any([True for i in ['3', '6', '9'] if i in str(x)]):
    # if any((one_num in str(x)) for one_num in ['3', '6', '9']):
        print("X", end=' ')
    else:
        print(x, end=' ') """


""" def my_func(x):
    return x + 1

my_func = lambda x: x + 1

result = my_func(2)
print(result)

# print((lambda a, b: a + b)(3, 7)) """


""" def my_func(x):
    return x < 5

print(list(filter(lambda x: x < 5, range(10)))) """


""" array1 = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array1, key=my_key)) # .sort() != sorted()
print(sorted(array1, key=lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10, 15, 20]
print(list1 + list2)
print(list(map(lambda a, b: a + b, list1, list2))) # map() : 각각의 원소 like iterate~ """




















# 연습문제
class Calculate :
    def __init__(self, a, b) :
        self.a = a
        self.b = b

    def __str__(self) : 
        return 'add 함수 사용해서 더할 수 있습니다'

    def add(self):
        return self.a + self.b