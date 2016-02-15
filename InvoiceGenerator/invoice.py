#!/usr/bin/python
# -*- coding: utf-8 -*-
#proba
from tkinter import *
from tkinter.messagebox import *
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics 
from reportlab.pdfbase.ttfonts import TTFont
import os 



pdfmetrics.registerFont(TTFont('Arial', 'arialbi.ttf'))
fields = ['Р�РјРµ РЅР° С„РёСЂРјР° (РџРѕР»СѓС‡Р°С‚РµР»)', 'Р“СЂР°Рґ/РЎРµР»Рѕ*', 'РђРґСЂРµСЃ:*', 'Р�РґРµРЅС‚. No:*', 'РњР°С‚РµСЂРёР°Р»РЅРѕ РћС‚РіРѕРІРѕСЂРЅРѕ Р›РёС†Рµ (РњРћР›)*', 'Р�РјРµ РЅР° С„Р°Р№Р»Р°(Р±РµР· СЂР°Р·С€РёСЂРµРЅРёРµС‚Рѕ)']
stringvars = []
D = {}
root = Tk()
frm = Frame(root, width=350, height=80)

def fetch():
    coords =  0
    filename = fields[-1]
    if D[filename].get() == '':
        showwarning('Р“СЂРµС€РєР°', 'РќРµ СЃС‚Рµ РІСЉРІРµР»Рё РёРјРµ РЅР° С„Р°Р№Р»Р°')
        return  
    else:
        pdfnum =  D[filename].get()   
    ime = pdfnum + '.pdf'   
    c = canvas.Canvas(pdfnum + '.pdf')
    fullpathtofile = os.path.abspath('') + os.sep + ime
    
    print(fullpathtofile)
    if os.path.isfile(fullpathtofile):
        showwarning('Р“СЂРµС€РєР°', 'Р¤Р°Р№Р»СЉС‚ РІРµС‡Рµ СЃСЉС‰РµСЃС‚РІСѓРІР°: ' + ime)
        return
    
    c.setFont("Arial", 14)        
         
    for key in list(D.keys()):       
        if D[key].get() == '':
            showwarning('Р“СЂРµС€РєР°', 'РњРѕР»СЏ, РїРѕРїСЉР»РЅРµС‚Рµ РїРѕР»РµС‚Рѕ:' + key)
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
button = Button(root, text='Р“РµРЅРµСЂРёСЂР°Р№ С„Р°РєС‚СѓСЂР°', command=fetch)
button.pack(side=TOP)

frm.pack()
root.mainloop()