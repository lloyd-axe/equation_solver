from tkinter import *
from main_solver import remote_solve

root = Tk()
root.title("Simple Calculator")

#USER ENTRY BAR
entry_b = Entry(root, width=55, borderwidth=5)
entry_b.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
entry_b.insert(0, "Enter Equation here")

def btn_clk(val):
    eq = entry_b.get()
    entry_b.delete(0, END)
    if val == '=':
        eq = remote_solve(eq)
        entry_b.insert(0, eq)
    elif val == 'c':
        entry_b.delete(0, END)
    else:
        if eq == "Enter Equation here":
                entry_b.insert(0,str(val))
        else:
                entry_b.insert(0, eq + str(val))
#No. Buttons
eq_btn = Button(root, text="=", command=lambda: btn_clk('='), width=26,height=3)
btn1 = Button(root, text='1', command=lambda: btn_clk(1), width=12,height=3)
btn2 = Button(root, text="2", command=lambda: btn_clk(2), width=12,height=3)
btn3 = Button(root, text="3", command=lambda: btn_clk(3), width=12,height=3)
btn4 = Button(root, text="4", command=lambda: btn_clk(4), width=12,height=3)
btn5 = Button(root, text="5", command=lambda: btn_clk(5), width=12,height=3)
btn6 = Button(root, text="6", command=lambda: btn_clk(6), width=12,height=3)
btn7 = Button(root, text="7", command=lambda: btn_clk(7), width=12,height=3)
btn8 = Button(root, text="8", command=lambda: btn_clk(8), width=12,height=3)
btn9 = Button(root, text="9", command=lambda: btn_clk(9), width=12,height=3)
btn0 = Button(root, text="0", command=lambda: btn_clk(0), width=12,height=3)
add_btn = Button(root, text="+", command=lambda: btn_clk("+"), width=12,height=3)
sub_btn = Button(root, text="-", command=lambda: btn_clk("-"), width=12,height=3)
mul_btn = Button(root, text="x", command=lambda: btn_clk("*"), width=12,height=3)
div_btn = Button(root, text="/", command=lambda: btn_clk("/"), width=12,height=3)
cls_btn = Button(root, text="CLS", command=lambda: btn_clk("c"), width=12,height=3)
ob_btn = Button(root, text="(", command=lambda: btn_clk("("), width=12,height=3)
cb_btn = Button(root, text=")", command=lambda: btn_clk(")"), width=12,height=3)
p_btn = Button(root, text="^", command=lambda: btn_clk("^"), width=12,height=3)


#Button Positions
eq_btn.grid(row=5,column=1,columnspan=2)
btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1)
btn3.grid(row=2,column=2)
btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btn7.grid(row=4,column=0)
btn8.grid(row=4,column=1)
btn9.grid(row=4,column=2)
btn0.grid(row=5,column=0)
add_btn.grid(row=2,column=3)
sub_btn.grid(row=3,column=3)
mul_btn.grid(row=4,column=3)
div_btn.grid(row=5,column=3)
cls_btn.grid(row=1,column=3)
ob_btn.grid(row=1,column=0)
cb_btn.grid(row=1,column=1)
p_btn.grid(row=1,column=2)

#MAIN LOOP
root.mainloop()

