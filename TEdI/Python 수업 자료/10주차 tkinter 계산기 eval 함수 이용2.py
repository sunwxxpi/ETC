from tkinter import *
 
def press(value):
    if value=='C':
        entry.delete(0, 'end')
    elif value=='=':
        result=eval(entry.get())
        entry.delete(0, 'end')
        entry.insert(0, result)
    elif value=='√':
        value='**0.5'
        entry.insert('end', value)
    elif value=='^':
        value='**'
        entry.insert('end', value)
    elif value=='@':
        value='/100'
        entry.insert('end', value)
    else:
        entry.insert('end', value)

root=Tk()
root.title('계산기_eval 함수이용')

entry=Entry(root, width=20, bg='white', fg='skyblue')
entry.insert(0, ' ')
entry.pack(pady=5)

buttons=['7410', '852.', '963=', '+-*/', 'C^√@']  

for col in buttons: #col=column의 약자
    frame=Frame(root)
    frame.pack(side=LEFT)
    for row in col:
        button=Button(frame, text=row, width=5, height=2, bg='white', fg='purple', \
                      command=(lambda char=row:press(char)))
        #char=character의 약자
        button.pack(fill=X, padx=5, pady=5)

root.mainloop()
