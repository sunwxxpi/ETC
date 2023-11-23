""" num = int(input("정수 1개를 입력하시오: "))
for x in range(1, num+1):
    if '3' in str(x) or '6' in str(x) or '9' in str(x):
    # if any([True for i in ['3', '6', '9'] if i in str(x)]):
    # if any([True if i in str(x) else False for i in ['3', '6', '9']]):
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


""" a, b = map(int, input().split())

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10, 15, 20]
print(list1 + list2)
print(list(map(lambda a, b: a + b, list1, list2))) # map() : 각각의 원소 like iterate~ """


""" print("3+4")
print(eval("3+4")) """

# class BlackBox:
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
# BlackBox.set_travel_mode(b1, 20) # 같은 것


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









""" # 연습문제
class Calculate:
    def __init__(self, a, b) :
        self.a = a
        self.b = b

    def __str__(self) : 
        return f'add 함수를 사용해서 {self.a}과 {self.b}을 더할 수 있습니다'

    def add(self):
        return self.a + self.b
    
cal = Calculate(3, 7)
result = cal.add()
print(result)

print(cal) """