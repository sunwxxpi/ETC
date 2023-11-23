import random
from tkinter import *

w = Tk()


print('영어 단어 번역 게임')
print('영어 단어를 번역하는 게임 입니다.')

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
