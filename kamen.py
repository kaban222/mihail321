from random import randint
from tkinter import *
root=Tk()
root.geometry('500x250') 
root["bg"] ="#7FFFD4"
lm = Label(root, text='что бы работоло нужно после хода нажимать кнопку очистить посленажать далее',fg="#eee", bg="#333" )
lm.pack()
 


def qaz():
  
  q = randint(1,3)
  def a():
      bttn.destroy()
      btttn.destroy()
      bttttn.destroy()
      n.destroy()
  
  def qwe():
         if q == 1:
          poetry = "проирал-бумага"
          label2 = Label(text=poetry, justify=LEFT)
          label2.place(relx=.2, rely=.3)
         if q == 2:
          poetry = "выйграл-ножнцы()"
          label2 = Label(text=poetry, justify=LEFT)
          label2.place(relx=.2, rely=.3)
          
         if q == 3:
          poetry = "()()ничья()()()"
          label2 = Label(text=poetry, justify=LEFT)
          label2.place(relx=.2, rely=.3)   
  def zxc():
        if q == 3:
         poetry = "выйграл-камень()"
         label2 = Label(text=poetry, justify=LEFT)
         label2.place(relx=.2, rely=.3)   
           
        if q == 2:
         poetry = "проиграл-ножницы"
         label2 = Label(text=poetry, justify=LEFT)
         label2.place(relx=.2, rely=.3)   
         
        if q == 1:
         poetry = "ничья"
         label2 = Label(text=poetry, justify=LEFT)
         label2.place(relx=.2, rely=.3) 
  def asd():
       if q == 1:
        poetry = "выйграл-бумага"
        label2 = Label(text=poetry, justify=LEFT)
        label2.place(relx=.2, rely=.3)   
        
       if q == 3:
        poetry = "проиграл-"
        label2 = Label(text=poetry, justify=LEFT)
        label2.place(relx=.2, rely=.3)
      
       if q == 2:
        poetry = "ничья  "
        label2 = Label(text=poetry, justify=LEFT)
        label2.place(relx=.2, rely=.3)
        
        
  bttn = Button(root, text="камень",command=qwe,
  background="#8B0000",     
             foreground="#FFFF00",     
             padx="20",            
             pady="8",           
             font="16"   )   
  bttn.pack()
  bttn.place(x=100, y=204)
  btttn = Button(root, text="бумага",command=zxc,
  background="#8B0000",     
             foreground="#FFFF00",     
             padx="20",            
             pady="8",           
             font="16")
  btttn.pack()
  btttn.place(x=316, y=204)
  bttttn =Button(root, text="ножницы",command=asd,
  background="#8B0000",     
             foreground="#FFFF00",     
             padx="20",            
             pady="8",           
             font="16"   )   
  bttttn.pack()
  bttttn.place(x=200, y=204)
  n = Button(root, text="очистить",command=a,
  background="#8B0000",     
             foreground="#ccc",     
             padx="10",            
             pady="8",          
             font="14"   )   
  n.pack()
  n.place(x=410, y=204)
 
btn = Button(root, text='далее', command=qaz,
background="#8B0000",     
             foreground="#ccc",     
             padx="20",            
             pady="8",           
             font="16"   )   
btn.pack()
btn.place(x=0, y=204)

