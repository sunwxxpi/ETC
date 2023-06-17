#연습문제
'''
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
'''
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















