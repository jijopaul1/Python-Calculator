
from tkinter import *

expression = ""

def presstheno(num):
    global expression
    expression = expression + str(num)
    box.set(expression)
 
def equaltoo():
    global expression
    total = str(eval(expression))
    box.set(total)
    expression = ""
 
def clear():
    global expression
    expression = ""
    box.set("")

if __name__ == "__main__":
    w = Tk()
    w.resizable(0,0)
    w.title('                                              CALCULATOR')
    w.geometry('454x180')
    

    button_7=Button(w,text="7",command=lambda: presstheno(7),width=10)
    button_7.grid(row=1,column=1,padx=5,pady=10)
    
    button_8=Button(w,text="8",command=lambda: presstheno(8),width=10)
    button_8.grid(row=1,column=2,padx=5,pady=10)
    
    button_9=Button(w,text="9",command=lambda: presstheno(9),width=10)
    button_9.grid(row=1,column=3,padx=5,pady=10)
    
    button_4=Button(w,text="4",command=lambda: presstheno(4),width=10)
    button_4.grid(row=2,column=1)
    
    button_5=Button(w,text="5",command=lambda: presstheno(5),width=10)
    button_5.grid(row=2,column=2)
    
    button_6=Button(w,text="6",command=lambda: presstheno(6),width=10)
    button_6.grid(row=2,column=3)
    
    button_1=Button(w,text="1",command=lambda: presstheno(1),width=10)
    button_1.grid(row=3,column=1,padx=5,pady=10)
    
    button_2=Button(w,text="2",command=lambda: presstheno(2),width=10)
    button_2.grid(row=3,column=2)
    
    button_3=Button(w,text="3",command=lambda: presstheno(3),width=10)
    button_3.grid(row=3,column=3)
    
    button_0=Button(w,text="0",command=lambda: presstheno(0),width=10)
    button_0.grid(row=4,column=1)
    
    button_dot=Button(w,text=".",command=lambda: presstheno('.'),width=10)
    button_dot.grid(row=4,column=2)
    
    button_plus=Button(w,text="+",command=lambda: presstheno('+'),width=10)
    button_plus.grid(row=1,column=5,padx=5,pady=10)
    
    button_minus=Button(w,text="-",command=lambda: presstheno('-'),width=10)
    button_minus.grid(row=1,column=6,padx=5,pady=10)
    
    button_power=Button(w,text="^",command=lambda: presstheno('^'),width=10)
    button_power.grid(row=3,column=5,padx=5,pady=10)
    
    button_multi=Button(w,text="*",command=lambda: presstheno('*'),width=10)
    button_multi.grid(row=2,column=5)
    
    button_div=Button(w,text="/",command=lambda: presstheno('/'),width=10)
    button_div.grid(row=2,column=6)
    
    button_modu=Button(w,text="%",command=lambda: presstheno('%'),width=10)
    button_modu.grid(row=3,column=6)
    
    button_clear=Button(w,text="CLEAR",command=clear,width=10,fg='red')
    button_clear.grid(row=4,column=3)
    
    button_equal=Button(w,text="=",command=equaltoo,width=23,fg='green')
    button_equal.grid(row=4,column=5,columnspan=2)
    
    box = StringVar()
    expression_field = Entry(w, textvariable=box)
    expression_field.grid(columnspan=45, ipadx=158,padx=5,pady=10)
        
    w.mainloop()

