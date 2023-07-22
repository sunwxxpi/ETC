""" # 논리 표현식의 단축 평가(Short-circuit Evaluation)
# x = 10
x = 25
print(x == (10 or 25))

# <and>
# TT T
# TF F
# FT F
# FF F

# <or>
# TT T
# TF T
# FT T
# FF F    
# True -> or : 왼, and : 오
# False -> or : 오, and : 왼
print(3 or 5) # 3
print(3 and 5) # 5
print(None or 5) # 5
print(None and 5) # None

print(3 and None and 4) # None
print(bool(None)) """


""" def return_var(x=None):
    var = x
    
    return var

y = return_var(5) or 3
print(y) """


""" f = open('8주차_list.txt', 'w', encoding='utf8') # File 없으면 자동으로 생성, 있으면 내용 초기화 후 write
f.write('피선우\n')
f.write('TEdI\n')
f.close() """


""" f = open('8주차_list.txt', 'r', encoding='utf8')
print(f)

for line in f:
    print(line.rstrip())
    # print(line, end='')
    
f.close() """


""" f = open('8주차_list.txt', 'r', encoding='utf8')
# f.seek(0)
# contents = f.read()
# contents = f.readline().rstrip()
contents = f.readlines()

print(contents)
f.close() """

""" # File 없으면 자동으로 생성, 있으면 내용 초기화 후 write
with open('8주차_list2.txt', 'w', encoding='utf8') as f:
    f.write('피선우\n')
    f.write('양재원\n')
    f.write('장한서\n') """
    

""" with open('8주차_list2.txt', 'a', encoding='utf8') as f: # File 없으면 자동으로 생성, 있으면 내용 추가 (append)
    f.write("Hello, i'm\n")
    f.write('Sun Woo Pi\n') """


# print('I'm Sun Woo Pi')


""" # good book friend
with open("8주차_list3.txt", "r", encoding="UTF8") as f:
    for line in f:
        # line = line.rstrip()
        # print(line)
        
        word_list = line.split()
        print(word_list)
        
        for word in word_list:
            print(word) """


""" in_file_name = input("입력 파일 이름 : ")
out_file_name = input("출력 파일 이름 : ")

infile = open(in_file_name, "r")
outfile = open(out_file_name, "w")

s = infile.read()
outfile.write(s)

infile.close()
outfile.close() """


'''import pickle

gameOption = {
    "Sound": 8,
    "VideoQuality": "HIGH", 
    "Money": 100000,
    "WeaponList": ["gun", "missile", "knife"]
    }

""" with open("8주차_game.txt", "wb") as file:
    pickle.dump(gameOption, file) # Dict를 pickle File에 저장 """

""" with open("game.txt", "rb") as file:
    data = pickle.load(file)
    print(data) """'''



















'''
#연습문제

#1
file = open("stationery.txt", mode = "r", encoding = "UTF8")
f = file.readlines ()
file.close()

s = [] 
for x in range(len(f)):
    a = f[x].split(',')
    s.append(a)

# 마지막 \n 작업 대신 int 함수 사용
m = 10000000000
i = 0 
for x in range(len(s)) :
    if int(s[x][2]) < m :
        m = int(s[x][2])
        i = x

print(s[i][0])

# 2

file = open("배수.txt", mode = "w", encoding = "UTF8")

for x in range(1, 101) :
    if x % 3 == 0 :
        t = str(x) + '\n'
        file.write(t) 

file.close()

# 3
f = input('파일명을 입력하세요')
text = input('삭제할 문자열을 입력하세요')
file = open(f, mode = "r", encoding = "UTF8")

fr = file.readlines()

file.close()

file = open(f, mode = "w", encoding = "UTF8") 
for x in range(len(fr)) :
    
    if text + '\n' != fr[x] :
        file.write(fr[x])

file.close()

# 4
import pickle as p 
a = 12
b = 3.14
c = [1,2,3,4,5]
file = open("test.dat", mode = "wb")
p.dump(a, file)
p.dump(b, file)
p.dump(c, file)
file.close()

file = open("test.dat", mode = "rb")
data = []
while True:
    try :
        d = p.load(file)
        data.append(d) 
    except :
        break 
        
print(data)
file.close()

# 5

file = open("student.txt", mode = "r", encoding = "UTF8")
f = file.readlines()
file.close()

students = {}

for x in range(len(f)) :
    f[x] = f[x].strip('\n') 
    f[x] = f[x].split(',')
    students[f[x][0]] = f[x][1:]

print(students)

import pickle
file = open("stduents_results.txt", mode = "wb")
pickle.dump(students, file)
file.close()


# 6

#import pickle
score = [87, 92, 73]
keys = list(students.keys()) 
for x in range(len(keys)) :
    students[keys[x]].append(score[x])


file = open("students_average.txt", mode = "wb")
pickle.dump(students, file)
file.close()

# 7
a = input('학번을 입력하시오')

print(f"{a} 학생 : {students[a][0]}, HP :{students[a][1]}")
'''