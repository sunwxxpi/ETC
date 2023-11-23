from tkinter import *

#변수에 대해 초기 값 선언
op=' ' #연산자 저장 변수
temp_num=0 #이전 값을 저장하기위한 변수


def button_press(value):  
    if value=='C':
        entry.delete(0, 'end')
    else:
        entry.insert('end',value)

def math_button(value):
    global op
    global temp_num
    if not entry.get()==' ': 
        op=value
        temp_num=float(entry.get())
        entry.delete(0,'end') # 입력상자의 이전 숫자 삭제되고,  다음 숫자를 받을 준비

def equal_button():
    global op
    global temp_num
    if not (op==' ' and entry.get()==' '): #연산기호와 숫자가 있을 때만 계산해야 한다.
        num=float(entry.get()) #op이후에 입력되는 숫자 값이 num에 저장된다. 
        if op == '/':
            result=temp_num/num
        elif op == '*':
            result=temp_num*num
        elif op == '+':
            result=temp_num+num
        else:
            result=temp_num-num
            
        entry.delete(0,'end') #계산식 지우기
        entry.insert(0,result) # 계산 결과 입력시키기

        op=' '
        temp_num=0

root=Tk()

root.title('My Calculator')
entry=Entry(root,width=33,bg='yellow')
entry.grid(row=0, column=0, columnspan=5)

b1=Button(root, text='7', width=5, command=lambda:button_press('7'))
b2=Button(root, text='8', width=5, command=lambda:button_press('8'))
b3=Button(root, text='9', width=5, command=lambda:button_press('9'))
b4=Button(root, text='/', width=5, command=lambda:math_button('/'))
b5=Button(root, text='C', width=5, command=lambda:button_press('C'))
b6=Button(root, text='4', width=5, command=lambda:button_press('4'))
b7=Button(root, text='5', width=5, command=lambda:button_press('5'))
b8=Button(root, text='6', width=5, command=lambda:button_press('6'))
b9=Button(root, text='*', width=5, command=lambda:math_button('*'))
b10=Button(root, text='&', width=5, command=lambda:button_press('&'))
b11=Button(root, text='1', width=5, command=lambda:button_press('1'))
b12=Button(root, text='2', width=5, command=lambda:button_press('2'))
b13=Button(root, text='3', width=5, command=lambda:button_press('3'))
b14=Button(root, text='-', width=5, command=lambda:math_button('-'))
b15=Button(root, text='^', width=5, command=lambda:button_press('^'))
b16=Button(root, text='0', width=5, command=lambda:button_press('0'))
b17=Button(root, text='.', width=5, command=lambda:button_press('.'))
b18=Button(root, text='=', width=5, command=lambda:equal_button())
b19=Button(root, text='+', width=5, command=lambda:math_button('+'))
b20=Button(root, text='@', width=5, command=lambda:button_press('@'))

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=1, column=3)
b5.grid(row=1, column=4)
b6.grid(row=2, column=0)
b7.grid(row=2, column=1)
b8.grid(row=2, column=2)
b9.grid(row=2, column=3)
b10.grid(row=2, column=4)
b11.grid(row=3, column=0)
b12.grid(row=3, column=1)
b13.grid(row=3, column=2)
b14.grid(row=3, column=3)
b15.grid(row=3, column=4)
b16.grid(row=4, column=0)
b17.grid(row=4, column=1)
b18.grid(row=4, column=2)
b19.grid(row=4, column=3)
b20.grid(row=4, column=4)

root.mainloop()
