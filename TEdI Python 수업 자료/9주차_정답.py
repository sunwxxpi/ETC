# 프로젝트 - painter 
'''
from tkinter import *

mycolor = "pink"
def paint(event):
    x1, y1 = (event.x-10), (event.y+10)
    x2, y2 = (event.x-2), (event.y+2)
    canvas.create_oval(x1, y1, x2, y2, fill = mycolor)    

def change_color(): # 색깔 바꾸기 함수 
    global mycolor
    mycolor = e.get()

window = Tk()

canvas = Canvas(window, width = 300, height = 300)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

e = Entry(window)
e.pack()

button = Button(window, text ="color : red", command = change_color) 
button.pack()
window.mainloop()

# 연습문제

from tkinter import *

mycolor = "pink"
b = "oval" # 연습문제
size = 10
def paint(event):
    
    x1, y1 = (event.x-size), (event.y+size)
    x2, y2 = (event.x), (event.y)
    if b == "oval":
        canvas.create_oval(x1, y1, x2, y2, fill = mycolor, outline = mycolor)    
    if b == "rectangle":
        canvas.create_rectangle(x1, y1, x2, y2, fill = mycolor, outline = mycolor)
    if b == "line":
        canvas.create_line(x1, y1, x2, y2, fill = mycolor, outline = mycolor)

    

def change_color(): # 색깔 바꾸기 함수 
    global mycolor
    mycolor = e.get()

def rect () : # 연습문제 1 
    global b
    b = "rectangle"
 
def line () : # 연습문제 2
    global b
    b = "line"


def up(): # 연습문제 3
    global size
    if size < 20 :
        size += 1

def down():
    global size
    if size > 1 :
        size -= 1 
    
window = Tk()

canvas = Canvas(window, width = 300, height = 300)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

e = Entry(window)
e.pack()

btn1 = Button(window, text = "직사각형", command = rect)
btn1.pack()
btn2 = Button(window, text = "line", command = line)
btn2.pack()
btn3 = Button(window, text = "Up", command = up)
btn3.pack()
btn4 = Button(window, text = "Down", command = down)
btn4.pack()

button = Button(window, text ="color : red", command = change_color) 
button.pack()
window.mainloop()


# 프로젝트 - 영어 퀴즈

import random
from tkinter import *

w = Tk()


dictionary = {
    'lion': '사자', 
    'apple': '사과',
    'airplane': '비행기',
    'zoo': '동물원',
    'sun': '태양'
}

keys = list(dictionary.keys())
k = 0
korean = ''
def question():
    global k
    global korean
    k = random.choice(keys)
    korean = dictionary[k]
    l1.config(text = korean)
    
def answer():
    global k
    global korean 
    guess = e.get()

    if guess == k: 
        l2.config(text = '정답') 
    else: 
        l2.config(text = '영어 단어의 번역이 틀립니다.')
l1 = Label(text = "영어 단어 번역 게임")
l1.pack()

l2 = Label(text = "다음 영어 단어를 번역하시오")
l2.pack()

e = Entry()
e.pack()

b1 = Button(text = "문제 출제", command = question)
b1.pack()

b2 = Button(text = "정답", command = answer)
b2.pack()

w.mainloop()

'''
# 사칙연산

import random
from tkinter import *

w = Tk()


a = 0
b = 0 

def question():
    global a, b 
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    t = str(a) + '+' + str(b)
    l2.config(text = t)
    
def answer():
    guess = int(e.get())
   
    if guess == a + b: 
        l2.config(text = '정답') 
    else: 
        l2.config(text = '오답.')
l1 = Label(text = "숫자 퀴즈")
l1.pack()

l2 = Label(text = '')
l2.pack()

e = Entry()
e.pack()

b1 = Button(text = "문제 출제", command = question)
b1.pack()

b2 = Button(text = "정답", command = answer)
b2.pack()

w.mainloop()

