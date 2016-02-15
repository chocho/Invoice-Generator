#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont
import os 



pdfmetrics.registerFont(TTFont('Arial', 'arialbi.ttf'))
fields = ['Име на фирма (Получател)', 'Град/Село*', 'Адрес:*', 'Идент. No:*', 'Материално Отговорно Лице (МОЛ)*', 'Име на файла(без разширението)']
stringvars = []
D = {}
root = Tk()
frm = Frame(root, width=350, height=80)

def fetch():
    coords =  0
    filename = fields[-1]
    if D[filename].get() == '':
        showwarning('Грешка', 'Не сте въвели име на файла')
        return  
    else:
        pdfnum =  D[filename].get()   
    ime = pdfnum + '.pdf'   
    c = canvas.Canvas(pdfnum + '.pdf')
    fullpathtofile = os.path.abspath('') + os.sep + ime
    
    print(fullpathtofile)
    if os.path.isfile(fullpathtofile):
        showwarning('Грешка', 'Файлът вече съществува: ' + ime)
        return
    
    c.setFont("Arial", 14)        
         
    for key in list(D.keys()):       
        if D[key].get() == '':
            showwarning('Грешка', 'Моля, попълнете полето:' + key)
            return
        x = D[key].get()
        c.drawString(coords, 50, x.encode('utf-8'))
        coords += 100    
    c.save()
    
for field in fields:
    var = StringVar()
    label = Label(root, text=field)
    label.pack(side=TOP)
    ent = Entry(root)
    ent.config(textvariable=var)
    ent.pack(side=TOP)
    D[field] = var
    #stringvars.append(D[field])
button = Button(root, text='Генерирай фактура', command=fetch)
button.pack(side=TOP)

frm.pack()
root.mainloop()