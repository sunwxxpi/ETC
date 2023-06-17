from tkinter import * 
# 그림판 

def paint(event): # 마우스의 x좌표 y좌표 전달 받음 
  x1, y1 = (event.x-10) , (event.y-10)
  x2, y2 = (event.x+10) , (event.y+10)
  canvas.create_oval(x1, y1, x2, y2, fill = "black", outline = "black")

window = Tk() 

canvas = Canvas(window, width = 300 , height = 300)
canvas.pack()
# 버튼을 클릭했을때 함수 실행 
canvas.bind("<B1-Motion>", paint) # paint 함수 실행 

black = Button(window, bg = "black")
black.place(x = 10, y = 10)
window.mainloop() 
