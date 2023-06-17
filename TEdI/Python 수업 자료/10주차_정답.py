# 연습문제 Guessing number
'''
import random
from tkinter import *

w = Tk()

#com = random.randint(1, 100)
com = 0 


def question():
    global com
    com = random.randint(1, 100)
    l2.config(text = t)
    
def answer():
    guess = int(e.get())
   
    if guess < com : 
        l2.config(text = '작음')
    elif guess > com : 
        l2.config(text = '큼') 
    else: 
        l2.config(text = '정답')
l1 = Label(text = "숫자 추측(1~100")
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
'''

from tkinter import *
def ctoi() :
    c = int(e2.get()) * 2.54
    e1.delete(0, "end") 
    e1.insert(0, str(c))

def itoc() :
    i = int(e1.get()) / 2.54
    e2.delete(0, "end") 
    e2.insert(0, str(i))



window = Tk()

l1 = Label(window, text = "인치")
l2 = Label(window, text = "센치")

l1.pack()
l2.pack()

e1 = Entry(window)
e2 = Entry(window)

e1.pack()
e2.pack()

b1 = Button(window, text = "인치 -> 센치", command = itoc)
b2 = Button(window, text = "센치 -> 인치", command = ctoi)
b1.pack()
b2.pack()


# 메뉴 위젯 생략 

window.mainloop()
