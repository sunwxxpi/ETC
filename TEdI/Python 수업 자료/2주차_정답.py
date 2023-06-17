# ppt


# b = " "
# print(a[2])
# print(b[0])

# a = "abcde"
# a = ["a", "b", "c", "d", "e"]
# print(a[0:4])
# print(a[0:3:2])

# print(a[:3])
# print(a[3:])
# print(a[:]) 

# print(a[::2])
# print(a[1:4:2])

# 첫 시작 index는 0 마지막 index는 -1
# 1. 순서대로인지 역순서대로인지 확인
# 2. [3 : 6]이면 3~(6-1)번째 <마지막 껄 뺀다>
# print(list1[4:-1])
# print(list1[4:-1:1])
# print(list1[::1])
# print(list1[::-2])
# print(list1[-1:-3:-1]) # 5, 6 아니다 -> 6, 5

# print(list1[0:3:-1])
# print(list1[-1:-3])

# list1 = [0, 1, 2, 3, 4, 5, 6]
# print(list1[:-4])
# print(list1[:-4:-1])


# print("Today's weather is %s" %weather)
# print("Today's temperature is %.1f and humidity is %d%%" %(temp, humid))


# print("Today's weather is {}".format(weather))
# print("Today's temperature is {:.1f} and humidity is {:.2f}%".format(temp, humid))

weather = 'sunny'
temp = 15.321
humid = 23
# print(f"Today's weather is {weather}")
# print(f"Today's temperature is {temp:.1f} and humidity is {humid:.3f}%")


odd = [1, 2, 3, ["one", "two", "three", ["hello", "hello2"]], 4, 3.2, ["five"]]
# print(odd[3][3][1])
# odd[3][3] = "four"
# print(odd)

# a.insert(2, 6)
# print(a) 
# print(len(a))
# del a[0]
# a.remove(3)
# print(a)
# print(a)
# a.insert(0, 11)
# print(a)

# a[0] = 1
# print(a)
a = [1,2,3,1,4,5,3]
# a.pop(0)
# print(a)
# pop = a.pop(4)
# print(a)
# print(pop)

# 요일 = ["Mon", "Tues", "Wednes", "Thurs", "Fri"]

# 요일.remove("월")
# print(요일)
# 요일.append("토")
# print(요일)
# 요일.insert(2, "공휴일")
# print(요일)
# 요일.pop(-2) # 앞에서 번호
# print(요일)
# print(len(요일))


# dir = "./psw/KLGrade/OAI-KL/main.py"
# dir_list = dir.split()
# print(dir_list)


# 요일 = ["Mon", "Tues", "Wednes", "Thurs", "Fri"]
# 요일 = 'day, '.join(요일)
# print(요일)


""" today = "23-01-01"
todays = today.split('-')
print(todays)
print('.'.join(todays)) """

# join 이용하여 리스트 to 문자열
list1 = ["hello", "my", "name", "is", "pisunwoo"]
print(' hjghjghj '.join(list1))


a = [1, 2, 3]
b = list(reversed(a))
# print(b)

# a.reverse()
# print(a)




list1 = "pisunwoo"
# list1.sort()
# print(list1)
# print(hello)

# Function : 함수
# Method : Class 함수 (객체)

# list2 = [1, 3, 5, 23, 6, 2, 8]
# str2 = "pisunwoo"
# sorted_str2 = sorted(str2)
# print(str2)
# print(sorted_str2)


















# #연습문제
# #1.
# name = '김테디'
# print(name[0]+'*'+name[1])

# #2.
# a = "The beginning is half of the whole"
# print(a[4:13])
# #3.
# print(a[::-1])

# #4.

# temperature = 17.7
# humidity = 58
# today = 3 
# date = "월요일"

# print("오늘은 %d일 %s입니다. 오늘은 %0.1f도이며, 습도는 %d%%입니다." % (today, date, temperature, humidity))


# #5.
# num = "210101-4258964"
# print(num[:6], num[7:])

# #6. #, '''

# # 7.
# 과일 = ["체리", "사과", "딸기"]
# 과일.append("포도")
# 과일[0] = "자두"
# 과일.insert(1, "복숭아")
# 과일.remove("사과")
# print(len(과일))


# # 8.
# data = "2021-12-31"
# data = data.split('-')
# print(data[0] + "년", data[1] + "월", data[2] + "일")

# # 9.
# new_year = "새,복,많,이,받,으,세,요"
# new_year = new_year.split(',')
# print(new_year)
# new_year ='*'.join(new_year)
# print(new_year)