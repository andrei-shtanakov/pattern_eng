import requests  # Import JSON encoder and decoder module
import time
import random
import json      # requests module used to send REST requests to API
from tabulate import *
from tkinter import *


items = []
dicts = []
main_key = ""
main_rus = ""
me = {"man": "мужчина", "boy": "мальчик", "bank": "банк"}
fe= {"woman": "женщина", "girl": "девочка", "plate": "тарелка"}
mn={"men": "мужчины", "boys": "мальчики", "banks": "банки","women": "женщины", "girls": "девочки", "plates": "тарелки"}
this=(me, fe)      
these=(mn,)
d = {"this": this, "these": these, "that": this, "those": these}

text_rus = ""
text_eng = ""
myflag = True




def make_this():
    global items 
    global dicts
    global  main_key
    global  main_rus
    global me 
    global fe
    global  mn
    global this     
    global  these

    global d 

    global text_rus
    global text_eng


    for i in (d.keys()):
        dicts .append(i)
    n= random.randint(0, len(d)-1)
    main_key = dicts[n]
    items = []

    j= random.randint(0, len(d[main_key])-1)
    for i in (d[main_key][j].keys()):
        items.append(i)


    if main_key == "this":
        if j == 0:
            main_rus = "этот"
        else:
            main_rus = "этa"
    elif main_key == "these":
        main_rus = "эти"
    elif main_key == "that":
        if j == 0:
            main_rus = "тот"
        else:
            main_rus = "тa"
    else:
        main_rus = "те"
    
    k= random.randint(0, len(items)-1)

    text_rus = main_rus+" "+d[main_key][j][items[k]]
    text_eng = main_key+" "+items[k]

def reaf_file():
    devices=[]
    file=open("devices.txt", "r")
    for item in file:
        item=item.strip()
        devices.append(item)
    file.close()
    print(devices)



def clicked(event):
    global myflag
    global infrx_i
    global infrx_j

    global text_rus
    global text_eng
    global myflag 

    if myflag:
        make_this()
        lbl_rus.configure(text=text_rus)
        lbl_eng.configure(text="")
        myflag = False
    else:
        myflag = True
        lbl_eng.configure(text=text_eng)



window = Tk()  
window.title("Отработка паттернов английского языка")
window.geometry('400x250')

lbl_rus = Label(window, text="Привет")  
lbl_eng = Label(window, text="Hello!")  
lbl_rus.grid(column=0, row=0)
lbl_eng.grid(column=0, row=2)  

#txt = Entry(window,width=10)  
#txt.grid(column=1, row=0)  
#btn = Button(window, text="Клик!", command=clicked(flag))  
btn = Button(window,                  #родительское окно
             text="Click me",       #надпись на кнопке
             width=30,height=1,     #ширина и высота
             bg="white",fg="black") #цвет фона и надписи
btn.bind("<Button-1>", clicked)       #при нажатии ЛКМ на кнопку вызывается функция Hello


btn.grid(column=0, row=5)
#txt.focus()
window.mainloop()


#make_this()

##print(text_rus)
#print(text_eng)
