from tkinter import *
import time
import random

W=[]
X=[]
Y=[]
Z=[]
H=0
LX=0
myflag = True
infrx_i = 0
infrx_j = 0

def load_file():
    file=open("w.txt", "r")
    for item in file:
        item=item.strip()
        W.append(item)
    file.close()
    print(W)
    file=open("x.txt", "r")
    for item in file:
        item=item.strip()
        X.append(item)
    file.close()
    print(X)
    file=open("y.txt", "r")
    for item in file:
        item=item.strip()
        Y.append(item)
    file.close()
    print(Y)
    file=open("z.txt", "r")
    for item in file:
        item=item.strip()
        Z.append(item)
    file.close()
    print(Z)
    LX=20
    
    


def get_text_rus(i=0, j=0):
    res_rus=W[i] + " " + X[j]
    return(res_rus)

def get_text_eng(i=0, j=0):
    res_eng=Y[i] + " " + Z[j]
    return(res_eng)
    



def clicked(event):
    global myflag
    global infrx_i
    global infrx_j
    if  myflag:
        infrx_i = random.randint(0, 3)
        if infrx_i<2:
            infrx_j =  random.randint(0, 10)
        else:
            infrx_j =  random.randint(10, 20)
        lbl_rus.configure(text=get_text_rus(infrx_i,infrx_j))
        myflag=False
    else:
        lbl_eng.configure(text=get_text_eng(infrx_i,infrx_j))
        myflag=True

    print(infrx_i)
    print(infrx_j)





load_file()
window = Tk()  
window.title("Отработка паттернов английского языка")
window.geometry('400x250')

lbl_rus = Label(window, text="Привет")  
lbl_eng = Label(window, text="Hello!")  
lbl_rus.grid(column=0, row=0)
lbl_eng.grid(column=0, row=1)  

#txt = Entry(window,width=10)  
#txt.grid(column=1, row=0)  
#btn = Button(window, text="Клик!", command=clicked(flag))  
btn = Button(window,                  #родительское окно
             text="Click me",       #надпись на кнопке
             width=30,height=5,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", clicked)       #при нажатии ЛКМ на кнопку вызывается функция Hello


btn.grid(column=0, row=3)
#txt.focus()
window.mainloop()

