from tkinter import *

window = Tk()
window.title("калькулятор")
window.geometry('400x250')

num1 = ''
#Op = None
def C1():
    txt.insert(END, '1')
    global num1
    num1 += '1'
    return num1
def C2():
    txt.insert(END, '2')
    global num1
    num1 += '2'
    return num1
def C3():
    txt.insert(END, '3')
    global num1
    num1 += '3'
    return num1
def C4():
    txt.insert(END, '4')
    global num1
    num1 += '4'
    return num1
def C5():
    txt.insert(END, '5')
    global num1
    num1 += '5'
    return num1
def C6():
    txt.insert(END, '6')
    global num1
    num1 += '6'
    return num1
def C7():
    txt.insert(END, '7')
    global num1
    num1 += '7'
    return num1
def C8():
    txt.insert(END, '8')
    global num1
    num1 += '8'
    return num1
def C9():
    txt.insert(END, '9')
    global num1
    num1 += '9'
    return num1
def C0():
    txt.insert(END, '0')
    global num1
    num1 += '0'
    return num1
def Op1():
    global Op, num1, num2
    txt.insert(END, '+')
    num2 = float(num1)
    num1 = ''
    Op = 1
    return Op, num1, num2
def Op2():
    global Op, num1, num2
    txt.insert(END, '-')
    num2 = float(num1)
    num1 = ''
    Op = 2
    return Op, num1, num2
def Op3():
    global Op, num1, num2
    txt.insert(END, '*')
    num2 = float(num1)
    num1 = ''
    Op = 3
    return Op, num1, num2
def Op4():
    global Op, num1, num2
    txt.insert(END, '/')
    num2 = float(num1)
    num1 = ''
    Op = 4
    return Op, num1, num2
def Op5():
    global num1
    txt.insert(END, '.')
    num1 += '.'
    return num1

def Op6():
    global Op, num1, num2
    txt.insert(END, '**')
    num2 = float(num1)
    num1 = ''
    Op = 6
    return Op, num1, num2
def OpDEL():
    global num1, num2
    txt.delete(0, END)
    num1 = ''
    num2 = ''
def OpEND():
    if Op == 1:
        anus = str(float(num2) + float(num1))
        print(anus)
        txt.insert(END, '=' + anus)
        #анусы для феди
    elif Op == 2:
        ans = str(float(num2) - float(num1))
        print(ans)
        txt.insert(END, '=' + ans)
    elif Op == 3:
        ans = str(float(num2) * float(num1))
        print(ans)
        txt.insert(END, '=' + ans)
    elif Op == 4:
        ans = str(float(num2) / float(num1))
        print(ans)
        txt.insert(END, '=' + ans)
    elif Op == 6:
        ans = str(float(num2) ** float(num1))
        print(ans)
        txt.insert(END, '=' + ans)

l = []
n = 10
for counter_num in range(1, n):
    command_name = 'c' + str(counter_num)
    button = Button(window, text=str(counter_num), command=command_name)
    button.grid(column= (counter_num % 3), row= (counter_num % 3 / 3))
#    l.append(button)
'''
txt = Entry(window, text='')
txt.grid(column=0, row=0, columnspan=4)

c1 = Button(window, text="1", command=C1)
c1.grid(column=0, row=1)

c2 = Button(window, text='2', command=C2)
c2.grid(column=1, row=1)

c3 = Button(window, text='3', command=C3)
c3.grid(column=2, row=1)

c4 = Button(window, text='4', command=C4)
c4.grid(column=0, row=2)

c5 = Button(window, text='5', command=C5)
c5.grid(column=1, row=2)

c6 = Button(window, text='6', command=C6)
c6.grid(column=2, row=2)

c7 = Button(window, text='7', command=C7)
c7.grid(column=0, row=3)

c8 = Button(window, text='8', command=C8)
c8.grid(column=1, row=3)

c9 = Button(window, text='9', command=C9)
c9.grid(column=2, row=3)

c0 = Button(window, text='0', command=C0)
c0.grid(column=1, row=4)
'''
Op1 = Button(window, text='+', command=Op1)
Op1.grid(column=3, row=1)

Op2 = Button(window, text='-', command=Op2)
Op2.grid(column=3, row=2)

Op3 = Button(window, text='*', command=Op3)
Op3.grid(column=3, row=3)

Op4 = Button(window, text=':', command=Op4)
Op4.grid(column=3, row=4)

Op5 = Button(window, text='.', command=Op5)
Op5.grid(column=4, row=1)

Op6 = Button(window, text='**', command=Op6)
Op6.grid(column=4, row=2)

OpEND = Button(window, text='=', command=OpEND)
OpEND.grid(column=0, row=4)

OpDEL = Button(window, text='del', command=OpDEL)
OpDEL.grid(column=2, row=4)


window.mainloop()
