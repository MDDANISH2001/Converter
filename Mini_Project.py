import tkinter as md
from tkinter.constants import ANCHOR, BOTTOM, CENTER, E, END, GROOVE, LEFT, N, RAISED, RIDGE, RIGHT, S, SUNKEN, W, X, Y
import tkinter.messagebox as tmsg
from turtle import width


root = md.Tk()

root.minsize(width=1000, height=750)
app_width = root.winfo_width()
app_height = root.winfo_height()
root.geometry(f'{app_width}x{app_width}')

root.title("Unit Converter")
root.wm_iconbitmap("img/unit converter.ico")





#************************************************Calculator Starts here**********************************************************************
#********************************************************************************************************************************************

from tkinter import *
from PIL import Image,ImageTk
def open_Calculator(*args):
    import itertools
    import math
    # import tkinter.messagebox
    Calc_window = md.Toplevel()
    Calc_window.title("Standard Calculator") 
    Calc_window.wm_iconbitmap("img/unit converter.ico")
    Calc_window.configure(background = 'white') 
    Calc_window.resizable(width=False, height=False)
    Calc_window.geometry("480x645+450+90")

    calc = Frame(Calc_window)
    calc.pack()


    class Calc():
        def __init__(self):
            self.total = 0
            self.current = ''
            self.input_value = True
            self.check_sum = False
            self.op = ''
            self.result = False

        def numberEnter(self, num):
            self.result = False
            firstnum = txtDisplay.get()
            secondnum = str(num)
            if self.input_value:
                self.current = secondnum
                self.input_value = False
            else:
                if secondnum == '.':
                    if secondnum in firstnum:
                        return
                self.current = firstnum+secondnum
            self.display(self.current)
    
        def sum_of_total(self):
            self.result = True
            self.current = float(self.current)
            if self.check_sum == True:
                self.valid_function()
            else:
                self.total = float(txtDisplay.get())
    
        def display(self, value):
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, value)
    
        def valid_function(self):
            if self.op == "add":
                self.total += self.current
            if self.op == "sub":
                self.total -= self.current
            if self.op == "multi":
                self.total *= self.current
            if self.op == "divide":
                self.total /= self.current
            if self.op == "mod":
                self.total %= self.current
            self.input_value = True
            self.check_sum = False
            self.display(self.total)
    
        def operation(self, op):
            self.current = float(self.current)
            if self.check_sum:
                self.valid_function()
            elif not self.result:
                self.total = self.current
                self.input_value = True
            self.check_sum = True
            self.op = op
            self.result = False
    
        def Clear_Entry(self):
            self.result = False
            self.current = "0"
            self.display(0)
            self.input_value = True
    
        def All_Clear_Entry(self):
            self.Clear_Entry()
            self.total = 0
    
        def pi(self):
            self.result = False
            self.current = math.pi
            self.display(self.current)
    
        def tau(self):
            self.result = False
            self.current = math.tau
            self.display(self.current)
    
        def e(self):
            self.result = False
            self.current = math.e
            self.display(self.current)
    
        def mathPM(self):
            self.result = False
            self.current = -(float(txtDisplay.get()))
            self.display(self.current)
    
        def squared(self):
            self.result = False
            self.current = math.sqrt(float(txtDisplay.get()))
            self.display(self.current)
    
        def cos(self):
            self.result = False
            self.current = math.cos(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def cosh(self):
            self.result = False
            self.current = math.cosh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def tan(self):
            self.result = False
            self.current = math.tan(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def tanh(self):
            self.result = False
            self.current = math.tanh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def sin(self):
            self.result = False
            self.current = math.sin(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def sinh(self):
            self.result = False
            self.current = math.sinh(math.radians(float(txtDisplay.get())))
            self.display(self.current)
    
        def log(self):
            self.result = False
            self.current = math.log(float(txtDisplay.get()))
            self.display(self.current)
    
        def exp(self):
            self.result = False
            self.current = math.exp(float(txtDisplay.get()))
            self.display(self.current)
    
        def acosh(self):
            self.result = False
            self.current = math.acosh(float(txtDisplay.get()))
            self.display(self.current)
    
        def asinh(self):
            self.result = False
            self.current = math.asinh(float(txtDisplay.get()))
            self.display(self.current)
    
        def expm1(self):
            self.result = False
            self.current = math.expm1(float(txtDisplay.get()))
            self.display(self.current)
    
        def lgamma(self):
            self.result = False
            self.current = math.lgamma(float(txtDisplay.get()))
            self.display(self.current)
    
        def degrees(self):
            self.result = False
            self.current = math.degrees(float(txtDisplay.get()))
            self.display(self.current)
    
        def log2(self):
            self.result = False
            self.current = math.log2(float(txtDisplay.get()))
            self.display(self.current)
    
        def log10(self):
            self.result = False
            self.current = math.log10(float(txtDisplay.get()))
            self.display(self.current)
    
        def log1p(self):
            self.result = False
            self.current = math.log1p(float(txtDisplay.get()))
            self.display(self.current)
    
    
    added_value = Calc()


    txtDisplay = md.Entry(calc,
                    font=('Helvetica', 19,
                            'bold'),
                    bg='black',
                    fg='#90FF00',
                    bd=34,
                    width=29,
                    justify=RIGHT)
    
    txtDisplay.grid(row=0,
                    column=0,
                    columnspan=4,
                    pady=1, padx=2)
    
    txtDisplay.insert(0, "0")

    numberpad = "789456123"
    
    i = 0
    
    btn = []
    
    for j in range(2, 5):
    
        for k in range(3):
            btn.append(md.Button(calc,
                            width=5,
                            height=1,
                            bg='#00F6FF',
                            fg='black',
                            font=('Calibri', 30, 'bold'),
                            bd=4, text=numberpad[i]))
    
            btn[i].grid(row=j, column=k, pady=1)
    
            btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
            i += 1

    btnClear = md.Button(calc, text=chr(67),
                    width=5, height=1,
                    bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4,
                    command=added_value.Clear_Entry).grid(
        row=1, column=0, pady=1)
    
    btnAllClear = md.Button(calc, text=chr(67)+chr(69),
                        width=5, height=1,
                        bg='#90FF00',
                        font=('Calibri', 30, 'bold'),
                        bd=4,
                        command=added_value.All_Clear_Entry).grid(
        row=1, column=1, pady=1)
    
    btnsq = md.Button(calc, text="\u221A", width=5,
                height=1, bg='#90FF00',
                font=('Calibri', 30, 'bold'),
                bd=4, command=added_value.squared).grid(
        row=1, column=2, pady=1)
    
    btnAdd = md.Button(calc, text="+", width=5,
                    height=1, bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.operation("add")
                    ).grid(row=1, column=3, pady=1)
    
    btnSub = md.Button(calc, text="-", width=5,
                    height=1, bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4,
                    command=lambda: added_value.operation("sub")
                    ).grid(row=2, column=3, pady=1)
    
    btnMul = md.Button(calc, text="x", width=5, height=1,
                    bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.operation("multi")
                    ).grid(row=3, column=3, pady=1)

    btnDiv = md.Button(calc, text="/", width=5,
                    height=1, bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.operation("divide")
                    ).grid(row=4, column=3, pady=1)
    
    btnZero = md.Button(calc, text="0", width=5,
                    height=1, bg='#00F6FF',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.numberEnter(0)
                    ).grid(row=5, column=0, pady=1)
    
    btnDot = md.Button(calc, text=".", width=5,
                    height=1, bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.numberEnter(".")
                    ).grid(row=5, column=1, pady=1)
    btnPM = md.Button(calc, text=chr(177), width=5,
                height=1, bg='#90FF00',
                font=('Calibri', 30, 'bold'),
                bd=4, command=added_value.mathPM
                ).grid(row=5, column=2, pady=1)
    
    btnEquals = md.Button(calc, text="=", width=5,
                    height=1, bg='#90FF00',
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.sum_of_total
                    ).grid(row=5, column=3, pady=1)
    # ROW 1 :

    btnPi = md.Button(calc, text="π", width=5,
                height=1, bg='#90FF00',
                font=('Calibri', 30, 'bold'),
                bd=4, command=added_value.pi
                ).grid(row=1, column=4, pady=1)
    
    btnCos = md.Button(calc, text="cos", width=5,
                    height=1, bg='#90FF00',
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.cos
                    ).grid(row=1, column=5, pady=1)
    
    btntan = md.Button(calc, text="tan", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.tan
                    ).grid(row=1, column=6, pady=1)
    
    btnsin = md.Button(calc, text="sin", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.sin
                    ).grid(row=1, column=7, pady=1)
    
    # ROW 2 :
    
    btn2Pi = md.Button(calc, text="2π", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.tau
                    ).grid(row=2, column=4, pady=1)
    
    btnCosh = md.Button(calc, text="cos h", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.cosh
                    ).grid(row=2, column=5, pady=1)
    
    btntanh = md.Button(calc, text="tan h", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.tanh
                    ).grid(row=2, column=6, pady=1)
    
    btnsinh = md.Button(calc, text="sin h", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.sinh
                    ).grid(row=2, column=7, pady=1)
    
    # ROW 3 :
    
    btnlog = md.Button(calc, text="log", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.log
                    ).grid(row=3, column=4, pady=1)
    
    btnExp = md.Button(calc, text="exp", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.exp
                    ).grid(row=3, column=5, pady=1)
    
    btnMod = md.Button(calc, text="%", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=lambda: added_value.operation("mod")
                    ).grid(row=3, column=6, pady=1)
    
    btnE = md.Button(calc, text="e", width=5,
                height=1, bg='#90FF00', 
                font=('Calibri', 30, 'bold'),
                bd=4, command=added_value.e
                ).grid(row=3, column=7, pady=1)
    
    # ROW 4 :
    
    btnlog10 = md.Button(calc, text="log\u2081\u2080", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.log10
                    ).grid(row=4, column=4, pady=1)
    
    btncos = md.Button(calc, text="log\u2081\u209A", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.log1p
                    ).grid(row=4, column=5, pady=1)
    
    btnexpm1 = md.Button(calc, text="e\u00b2-1", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.expm1
                    ).grid(row=4, column=6, pady=1)
    
    btngamma = md.Button(calc, text="Gamma\nln((x-1)!)", width=8,
                    height=2, bg='#90FF00', 
                    font=('Calibri', 19, 'bold'),
                    bd=4, command=added_value.lgamma
                    ).grid(row=4, column=7)
    # ROW 5 :
    
    btnlog2 = md.Button(calc, text="log\u2082", width=5,
                    height=1, bg='#90FF00', 
                    font=('Calibri', 30, 'bold'),
                    bd=4, command=added_value.log2
                    ).grid(row=5, column=4, pady=1)
    
    btndeg = md.Button(calc, text="\u00b0r→\u00b0d", width=6,
                    height=1, bg='#90FF00', 
                    font=('california fb', 21, 'bold'),
                    bd=4, command=added_value.degrees, pady=15
                    ).grid(row=5, column=5, pady=1)
    
    btnacosh = md.Button(calc, text="a cos h", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.acosh
                    ).grid(row=5, column=6, pady=1)
    
    btnasinh = md.Button(calc, text="a sin h", width=5,
                    height=1, bg='#90FF00', 
                    font=('Monotype Corsiva', 30, 'bold'),
                    bd=4, command=added_value.asinh
                    ).grid(row=5, column=7, pady=1)
    
    lblDisplay = md.Label(calc, text="SCIENTIFIC CALCULATOR",
                    font=('Helvetica', 22,
                            'bold'),
                    bg='red',
                    fg='WHITE',
                    bd=15,
                    width=24,height=2, justify=CENTER, relief=RAISED)
    lblDisplay.grid(row=0, column=4, columnspan=4, padx = 2)

    def iExit(): 
        Calc_window.destroy()
    
    def Scientific():
        Calc_window.resizable(width=False, height=False)
        Calc_window.geometry("960x645+0+0")
        Calc_window.title("Scientific Calculator")
    
    def Standard():
        Calc_window.resizable(width=False, height=False)
        Calc_window.geometry("480x645+0+0")
        Calc_window.title("Standard Calculator")

    toggle_funcs = itertools.cycle((Scientific, Standard))

    def toggle():
        func = next(toggle_funcs)
        func()

    button_frame = md.Frame(Calc_window, background='white')
    button_frame.pack()

    exit_button = md.Button(button_frame,bg = 'orange', bd = 6, command = iExit)
    exit_button.grid (row = 0, column = 0, padx=7)
    image = Image.open("img/back_button.png")
    resize_image = image.resize((61,50), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize_image)
    exit_button.img_ref = img
    exit_button.config(image = img, justify=LEFT)

    normal_scientific = md.Button(button_frame, text = "Normal ⇌ Scientific", width=10, border = 6, fg = 'red',bg = 'yellow',font = ("Bookman Old Style", 20,"bold"), command = toggle)
    normal_scientific.grid(row = 0,column=1, columnspan=4,ipadx=170, pady=4)

    image = Image.open("img/unit converter.png")
    resize_image = image.resize((62,49), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resize_image)
    normal_scientific.img_ref = img
    normal_scientific.config(image = img, compound=LEFT)

#*************************************************Calculator Ends Here*************************************************
#**********************************************************************************************************************


class Screens:
    def __init__(self):
        self.frame = None
        self.main_screen()


    def main_screen(self, *args):
        if self.frame is not None:
            self.frame.destroy()        
        from PIL import Image, ImageTk

        frame = md.Frame(root, background='light blue')
        frame.pack()

        frame1 = md.Frame(frame, background='light blue')
        frame1.pack()

        frame2 = md.Frame(frame, bg = 'orange', border = 4, relief=GROOVE)
        frame2.pack(pady = 20)


        label = md.Label(frame1, background='light blue')
        label.grid (row = 0, column = 2)
        image = Image.open("img/unit converter.png")
        resize_image = image.resize((235,180))
        img = ImageTk.PhotoImage(resize_image)
        label.img_ref = img
        label.config(image = img)

        head= md.Label(frame1, text =" Welcome to Unit Converter ", font=("Calibri", 50, "bold"), foreground= "black", background = "light green",relief=RIDGE, border = 10)
        head.grid(row = 1, column = 2)


        b1 = Button(frame2, text = "Standard Converter",command = self.standard_converter)
        b1.grid(row = 1, column = 1, padx = 10, pady = 20)

        b2 = Button(frame2, text = "Scientific Converter", command = self.scientific_converter)
        b2.grid(row = 1, column = 2, padx = 10)

        b3 = Button(frame2, text = "Calculator", command = open_Calculator)
        b3.grid(row = 2, column = 1, padx = 10, pady= 20)

        b5 = Button(frame2, text = "Currency", command = self.currency_converter)
        b5.grid(row = 2, column = 2, padx = 10, pady= 10)

        b4 = Button(frame2, text = "Binary ⇌ Decimal", command = self.binary_to_decimal)
        b4.grid(row = 3, column = 1,columnspan=2, padx = 10, pady= 10)


        def exit_window(): 
            iExit = tmsg.askquestion("Converter", "Do you want to exit ?")
            root.wm_iconbitmap("img/unit converter.ico")
            if iExit=="yes":
                root.destroy()
                
        def exit_button_enter(e):
            exit_button["bg"] = "red"
            exit_button["fg"] = "blue"
            statusvar.set("Sorry to see you go")
        def exit_button_leave(e):
            exit_button["bg"] = 'blue'
            exit_button["fg"] = 'red'
            statusvar.set("Status is good.")
        exit_button_frame = md.Frame(frame, background='light blue')
        exit_button_frame.pack(fill=BOTH)
    

        exit_button = md.Button(exit_button_frame, text = "Exit",bd = 0,font = ("Arial", 15, "bold"), fg = "red",bg = "blue", command = exit_window)
        exit_button.pack(side = BOTTOM, anchor = "w", fill = Y, ipadx = 7,padx = 50)

        image = Image.open("img/unit converter.png")
        resize_image = image.resize((51,40), Image.ANTIALIAS)
        img_exit = ImageTk.PhotoImage(resize_image)
        exit_button.img_ref = img_exit
        exit_button.config(image = img_exit,compound=TOP)
        exit_button.bind("<Leave>", exit_button_leave)
        exit_button.bind("<Enter>", exit_button_enter)

        root["background"] = "light blue"
        
        self.frame = frame
  

#******************************************************Standard Converter Starts Here***************************************************
#***************************************************************************************************************************************

    def standard_converter(self, *args):
        self.frame.destroy()

        def nextbox(event):

            listbox_get = str(listbox.get(ANCHOR))

            if listbox_get =="Distance":
            
                def from_box(event):

                    fromlistbox_get = str(from_listbox.get(ANCHOR))
                    
                    if fromlistbox_get == "Kilometer(km)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Hectometer(hm)":
                                def convert():
                                    km = float(input_entry.get())
                                    hm = float(km*10)
                                    hm = round(hm , 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config(text = "Kilometer(km) to Hectometer(hm)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometer(km):")
                                input_EL.config(text = "km")
                                output_OL.config(text = "hm")
                            
                            elif tolistbox_get == "Decameter(dam)":
                                def convert():
                                    km = float(input_entry.get())
                                    dam = float(km*100)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Kilometer(km) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(km):")
                                input_EL.config( text = "km")
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Meter(m)":
                                def convert():
                                    km = float(input_entry.get())
                                    m = float(km*1000)
                                    m = round( m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Kilometer(km) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(km):")
                                input_EL.config( text = "km")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():                  
                                    km = float(input_entry.get())
                                    dm = float(km*10000)
                                    dm = round(dm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Kilometer(km) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(km):")
                                input_EL.config( text = "km")
                                output_OL.config( text = "dm")

                            elif tolistbox_get == "Centimeter(cm)":
                                def convert():
                                    km = float(input_entry.get())
                                    cm = float(km*100000)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Kilometer(km) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(km):")
                                input_EL.config( text = "km")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Millimeter(mm)":                        
                                def convert():
                                    km = float(input_entry.get())
                                    mm = float(km*1000000)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Kilometer(km) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(km):")
                                input_EL.config( text = "km")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Miles(mi)":
                                def convert():
                                    km = float(input_entry.get())
                                    mi = float(km/1.609)
                                    mi = round(mi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mi}")
                                heading_label.config( text = "Kilometer(km) to Miles(mi)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(km):")
                                input_EL.config( text = "km")
                                output_OL.config( text = "mi")

                            elif tolistbox_get == "Yards(yd)":
                                def convert():
                                    km = float(input_entry.get())
                                    yd = float(km*1093.6)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Kilometer(km) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(km):")
                                input_EL.config( text = "km")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Foot(ft)":
                                def convert():
                                    km = float(input_entry.get())
                                    ft = float(km*3280.8)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Kilometer(km) to Foot(ft)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(km):")
                                input_EL.config( text = "km")
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Inches(in)":                        
                                def convert():
                                    km = float(input_entry.get())
                                    inches = float(km*39370)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Kilometer(km) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(km):")
                                input_EL.config( text = "km")
                                output_OL.config( text = "in")

                            elif tolistbox_get == "Soot(soot)":
                                def convert():
                                    km = float(input_entry.get())
                                    soot = float(km*3175000)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Kilometer(km) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(km):")
                                input_EL.config( text = "km")
                                output_OL.config( text = "sut")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Hectometer(hm)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilometer(km)":
                                def convert():                            
                                    hm = float(input_entry.get())
                                    km = float(hm/10)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Hectometer(hm) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")
                                output_OL.config( text = "km")

                            elif tolistbox_get == "Decameter(dam)":
                                def convert():                            
                                    hm = float(input_entry.get())
                                    dam = float(hm*10)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Hectometer(hm) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")                        
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Meter(m)":
                                def convert():
                                    hm = float(input_entry.get())
                                    m = float(hm*100)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Hectometer(hm) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():                            
                                    hm = float(input_entry.get())
                                    dm = float(hm*1000)
                                    dm = round(dm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Hectometer(hm) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")
                                output_OL.config( text = "dm")
                            
                            elif tolistbox_get == "Centimeter(cm)":
                                def convert():
                                    hm = float(input_entry.get())
                                    cm = float(hm*10000)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Hectometer(hm) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Millimeter(mm)":                        
                                def convert():
                                    hm = float(input_entry.get())
                                    mm = float(hm*100000)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Hectometer(hm) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Miles(mi)":                        
                                def convert():
                                    hm = float(input_entry.get())
                                    mi = float(hm/16.093)
                                    mi = round(mi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mi}")
                                heading_label.config( text = "Hectometer(hm) to Miles(mi)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")
                                output_OL.config( text = "mi")

                            elif tolistbox_get == "Yards(yd)":
                                def convert():
                                    hm = float(input_entry.get())
                                    yd = float(hm*109)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Hectometer(hm) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Foot(ft)":
                                def convert():
                                    hm = float(input_entry.get())
                                    ft = float(hm*328)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Hectometer(hm) to Foot(ft)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Inches(in)":
                                def convert():
                                    hm = float(input_entry.get())
                                    inches = float(hm*3937)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Hectometer(hm) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")
                                output_OL.config( text = "in")

                            elif tolistbox_get == "Soot(soot)":
                                def convert():
                                    hm = float(input_entry.get())
                                    soot = float(hm*317500)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Hectometer(hm) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectometer(hm):")
                                input_EL.config( text = "hm")
                                output_OL.config( text = "sut")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
                    

                    elif fromlistbox_get == "Decameter(dam)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilometer(km)":
                                def convert():                            
                                    dam = float(input_entry.get())
                                    km = float(dam/100)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Decameter(dam) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "km")

                            elif tolistbox_get == "Hectometer(hm)":
                                def convert():                            
                                    dam = float(input_entry.get())
                                    hm = float(dam/10)
                                    hm = round(hm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config( text = "Decameter(dam) to Hectometer(hm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "hm")

                            elif tolistbox_get == "Meter(m)":
                                def convert():    
                                    dam = float(input_entry.get())
                                    m = float(dam*10)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Decameter(dam) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():
                                    dam = float(input_entry.get())
                                    dm = float(dam*100)
                                    dm = round(dm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Decameter(dam) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "dm")

                            elif tolistbox_get == "Centimeter(cm)":
                                def convert():
                                    dam = float(input_entry.get())
                                    cm = float(dam*1000)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Decameter(dam) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Millimeter(mm)":
                                def convert():
                                    dam = float(input_entry.get())
                                    mm = float(dam*10000)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Decameter(dam) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Miles(mi)":
                                def convert():
                                    dam = float(input_entry.get())
                                    mi = float(dam/161)
                                    mi = round(mi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mi}")
                                heading_label.config( text = "Decameter(dam) to Miles(mi)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "mi")

                            elif tolistbox_get == "Yards(yd)":
                                def convert():
                                    dam = float(input_entry.get())
                                    yd = float(dam*10.936)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Decameter(dam) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Foot(ft)":                        
                                def convert():
                                    dam = float(input_entry.get())
                                    ft = float(dam*32.808)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Decameter(dam) to Foot(ft)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Inches(in)":
                                def convert():
                                    dam = float(input_entry.get())
                                    inches = float(dam*394.7)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Decameter(dam) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "in")

                            elif tolistbox_get == "Soot(soot)":
                                def convert():
                                    dam = float(input_entry.get())
                                    soot = float(dam*31750)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Decameter(dam) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decameter(dam):")
                                input_EL.config( text = "dam")
                                output_OL.config( text = "sut")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Meter(m)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilometer(km)":
                                def convert():                            
                                    m = float(input_entry.get())
                                    km = float(m/1000)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Meter(m) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")
                                input_EL.config( text = "m")
                                output_OL.config( text = "km")
                            
                            elif tolistbox_get == "Hectometer(hm)":
                                def convert():
                                    m = float(input_entry.get())
                                    hm = float(m/100)
                                    hm = round(hm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config( text = "Meter(m) to Hectometer(hm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")                        
                                input_EL.config( text = "m")
                                output_OL.config( text = "hm")

                            elif tolistbox_get == "Decameter(dam)":
                                def convert():                            
                                    m = float(input_entry.get())
                                    dam = float(m/10)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Meter(m) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")
                                input_EL.config( text = "m")
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():
                                    m = float(input_entry.get())
                                    dm = float(m*10)
                                    dm = round(dm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Meter(m) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")
                                input_EL.config( text = "m")
                                output_OL.config( text = "dm")

                            elif tolistbox_get == "Centimeter(cm)":
                                def convert():
                                    m = float(input_entry.get())
                                    cm = float(m*100)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Meter(m) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")
                                input_EL.config( text = "m")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Millimeter(mm)":
                                def convert():
                                    m = float(input_entry.get())
                                    mm = float(m*1000)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Meter(m) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")
                                input_EL.config( text = "m")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Miles(mi)":
                                def convert():
                                    m = float(input_entry.get())
                                    mi = float(m/1609)
                                    mi = round(mi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mi}")
                                heading_label.config( text = "Meter(m) to Miles(mi)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")
                                input_EL.config( text = "m")
                                output_OL.config( text = "mi")

                            elif tolistbox_get == "Yards(yd)":                        
                                def convert():
                                    m = float(input_entry.get())
                                    yd = float(m/1609)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Meter(m) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")
                                input_EL.config( text = "m")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Foot(ft)":                        
                                def convert():
                                    m = float(input_entry.get())
                                    ft = float(m*3.281)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Meter(m) to Foot(ft)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")
                                input_EL.config( text = "m")
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Inches(in)":
                                def convert():
                                    m = float(input_entry.get())
                                    inches = float(m*39.37)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Meter(m) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")
                                input_EL.config( text = "m")
                                output_OL.config( text = "in")

                            elif tolistbox_get == "Soot(soot)":
                                def convert():
                                    m = float(input_entry.get())
                                    soot = float(m*3175)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Meter(m) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Meters(m):")
                                input_EL.config( text = "m")
                                output_OL.config( text = "si")
                            
                        to_listbox.bind('<<ListboxSelect>>', to_box)

                        
                    elif fromlistbox_get == "Decimeter(dm)":

                        def to_box(event):
                    
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilometer(km)":
                                def convert():
                                    dm = float(input_entry.get())
                                    km = float(dm/10000)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Decimeter(dm) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "km")

                            elif tolistbox_get == "Hectometer(hm)":
                                def convert():                            
                                    dm = float(input_entry.get())
                                    hm = float(dm/1000)
                                    hm = round(hm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config( text = "Decimeter(dm) to Hectometer(hm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "hm")

                            elif tolistbox_get == "Decameter(dam)":
                                def convert():
                                    dm = float(input_entry.get())
                                    dam = float(dm/100)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Decimeter(dm) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Meter(m)":
                                def convert():
                                    dm = float(input_entry.get())
                                    m = float(dm/10)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Decimeter(dm) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Centimeter(cm)":
                                def convert():
                                    dm = float(input_entry.get())
                                    cm = float(dm*10)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Decimeter(dm) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Millimeter(mm)":
                                def convert():
                                    dm = float(input_entry.get())
                                    mm = float(dm*100)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Decimeter(dm) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Miles(mi)":                        
                                def convert():
                                    dm = float(input_entry.get())
                                    mi = float(dm/16093)
                                    mi = round(mi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mi}")
                                heading_label.config( text = "Decimeter(dm) to Miles(mi)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "mi")

                            elif tolistbox_get == "Yards(yd)":
                                def convert():
                                    dm = float(input_entry.get())
                                    yd = float(dm/9.144)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Decimeter(dm) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Foot(ft)":
                                def convert():
                                    dm = float(input_entry.get())
                                    ft = float(dm/3.048)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Decimeter(dm) to Foot(ft)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Inches(in)":
                                def convert():
                                    dm = float(input_entry.get())
                                    inches = float(dm*3.937)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Decimeter(dm) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "in")

                            elif tolistbox_get == "Soot(soot)":
                                def convert():
                                    dm = float(input_entry.get())
                                    soot = float(dm*317.5)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Decimeter(dm) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decimeter(dm):")
                                input_EL.config( text = "dm")
                                output_OL.config( text = "sut")
                            
                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Centimeter(cm)":
                    
                        def to_box(event):
                    
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilometer(km)":
                                def convert():
                                    cm = float(input_entry.get())
                                    km = float(cm/100000)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Centimeter(cm) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "km")

                            elif tolistbox_get == "Hectometer(hm)":
                                def convert():    
                                    cm = float(input_entry.get())
                                    hm = float(cm/10000)
                                    hm = round(hm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config( text = "Centimeter(cm) to Hectometer(hm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "hm")

                            elif tolistbox_get == "Decameter(dam)":
                                def convert():
                                    cm = float(input_entry.get())
                                    dam = float(cm/1000)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Centimeter(cm) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Meter(m)":
                                def convert():
                                    cm = float(input_entry.get())
                                    m = float(cm/100)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Centimeter(cm) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():
                                    cm = float(input_entry.get())
                                    dm = float(cm/10)
                                    dm = round(dm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Centimeter(cm) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "dm")

                            elif tolistbox_get == "Millimeter(mm)":
                                def convert():
                                    cm = float(input_entry.get())
                                    mm = float(cm*10)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Centimeter(cm) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Miles(mi)":                        
                                def convert():
                                    cm = float(input_entry.get())
                                    mi = float(cm/160934)
                                    mi = round(mi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mi}")
                                heading_label.config( text = "Centimeter(cm) to Miles(mi)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "mi")

                            elif tolistbox_get == "Yards(yd)":
                                def convert():
                                    cm = float(input_entry.get())
                                    yd = float(cm/91.44)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Centimeter(cm) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Foot(ft)":
                                def convert():
                                    cm = float(input_entry.get())
                                    ft = float(cm/30.48)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Centimeter(cm) to Foot(ft)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Inches(in)":                        
                                def convert():
                                    cm = float(input_entry.get())
                                    inches = float(cm/2.54)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Centimeter(cm) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "in")

                            elif tolistbox_get == "Soot(soot)":
                                def convert():
                                    cm = float(input_entry.get())
                                    soot = float(cm*0.3175)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Centimeter(cm) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centimeter(cm):")
                                input_EL.config( text = "cm")
                                output_OL.config( text = "sut")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Millimeter(mm)":            
                        def to_box(event):
                            tolistbox_get = str(to_listbox.get(ANCHOR))
                            if tolistbox_get == "Kilometer(km)":
                                def convert():
                                    mm = float(input_entry.get())
                                    km = float(mm/1000000)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Millimeter(mm) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Millimeter(mm):")
                                input_EL.config( text = "mm")
                                output_OL.config( text = "km")

                            elif tolistbox_get == "Hectometer(hm)":
                                def convert():
                                    mm = float(input_entry.get())
                                    hm = float(mm/100000)
                                    hm = round(hm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config( text = "Millimeter(mm) to Hectometer(hm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Millimeter(mm):")
                                input_EL.config( text = "mm")
                                output_OL.config( text = "hm")

                            elif tolistbox_get == "Decameter(dam)":
                                def convert():    
                                    mm = float(input_entry.get())
                                    dam = float(mm/10000)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Millimeter(mm) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Millimeter(mm):")
                                input_EL.config( text = "mm")
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Meter(m)":
                                def convert():    
                                    mm = float(input_entry.get())
                                    m = float(mm/1000)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Millimeter(mm) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Millimeter(mm):")
                                input_EL.config( text = "mm")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():
                                    mm = float(input_entry.get())
                                    dm = float(mm/100)
                                    dm = round(dm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Millimeter(mm) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Millimeter(mm):")
                                input_EL.config( text = "mm")
                                output_OL.config( text = "dm")

                            elif tolistbox_get == "Centimeter(cm)":
                                def convert():
                                    mm = float(input_entry.get())
                                    cm = float(mm/10)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Millimeter(mm) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Millimeter(mm):")
                                input_EL.config( text = "mm")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Yards(yd)":                        
                                def convert():
                                    mm = float(input_entry.get())
                                    yd = float(mm/914)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Millimeter(mm) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Millimeter(mm):")
                                input_EL.config( text = "mm")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Foot(ft)":                        
                                def convert():
                                    mm = float(input_entry.get())
                                    ft = float(mm/305)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Millimeter(mm) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Millimeter(mm):")
                                input_EL.config( text = "mm")
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Inches(in)":
                                def convert():
                                    mm = float(input_entry.get())
                                    inches = float(mm/25.4)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Millimeter(mm) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Millimeter(mm):")
                                input_EL.config( text = "mm")
                                output_OL.config( text = "in")

                            elif tolistbox_get == "Soot(soot)":                        
                                def convert():
                                    mm = float(input_entry.get())
                                    soot = float(mm/3.175)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Millimeter(mm) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Millimeter(mm):")
                                input_EL.config( text = "mm")
                                output_OL.config( text = "sut")

                        to_listbox.bind('<<ListboxSelect>>', to_box)

                            
                    elif fromlistbox_get == "Miles(mi)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilometer(km)":
                                def convert():
                                    mi = float(input_entry.get())
                                    km = float(mi*1.609)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Miles(mi) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi):")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "km")

                            elif tolistbox_get == "Hectometer(hm)":
                                def convert():                            
                                    mi = float(input_entry.get())
                                    hm = float(mi*16.039)
                                    hm = round(hm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config( text = "Miles(mi) to Hectometer(hm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi)")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "hm")

                            elif tolistbox_get == "Decameter(dam)":
                                def convert():    
                                    mi = float(input_entry.get())
                                    dam = float(mi*160.93)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Miles(mi) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi):")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Meter(m)":
                                def convert():
                                    mi = float(input_entry.get())
                                    m = float(mi*1609)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Miles(mi) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi):")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():
                                    mi = float(input_entry.get())
                                    dm = float(mi*16093)
                                    dm = round(dm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Miles(mi) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi):")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "dm")

                            elif tolistbox_get == "Centimeter(cm)":
                                def convert():
                                    mi = float(input_entry.get())
                                    cm = float(mi*160934)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Miles(mi) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi)):")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Millimeter(mm)":                        
                                def convert():
                                    mi = float(input_entry.get())
                                    mm = float(mi*1609000)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Miles(mi) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi)):")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Yards(yd)":                        
                                def convert():
                                    mi = float(input_entry.get())
                                    yd = float(mi*1760)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Miles(mi) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi):")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Foot(ft)":
                                def convert():
                                    mi = float(input_entry.get())
                                    ft = float(mi*5280)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Miles(mi) to Foot(ft)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi)")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Inches(in)":                        
                                def convert():
                                    mi = float(input_entry.get())
                                    inches = float(mi*63360)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Miles(mi) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi):")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "in")

                            elif tolistbox_get == "Soot(soot)":                        
                                def convert():
                                    mi = float(input_entry.get())
                                    soot = float(mi*506880)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Miles(mi) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Miles(mi):")
                                input_EL.config( text = "mi")
                                output_OL.config( text = "sut")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
                            

                    elif fromlistbox_get == "Yards(yd)":
                        def to_box(event):
                            tolistbox_get = str(to_listbox.get(ANCHOR))
                            if tolistbox_get == "Kilometer(km)":
                                def convert():
                                    yd = float(input_entry.get())
                                    km = float(yd/1094)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Yards(yd) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd):")
                                input_EL.config( text = "yd")
                                output_OL.config( text = "km")

                            elif tolistbox_get == "Hectometer(hm)":
                                def convert():                            
                                    yd = float(input_entry.get())
                                    hm = float(yd/109)
                                    hm = round(hm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config( text = "Yards(yd) to Hectometer(hm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd)")
                                input_EL.config( text = "yd")
                                output_OL.config( text = "hm")

                            elif tolistbox_get == "Decameter(dam)":
                                def convert():
                                    yd = float(input_entry.get())
                                    dam = float(yd/10.936)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Yards(yd) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd):")
                                input_EL.config( text = "yd")
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Meter(m)":
                                def convert():
                                    yd = float(input_entry.get())
                                    m = float(yd/1.094)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Yards(yd) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd):")
                                input_EL.config( text = "yd")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():
                                    yd = float(input_entry.get())
                                    dm = float(yd*9.144)
                                    dm = round(dm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Yards(yd) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd):")
                                input_EL.config( text = "yd")
                                output_OL.config( text = "dm")

                            elif tolistbox_get == "Centimeter(cm)":
                                def convert():
                                    yd = float(input_entry.get())
                                    cm = float(yd*91.44)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Yards(yd) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd):")
                                input_EL.config( text = "yd")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Millimeter(mm)":
                                def convert():
                                    yd = float(input_entry.get())
                                    mm = float(yd*914.4)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Yards(yd) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd):")
                                input_EL.config( text = "yd")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Miles(mi)":
                                def convert():
                                    yd = float(input_entry.get())
                                    mi = float(yd/1760)
                                    mi = round(mi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mi}")
                                heading_label.config( text = "Yards(yd) to Miles(mi)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd):")
                                input_EL.config( text = "yd")
                                output_OL.config( text = "mi")

                            elif tolistbox_get == "Foot(ft)":
                                def convert():
                                    yd = float(input_entry.get())
                                    ft = float(yd*3)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Yards(yd) to Foot(ft)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd)")
                                input_EL.config( text = "yd")                        
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Inches(in)":                        
                                def convert():
                                    yd = float(input_entry.get())
                                    inches = float(yd*36)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Yards(yd) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd):")
                                input_EL.config( text = "yd")
                                output_OL.config( text = "in")

                            elif tolistbox_get == "Soot(soot)":                        
                                def convert():
                                    yd = float(input_entry.get())
                                    soot = float(yd*288)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Yards(yd) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Yards(yd):")
                                input_EL.config( text = "yd")
                                output_OL.config( text = "sut")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
                            

                    elif fromlistbox_get == "Foot(ft)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilometer(km)":
                                def convert():                            
                                    ft = float(input_entry.get())
                                    km = float(ft/3281)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Foot(ft) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "km")
                            
                            elif tolistbox_get == "Hectometer(hm)":
                                def convert():
                                    ft = float(input_entry.get())
                                    hm = float(ft/328)
                                    hm = round(hm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config( text = "Foot(ft) to Hectometer(hm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "hm")

                            elif tolistbox_get == "Decameter(dam)":
                                def convert():
                                    ft = float(input_entry.get())
                                    dam = float(ft/32.81)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Foot(ft) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Meter(m)":
                                def convert():
                                    ft = float(input_entry.get())
                                    m = float(ft/3.281)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Foot(ft) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():
                                    ft = float(input_entry.get())
                                    dm = float(ft*3.048)
                                    dm = round(dm , 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Foot(ft) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "dm")

                            elif tolistbox_get == "Centimeter(cm)":                        
                                def convert():
                                    ft = float(input_entry.get())
                                    cm = float(ft*30.48)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Foot(ft) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Millimeter(mm)":
                                def convert():
                                    ft = float(input_entry.get())
                                    mm = float(ft*304.8)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Foot(ft) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Miles(mi)":
                                def convert():
                                    ft = float(input_entry.get())
                                    mi = float(ft/5280)
                                    mi = round(mi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mi}")
                                heading_label.config( text = "Foot(ft) to Miles(mi)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "mi")

                            elif tolistbox_get == "Yards(yd)":
                                def convert():
                                    ft = float(input_entry.get())
                                    yd = float(ft/3)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Foot(ft) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Inches(in)":                        
                                def convert():
                                    ft = float(input_entry.get())
                                    inches = float(ft*12)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Foot(ft) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "in")

                            elif tolistbox_get == "Soot(soot)":                        
                                def convert():
                                    ft = float(input_entry.get())
                                    soot = float(ft*96)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Foot(ft) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Foot(ft):")
                                input_EL.config( text = "ft")
                                output_OL.config( text = "sut")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Inches(in)":            
                        def to_box(event):
                            tolistbox_get = str(to_listbox.get(ANCHOR))
                            if tolistbox_get == "Kilometer(km)":
                                def convert():
                                    inches = float(input_entry.get())
                                    km = float(inches/39370)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Inches(in) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")
                                input_EL.config( text = "in")
                                output_OL.config( text = "km")

                            elif tolistbox_get == "Hectometer(hm)":
                                def convert():
                                    inches = float(input_entry.get())
                                    hm = float(inches/3937)
                                    hm = round(hm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config( text = "Inches(in) to Hectometer(hm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")
                                input_EL.config( text = "in")
                                output_OL.config( text = "hm")

                            elif tolistbox_get == "Decameter(dam)":
                                def convert():
                                    inches = float(input_entry.get())
                                    dam = float(inches/394)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Inches(in) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")
                                input_EL.config( text = "in")
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Meter(m)":
                                def convert():    
                                    inches = float(input_entry.get())
                                    m = float(inches/39.37)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Inches(in) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")
                                input_EL.config( text = "in")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():
                                    inches = float(input_entry.get())
                                    dm = float(inches*3.937)
                                    dm = round(dm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Inches(in) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")
                                input_EL.config( text = "in")
                                output_OL.config( text = "dm")

                            elif tolistbox_get == "Centimeter(cm)":
                                def convert():
                                    inches = float(input_entry.get())
                                    cm = float(inches*2.54)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Inches(in) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")
                                input_EL.config( text = "in")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Millimeter(mm)":                        
                                def convert():
                                    inches = float(input_entry.get())
                                    mm = float(inches*25.4)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Inches(in) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")
                                input_EL.config( text = "in")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Miles(mi)":
                                def convert():
                                    inches = float(input_entry.get())
                                    mi = float(inches/63360)
                                    mi = round(mi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mi}")
                                heading_label.config( text = "Inches(in) to Miles(mi)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")
                                input_EL.config( text = "in")
                                output_OL.config( text = "mi")

                            elif tolistbox_get == "Yards(yd)":
                                def convert():
                                    inches = float(input_entry.get())
                                    yd = float(inches/36)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Inches(in) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")                        
                                input_EL.config( text = "in")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Foot(ft)":                        
                                def convert():
                                    inches = float(input_entry.get())
                                    ft = float(inches/12)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Inches(in) to Foot(ft)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")
                                input_EL.config( text = "in")
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Soot(soot)":                        
                                def convert():
                                    inches = float(input_entry.get())
                                    soot = float(inches*8)
                                    soot = round(soot, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{soot}")
                                heading_label.config( text = "Inches(in) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Inches(in):")
                                input_EL.config( text = "in")
                                output_OL.config( text = "sut")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Soot(soot)":
                    
                        def to_box(event):    

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilometer(km)":
                                def convert():                            
                                    soot = float(input_entry.get())
                                    km = float(soot/3175000)
                                    km = round(km, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{km}")
                                heading_label.config( text = "Soot(soot) to Kilometer(km)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "sut")
                                output_OL.config( text = "km")

                            elif tolistbox_get == "Hectometer(hm)":
                                def convert():
                                    soot = float(input_entry.get())
                                    hm = float(soot/317500)
                                    hm = round(hm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hm}")
                                heading_label.config( text = "Soot(soot) to Hectometer(hm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "sut")
                                output_OL.config( text = "hm")

                            elif tolistbox_get == "Decameter(dam)":
                                def convert():
                                    soot = float(input_entry.get())
                                    dam = float(soot/31750)
                                    dam = round(dam, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dam}")
                                heading_label.config( text = "Soot(soot) to Decameter(dam)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "soot")
                                output_OL.config( text = "dam")

                            elif tolistbox_get == "Meter(m)":
                                def convert():    
                                    soot = float(input_entry.get())
                                    m = float(soot/3175)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Soot(soot) to Meter(m)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "sut")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decimeter(dm)":
                                def convert():
                                    soot = float(input_entry.get())
                                    dm = float(soot/317.5)
                                    dm = round(dm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dm}")
                                heading_label.config( text = "Soot(soot) to Decimeter(dm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "sut")
                                output_OL.config( text = "dm")

                            elif tolistbox_get == "Centimeter(cm)":
                                def convert():
                                    soot = float(input_entry.get())
                                    cm = float(soot/0.3175)
                                    cm = round(cm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cm}")
                                heading_label.config( text = "Soot(soot) to Centimeter(cm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "sut")
                                output_OL.config( text = "cm")

                            elif tolistbox_get == "Millimeter(mm)":
                                def convert():
                                    soot = float(input_entry.get())
                                    mm = float(soot*3.175)
                                    mm = round(mm, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mm}")
                                heading_label.config( text = "Soot(soot) to Millimeter(mm)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "sut")
                                output_OL.config( text = "mm")

                            elif tolistbox_get == "Miles(mi)":
                                def convert():
                                    soot = float(input_entry.get())
                                    mi = float(soot/506880)
                                    mi = round(mi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mi}")
                                heading_label.config( text = "Soot(soot) to Miles(mi)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "sut")
                                output_OL.config( text = "mi")

                            elif tolistbox_get == "Yards(yd)":                        
                                def convert():
                                    soot = float(input_entry.get())
                                    yd = float(soot/288)
                                    yd = round(yd, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{yd}")
                                heading_label.config( text = "Soot(soot) to Yards(yd)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "sut")
                                output_OL.config( text = "yd")

                            elif tolistbox_get == "Foot(ft)":                        
                                def convert():
                                    soot = float(input_entry.get())
                                    ft = float(soot/96)
                                    ft = round(ft, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ft}")
                                heading_label.config( text = "Soot(soot) to Foot(ft)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "sut")
                                output_OL.config( text = "ft")

                            elif tolistbox_get == "Inches(in)":                        
                                def convert():
                                    soot = float(input_entry.get())
                                    inches = float(soot/8)
                                    inches = round(inches, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{inches}")
                                heading_label.config( text = "Soot(soot) to Inches(in)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Soot(soot):")
                                input_EL.config( text = "sut")
                                output_OL.config( text = "in")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                def to_snapHighlightToMouse(event):
                    to_listbox.selection_clear(0, END)
                    to_listbox.selection_set(to_listbox.nearest(event.y))

                def to_unhighlight():
                    to_listbox.selection_clear(0, END)

                to_listbox.delete(0, END)
                for item in range(len(distance_dict)):
                    to_listbox.insert(END, distance_dict[item])
                to_listbox.bind('<Motion>', lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Enter>',  lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Leave>',  lambda _: to_unhighlight())
                    
                            
                def snapHighlightToMouse(event):
                    from_listbox.selection_clear(0, END)
                    from_listbox.selection_set(from_listbox.nearest(event.y))

                def unhighlight():
                    from_listbox.selection_clear(0, END)  
                
                standard_heading.config(text = "Distance", foreground='red',background='sky blue')

                from_listbox.delete(0, END)
                for item in range(len(distance_dict)):
                    from_listbox.insert(END, distance_dict[item])
                from_listbox.bind('<<ListboxSelect>>', from_box)
                from_listbox.bind('<Motion>', lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Enter>',  lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Leave>',  lambda _: unhighlight())
            
            elif listbox_get =="Mass":
            
                def from_box(event):
                    fromlistbox_get = str(from_listbox.get(ANCHOR))

                    if fromlistbox_get == "Kilograms(kg)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Hectogram(hg)":
                                def convert():
                                    kg = float(input_entry.get())
                                    hg = float(kg*10)
                                    hg = round(hg , 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config(text = "Kilograms(kg) to Hectogram(hg)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometer(kg):")
                                input_EL.config(text = "kg")
                                output_OL.config(text = "hg")
                            
                            elif tolistbox_get == "Decagram(dag)":
                                def convert():
                                    kg = float(input_entry.get())
                                    dag = float(kg*100)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Kilograms(kg) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():
                                    kg = float(input_entry.get())
                                    g = float(kg*1000)
                                    g = round( g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Kilograms(kg) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():                  
                                    kg = float(input_entry.get())
                                    dg = float(kg*10000)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Kilograms(kg) to Decigram(dgg",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    kg = float(input_entry.get())
                                    cg = float(kg*100000)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Kilograms(kg) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":                        
                                def convert():
                                    kg = float(input_entry.get())
                                    mg = float(kg*1000000)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Kilograms(kg) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":
                                def convert():
                                    kg = float(input_entry.get())
                                    ct = float(kg*5000)
                                    ct = round(ct, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Kilograms(kg) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":
                                def convert():
                                    kg = float(input_entry.get())
                                    gr = float(kg*15432.358352941432832)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Kilograms(kg) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":
                                def convert():
                                    kg = float(input_entry.get())
                                    oz = float(kg*35.27396194958041088)
                                    oz = round(oz, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Kilograms(kg) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":                        
                                def convert():
                                    kg = float(input_entry.get())
                                    dwt = float(kg*643.01493137255956480)
                                    dwt = round(dwt, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Kilograms(kg) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":
                                def convert():
                                    kg = float(input_entry.get())
                                    lb = float(kg*2.2046226218487758848)
                                    lb = round(lb, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Kilograms(kg) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":
                                def convert():
                                    kg = float(input_entry.get())
                                    st = float(kg*0.15747304441776969728)
                                    st = round(st, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Kilograms(kg) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "st")
                            
                            elif tolistbox_get == "Tones(t)":
                                def convert():
                                    kg = float(input_entry.get())
                                    t = float(kg*0.0011023113109243879424)
                                    t = round(t, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Kilograms(kg) to Soot(soot)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Kilometer(kg):")
                                input_EL.config( text = "kg")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Hectogram(hg)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))
                        

                            if tolistbox_get == "Kilograms(kg)":
                                def convert():                            
                                    hg = float(input_entry.get())
                                    kg = float(hg/10)
                                    kg = round(kg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Hectogram(hg) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():                            
                                    hg = float(input_entry.get())
                                    dag = float(hg*10)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Hectogram(hg) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")                        
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():
                                    hg = float(input_entry.get())
                                    g = float(hg*100)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Hectogram(hg) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():                            
                                    hg = float(input_entry.get())
                                    dg = float(hg*1000)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Hectogram(hg) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "dg")
                            
                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    hg = float(input_entry.get())
                                    cg = float(hg*10000)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Hectogram(hg) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":                        
                                def convert():
                                    hg = float(input_entry.get())
                                    mg = float(hg*100000)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Hectogram(hg) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":                        
                                def convert():
                                    hg = float(input_entry.get())
                                    ct = float(hg*500)
                                    ct = round(ct, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Hectogram(hg) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":
                                def convert():
                                    hg = float(input_entry.get())
                                    gr = float(hg*1543.2358352941432832)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Hectogram(hg) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":
                                def convert():
                                    hg = float(input_entry.get())
                                    oz = float(hg*3.527396194958041088)
                                    oz = round(oz, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Hectogram(hg) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":
                                def convert():
                                    hg = float(input_entry.get())
                                    dwt = float(hg*64.301493137255956480)
                                    dwt = round(dwt, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Hectogram(hg) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":
                                def convert():
                                    hg = float(input_entry.get())
                                    lb = float(hg*0.22046226218487758848)
                                    lb = round(lb, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Hectogram(hg) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":
                                def convert():
                                    hg = float(input_entry.get())
                                    st = float(hg*0.015747304441776969728)
                                    st = round(st, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Hectogram(hg) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":
                                def convert():
                                    hg = float(input_entry.get())
                                    t = float(hg*0.00011023113109243879424)
                                    t = round(t, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Hectogram(hg) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Hectogram(hg):")
                                input_EL.config( text = "hg")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
                    

                    elif fromlistbox_get == "Decagram(dag)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilograms(kg)":
                                def convert():                            
                                    dag = float(input_entry.get())
                                    kg = float(dag/100)
                                    kg = round(kg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Decagram(dag) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():                            
                                    dag = float(input_entry.get())
                                    hg = float(dag/10)
                                    hg = round(hg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Decagram(dag) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Gram(g)":
                                def convert():    
                                    dag = float(input_entry.get())
                                    g = float(dag*10)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Decagram(dag) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    dag = float(input_entry.get())
                                    dg = float(dag*100)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Decagram(dag) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    dag = float(input_entry.get())
                                    cg = float(dag*1000)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Decagram(dag) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":
                                def convert():
                                    dag = float(input_entry.get())
                                    mg = float(dag*10000)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Decagram(dag) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":
                                def convert():
                                    dag = float(input_entry.get())
                                    ct = float(dag*50)
                                    ct = round(ct, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Decagram(dag) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":
                                def convert():
                                    dag = float(input_entry.get())
                                    gr = float(dag*154.32358352941432832)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Decagram(dag) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":                        
                                def convert():
                                    dag = float(input_entry.get())
                                    oz = float(dag*0.3527396194958041088)
                                    oz = round(oz, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Decagram(dag) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":
                                def convert():
                                    dag = float(input_entry.get())
                                    dwt = float(dag*6.4301493137255956480)
                                    dwt = round(dwt, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Decagram(dag) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":
                                def convert():
                                    dag = float(input_entry.get())
                                    lb = float(dag*0.022046226218487758848)
                                    lb = round(lb, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Decagram(dag) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":
                                def convert():
                                    dag = float(input_entry.get())
                                    st = float(dag*0.0015747304441776969728)
                                    st = round(st, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Decagram(dag) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":
                                def convert():
                                    dag = float(input_entry.get())
                                    t = float(dag*0.000011023113109243879424)
                                    t = round(t, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Decagram(dag) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decagrams(dag):")
                                input_EL.config( text = "dag")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Gram(g)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilograms(kg)":
                                def convert():                            
                                    g = float(input_entry.get())
                                    kg = float(g/1000)
                                    kg = round(kg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Gram(g) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "kg")
                            
                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():
                                    g = float(input_entry.get())
                                    hg = float(g/100)
                                    hg = round(hg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Gram(g) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")                        
                                input_EL.config( text = "g")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():                            
                                    g = float(input_entry.get())
                                    dag = float(g/10)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Gram(g) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    g = float(input_entry.get())
                                    dg = float(g*10)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Gram(g) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    g = float(input_entry.get())
                                    cg = float(g*100)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Gram(g) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":
                                def convert():
                                    g = float(input_entry.get())
                                    mg = float(g*1000)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Gram(g) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":
                                def convert():
                                    g = float(input_entry.get())
                                    ct = float(g*5)
                                    ct = round(ct, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Gram(g) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":                        
                                def convert():
                                    g = float(input_entry.get())
                                    gr = float(g*15.432358352941432832)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Gram(g) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":                        
                                def convert():
                                    g = float(input_entry.get())
                                    oz = float(g*0.03527396194958041088)
                                    oz = round(oz, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Gram(g) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":
                                def convert():
                                    g = float(input_entry.get())
                                    dwt = float(g*0.64301493137255956480)
                                    dwt = round(dwt, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Gram(g) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":
                                def convert():
                                    g = float(input_entry.get())
                                    lb = float(g*0.0022046226218487758848)
                                    lb = round(lb, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Gram(g) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":
                                def convert():
                                    g = float(input_entry.get())
                                    st = float(g*0.00015747304441776969728)
                                    st = round(st, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Gram(g) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":
                                def convert():
                                    g = float(input_entry.get())
                                    t = float(g*0.0000011023113109243879424)
                                    t = round(t, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Gram(g) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grams(g):")
                                input_EL.config( text = "g")
                                output_OL.config( text = "t")
                            
                        to_listbox.bind('<<ListboxSelect>>', to_box)

                        
                    elif fromlistbox_get == "Decigram(dg)":

                        def to_box(event):
                    
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilograms(kg)":
                                def convert():
                                    dg = float(input_entry.get())
                                    kg = float(dg/10000)
                                    kg = round(kg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Decigram(dg) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():                            
                                    dg = float(input_entry.get())
                                    hg = float(dg/1000)
                                    hg = round(hg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Decigram(dg) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():
                                    dg = float(input_entry.get())
                                    dag = float(dg/100)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Decigram(dg) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():
                                    dg = float(input_entry.get())
                                    g = float(dg/10)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Decigram(dg) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    dg = float(input_entry.get())
                                    cg = float(dg*10)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Decigram(dg) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":
                                def convert():
                                    dg = float(input_entry.get())
                                    mg = float(dg*100)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Decigram(dg) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":                        
                                def convert():
                                    dg = float(input_entry.get())
                                    ct = float(dg*0.5)
                                    ct = round(ct, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Decigram(dg) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":
                                def convert():
                                    dg = float(input_entry.get())
                                    gr = float(dg*1.5432358352941432832)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Decigram(dg) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":
                                def convert():
                                    dg = float(input_entry.get())
                                    oz = float(dg*0.003527396194958041088)
                                    oz = round(oz, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Decigram(dg) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":
                                def convert():
                                    dg = float(input_entry.get())
                                    dwt = float(dg*0.064301493137255956480)
                                    dwt = round(dwt, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Decigram(dg) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":
                                def convert():
                                    dg = float(input_entry.get())
                                    lb = float(dg*0.00022046226218487758848)
                                    lb = round(lb, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Decigram(dg) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":
                                def convert():
                                    dg = float(input_entry.get())
                                    st = float(dg*0.000015747304441776969728)
                                    st = round(st, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Decigram(dg) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":
                                def convert():
                                    dg = float(input_entry.get())
                                    t = float(dg*0.00000011023113109243879424)
                                    t = round(t, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Decigram(dg) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Decigrams(dg):")
                                input_EL.config( text = "dg")
                                output_OL.config( text = "t")
                            
                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Centigram(cg)":
                    
                        def to_box(event):
                    
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilograms(kg)":
                                def convert():
                                    cg = float(input_entry.get())
                                    kg = float(cg/100000)
                                    kg = round(kg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Centigram(cg) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():    
                                    cg = float(input_entry.get())
                                    hg = float(cg/10000)
                                    hg = round(hg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Centigram(cg) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():
                                    cg = float(input_entry.get())
                                    dag = float(cg/1000)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Centigram(cg) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():
                                    cg = float(input_entry.get())
                                    g = float(cg/100)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Centigram(cg) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    cg = float(input_entry.get())
                                    dg = float(cg/10)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Centigram(cg) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Milligrams(mg)":
                                def convert():
                                    cg = float(input_entry.get())
                                    mg = float(cg*10)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Centigram(cg) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":                        
                                def convert():
                                    cg = float(input_entry.get())
                                    ct = float(cg*0.05)
                                    ct = round(ct, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Centigram(cg) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":
                                def convert():
                                    cg = float(input_entry.get())
                                    gr = float(cg*0.15432358352941432832)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Centigram(cg) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":
                                def convert():
                                    cg = float(input_entry.get())
                                    oz = float(cg*0.0003527396194958041088)
                                    oz = round(oz, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Centigram(cg) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":                        
                                def convert():
                                    cg = float(input_entry.get())
                                    dwt = float(cg*0.0064301493137255956480)
                                    dwt = round(dwt, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Centigram(cg) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":
                                def convert():
                                    cg = float(input_entry.get())
                                    lb = float(cg*0.000022046226218487758848)
                                    lb = round(lb, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Centigram(cg) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":
                                def convert():
                                    cg = float(input_entry.get())
                                    st = float(cg*0.0000015747304441776969728)
                                    st = round(st, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Centigram(cg) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":
                                def convert():
                                    cg = float(input_entry.get())
                                    t = float(cg*0.000000011023113109243879424)
                                    t = round(t, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Centigram(cg) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Centigrams(cg):")
                                input_EL.config( text = "cg")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Milligrams(mg)":

                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))
                            
                            if tolistbox_get == "Kilograms(kg)":
                                def convert():
                                    mg = float(input_entry.get())
                                    kg = float(mg/1000000)
                                    kg = round(kg, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Milligrams(mg) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():
                                    mg = float(input_entry.get())
                                    hg = float(mg/100000)
                                    hg = round(hg, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Milligrams(mg) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():    
                                    mg = float(input_entry.get())
                                    dag = float(mg/10000)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Milligrams(mg) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():    
                                    mg = float(input_entry.get())
                                    m = float(mg/1000)
                                    m = round(m, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{m}")
                                heading_label.config( text = "Milligrams(mg) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "m")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    mg = float(input_entry.get())
                                    dg = float(mg/100)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Milligrams(mg) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    mg = float(input_entry.get())
                                    cg = float(mg/10)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Milligrams(mg) to Centigrams(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Carats(ct)":
                                def convert():
                                    mg = float(input_entry.get())
                                    ct = float(mg*0.005)
                                    ct = round(ct, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Milligrams(mg) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":                        
                                def convert():
                                    mg = float(input_entry.get())
                                    gr = float(mg*0.015432358352941432832)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Milligrams(mg) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":                        
                                def convert():
                                    mg = float(input_entry.get())
                                    oz = float(mg/305)
                                    oz = round(oz, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Milligrams(mg) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":
                                def convert():
                                    mg = float(input_entry.get())
                                    dwt = float(mg*0.00064301493137255956480)
                                    dwt = round(dwt, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Milligrams(mg) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":                        
                                def convert():
                                    mg = float(input_entry.get())
                                    lb = float(mg*0.0000022046226218487758848)
                                    lb = round(lb, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Milligrams(mg) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":                        
                                def convert():
                                    mg = float(input_entry.get())
                                    st = float(mg*0.0000022046226218487758848)
                                    st = round(st, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Milligrams(mg) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":                        
                                def convert():
                                    mg = float(input_entry.get())
                                    t = float(mg*0.0000000011023113109243879424)
                                    t = round(t, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Milligrams(mg) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Milligrams(mg):")
                                input_EL.config( text = "mg")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)

                            
                    elif fromlistbox_get == "Carats(ct)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilograms(kg)":
                                def convert():
                                    ct = float(input_entry.get())
                                    kg = float(ct*0.0002)
                                    kg = round(kg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Carats(ct) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():                            
                                    ct = float(input_entry.get())
                                    hg = float(ct*0.002)
                                    hg = round(hg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Carats(ct) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct)")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():    
                                    ct = float(input_entry.get())
                                    dag = float(ct*0.02)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Carats(ct) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():
                                    ct = float(input_entry.get())
                                    g = float(ct*0.2)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Carats(ct) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    ct = float(input_entry.get())
                                    dg = float(ct*2)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Carats(ct) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    ct = float(input_entry.get())
                                    cg = float(ct*20)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Carats(ct) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct)):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":                        
                                def convert():
                                    ct = float(input_entry.get())
                                    mg = float(ct*200)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Carats(ct) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct)):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Grains(gr)":                        
                                def convert():
                                    ct = float(input_entry.get())
                                    gr = float(ct*3.0864716705882865664)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Carats(ct) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":
                                def convert():
                                    ct = float(input_entry.get())
                                    oz = float(ct*0.0070547923899160821760)
                                    oz = round(oz, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Carats(ct) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct)")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":                        
                                def convert():
                                    ct = float(input_entry.get())
                                    dwt = float(ct*0.12860298627451191296)
                                    dwt = round(dwt, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Carats(ct) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":                        
                                def convert():
                                    ct = float(input_entry.get())
                                    lb = float(ct*0.00044092452436975517696)
                                    lb = round(lb, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Carats(ct) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":                        
                                def convert():
                                    ct = float(input_entry.get())
                                    st = float(ct*0.000031494608883553939456)
                                    st = round(st, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Carats(ct) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":
                                def convert():
                                    ct = float(input_entry.get())
                                    t = float(ct*0.00000022046226218487758848)
                                    t = round(t, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Carats(ct) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Carats(ct):")
                                input_EL.config( text = "ct")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
                            

                    elif fromlistbox_get == "Grains(gr)":
                        def to_box(event):
                            tolistbox_get = str(to_listbox.get(ANCHOR))
                            if tolistbox_get == "Kilograms(kg)":
                                def convert():
                                    gr = float(input_entry.get())
                                    kg = float(gr*0.00006479891)
                                    kg = round(kg, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Grains(gr) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():                            
                                    gr = float(input_entry.get())
                                    hg = float(gr*0.0006479891)
                                    hg = round(hg, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Grains(gr) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr)")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():
                                    gr = float(input_entry.get())
                                    dag = float(gr*0.006479891)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Grains(gr) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():
                                    gr = float(input_entry.get())
                                    g = float(gr*0.06479891)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Grains(gr) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    gr = float(input_entry.get())
                                    dg = float(gr*0.6479891)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Grains(gr) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    gr = float(input_entry.get())
                                    cg = float(gr*6.479891)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Grains(gr) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":
                                def convert():
                                    gr = float(input_entry.get())
                                    mg = float(gr*64.79891)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Grains(gr) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":
                                def convert():
                                    gr = float(input_entry.get())
                                    ct = float(gr*0.32399455)
                                    ct = round(ct, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Grains(gr) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Ounce(oz)":
                                def convert():
                                    gr = float(input_entry.get())
                                    oz = float(gr*0.0022857142857142857728)
                                    oz = round(oz, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Grains(gr) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr)")
                                input_EL.config( text = "gr")                        
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":                        
                                def convert():
                                    gr = float(input_entry.get())
                                    dwt = float(gr*0.041666666666667)
                                    dwt = round(dwt, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Grains(gr) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":                        
                                def convert():
                                    gr = float(input_entry.get())
                                    lb = float(gr*0.00014285714285714282496)
                                    lb = round(lb, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Grains(gr) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":                        
                                def convert():
                                    gr = float(input_entry.get())
                                    st = float(gr/98000)
                                    st = round(st, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Grains(gr) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":                        
                                def convert():
                                    gr = float(input_entry.get())
                                    t = float(gr*0.000000071428571428571422720)
                                    t = round(t, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Grains(gr) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Grains(gr):")
                                input_EL.config( text = "gr")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
                            

                    elif fromlistbox_get == "Ounce(oz)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilograms(kg)":
                                def convert():                            
                                    oz = float(input_entry.get())
                                    kg = float(oz*0.028349523125)
                                    kg = round(kg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Ounce(oz) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "kg")
                            
                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():
                                    oz = float(input_entry.get())
                                    hg = float(oz*0.28349523125)
                                    hg = round(hg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Ounce(oz) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():
                                    oz = float(input_entry.get())
                                    dag = float(oz*2.8349523125)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Ounce(oz) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():
                                    oz = float(input_entry.get())
                                    g = float(oz*28.349523125)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Ounce(oz) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    oz = float(input_entry.get())
                                    dg = float(oz*283.49523125)
                                    dg = round(dg , 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Ounce(oz) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":                        
                                def convert():
                                    oz = float(input_entry.get())
                                    cg = float(oz*2834.9523125)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Ounce(oz) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":
                                def convert():
                                    oz = float(input_entry.get())
                                    mg = float(oz*28349.523125)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Ounce(oz) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":
                                def convert():
                                    oz = float(input_entry.get())
                                    ct = float(oz*141.747615625)
                                    ct = round(ct, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Ounce(oz) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":
                                def convert():
                                    oz = float(input_entry.get())
                                    gr = float(oz*437.5)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Ounce(oz) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Pennyweights(dwt)":                        
                                def convert():
                                    oz = float(input_entry.get())
                                    dwt = float(oz*18.2291666667)
                                    dwt = round(dwt, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Ounce(oz) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":                        
                                def convert():
                                    oz = float(input_entry.get())
                                    lb = float(oz*0.0625)
                                    lb = round(lb, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Ounce(oz) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":                        
                                def convert():
                                    oz = float(input_entry.get())
                                    st = float(oz/224)
                                    st = round(st, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Ounce(oz) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":                        
                                def convert():
                                    oz = float(input_entry.get())
                                    t = float(oz*2.8349523125e-5)
                                    t = round(t, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Ounce(oz) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Ounce(oz):")
                                input_EL.config( text = "oz")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Pennyweights(dwt)":            
                        def to_box(event):
                            tolistbox_get = str(to_listbox.get(ANCHOR))
                            if tolistbox_get == "Kilograms(kg)":
                                def convert():
                                    dwt = float(input_entry.get())
                                    kg = float(dwt*0.00155517384)
                                    kg = round(kg, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Pennyweights(dwt) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():
                                    dwt = float(input_entry.get())
                                    hg = float(dwt*0.0155517384)
                                    hg = round(hg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Pennyweights(dwt) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():
                                    dwt = float(input_entry.get())
                                    dag = float(dwt*0.155517384)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Pennyweights(dwt) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():    
                                    dwt = float(input_entry.get())
                                    g = float(dwt*1.55517384)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Pennyweights(dwt) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    dwt = float(input_entry.get())
                                    dg = float(dwt*15.5517384)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Pennyweights(dwt) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    dwt = float(input_entry.get())
                                    cg = float(dwt*155.517384)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Pennyweights(dwt) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":                        
                                def convert():
                                    dwt = float(input_entry.get())
                                    mg = float(dwt*1555.17384)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Pennyweights(dwt) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":
                                def convert():
                                    dwt = float(input_entry.get())
                                    ct = float(dwt*7.7758692)
                                    ct = round(ct, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Pennyweights(dwt) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":
                                def convert():
                                    dwt = float(input_entry.get())
                                    gr = float(dwt*24)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Pennyweights(dwt) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")                        
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":                        
                                def convert():
                                    dwt = float(input_entry.get())
                                    oz = float(dwt*0.054857142857142853632)
                                    oz = round(oz, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Pennyweights(dwt) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pounds(lb)":                        
                                def convert():
                                    dwt = float(input_entry.get())
                                    lb = float(dwt*0.0034285714285714284544)
                                    lb = round(lb, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Pennyweights(dwt) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":                        
                                def convert():
                                    dwt = float(input_entry.get())
                                    st = float(dwt*0.0034285714285714284544)
                                    st = round(st, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Pennyweights(dwt) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":                        
                                def convert():
                                    dwt = float(input_entry.get())
                                    t = float(dwt*0.0000017142857142857144320)
                                    t = round(t, 9)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Pennyweights(dwt) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pennyweights(dwt):")
                                input_EL.config( text = "dwt")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Pounds(lb)":
                    
                        def to_box(event):    

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilograms(kg)":
                                def convert():                            
                                    lb = float(input_entry.get())
                                    kg = float(lb/2.2046226218487758848)
                                    kg = round(kg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Pounds(lb) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():
                                    lb = float(input_entry.get())
                                    hg = float(lb*4.5359237)
                                    hg = round(hg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Pounds(lb) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():
                                    lb = float(input_entry.get())
                                    dag = float(lb*45.359237)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Pounds(lb) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():    
                                    lb = float(input_entry.get())
                                    g = float(lb*453.59237)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Pounds(lb) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    lb = float(input_entry.get())
                                    dg = float(lb*4535.9237)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Pounds(lb) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    lb = float(input_entry.get())
                                    cg = float(lb*45359.237)
                                    cg = round(cg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Pounds(lb) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":
                                def convert():
                                    lb = float(input_entry.get())
                                    mg = float(lb*453592.37)
                                    mg = round(mg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Pounds(lb) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":
                                def convert():
                                    lb = float(input_entry.get())
                                    ct = float(lb*2267.96)
                                    ct = round(ct, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Pounds(lb) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":                        
                                def convert():
                                    lb = float(input_entry.get())
                                    gr = float(lb*7000)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Pounds(lb) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":                        
                                def convert():
                                    lb = float(input_entry.get())
                                    oz = float(lb*16)
                                    oz = round(oz, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Pounds(lb) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":                        
                                def convert():
                                    lb = float(input_entry.get())
                                    dwt = float(lb*291.666666666667)
                                    dwt = round(dwt, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Pounds(lb) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Stones(st)":                        
                                def convert():
                                    lb = float(input_entry.get())
                                    st = float(lb*0.071428571428571422720)
                                    st = round(st, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Pounds(lb) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "st")

                            elif tolistbox_get == "Tones(t)":                        
                                def convert():
                                    lb = float(input_entry.get())
                                    t = float(lb*0.0005)
                                    t = round(t, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Pounds(lb) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Pounds(lb):")
                                input_EL.config( text = "lb")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Stones(st)":
                    
                        def to_box(event):    

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilograms(kg)":
                                def convert():                            
                                    st = float(input_entry.get())
                                    kg = float(st*6.35029318)
                                    kg = round(kg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Stones(st) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():
                                    st = float(input_entry.get())
                                    hg = float(st*63.5029318)
                                    hg = round(hg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Stones(st) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():
                                    st = float(input_entry.get())
                                    dag = float(st*635.029318)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Stones(st) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():    
                                    st = float(input_entry.get())
                                    g = float(st*6350.29318)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Stones(st) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    st = float(input_entry.get())
                                    dg = float(st*63502.9318)
                                    dg = round(dg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Stones(st) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    st = float(input_entry.get())
                                    cg = float(st*635029.318)
                                    cg = round(cg, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Stones(st) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":
                                def convert():
                                    st = float(input_entry.get())
                                    mg = float(st*6350293.18)
                                    mg = round(mg, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Stones(st) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":
                                def convert():
                                    st = float(input_entry.get())
                                    ct = float(st*31751.5)
                                    ct = round(ct, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Stones(st) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":                        
                                def convert():
                                    st = float(input_entry.get())
                                    gr = float(st*98000)
                                    gr = round(gr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Stones(st) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":                        
                                def convert():
                                    st = float(input_entry.get())
                                    oz = float(st*224)
                                    oz = round(oz, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Stones(st) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":                        
                                def convert():
                                    st = float(input_entry.get())
                                    dwt = float(st*4083.33333333333)
                                    dwt = round(dwt, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Stones(st) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":                        
                                def convert():
                                    st = float(input_entry.get())
                                    lb = float(st*14)
                                    lb = round(lb, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Stones(st) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Tones(t)":                        
                                def convert():
                                    st = float(input_entry.get())
                                    t = float(st*0.007)
                                    t = round(t, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{t}")
                                heading_label.config( text = "Stones(st) to Tones(t)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Stones(st):")
                                input_EL.config( text = "st")
                                output_OL.config( text = "t")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                    elif fromlistbox_get == "Tones(t)":
                    
                        def to_box(event):    

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Kilograms(kg)":
                                def convert():                            
                                    t = float(input_entry.get())
                                    kg = float(t*907.18474)
                                    kg = round(kg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kg}")
                                heading_label.config( text = "Tones(t) to Kilograms(kg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "kg")

                            elif tolistbox_get == "Hectogram(hg)":
                                def convert():
                                    t = float(input_entry.get())
                                    hg = float(t*9071.8474)
                                    hg = round(hg, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hg}")
                                heading_label.config( text = "Tones(t) to Hectogram(hg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "hg")

                            elif tolistbox_get == "Decagram(dag)":
                                def convert():
                                    t = float(input_entry.get())
                                    dag = float(t*90718.474)
                                    dag = round(dag, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dag}")
                                heading_label.config( text = "Tones(t) to Decagram(dag)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "dag")

                            elif tolistbox_get == "Gram(g)":
                                def convert():    
                                    t = float(input_entry.get())
                                    g = float(t*907184.74)
                                    g = round(g, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{g}")
                                heading_label.config( text = "Tones(t) to Gram(g)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "g")

                            elif tolistbox_get == "Decigram(dg)":
                                def convert():
                                    t = float(input_entry.get())
                                    dg = float(t*9071847.4)
                                    dg = round(dg, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dg}")
                                heading_label.config( text = "Tones(t) to Decigram(dg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "dg")

                            elif tolistbox_get == "Centigram(cg)":
                                def convert():
                                    t = float(input_entry.get())
                                    cg = float(t*90718474)
                                    cg = round(cg, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cg}")
                                heading_label.config( text = "Tones(t) to Centigram(cg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "cg")

                            elif tolistbox_get == "Milligrams(mg)":
                                def convert():
                                    t = float(input_entry.get())
                                    mg = float(t*907184740)
                                    mg = round(mg, 2)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mg}")
                                heading_label.config( text = "Tones(t) to Milligrams(mg)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "mg")

                            elif tolistbox_get == "Carats(ct)":
                                def convert():
                                    t = float(input_entry.get())
                                    ct = float(t*4535923.7)
                                    ct = round(ct, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ct}")
                                heading_label.config( text = "Tones(t) to Carats(ct)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "ct")

                            elif tolistbox_get == "Grains(gr)":                        
                                def convert():
                                    t = float(input_entry.get())
                                    gr = float(t*14000000)
                                    gr = round(gr, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{gr}")
                                heading_label.config( text = "Tones(t) to Grains(gr)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "gr")

                            elif tolistbox_get == "Ounce(oz)":                        
                                def convert():
                                    t = float(input_entry.get())
                                    oz = float(t/2.8349523125e-5)
                                    oz = round(oz, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{oz}")
                                heading_label.config( text = "Tones(t) to Ounce(oz)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "oz")

                            elif tolistbox_get == "Pennyweights(dwt)":                        
                                def convert():
                                    t = float(input_entry.get())
                                    dwt = float(t*583333)
                                    dwt = round(dwt, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{dwt}")
                                heading_label.config( text = "Tones(t) to Pennyweights(dwt)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "dwt")

                            elif tolistbox_get == "Pounds(lb)":                        
                                def convert():
                                    t = float(input_entry.get())
                                    lb = float(t*2000)
                                    lb = round(lb, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{lb}")
                                heading_label.config( text = "Tones(t) to Pounds(lb)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "lb")

                            elif tolistbox_get == "Stones(st)":                        
                                def convert():
                                    t = float(input_entry.get())
                                    st = float(t*142.85714285714286592)
                                    st = round(st, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{st}")
                                heading_label.config( text = "Tones(t) to Stones(st)",background = "white")
                                convert_button.config( command = convert)
                                enter_label.config( text = "Enter the Tones(t):")
                                input_EL.config( text = "t")
                                output_OL.config( text = "st")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
                
                def to_snapHighlightToMouse(event):
                    to_listbox.selection_clear(0, END)
                    to_listbox.selection_set(to_listbox.nearest(event.y))

                def to_unhighlight():
                    to_listbox.selection_clear(0, END)

                to_listbox.delete(0, END)
                for item in range(len(mass_dict)):
                    to_listbox.insert(END, mass_dict[item])
                to_listbox.bind('<Motion>', lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Enter>',  lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Leave>',  lambda _: to_unhighlight())
         
                def snapHighlightToMouse(event):
                    from_listbox.selection_clear(0, END)
                    from_listbox.selection_set(from_listbox.nearest(event.y))

                def unhighlight():
                    from_listbox.selection_clear(0, END)  
                
                standard_heading.config(text = "Distance", foreground='red',background='sky blue')

                from_listbox.delete(0, END)
                for item in range(len(mass_dict)):
                    from_listbox.insert(END, mass_dict[item])
                from_listbox.bind('<<ListboxSelect>>', from_box)
                from_listbox.bind('<Motion>', lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Enter>',  lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Leave>',  lambda _: unhighlight())



            elif listbox_get =="Velocity":
            
                def from_box(event):

                    fromlistbox_get = str(from_listbox.get(ANCHOR))

                    if fromlistbox_get == "Centimeter/Hours(cm/h)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    cmmin = float(cmh/60)
                                    cmmin = round(cmmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    cmsec = float(cmh/3600)
                                    cmsec = round(cmsec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    fth = float(cmh/30.48)
                                    fth = round(fth, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    fth = float(cmh*0.00054680664916885381120)
                                    fth = round(fth, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    ftsec = float(cmh/109728)
                                    ftsec = round(ftsec, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    kmh = float(cmh/100000)
                                    kmh = round(kmh, 9)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    kmmin = float(cmh/6000000)
                                    kmmin = round(kmmin, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    kmsec = float(cmh/360000000)
                                    kmsec = round(kmsec, 13)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    kn = float(cmh/185200)
                                    kn = round(kn, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    c = float(cmh*0.0000000000000092656693110597779456)
                                    c = round(c, 18)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    M = float(cmh* 0.0000000080984774862325874688)
                                    M = round(M, 15)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    mh = float(cmh/100)
                                    mh = round(mh, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    mmin = float(cmh/6000)
                                    mmin = round(mmin, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    msec = float(cmh/360000)
                                    msec = round(msec, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    mih = float(cmh/160934)
                                    mih = round(mih, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    mimin = float(cmh*0.00000010356186537288900608)
                                    mimin = round(mimin, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    cmh = float(input_entry.get())
                                    misec = float(cmh*0.0000000017260310895481497600)
                                    misec = round(misec, 13)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Centimeter/Hours(cm/h) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeter/Hours(cm/h):")
                                input_EL.config(text = "cm/h")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)

                    elif fromlistbox_get == "Centimeters/Minutes(cm/min)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    cmh = float(cmmin*60)
                                    cmh = round(cmh, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    cmsec = float(cmmin/60)
                                    cmsec = round(cmsec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    fth = float(cmmin*1.9685039370078736384)
                                    fth = round(fth, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    fth = float(cmmin/30.48)
                                    fth = round(fth, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    ftsec = float(cmmin*0.00054680664916885381120)
                                    ftsec = round(ftsec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    kmh = float(cmmin/1667)
                                    kmh = round(kmh, 9)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    kmmin = float(cmmin/100000)
                                    kmmin = round(kmmin, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    kmsec = float(cmmin/6000000)
                                    kmsec = round(kmsec, 12)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    kn = float(cmmin*0.00032397408235332530176)
                                    kn = round(kn, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    c = float(cmmin* 0.00000000000055594015866358677504)
                                    c = round(c, 17)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    M = float(cmmin* 0.00000048590864917395529728)
                                    M = round(M, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    mh = float(cmmin/1.667)
                                    mh = round(mh, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    mmin = float(cmmin/100)
                                    mmin = round(mmin, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    msec = float(cmmin/6000)
                                    msec = round(msec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    mih = float(cmmin*0.00037282271534240030720)
                                    mih = round(mih, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    mimin = float(cmmin*0.0000062137119223733395456)
                                    mimin = round(mimin, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    cmmin = float(input_entry.get())
                                    misec = float(cmmin*0.00000010356186537288898560)
                                    misec = round(misec, 11)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Centimeters/Minutes(cm/min) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Minutes(cm/min):")
                                input_EL.config(text = "cm/min")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)

                    elif fromlistbox_get == "Centimeters/Seconds(cm/sec)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    cmh = float(cmsec*3600)
                                    cmh = round(cmh, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    cmmin = float(cmsec*5)
                                    cmmin = round(cmmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    fth = float(cmsec*118.11023622047242240)
                                    fth = round(fth, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    fth = float(cmsec*1.9685039370078740480)
                                    fth = round(fth, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    ftsec = float(cmsec*0.032808398950131232768)
                                    ftsec = round(ftsec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    kmh = float(cmsec/27.778)
                                    kmh = round(kmh, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    kmmin = float(cmsec/1667)
                                    kmmin = round(kmmin, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    kmsec = float(cmsec/100000)
                                    kmsec = round(kmsec, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    kn = float(cmsec*0.019438444941199519744)
                                    kn = round(kn, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    c = float(cmsec* 0.000000000033356409519815204864)
                                    c = round(c, 15)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    M = float(cmsec/34300)
                                    M = round(M, 9)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    mh = float(cmsec*36)
                                    mh = round(mh, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    mmin = float(cmsec/1.667)
                                    mmin = round(mmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    msec = float(cmsec/100)
                                    msec = round(msec, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    mih = float(cmsec*0.022369362920544022528)
                                    mih = round(mih, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    mimin = float(cmsec*0.00037282271534240038912)
                                    mimin = round(mimin, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    cmsec = float(input_entry.get())
                                    misec = float(cmsec*0.0000062137119223733403648)
                                    misec = round(misec, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Centimeters/Seconds(cm/sec) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Centimeters/Seconds(cm/sec):")
                                input_EL.config(text = "cm/sec")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)

                    elif fromlistbox_get == "Feet/Hours(ft/h)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    fth = float(input_entry.get())
                                    cmh = float(fth*30.48)
                                    cmh = round(cmh, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    fth = float(input_entry.get())
                                    cmmin = float(fth/1.969)
                                    cmmin = round(cmmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    fth = float(input_entry.get())
                                    cmsec = float(fth/118.11023622047242240)
                                    cmsec = round(cmsec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    fth = float(input_entry.get())
                                    ftmin = float(fth/60)
                                    ftmin = round(ftmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    fth = float(input_entry.get())
                                    ftsec = float(fth/3600)
                                    ftsec = round(ftsec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    fth = float(input_entry.get())
                                    kmh = float(fth/3281)
                                    kmh = round(kmh, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    fth = float(input_entry.get())
                                    kmmin = float(fth/196850)
                                    kmmin = round(kmmin, 11)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    fth = float(input_entry.get())
                                    kmsec = float(fth*8.4667e-8)
                                    kmsec = round(kmsec, 12)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    fth = float(input_entry.get())
                                    kn = float(fth*0.00016457883383548928)
                                    kn = round(kn, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    fth = float(input_entry.get())
                                    c = float(fth*2.8241760060110209024e-13)
                                    c = round(c, 16)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    fth = float(input_entry.get())
                                    M = float(fth*4051181.1023622046335)
                                    M = round(M, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    fth = float(input_entry.get())
                                    mh = float(fth/3.281)
                                    mh = round(mh, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    fth = float(input_entry.get())
                                    mmin = float(fth/197)
                                    mmin = round(mmin, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    fth = float(input_entry.get())
                                    msec = float(fth/11811)
                                    msec = round(msec, 9)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    fth = float(input_entry.get())
                                    mih = float(fth/5280)
                                    mih = round(mih, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    fth = float(input_entry.get())
                                    mimin = float(fth/316800)
                                    mimin = round(mimin, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    fth = float(input_entry.get())
                                    misec = float(fth*5.2609427609427607552e-8)
                                    misec = round(misec, 12)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Feet/Hours(ft/h) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Hours(ft/h):")
                                input_EL.config(text = "ft/h")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)

                    elif fromlistbox_get == "Feet/Minutes(ft/min)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    cmh = float(ftmin*1828.80)
                                    cmh = round(cmh, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    cmmin = float(ftmin*30.48)
                                    cmmin = round(cmmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    cmsec = float(ftmin*1.9685039370078740480)
                                    cmsec = round(cmsec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    fth = float(ftmin*60)
                                    fth = round(fth, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    ftsec = float(ftmin/60)
                                    ftsec = round(ftsec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    kmh = float(ftmin/54.681)
                                    kmh = round(kmh, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    kmmin = float(ftmin/3281)
                                    kmmin = round(kmmin, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    kmsec = float(ftmin*196850)
                                    kmsec = round(kmsec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    kn = float(ftmin*0.0098747300301293568000)
                                    kn = round(kn, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    c = float(ftmin*5.901e+10)
                                    c = round(c, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    M = float(ftmin*67519.7)
                                    M = round(M, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    mh = float(ftmin*18.287985369611704320)
                                    mh = round(mh, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    mmin = float(ftmin/3.281)
                                    mmin = round(mmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    msec = float(ftmin/197)
                                    msec = round(msec, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    mih = float(ftmin/88)
                                    mih = round(mih, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    mimin = float(ftmin/5280)
                                    mimin = round(mimin, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    ftmin = float(input_entry.get())
                                    misec = float(ftmin/316800)
                                    misec = round(misec, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Feet/Minutes(ft/min) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Minutes(ft/min):")
                                input_EL.config(text = "ft/min")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Feet/Seconds(ft/sec)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    cmh = float(ftsec*109728)
                                    cmh = round(cmh, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    cmmin = float(ftsec*1828.8)
                                    cmmin = round(cmmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    cmsec = float(ftsec*30.48)
                                    cmsec = round(cmsec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    fth = float(ftsec*3600)
                                    fth = round(fth, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    ftmin = float(ftsec*60)
                                    ftmin = round(ftmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    kmh = float(ftsec*1.09728)
                                    kmh = round(kmh, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    kmmin = float(ftsec/54.681)
                                    kmmin = round(kmmin, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    kmsec = float(ftsec/3281)
                                    kmsec = round(kmsec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    kn = float(ftsec*0.59248380180776140800)
                                    kn = round(kn, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    c = float(ftsec*1.0167033621639675904e-9)
                                    c = round(c, 14)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    M = float(ftsec*0.00088862973760932937728)
                                    M = round(M, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    mh = float(ftsec*1097.28)
                                    mh = round(mh, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    mmin = float(ftsec*18.288)
                                    mmin = round(mmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    msec = float(ftsec/3.281)
                                    msec = round(msec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    mih = float(ftsec/1.467)
                                    mih = round(mih, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    mimin = float(ftsec/88)
                                    mimin = round(mimin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    ftsec = float(input_entry.get())
                                    misec = float(ftsec/5280)
                                    misec = round(misec, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Feet/Seconds(ft/sec) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Feet/Seconds(ft/sec):")
                                input_EL.config(text = "ft/sec")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Kilometers/Hours(km/h)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    cmh = float(kmh*100000)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    cmmin = float(kmh*1666.6666667)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    cmsec = float(kmh*27.7777777778)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    fth = float(kmh*3280.83989501338527)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    ftmin = float(kmh*54.680664916889763840)
                                    ftmin = round(ftmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    ftsec = float(kmh*0.91134441528149590016)
                                    ftsec = round(ftsec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    kmmin = float(kmh/60)
                                    kmmin = round(kmmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    kmsec = float(kmh/3600)
                                    kmsec = round(kmsec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    kn = float(kmh*0.53995680392225210368)
                                    kn = round(kn, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    c = float(kmh*9.2656693110605201408e-10)
                                    c = round(c, 14)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    M = float(kmh*0.00080984774862332346368)
                                    M = round(M, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    mh = float(kmh*1000)
                                    mh = round(mh, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    mmin = float(kmh*16.666666666667)
                                    mmin = round(mmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    msec = float(kmh/3.6)
                                    msec = round(msec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    mih = float(kmh*0.62137119223738368000)
                                    mih = round(mih, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    mimin = float(kmh*0.010356186537289725952)
                                    mimin = round(mimin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    kmh = float(input_entry.get())
                                    misec = float(kmh*0.00017260310895482877952)
                                    misec = round(misec, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Kilometers/Hours(km/h) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Hours(km/h):")
                                input_EL.config(text = "km/h")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Kilometers/Minutes(km/min)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    cmh = float(kmmin*6e+6)
                                    cmh = round(cmh, 2)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    cmmin = float(kmmin*100000)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    cmsec = float(kmmin*1666.66666666666667)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    fth = float(kmmin*196850)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    ftmin = float(kmmin*3281)
                                    ftmin = round(ftmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    ftsec = float(kmmin*54.680664916885389312)
                                    ftsec = round(ftsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    kmh = float(kmmin*60)
                                    kmh = round(kmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    kmsec = float(kmmin/60)
                                    kmsec = round(kmsec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    kn = float(kmmin*32.397408235332538368)
                                    kn = round(kn, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    c = float(kmmin*5.5594015866358685696e-8)
                                    c = round(c, 12)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    M = float(kmmin/20.58)
                                    M = round(M, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    mh = float(kmmin*60000)
                                    mh = round(mh, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    mmin = float(kmmin*1000)
                                    mmin = round(mmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    msec = float(kmmin*16.6666666666666667)
                                    msec = round(msec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    mih = float(kmmin*37.282271534240038912)
                                    mih = round(mih, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    mimin = float(kmmin*0.62137119223733395456)
                                    mimin = round(mimin, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    kmmin = float(input_entry.get())
                                    misec = float(kmmin*0.010356186537288900608)
                                    misec = round(misec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Kilometers/Minutes(km/min) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Minutes(km/min):")
                                input_EL.config(text = "km/min")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Kilometers/Seconds(km/sec)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    cmh = float(kmsec*3.6e+8)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    cmmin = float(kmsec*6e+6)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    cmsec = float(kmsec*100000)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    fth = float(kmsec*1.181e+7)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    ftmin = float(kmsec*196850)
                                    ftmin = round(ftmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    ftsec = float(kmsec*3280.84)
                                    ftsec = round(ftsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    kmh = float(kmsec*3600)
                                    kmh = round(kmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    kmmin = float(kmsec*60)
                                    kmmin = round(kmmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    kn = float(kmsec*1943.84)
                                    kn = round(kn, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    c = float(kmsec*3.3356409519815208960e-6)
                                    c = round(c, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    M = float(kmsec*2.9154518950437318656)
                                    M = round(M, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    mh = float(kmsec*3.6e+6)
                                    mh = round(mh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    mmin = float(kmsec*60000)
                                    mmin = round(mmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    msec = float(kmsec*1000)
                                    msec = round(msec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    mih = float(kmsec*2236.94)
                                    mih = round(mih, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    mimin = float(kmsec*37.282271534240038912)
                                    mimin = round(mimin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    kmsec = float(input_entry.get())
                                    misec = float(kmsec*0.62137119223733387264)
                                    misec = round(misec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Kilometers/Seconds(km/sec) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Kilometers/Seconds(km/sec):")
                                input_EL.config(text = "km/sec")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Knots(kn)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    kn = float(input_entry.get())
                                    cmh = float(kn*185200)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Knots(kn) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    kn = float(input_entry.get())
                                    cmmin = float(kn*3086.67)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Knots(kn) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    kn = float(input_entry.get())
                                    cmsec = float(kn*51.4444444)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Knots(kn) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    kn = float(input_entry.get())
                                    fth = float(kn*6076.12)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Knots(kn) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    kn = float(input_entry.get())
                                    ftmin = float(kn*101.26859133858267136)
                                    ftmin = round(ftmin, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Knots(kn) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    kn = float(input_entry.get())
                                    ftsec = float(kn*1.6878098556430444544)
                                    ftsec = round(ftsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Knots(kn) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    kn = float(input_entry.get())
                                    kmh = float(kn*1.852)
                                    kmh = round(kmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Knots(kn) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    kn = float(input_entry.get())
                                    kmmin = float(kn*0.03086666664)
                                    kmmin = round(kmmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Knots(kn) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    kn = float(input_entry.get())
                                    kmsec = float(kn/1944)
                                    kmsec = round(kmsec, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Knots(kn) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    kn = float(input_entry.get())
                                    c = float(kn*1.7160019549257639936e-9)
                                    c = round(c, 13)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Knots(kn) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    kn = float(input_entry.get())
                                    M = float(kn*0.0014998380291545190400)
                                    M = round(M, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Knots(kn) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    kn = float(input_entry.get())
                                    mh = float(kn*1851.99851680118637)
                                    mh = round(mh, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Knots(kn) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    kn = float(input_entry.get())
                                    mmin = float(kn*0.032397408235332534272)
                                    mmin = round(mmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Knots(kn) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    kn = float(input_entry.get())
                                    msec = float(kn*0.514444444)
                                    msec = round(msec, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Knots(kn) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    kn = float(input_entry.get())
                                    mih = float(kn*1.1507794470293485568)
                                    mih = round(mih, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Knots(kn) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    kn = float(input_entry.get())
                                    mimin = float(kn*0.019179657450489143296)
                                    mimin = round(mimin, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Knots(kn) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    kn = float(input_entry.get())
                                    misec = float(kn*0.00031966095750815232000)
                                    misec = round(misec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Knots(kn) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Knots(kn):")
                                input_EL.config(text = "kn")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Light Speed(c)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    c = float(input_entry.get())
                                    cmh = float(c*1.079e+14)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Light Speed(c) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    c = float(input_entry.get())
                                    cmmin = float(c*1.799e+12)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Light Speed(c) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    c = float(input_entry.get())
                                    cmsec = float(c*2.998e+10)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Light Speed(c) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    c = float(input_entry.get())
                                    fth = float(c*3.541e+12)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Light Speed(c) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    c = float(input_entry.get())
                                    ftmin = float(c*5.901e+10)
                                    ftmin = round(ftmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Light Speed(c) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    c = float(input_entry.get())
                                    ftsec = float(c*9.836e+8)
                                    ftsec = round(ftsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Light Speed(c) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    c = float(input_entry.get())
                                    kmh = float(c*1.079e+9)
                                    kmh = round(kmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Light Speed(c) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    c = float(input_entry.get())
                                    kmmin = float(c*1.799e+7)
                                    kmmin = round(kmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Light Speed(c) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    c = float(input_entry.get())
                                    kmsec = float(c*299792)
                                    kmsec = round(kmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Light Speed(c) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    c = float(input_entry.get())
                                    kn = float(c*5.827e+8)
                                    kn = round(kn, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Light Speed(c) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    c = float(input_entry.get())
                                    M = float(c*874030)
                                    M = round(M, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Light Speed(c) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    c = float(input_entry.get())
                                    mh = float(c*1.079e+12)
                                    mh = round(mh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Light Speed(c) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    c = float(input_entry.get())
                                    mmin = float(c*1.799e+10)
                                    mmin = round(mmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Light Speed(c) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    c = float(input_entry.get())
                                    msec = float(c*2.998e+8)
                                    msec = round(msec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Light Speed(c) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    c = float(input_entry.get())
                                    mih = float(c*6.706e+8)
                                    mih = round(mih, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Light Speed(c) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    c = float(input_entry.get())
                                    mimin = float(c*96.56064)
                                    mimin = round(mimin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Light Speed(c) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    c = float(input_entry.get())
                                    misec = float(c*5793.64)
                                    misec = round(misec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Light Speed(c) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Light Speed(c):")
                                input_EL.config(text = "c")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Mach(M)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    M = float(input_entry.get())
                                    cmh = float(M*1.235e+8)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Mach(M) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    M = float(input_entry.get())
                                    cmmin = float(M*2.058e+6)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Mach(M) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    M = float(input_entry.get())
                                    cmsec = float(M*34300)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Mach(M) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    M = float(input_entry.get())
                                    fth = float(M*4.051e+6)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Mach(M) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    M = float(input_entry.get())
                                    ftmin = float(M*67519.7)
                                    ftmin = round(ftmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Mach(M) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    M = float(input_entry.get())
                                    ftsec = float(M*1125.33)
                                    ftsec = round(ftsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Mach(M) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    M = float(input_entry.get())
                                    kmh = float(M*1225.04)
                                    kmh = round(kmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Mach(M) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    M = float(input_entry.get())
                                    kmmin = float(M*20.58)
                                    kmmin = round(kmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Mach(M) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    M = float(input_entry.get())
                                    kmsec = float(M/2.915)
                                    kmsec = round(kmsec, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Mach(M) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    M = float(input_entry.get())
                                    kn = float(M*666.73866148314357760)
                                    kn = round(kn, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Mach(M) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    M = float(input_entry.get())
                                    c = float(M*1.1441248465296615424e-6)
                                    c = round(c, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Mach(M) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    M = float(input_entry.get())
                                    mh = float(M*1.235e+6)
                                    mh = round(mh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Mach(M) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    M = float(input_entry.get())
                                    mmin = float(M*20580)
                                    mmin = round(mmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Mach(M) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    M = float(input_entry.get())
                                    msec = float(M*343)
                                    msec = round(msec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Mach(M) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    M = float(input_entry.get())
                                    mih = float(M*767.26914817466007552)
                                    mih = round(mih, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Mach(M) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    M = float(input_entry.get())
                                    mimin = float(M*12.787819136244332544)
                                    mimin = round(mimin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Mach(M) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    M = float(input_entry.get())
                                    misec = float(M/4.692)
                                    misec = round(misec, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Mach(M) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Mach(M):")
                                input_EL.config(text = "M")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Meters/Hours(m/h)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    mh = float(input_entry.get())
                                    cmh = float(mh*100)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Meters/Hours(m/h) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    mh = float(input_entry.get())
                                    cmmin = float(mh*1.666668)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Meters/Hours(m/h) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    mh = float(input_entry.get())
                                    cmsec = float(mh/36)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Meters/Hours(m/h) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    mh = float(input_entry.get())
                                    fth = float(mh*3.2808425196850388992)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Meters/Hours(m/h) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    mh = float(input_entry.get())
                                    ftmin = float(mh*0.054680708661417320448)
                                    ftmin = round(ftmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Meters/Hours(m/h) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    mh = float(input_entry.get())
                                    ftsec = float(mh*0.00091134514435695525888)
                                    ftsec = round(ftsec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Meters/Hours(m/h) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    mh = float(input_entry.get())
                                    kmh = float(mh/1000)
                                    kmh = round(kmh, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Meters/Hours(m/h) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    mh = float(input_entry.get())
                                    kmmin = float(mh/60000)
                                    kmmin = round(kmmin, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Meters/Hours(m/h) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    mh = float(input_entry.get())
                                    kmsec = float(mh*2.77778e-7)
                                    kmsec = round(kmsec, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Meters/Hours(m/h) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    mh = float(input_entry.get())
                                    kn = float(mh*0.00053995723588765204480)
                                    kn = round(kn, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Meters/Hours(m/h) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    mh = float(input_entry.get())
                                    c = float(mh*9.2656767235952279552e-13)
                                    c = round(c, 16)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Meters/Hours(m/h) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    mh = float(input_entry.get())
                                    M = float(mh*8.0984774862325874688e-7)
                                    M = round(M, 11)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Meters/Hours(m/h) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    mh = float(input_entry.get())
                                    mmin = float(mh/60)
                                    mmin = round(mmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Meters/Hours(m/h) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    mh = float(input_entry.get())
                                    msec = float(mh/3600)
                                    msec = round(msec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Meters/Hours(m/h) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    mh = float(input_entry.get())
                                    mih = float(mh*0.00062137168933428772864)
                                    mih = round(mih, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Meters/Hours(m/h) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    mh = float(input_entry.get())
                                    mimin = float(mh*1.0356194822238128128e-5)
                                    mimin = round(mimin, 9)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Meters/Hours(m/h) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    mh = float(input_entry.get())
                                    misec = float(mh*1.7260324703730214912e-7)
                                    misec = round(misec, 11)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Meters/Hours(m/h) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Hours(m/h):")
                                input_EL.config(text = "m/h")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Meters/Minutes(m/min)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    cmh = float(mmin*6000)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    cmmin = float(mmin*100)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "cm/min")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    cmsec = float(mmin*1.66666667)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    fth = float(mmin*196.85039370078740480)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    ftmin = float(mmin*3.2808398950131228672)
                                    ftmin = round(ftmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    ftsec = float(mmin/18.288)
                                    ftsec = round(ftsec, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    kmh = float(mmin/16.667)
                                    kmh = round(kmh, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    kmmin = float(mmin/1000)
                                    kmmin = round(kmmin, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    kmsec = float(mmin/60000)
                                    kmsec = round(kmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    kn = float(mmin*0.032397408235332534272)
                                    kn = round(kn, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    c = float(mmin*5.5594015866358677504e-11)
                                    c = round(c, 15)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    M = float(mmin/20580)
                                    M = round(M, 11)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    mh = float(mmin/60)
                                    mh = round(mh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    msec = float(mmin*60)
                                    msec = round(msec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    mih = float(mmin*0.037282271534240038912)
                                    mih = round(mih, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    mimin = float(mmin*0.00062137119223733387264)
                                    mimin = round(mimin, 9)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    mmin = float(input_entry.get())
                                    misec = float(mmin*1.0356186537288898560e-5)
                                    misec = round(misec, 11)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Meters/Minutes(m/min) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Minutes(m/min):")
                                input_EL.config(text = "m/min")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Meters/Seconds(m/sec)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    msec = float(input_entry.get())
                                    cmh = float(msec*360000)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    msec = float(input_entry.get())
                                    cmmin = float(msec*6000)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    msec = float(input_entry.get())
                                    cmsec = float(msec*100)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    msec = float(input_entry.get())
                                    fth = float(msec*11811)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    msec = float(input_entry.get())
                                    ftmin = float(msec*196.85039370078740480)
                                    ftmin = round(ftmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    msec = float(input_entry.get())
                                    ftsec = float(msec*3.2808398950131232768)
                                    ftsec = round(ftsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    msec = float(input_entry.get())
                                    kmh = float(msec*3.6)
                                    kmh = round(kmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    msec = float(input_entry.get())
                                    kmmin = float(msec/16.667)
                                    kmmin = round(kmmin, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    msec = float(input_entry.get())
                                    kmsec = float(msec/1000)
                                    kmsec = round(kmsec, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    msec = float(input_entry.get())
                                    kn = float(msec*1.9438444941199519744)
                                    kn = round(kn, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    msec = float(input_entry.get())
                                    c = float(msec*3.3356409519815204864e-9)
                                    c = round(c, 14)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    msec = float(input_entry.get())
                                    M = float(msec/343)
                                    M = round(M, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    msec = float(input_entry.get())
                                    mh = float(msec*3600)
                                    mh = round(mh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    msec = float(input_entry.get())
                                    mmin = float(msec*60)
                                    mmin = round(mmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    msec = float(input_entry.get())
                                    mih = float(msec*2.2369362920544022528)
                                    mih = round(mih, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    msec = float(input_entry.get())
                                    mimin = float(msec*0.037282271534240038912)
                                    mimin = round(mimin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    msec = float(input_entry.get())
                                    misec = float(msec*0.00062137119223733387264)
                                    misec = round(misec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Meters/Seconds(m/sec) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Meters/Seconds(m/sec):")
                                input_EL.config(text = "m/sec")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Miles/Hours(mi/h)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    mih = float(input_entry.get())
                                    cmh = float(mih*160934)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    mih = float(input_entry.get())
                                    cmmin = float(mih*2682.24)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    mih = float(input_entry.get())
                                    cmsec = float(mih*44.704)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    mih = float(input_entry.get())
                                    fth = float(mih*5280)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    mih = float(input_entry.get())
                                    ftmin = float(mih*88)
                                    ftmin = round(ftmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    mih = float(input_entry.get())
                                    ftsec = float(mih*1.4666666666666666667)
                                    ftsec = round(ftsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    mih = float(input_entry.get())
                                    kmh = float(mih*1.609344)
                                    kmh = round(kmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    mih = float(input_entry.get())
                                    kmmin = float(mih/37.282)
                                    kmmin = round(kmmin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    mih = float(input_entry.get())
                                    kmsec = float(mih/2237)
                                    kmsec = round(kmsec, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    mih = float(input_entry.get())
                                    kn = float(mih*0.86897624265138339840)
                                    kn = round(kn, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    mih = float(input_entry.get())
                                    c = float(mih*1.4911649311738187776e-9)
                                    c = round(c, 14)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    mih = float(input_entry.get())
                                    M = float(mih*0.0013033236151603499008)
                                    M = round(M, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    mih = float(input_entry.get())
                                    mh = float(mih*1609.34)
                                    mh = round(mh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    mih = float(input_entry.get())
                                    mmin = float(mih*26.8224)
                                    mmin = round(mmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    mih = float(input_entry.get())
                                    msec = float(mih/2.237)
                                    msec = round(msec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    mih = float(input_entry.get())
                                    mimin = float(mih/60)
                                    mimin = round(mimin, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "mi/min")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    mih = float(input_entry.get())
                                    misec = float(mih/3600)
                                    misec = round(misec, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Miles/Hours(mi/h) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Hours(mi/h):")
                                input_EL.config(text = "mi/h")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Miles/Minutes(mi/min)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    cmh = float(mimin*9.656e+6)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    cmmin = float(mimin*160934)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    cmsec = float(mimin*2682.24)
                                    cmsec = round(cmsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    fth = float(mimin*316800)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    ftmin = float(mimin*5280)
                                    ftmin = round(ftmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    ftsec = float(mimin*88)
                                    ftsec = round(ftsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    kmh = float(mimin*96.56064)
                                    kmh = round(kmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    kmmin = float(mimin*1.60934)
                                    kmmin = round(kmmin, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    kmsec = float(mimin*0.0268224)
                                    kmsec = round(kmsec, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    kn = float(mimin*52.138574559083003904)
                                    kn = round(kn, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    c = float(mimin*8.9469895870429134848e-8)
                                    c = round(c, 12)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    M = float(mimin*0.078199416909620985856)
                                    M = round(M, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    mh = float(mimin*96560.6)
                                    mh = round(mh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    mmin = float(mimin*1609.34)
                                    mmin = round(mmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    msec = float(mimin*26.8224)
                                    msec = round(msec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    mih = float(mimin/60)
                                    mih = round(mih, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Seconds(mi/sec)":
                                def convert():
                                    mimin = float(input_entry.get())
                                    misec = float(mimin*60)
                                    misec = round(misec, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{misec}")
                                heading_label.config(text = "Miles/Minutes(mi/min) to Miles/Seconds(mi/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Minutes(mi/min):")
                                input_EL.config(text = "mi/min")
                                output_OL.config(text = "mi/sec")

                        to_listbox.bind('<<ListboxSelect>>', to_box)
 
                    elif fromlistbox_get == "Miles/Seconds(mi/sec)":
                    
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get == "Centimeter/Hours(cm/h)":
                                def convert():
                                    misec = float(input_entry.get())
                                    cmh = float(misec*5.794e+8)
                                    cmh = round(cmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmh}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Centimeter/Hours(cm/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "cm/h")

                            elif tolistbox_get == "Centimeters/Minutes(cm/min)":
                                def convert():
                                    misec = float(input_entry.get())
                                    cmmin = float(misec*9.656e+6)
                                    cmmin = round(cmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmmin}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Centimeters/Minutes(cm/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Centimeters/Seconds(cm/sec)":
                                def convert():
                                    misec = float(input_entry.get())
                                    cmsec = float(misec*160934)
                                    cmsec = round(cmsec, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{cmsec}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Centimeters/Seconds(cm/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "cm/sec")

                            elif tolistbox_get == "Feet/Hours(ft/h)":
                                def convert():
                                    misec = float(input_entry.get())
                                    fth = float(misec*1.901e+7)
                                    fth = round(fth, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{fth}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Feet/Hours(ft/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "ft/h")

                            elif tolistbox_get == "Feet/Minutes(ft/min)":
                                def convert():
                                    misec = float(input_entry.get())
                                    ftmin = float(misec*316800)
                                    ftmin = round(ftmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftmin}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Feet/Minutes(ft/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "ft/min")

                            elif tolistbox_get == "Feet/Seconds(ft/sec)":
                                def convert():
                                    misec = float(input_entry.get())
                                    ftsec = float(misec*5280)
                                    ftsec = round(ftsec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ftsec}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Feet/Seconds(ft/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "ft/sec")

                            elif tolistbox_get == "Kilometers/Hours(km/h)":
                                def convert():
                                    misec = float(input_entry.get())
                                    kmh = float(misec*5793.64)
                                    kmh = round(kmh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmh}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Kilometers/Hours(km/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "km/h")

                            elif tolistbox_get == "Kilometers/Minutes(km/min)":
                                def convert():
                                    misec = float(input_entry.get())
                                    kmmin = float(misec*96.56064)
                                    kmmin = round(kmmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmmin}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Kilometers/Minutes(km/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "km/min")

                            elif tolistbox_get == "Kilometers/Seconds(km/sec)":
                                def convert():
                                    misec = float(input_entry.get())
                                    kmsec = float(misec*1.609344)
                                    kmsec = round(kmsec, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kmsec}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Kilometers/Seconds(km/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "km/sec")

                            elif tolistbox_get == "Knots(kn)":
                                def convert():
                                    misec = float(input_entry.get())
                                    kn = float(misec*3128.31)
                                    kn = round(kn, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{kn}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Knots(kn)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "kn")

                            elif tolistbox_get == "Light Speed(c)":
                                def convert():
                                    misec = float(input_entry.get())
                                    c = float(misec*5.3681937522257485824e-6)
                                    c = round(c, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Light Speed(c)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "c")

                            elif tolistbox_get == "Mach(M)":
                                def convert():
                                    misec = float(input_entry.get())
                                    M = float(misec*4.6919650145772593152)
                                    M = round(M, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{M}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Mach(M)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "M")

                            elif tolistbox_get == "Meters/Hours(m/h)":
                                def convert():
                                    misec = float(input_entry.get())
                                    mh = float(misec*5.794e+6)
                                    mh = round(mh, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mh}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Meters/Hours(m/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "m/h")

                            elif tolistbox_get == "Meters/Minutes(m/min)":
                                def convert():
                                    misec = float(input_entry.get())
                                    mmin = float(misec*96560.6)
                                    mmin = round(mmin, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mmin}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Meters/Minutes(m/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "m/min")

                            elif tolistbox_get == "Meters/Seconds(m/sec)":
                                def convert():
                                    misec = float(input_entry.get())
                                    msec = float(misec*1609.34)
                                    msec = round(msec, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{msec}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Meters/Seconds(m/sec)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "m/sec")

                            elif tolistbox_get == "Miles/Hours(mi/h)":
                                def convert():
                                    misec = float(input_entry.get())
                                    mih = float(misec/3600)
                                    mih = round(mih, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mih}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Miles/Hours(mi/h)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "mi/h")

                            elif tolistbox_get == "Miles/Minutes(mi/min)":
                                def convert():
                                    misec = float(input_entry.get())
                                    mimin = float(misec/60)
                                    mimin = round(mimin, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{mimin}")
                                heading_label.config(text = "Miles/Seconds(mi/sec) to Miles/Minutes(mi/min)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter the Miles/Seconds(mi/sec):")
                                input_EL.config(text = "mi/sec")
                                output_OL.config(text = "mi/min")

                        to_listbox.bind('<<ListboxSelect>>', to_box)


                def to_snapHighlightToMouse(event):
                    to_listbox.selection_clear(0, END)
                    to_listbox.selection_set(to_listbox.nearest(event.y))

                def to_unhighlight():
                    to_listbox.selection_clear(0, END)

                to_listbox.delete(0, END)
                for item in range(len(velocity_dict)):
                    to_listbox.insert(END, velocity_dict[item])
                to_listbox.bind('<Motion>', lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Enter>',  lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Leave>',  lambda _: to_unhighlight())

                def snapHighlightToMouse(event):
                    from_listbox.selection_clear(0, END)
        
                    from_listbox.selection_set(from_listbox.nearest(event.y))

                def unhighlight():
                    from_listbox.selection_clear(0, END)  
                
                standard_heading.config(text = "Velocity", foreground='red',background='sky blue')

                from_listbox.delete(0, END)
                for item in range(len(velocity_dict)):
                    from_listbox.insert(END, velocity_dict[item])
                from_listbox.bind('<<ListboxSelect>>', from_box)
                from_listbox.bind('<Motion>', lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Enter>',  lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Leave>',  lambda _: unhighlight())


        def snapHighlightToMouse(event):
            listbox.selection_clear(0, END)
            listbox.selection_set(listbox.nearest(event.y))

        def unhighlight():
            listbox.selection_clear(0, END)  


        root["background"] = "light green"

        main_dict = ["Distance","Mass","Velocity"]
        distance_dict = ["Kilometer(km)", "Hectometer(hm)", "Decameter(dam)", "Meter(m)", "Decimeter(dm)", "Centimeter(cm)", "Millimeter(mm)", "Miles(mi)", "Yards(yd)", "Foot(ft)", "Inches(in)", "Soot(soot)"]
        mass_dict = ["Kilograms(kg)", "Hectogram(hg)", "Decagram(dag)","Gram(g)","Decigram(dg)","Centigram(cg)", "Milligrams(mg)", "Carats(ct)", "Grains(gr)", "Ounce(oz)", "Pennyweights(dwt)", "Pounds(lb)", "Stones(st)", "Tones(t)"]
        velocity_dict = ["Centimeter/Hours(cm/h)", "Centimeters/Minutes(cm/min)", "Centimeters/Seconds(cm/sec)", "Feet/Hours(ft/h)", "Feet/Minutes(ft/min)", "Feet/Seconds(ft/sec)", "Kilometers/Hours(km/h)", "Kilometers/Minutes(km/min)", "Kilometers/Seconds(km/sec)", "Knots(kn)", "Light Speed(c)", "Mach(M)", "Meters/Hours(m/h)", "Meters/Minutes(m/min)", "Meters/Seconds(m/sec)", "Miles/Hours(mi/h)", "Miles/Minutes(mi/min)", "Miles/Seconds(mi/sec)"]


        
        standard_frame = md.Frame(root,bg = 'light green')
        standard_frame.pack()

        normal_heading_frame = md.Frame(standard_frame, bg = 'light green')
        normal_heading_frame.grid()

        listbox_frame = md.Frame(standard_frame, bg = 'light green')
        listbox_frame.grid()

        convert_frame = md.Frame(standard_frame, bg = 'light green')
        convert_frame.grid()

#*****************************************************Heading Labels.***************************************
        standard_heading_label= Label(normal_heading_frame, text = "Standard Converter",background= 'light green', foreground = "Blue", font =(("Bookman Old Style"), 30, "bold"),padding = (100,5))
        standard_heading_label.grid(row = 1, )

        standard_heading = Label(normal_heading_frame, font =("Bookman Old Style", 25, "bold"), background= 'light green',padding = (100,1))
        standard_heading.grid(row = 2)

        heading_label = Label(normal_heading_frame, font =(("Times New Roman"), 20), background= 'light green',padding = (100,5))
        heading_label.grid(row = 3,pady = 2)

#**********************************Listbox Labels*************************************
        listbox = md.Listbox(listbox_frame, width = 20, height = 10, font ="verdana 11 bold")
        listbox.grid(row = 2, column = 1)

        for item in range(len(main_dict)):
            listbox.insert(END, main_dict[item])
        listbox.bind('<<ListboxSelect>>', nextbox)
        listbox.bind('<Motion>', lambda event: snapHighlightToMouse(event))
        listbox.bind('<Enter>',  lambda event: snapHighlightToMouse(event))
        listbox.bind('<Leave>',  lambda _: unhighlight())

        symbol_label = Label(listbox_frame,background='light green', text = "→", font =("Algerian", 50, "bold"))
        symbol_label.grid(row = 2, column = 2)

        from_label = Label(listbox_frame,background='light green', text = "From",anchor='s', font = ("Times New Roman", 15, "bold"))
        from_label.grid(row = 1, column = 3,ipady = 10)

        from_listbox = md.Listbox(listbox_frame, width = 20, height = 10, font ="verdana 11")
        from_listbox.grid(row = 2, column = 3)

        scrollbar = Scrollbar(listbox_frame, orient="vertical", command=from_listbox.yview,)
        scrollbar.grid(row = 2, column = 4, sticky= N + S)

        symbol_label = Label(listbox_frame,background='light green', text = "→", font =("Algerian", 50, "bold"))
        symbol_label.grid(row = 2, column = 5)

        to_label = Label(listbox_frame,background='light green', text = "To",anchor='s', font = ("Times New Roman", 15, "bold"))
        to_label.grid(row = 1, column =6,ipady = 10)

        to_listbox = md.Listbox(listbox_frame,width = 20, height = 10, font ="verdana 11")
        to_listbox.grid(row = 2, column = 6)

        scrollbar = Scrollbar(listbox_frame, orient="vertical",command=to_listbox.yview)
        scrollbar.grid(row = 2, column = 7, sticky= N + S)

#**********************************Conversion Part of Converter.********************************************
        enter_label = md.Label(convert_frame,background='light green', font = "Verdana 16", padx = 30)
        enter_label.grid(row = 3, column = 2, pady =5)

        input_entry = md.Entry(convert_frame,justify=CENTER, width=30, font = "Verdana 16")
        input_entry.grid(row = 4, column = 2, sticky =(E, W))
        input_EL = md.Label(convert_frame,background='light green', font = "verdana 16")
        input_EL.grid(row = 4, column = 3, sticky =(E, W))

        convert_button = md.Button(convert_frame, text = "Convert To", font = ("Bookman Old Style", 18, "bold"))
        convert_button.grid(row = 5, column = 2, pady = 10, ipadx=10)
        
        output_entry = md.Entry(convert_frame,justify=CENTER, width= 30, font = "Verdana 16")
        output_entry.grid(row = 6, column = 2, sticky =(E, W))
        output_OL = md.Label(convert_frame,background='light green', font = "verdana 16")
        output_OL.grid(row = 6, column = 3, sticky =(E, W))

#**********************************************All buttons and Frame*************************************************************
        button_frame = md.Frame(standard_frame, background='light green')
        button_frame.grid(pady=25, sticky=S)
        
        
        back_button = md.Button(button_frame, bd = 0, background='light green', command = self.main_screen)
        back_button.grid(row = 1, column = 1, padx=50)
        def back_button_enter(e):
            back_button["bg"] = "grey"
            back_label.config(text = "Home", font = ("Bookman Old Style", 13))
            statusvar.set("Go to Home!")

        def back_button_leave(e):
            back_button["bg"] = 'light green'
            back_label.config(text = "")
            statusvar.set("Status is good.")
        back_label = Label(button_frame, font = ("Bookman Old Style", 13), background='light green')
        back_label.grid(row = 0, column = 1, sticky=S)
        back_button.bind("<Enter>", back_button_enter)
        back_button.bind("<Leave>", back_button_leave)
        
        image = Image.open("img/home.png")
        resize_image = image.resize((60,58), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        back_button.img_ref = img
        back_button.config(image = img, justify=LEFT)

        scientific_button = md.Button(button_frame, background = 'light green', bd = 0, padx = 20, command = self.scientific_converter)
        scientific_button.grid(row = 1, column = 2, padx = 50)
        def standard_entry(e):
            scientific_button["bg"] = "grey"
            scientific_label.config(text = "Scientific", font = ("Bookman Old Style", 13))
            statusvar.set("Scientific Converter")

        def standard_leave(e):
            scientific_button["bg"] = 'light green'
            scientific_label.config(text = "")
            statusvar.set("Status is good.")
        scientific_label = Label(button_frame, background='light green')
        scientific_label.grid(row = 0, column = 2, sticky=S)
        scientific_button.bind("<Enter>", standard_entry)
        scientific_button.bind("<Leave>", standard_leave)

        image = Image.open("img/scientific.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        scientific_button.img_ref = img
        scientific_button.config(image = img, justify=LEFT)
        
        currency_button = md.Button(button_frame, background='light green', bd = 0, padx = 20, command = self.currency_converter)
        currency_button.grid(row = 1, column = 3, padx = 50)
        def binary_entry(e):
            currency_button["bg"] = "grey"
            currency_label.config(text = "Currency", font = ("Bookman Old Style", 13))
            statusvar.set("Currency Converter")
        def binary_leave(e):
            currency_button["bg"] = 'light green'
            currency_label.config(text = "")
            statusvar.set("Status is good.")
        currency_label = Label(button_frame, background='light green')
        currency_label.grid(row = 0, column = 3, sticky=S)
        currency_button.bind("<Enter>", binary_entry)
        currency_button.bind("<Leave>", binary_leave)

        image = Image.open("img/currency.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        currency_button.img_ref = img
        currency_button.config(image = img, justify=LEFT)

        binary_button = md.Button(button_frame, background = 'light green', bd = 0, padx = 20, command = self.binary_to_decimal)
        binary_button.grid(row = 1, column = 4, padx = 50)
        def binary_entry(e):
            binary_button["bg"] = "grey"
            binary_label.config(text = "B ⇌ D", font = ("Bookman Old Style", 13))
            statusvar.set("Binary Converter")

        def binary_leave(e):
            binary_button["bg"] = 'light green'
            binary_label.config(text = "")
            statusvar.set("Status is good.")
        binary_label = Label(button_frame, background='light green')
        binary_label.grid(row = 0, column = 4, sticky=S)
        binary_button.bind("<Enter>", binary_entry)
        binary_button.bind("<Leave>", binary_leave)

        image = Image.open("img/binary.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        binary_button.img_ref = img
        binary_button.config(image = img, justify=LEFT)

        calculator_button = md.Button(button_frame, background='light green', bd = 0, padx = 20, command = open_Calculator)
        calculator_button.grid(row = 1, column = 5, padx = 50)
        def binary_entry(e):
            calculator_button["bg"] = "grey"
            calculator_label.config(text = "Calculator", font = ("Bookman Old Style", 13))
            statusvar.set("Calculator")

        def binary_leave(e):
            calculator_button["bg"] = 'light green'
            calculator_label.config(text = "")
            statusvar.set("Status is good.")
        calculator_label = Label(button_frame, background='light green')
        calculator_label.grid(row = 0, column = 5, sticky=S)
        calculator_button.bind("<Enter>", binary_entry)
        calculator_button.bind("<Leave>", binary_leave)

        image = Image.open("img/calculator.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        calculator_button.img_ref = img
        calculator_button.config(image = img, justify=LEFT)

        self.frame = standard_frame
        
#*********************************************************Standard Converter Ends here*****************************************************
#******************************************************************************************************************************************


# accel_dict = ["Centimeter/Second\u00b2(cm/sec\u00b2)", "Feet/Second\u00b2(ft/sec\u00b2)", "Gravity(g)", "Inches/Second\u00b2(in/sec\u00b2)", "Meters/Second\u00b2(m/sec\u00b2)", "Kilometers/Hour-Second(km/h-sec)", "Meters/Second\u00b2(m/sec\u00b2)", "Miles/Hours-Minute(mi/h-min)", "Miles/Hours-Second(mi/h-sec)", "Yards/Second]\u00b2(yd/sec\u00b2)"]
        # area_dict = ["Acres(ac)", "Centimeters\u00b2(cm\u00b2)", "Feet\u00b2(ft\u00b2)", "Hectares(ha)", "Inches\u00b2(in\u00b2)", "Kilometers\u00b2(km\u00b2)", "Meters\u00b2(m\u00b2)", "Miles\u00b2(mi\u00b2)", "Millimeters\u00b2(mm\u00b2)", "Yards\u00b2(yd\u00b2)"]
        # density_dict = ["Grains/Gallon(gr/gal)", "Grams/Centimeter\u00b3(gm/cm\u00b3)", "Grams/Meter\u00b3(gm/m\u00b3)", "Kilograms/Meter\u00b3(kg/m\u00b3)", "Milligrams/Meter\u00b3(mm/m\u00b3)", "Ounces/Gallon(oz/gal)", "Pounds/Foot\u00b3(lb/ft\u00b3)", "Pounds/Gallong(lb/gal)", "Pounds/Inches\u00b3(lb/in\u00b3)", "Pounds/Yards\u00b3(lb/yd\u00b3)", "Tones/Yards\u00b3(t/yd\u00b3)"]


#********************************************************Scientific Converter Stars Here***************************************************
#******************************************************************************************************************************************

    def scientific_converter(self, *args):
        self.frame.destroy()

        def nextbox(event):
        
            listbox_get = str(listbox.get(ANCHOR))

        #**************************TEMPERATURE LIST BOX STARTS HERE*************************
            if listbox_get=="Temperature":
                
                def from_box(event):
                    
                    fromlistbox_get = str(from_listbox.get(ANCHOR))
                    
                    if fromlistbox_get=="Kelvin(K)":                
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Fahrenheit(\u00b0F)":
                                def convert():
                                    K = float(input_entry.get())
                                    f = float((K - 273.15)*1.8+32)
                                    f = round(f, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{f}")
                                heading_label.config(text = "Kelvin(K) to Fahrenheit(\u00b0F)", background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Kelvin(K):")
                                input_EL.config(text = "K")                    
                                output_OL.config(text = "\u00b0F")
                            
                            elif tolistbox_get=="Celcius/Centigrade(\u00b0C)":
                                def convert():
                                    K = float(input_entry.get())
                                    c = float(K - 273.15)
                                    c= round(c, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config( text = "Kelvin(K) to Celcius/Centigrade(\u00b0C)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Kelvin(K):")
                                input_EL.config( text = "K")
                                output_OL.config( text = "\u00b0C")
                            
                            elif tolistbox_get=="Rankine(\u00b0R / \u00b0Ra)":
                                def convert():
                                    K = float(input_entry.get())
                                    Ra = float(K * 1.8)
                                    Ra= round(Ra, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ra}")
                                heading_label.config( text = "Kelvin(K) to Rankine(\u00b0R / \u00b0Ra)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Kelvin(K):")
                                input_EL.config( text = "K")
                                output_OL.config( text = "\u00b0Ra")

                            elif tolistbox_get=="Réaumur(\u00b0Ré / \u00b0Re)":
                                def convert():
                                    K = float(input_entry.get())
                                    Re = float((K - 273.15)/1.25)
                                    Re= round(Re, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Re}")
                                heading_label.config( text = "Kelvin(K) to Réaumur(\u00b0Ré / \u00b0Re)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Kelvin(K):")
                                input_EL.config( text = "K")
                                output_OL.config( text = "\u00b0Re")
                            
                            elif tolistbox_get=="Rømer(\u00b0Rø)":
                                def convert():
                                    K = float(input_entry.get())
                                    Rø = float((K / 1.904) - 135.903)
                                    Rø= round(Rø, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Rø}")
                                heading_label.config( text = "Kelvin(K) to Rømer(\u00b0Rø)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Kelvin(K):")
                                input_EL.config( text = "K")
                                output_OL.config( text = "\u00b0Rø")
                            
                            elif tolistbox_get=="Newton(\u00b0N)":
                                def convert():
                                    K = float(input_entry.get())
                                    N = float((K - 273.15) * 33/100)
                                    N= round(N, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{N}")
                                heading_label.config( text = "Kelvin(K) to Newton(\u00b0N)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Kelvin(K):")
                                input_EL.config( text = "K")
                                output_OL.config( text = "\u00b0N")
                            
                            elif tolistbox_get=="Delisle(\u00b0D)":
                                def convert():
                                    K = float(input_entry.get())
                                    D = float((373.15 - K) * 3/2)
                                    D= round(D, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{D}")
                                heading_label.config( text = "Kelvin(K) to Delisle(\u00b0D)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Kelvin(K):")
                                input_EL.config( text = "K")
                                output_OL.config( text = "\u00b0D")
                            
                            elif tolistbox_get=="Wedgwood(\u00b0W)":
                                def convert():
                                    K = float(input_entry.get())
                                    W = float( (K / 72.221) - 11.823)
                                    W= round(W, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{W}")
                                heading_label.config( text = "Kelvin(K) to Wedgwood(\u00b0W)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Kelvin(K):")
                                input_EL.config( text = "K")
                                output_OL.config( text = "\u00b0W")
                        
                        to_listbox.bind("<<ListboxSelect>>", to_box)


                    elif fromlistbox_get=="Fahrenheit(\u00b0F)":                
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Kelvin(K)":    
                                def convert():
                                    F = float(input_entry.get())
                                    K = float((F - 32) * (5/9) + 273.15)
                                    K= round(K, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{K}")
                                heading_label.config( text = "Fahrenheit(\u00b0F) to Kelvin(K) ",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Fahrenheit(\u00b0F):")
                                input_EL.config( text = "\u00b0F")
                                output_OL.config( text = "K")
                            
                            elif tolistbox_get=="Celcius/Centigrade(\u00b0C)":
                                def convert():
                                    F = float(input_entry.get())
                                    c = float((F-32) * 5/9)
                                    c= round(c, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{c}")
                                heading_label.config( text = "Fahrenheit(\u00b0F) to Celcius/Centigrade(\u00b0C)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Fahrenheit(\u00b0F):")
                                input_EL.config( text = "\u00b0F")
                                output_OL.config( text = "\u00b0C", font = "verdana 16",padx = 10)

                            elif tolistbox_get=="Rankine(\u00b0R / \u00b0Ra)":
                                def convert():
                                    F = float(input_entry.get())
                                    Ra = float(F + 459.67)
                                    Ra= round(Ra, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ra}")
                                heading_label.config( text = "Fahrenheit(\u00b0F) to Rankine(\u00b0R / \u00b0Ra)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Fahrenheit(\u00b0F):")
                                input_EL.config( text = "\u00b0F")
                                output_OL.config( text = "\u00b0Ra")
                            
                            elif tolistbox_get=="Réaumur(\u00b0Ré / \u00b0Re)":
                                def convert():
                                    F = float(input_entry.get())
                                    Re = float((F - 32) * 4/9)
                                    Re= round(Re, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Re}")
                                heading_label.config( text = "Fahrenheit(\u00b0F) to Réaumur(\u00b0Ré / \u00b0Re)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Fahrenheit(\u00b0F):")
                                input_EL.config( text = "\u00b0F")
                                output_OL.config( text = "\u00b0Ré / \u00b0Re")
                            
                            elif tolistbox_get=="Rømer(\u00b0Rø)":
                                def convert():
                                    F = float(input_entry.get())
                                    Rø = float((F - 32) * 7/24 + 7.5)
                                    Rø= round(Rø, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Rø}")
                                heading_label.config( text = "Fahrenheit(\u00b0F) to Rømer(\u00b0Rø)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Fahrenheit(\u00b0F):")
                                input_EL.config( text = "\u00b0F")
                                output_OL.config( text = "\u00b0Rø")
                            
                            elif tolistbox_get=="Newton(\u00b0N)":
                                def convert():
                                    F = float(input_entry.get())
                                    N = float((F - 32) * 11/60)
                                    N= round(N, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{N}")
                                heading_label.config( text = "Fahrenheit(\u00b0F) to Newton(\u00b0N)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Fahrenheit(\u00b0F):")
                                input_EL.config( text = "\u00b0F")
                                output_OL.config( text = "\u00b0N")
                            
                            elif tolistbox_get=="Delisle(\u00b0D)":
                                def convert():
                                    F = float(input_entry.get())
                                    D = float((212 - F) * 5/6)
                                    D= round(D, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{D}")
                                heading_label.config( text = "Fahrenheit(\u00b0F) to Delisle(\u00b0D)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Fahrenheit(\u00b0F):")
                                input_EL.config( text = "\u00b0F")
                                output_OL.config( text = "\u00b0D")

                            elif tolistbox_get=="Wedgwood(\u00b0W)":
                                def convert():
                                    F = float(input_entry.get())
                                    W = float((F / 129.999) - 8.288)
                                    W= round(W, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{W}")
                                heading_label.config( text = "Fahrenheit(\u00b0F) to Wedgwood(\u00b0W)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Fahrenheit(\u00b0F):")
                                input_EL.config( text = "\u00b0F")
                                output_OL.config( text = "\u00b0W")
                        
                        to_listbox.bind("<<ListboxSelect>>", to_box)


                    elif fromlistbox_get=="Celcius/Centigrade(\u00b0C)":                
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Kelvin(K)":    
                                def convert():
                                    C = float(input_entry.get())
                                    K = float(C + 273.15)
                                    K= round(K, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{K}")
                                heading_label.config( text = "Celcius/Centigrade(\u00b0C) to Kelvin(K)", foreground = "Black",background = "white", font =(("Times New Roman"), 20),padding = (100,5))
                                heading_label.grid(row = 1)
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Centigrade(\u00b0C):")
                                input_EL.config( text = "\u00b0C")
                                output_OL.config( text = "K")
                            
                            elif tolistbox_get=="Fahrenheit(\u00b0F)":
                                def convert():
                                    C = float(input_entry.get())
                                    F = float((C * 9/5) + 32)
                                    F= round(F, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{F}")
                                heading_label.config( text = "Celcius/Centigrade(\u00b0C) to Fahrenheit(\u00b0F)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Centigrade(\u00b0C):")
                                input_EL.config( text = "\u00b0C")
                                output_OL.config( text = "\u00b0F")

                            elif tolistbox_get=="Rankine(\u00b0R / \u00b0Ra)":
                                def convert():
                                    C = float(input_entry.get())
                                    F = float((C * 9/5) + 491.67)
                                    F= round(F, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{F}")
                                heading_label.config( text = "Celcius/Centigrade(\u00b0C) to Rankine(\u00b0R / \u00b0Ra)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Centigrade(\u00b0C):")
                                input_EL.config( text = "\u00b0C")                                
                                output_OL.config( text = "\u00b0Ra")

                            elif tolistbox_get=="Réaumur(\u00b0Ré / \u00b0Re)":
                                def convert():
                                    C = float(input_entry.get())
                                    Re = float(C * 4/5)
                                    Re= round(Re, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Re}")
                                heading_label.config( text = "Celcius/Centigrade(\u00b0C) to Réaumur(\u00b0Ré / \u00b0Re)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Centigrade(\u00b0C):")                    
                                input_EL.config( text = "\u00b0C")
                                output_OL.config( text = "\u00b0Re")
                            
                            elif tolistbox_get=="Rømer(\u00b0Rø)":
                                def convert():
                                    C = float(input_entry.get())
                                    Rø = float(C * 21/40 + 7.5)
                                    Rø= round(Rø, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Rø}")
                                heading_label.config( text = "Celcius/Centigrade(\u00b0C) to Rømer(\u00b0Rø)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Centigrade(\u00b0C):")
                                input_EL.config( text = "\u00b0C")
                                output_OL.config( text = "\u00b0Rø")
                            
                            elif tolistbox_get=="Newton(\u00b0N)":
                                def convert():
                                    C = float(input_entry.get())
                                    N = float(C * 33/100)
                                    N= round(N, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{N}")
                                heading_label.config( text = "Celcius/Centigrade(\u00b0C) to Newton(\u00b0N)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Centigrade(\u00b0C):")
                                input_EL.config( text = "\u00b0C")
                                output_OL.config( text = "\u00b0N")
                            
                            elif tolistbox_get=="Delisle(\u00b0D)":
                                def convert():
                                    C = float(input_entry.get())
                                    D = float((100 - C) * 3/2)
                                    D= round(D, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{D}")
                                heading_label.config( text = "Celcius/Centigrade(\u00b0C) to Delisle(\u00b0D)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Centigrade(\u00b0C):")
                                input_EL.config( text = "\u00b0C")
                                output_OL.config( text = "\u00b0D")
                            
                            elif tolistbox_get=="Wedgwood(\u00b0W)":
                                def convert():
                                    C = float(input_entry.get())
                                    W = float((100 - C) * 3/2)
                                    W= round(W, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{W}")
                                heading_label.config( text = "Celcius/Centigrade(\u00b0C) to Wedgwood(\u00b0W)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Centigrade(\u00b0C):")
                                input_EL.config( text = "\u00b0C")
                                output_OL.config( text = "\u00b0W")

                        to_listbox.bind("<<ListboxSelect>>", to_box)


                    elif fromlistbox_get=="Rankine(\u00b0R / \u00b0Ra)":                
                        
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Kelvin(K)":                                
                                def convert():
                                    Ra = float(input_entry.get())
                                    K = float(Ra * 5/9)
                                    K= round(K, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{K}")
                                heading_label.config( text = "Rankine(\u00b0R / \u00b0Ra) to Kelvin(K)", foreground = "Black",background = "white", font =(("Times New Roman"), 20),padding = (100,5))
                                heading_label.grid(row = 1)
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rankine(\u00b0R / \u00b0Ra):")
                                input_EL.config( text = "\u00b0Ra")
                                output_OL.config( text = "K")
                            
                            elif tolistbox_get=="Fahrenheit(\u00b0F)":
                                def convert():
                                    Ra = float(input_entry.get())
                                    F = float(Ra - 459.67)
                                    F= round(F, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{F}")
                                heading_label.config( text = "Rankine(\u00b0R / \u00b0Ra) to Fahrenheit(\u00b0F)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rankine(\u00b0R / \u00b0Ra):")
                                input_EL.config( text = "\u00b0Ra")
                                output_OL.config( text = "\u00b0F")
                            
                            elif tolistbox_get=="Celcius/Centigrade(\u00b0C)":
                                def convert():
                                    Ra = float(input_entry.get())
                                    C = float((Ra - 491.67) * 5/9)
                                    C= round(C, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{C}")
                                heading_label.config( text = "Rankine(\u00b0R / \u00b0Ra) to Celcius/Centigrade(\u00b0C)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rankine(\u00b0R / \u00b0Ra):")
                                input_EL.config( text = "\u00b0Ra")
                                output_OL.config( text = "\u00b0C")
                            
                            elif tolistbox_get=="Réaumur(\u00b0Ré / \u00b0Re)":
                                def convert():
                                    Ra = float(input_entry.get())
                                    Re = float((Ra - 491.67) * 4/9)
                                    Re= round(Re, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Re}")
                                heading_label.config( text = "Rankine(\u00b0R / \u00b0Ra) to Réaumur(\u00b0Ré / \u00b0Re)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rankine(\u00b0R / \u00b0Ra):")
                                input_EL.config( text = "\u00b0Ra")
                                output_OL.config( text = "\u00b0Re")
                            
                            elif tolistbox_get=="Rømer(\u00b0Rø)":
                                def convert():
                                    Ra = float(input_entry.get())
                                    Rø = float((Ra - 491.67) * 7/24 + 7.5)
                                    Rø= round(Rø, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Rø}")
                                heading_label.config( text = "Rankine(\u00b0R / \u00b0Ra) to Rømer(\u00b0Rø)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rankine(\u00b0R / \u00b0Ra):")
                                input_EL.config( text = "\u00b0Ra")
                                output_OL.config( text = "\u00b0Rø")
                            
                            elif tolistbox_get=="Newton(\u00b0N)":
                                def convert():
                                    Ra = float(input_entry.get())
                                    N = float((Ra - 491.67) * 11/60)
                                    N= round(N, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{N}")
                                heading_label.config( text = "Rankine(\u00b0R / \u00b0Ra) to Newton(\u00b0N)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rankine(\u00b0R / \u00b0Ra):")
                                input_EL.config( text = "\u00b0Ra")
                                output_OL.config( text = "\u00b0N")
                            
                            elif tolistbox_get=="Delisle(\u00b0D)":
                                def convert():
                                    Ra = float(input_entry.get())
                                    D = float((671.67 - Ra) * 5/6)
                                    D= round(D, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{D}")
                                heading_label.config( text = "Rankine(\u00b0R / \u00b0Ra) to Delisle(\u00b0D)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rankine(\u00b0R / \u00b0Ra):")
                                input_EL.config( text = "\u00b0Ra")
                                output_OL.config( text = "\u00b0D")
                            
                            elif tolistbox_get=="Wedgwood(\u00b0W)":
                                def convert():
                                    Ra = float(input_entry.get())
                                    W = float((Ra / 129.999) - 11.823)
                                    W= round(W, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{W}")
                                heading_label.config( text = "Rankine(\u00b0R / \u00b0Ra) to Wedgwood(\u00b0W)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rankine(\u00b0R / \u00b0Ra):")
                                input_EL.config( text = "\u00b0Ra")
                                output_OL.config( text = "\u00b0W")

                        to_listbox.bind("<<ListboxSelect>>", to_box)


                    elif fromlistbox_get=="Réaumur(\u00b0Ré / \u00b0Re)":                
                        
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Kelvin(K)":                                
                                def convert():
                                    Re = float(input_entry.get())
                                    K = float(Re * 5/4 + 273.15)
                                    K= round(K, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{K}")
                                heading_label.config( text = "Réaumur(\u00b0Ré / \u00b0Re) to Kelvin(K)", foreground = "Black",background = "white", font =(("Times New Roman"), 20),padding = (100,5))
                                heading_label.grid(row = 1)
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Réaumur(\u00b0Ré / \u00b0Re):")
                                input_EL.config( text = "\u00b0Re")
                                output_OL.config( text = "K")
                            
                            elif tolistbox_get=="Fahrenheit(\u00b0F)":
                                def convert():
                                    Re = float(input_entry.get())
                                    F = float(Re * 9/4 + 32)
                                    F= round(F, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{F}")
                                heading_label.config( text = "Réaumur(\u00b0Ré / \u00b0Re) to Fahrenheit(\u00b0F)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Réaumur(\u00b0Ré / \u00b0Re):")
                                input_EL.config( text = "\u00b0Re")
                                output_OL.config( text = "\u00b0F")

                            elif tolistbox_get=="Celcius/Centigrade(\u00b0C)":
                                def convert():
                                    Re = float(input_entry.get())
                                    C = float(Re * 5/4)
                                    C= round(C, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{C}")
                                heading_label.config( text = "Réaumur(\u00b0Ré / \u00b0Re) to Celcius/Centigrade(\u00b0C)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Réaumur(\u00b0Ré / \u00b0Re):")
                                input_EL.config( text = "\u00b0Re")
                                output_OL.config( text = "\u00b0C")
                            
                            elif tolistbox_get=="Rankine(\u00b0R / \u00b0Ra)":
                                def convert():
                                    Re = float(input_entry.get())
                                    Ra = float(Re * 9/4 + 491.67)
                                    Ra= round(Ra, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ra}")
                                heading_label.config( text = "Réaumur(\u00b0Ré / \u00b0Re) to Rankine(\u00b0R / \u00b0Ra)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Réaumur(\u00b0Ré / \u00b0Re):")
                                input_EL.config( text = "\u00b0Re")
                                output_OL.config( text = "\u00b0Ra")
                            
                            elif tolistbox_get=="Rømer(\u00b0Rø)":
                                def convert():
                                    Re = float(input_entry.get())
                                    Rø = float(Re * 21/32 + 7.5)
                                    Rø = round(Rø, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Rø}")
                                heading_label.config( text = "Réaumur(\u00b0Ré / \u00b0Re) to Rømer(\u00b0Rø)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Réaumur(\u00b0Ré / \u00b0Re):")
                                input_EL.config( text = "\u00b0Re")
                                output_OL.config( text = "\u00b0Rø")
                            
                            elif tolistbox_get=="Newton(\u00b0N)":
                                def convert():
                                    Re = float(input_entry.get())
                                    N = float(Re * 33/80)
                                    N= round(N, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{N}")
                                heading_label.config( text = "Réaumur(\u00b0Ré / \u00b0Re) to Newton(\u00b0N)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Réaumur(\u00b0Ré / \u00b0Re):")                                
                                input_EL.config( text = "\u00b0Re")
                                output_OL.config( text = "\u00b0N")
                            
                            elif tolistbox_get=="Delisle(\u00b0D)":
                                def convert():
                                    Re = float(input_entry.get())
                                    D = float((80 - Re) * 15/8)
                                    D= round(D, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{D}")
                                heading_label.config( text = "Réaumur(\u00b0Ré / \u00b0Re) to Delisle(\u00b0D)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Réaumur(\u00b0Ré / \u00b0Re):")
                                input_EL.config( text = "\u00b0Re")
                                output_OL.config( text = "\u00b0D")
                            
                            elif tolistbox_get=="Wedgwood(\u00b0W)":
                                def convert():
                                    Re = float(input_entry.get())
                                    W = float((Re / 57.777) - 8.041)
                                    W= round(W, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{W}")
                                heading_label.config( text = "Réaumur(\u00b0Ré / \u00b0Re) to Wedgwood(\u00b0W)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Réaumur(\u00b0Ré / \u00b0Re):")
                                input_EL.config( text = "\u00b0Re")
                                output_OL.config( text = "\u00b0W")
                        
                        to_listbox.bind("<<ListboxSelect>>", to_box)


                    elif fromlistbox_get=="Rømer(\u00b0Rø)":                
                        
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Kelvin(K)":                                
                                def convert():
                                    Rø = float(input_entry.get())
                                    K = float((Rø - 7.5) * 40/21 + 273.15)
                                    K = round(K, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{K}")
                                heading_label.config( text = "Rømer(\u00b0Rø) to Kelvin(K)", foreground = "Black",background = "white", font =(("Times New Roman"), 20),padding = (100,5))
                                heading_label.grid(row = 1)
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rømer(\u00b0Rø):")
                                input_EL.config( text = "\u00b0Rø")
                                output_OL.config( text = "K")
                            
                            elif tolistbox_get=="Fahrenheit(\u00b0F)":
                                def convert():
                                    Rø = float(input_entry.get())
                                    F = float((Rø - 7.5) * 24/7 + 32)
                                    F = round(F, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{F}")
                                heading_label.config( text = "Rømer(\u00b0Rø) to Fahrenheit(\u00b0F)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rømer(\u00b0Rø):")
                                input_EL.config( text = "\u00b0Rø")
                                output_OL.config( text = "\u00b0F")
                            
                            elif tolistbox_get=="Celcius/Centigrade(\u00b0C)":
                                def convert():
                                    Rø = float(input_entry.get())
                                    C = float((Rø - 7.5) * 40/21)
                                    C = round(C, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{C}")
                                heading_label.config( text = "Rømer(\u00b0Rø) to Celcius/Centigrade(\u00b0C)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rømer(\u00b0Rø):")
                                input_EL.config( text = "\u00b0Rø")
                                output_OL.config( text = "\u00b0C")
                            
                            elif tolistbox_get=="Rankine(\u00b0R / \u00b0Ra)":
                                def convert():
                                    Rø = float(input_entry.get())
                                    Ra = float((Rø - 7.5) * 24/7 + 491.67)
                                    Ra = round(Ra, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ra}")
                                heading_label.config( text = "Rømer(\u00b0Rø) to Rankine(\u00b0R / \u00b0Ra)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rømer(\u00b0Rø):")                                
                                input_EL.config( text = "\u00b0Rø")
                                output_OL.config( text = "\u00b0Ra")
                            
                            elif tolistbox_get=="Réaumur(\u00b0Ré / \u00b0Re)":
                                def convert():
                                    Rø = float(input_entry.get())
                                    Re = float((Rø - 7.5) * 32/21)
                                    Re = round(Re, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Re}")
                                heading_label.config( text = "Rømer(\u00b0Rø) to Réaumur(\u00b0Ré / \u00b0Re)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rømer(\u00b0Rø):")
                                input_EL.config( text = "\u00b0Rø")
                                output_OL.config( text = "\u00b0Re")
                            
                            elif tolistbox_get=="Newton(\u00b0N)":
                                def convert():
                                    Rø = float(input_entry.get())
                                    N = float((Rø - 7.5) * 22/35)
                                    N = round(N, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{N}")
                                heading_label.config( text = "Rømer(\u00b0Rø) to Newton(\u00b0N)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rømer(\u00b0Rø):")
                                input_EL.config( text = "\u00b0Rø")
                                output_OL.config( text = "\u00b0N")
                            
                            elif tolistbox_get=="Delisle(\u00b0D)":
                                def convert():
                                    Rø = float(input_entry.get())
                                    D = float((60 - Rø) * 20/7)
                                    D = round(D, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{D}")
                                heading_label.config( text = "Rømer(\u00b0Rø) to Delisle(\u00b0D)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rømer(\u00b0Rø):")
                                input_EL.config( text = "\u00b0Rø")
                                output_OL.config( text = "\u00b0D")
                            
                            elif tolistbox_get=="Wedgwood(\u00b0W)":
                                def convert():
                                    Rø = float(input_entry.get())
                                    W = float((Rø / 37.916) - 8.239)
                                    W = round(W, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{W}")
                                heading_label.config( text = "Rømer(\u00b0Rø) to Wedgwood(\u00b0W)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Rømer(\u00b0Rø):")
                                input_EL.config( text = "\u00b0Rø")
                                output_OL.config( text = "\u00b0W")
                        
                        to_listbox.bind("<<ListboxSelect>>", to_box)


                    elif fromlistbox_get=="Newton(\u00b0N)":                
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Kelvin(K)":    
                                def convert():
                                    N = float(input_entry.get())
                                    K = float(N * 100/33 + 273.15)
                                    K = round(K, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{K}")
                                heading_label.config( text = "Newton(\u00b0N) to Kelvin(K)", foreground = "Black",background = "white", font =(("Times New Roman"), 20),padding = (100,5))
                                heading_label.grid(row = 1)
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Newton(\u00b0N):")
                                input_EL.config( text = "\u00b0N")
                                output_OL.config( text = "K")
                            
                            elif tolistbox_get=="Fahrenheit(\u00b0F)":
                                def convert():
                                    N = float(input_entry.get())
                                    F = float(N * 60/11 + 32)
                                    F = round(F, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{F}")
                                heading_label.config( text = "Newton(\u00b0N) to Fahrenheit(\u00b0F)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Newton(\u00b0N):")
                                input_EL.config( text = "\u00b0N")
                                output_OL.config( text = "\u00b0F")
                            
                            elif tolistbox_get=="Celcius/Centigrade(\u00b0C)":
                                def convert():
                                    N = float(input_entry.get())
                                    C = float(N * 100/33)
                                    C = round(C, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{C}")
                                heading_label.config( text = "Newton(\u00b0N) to Celcius/Centigrade(\u00b0C)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Newton(\u00b0N):")
                                input_EL.config( text = "\u00b0N")
                                output_OL.config( text = "\u00b0C")
                            
                            elif tolistbox_get=="Rankine(\u00b0R / \u00b0Ra)":
                                def convert():
                                    N = float(input_entry.get())
                                    Ra = float(N * 60/11 + 491.67)
                                    Ra = round(Ra, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ra}")
                                heading_label.config( text = "Newton(\u00b0N) to Rankine(\u00b0R / \u00b0Ra)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Newton(\u00b0N):")
                                input_EL.config( text = "\u00b0N")
                                output_OL.config( text = "\u00b0Ra")
                            
                            elif tolistbox_get=="Réaumur(\u00b0Ré / \u00b0Re)":
                                def convert():
                                    N = float(input_entry.get())
                                    Re = float(N *  80/33)
                                    Re = round(Re, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Re}")
                                heading_label.config( text = "Newton(\u00b0N) to Réaumur(\u00b0Ré / \u00b0Re)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Newton(\u00b0N):")
                                input_EL.config( text = "\u00b0N")
                                output_OL.config( text = "\u00b0Re")
                            
                            elif tolistbox_get=="Rømer(\u00b0Rø)":
                                def convert():
                                    N = float(input_entry.get())
                                    Rø = float(N * 35/22 + 7.5)
                                    Rø = round(Rø, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Rø}")
                                heading_label.config( text = "Newton(\u00b0N) to Rømer(\u00b0Rø)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Newton(\u00b0N):")
                                input_EL.config( text = "\u00b0N")
                                output_OL.config( text = "\u00b0Rø")

                            elif tolistbox_get=="Delisle(\u00b0D)":
                                def convert():
                                    N = float(input_entry.get())
                                    D = float((33 - N) * 50/11)
                                    D = round(D, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{D}")
                                heading_label.config( text = "Newton(\u00b0N) to Delisle(\u00b0D)",background = "white")
                                convert_button.config(command = convert)                    
                                enter_label.config( text = "Enter Newton(\u00b0N):")
                                input_EL.config( text = "\u00b0N")
                                output_OL.config( text = "\u00b0D")
                            
                            elif tolistbox_get=="Wedgwood(\u00b0W)":
                                def convert():
                                    N = float(input_entry.get())
                                    W = float((N / 23.833) - 8.041)
                                    W = round(W, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{W}")
                                heading_label.config( text = "Newton(\u00b0N) to Wedgwood(\u00b0W)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Newton(\u00b0N):")
                                input_EL.config( text = "\u00b0N")
                                output_OL.config( text = "\u00b0W")

                        to_listbox.bind("<<ListboxSelect>>", to_box)


                    elif fromlistbox_get=="Delisle(\u00b0D)":                
                        
                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Kelvin(K)":                                
                                def convert():
                                    D = float(input_entry.get())
                                    K = float(373.15 - D * 2/3)
                                    K = round(K, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{K}")
                                heading_label.config( text = "Delisle(\u00b0D) to Kelvin(K)", foreground = "Black",background = "white", font =(("Times New Roman"), 20),padding = (100,5))
                                heading_label.grid(row = 1)
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Delisle(\u00b0D):")
                                input_EL.config( text = "\u00b0D")
                                output_OL.config( text = "K")
                            
                            elif tolistbox_get=="Fahrenheit(\u00b0F)":
                                def convert():
                                    D = float(input_entry.get())
                                    F = float(212 - D * 6/5)
                                    F = round(F, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{F}")
                                heading_label.config( text = "Delisle(\u00b0D) to Fahrenheit(\u00b0F)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Delisle(\u00b0D):")
                                input_EL.config( text = "\u00b0D")
                                output_OL.config( text = "\u00b0F")
                            
                            elif tolistbox_get=="Celcius/Centigrade(\u00b0C)":
                                def convert():
                                    D = float(input_entry.get())
                                    C = float(100 - D * 2/3)
                                    C = round(C, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{C}")
                                heading_label.config( text = "Delisle(\u00b0D) to Celcius/Centigrade(\u00b0C)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Delisle(\u00b0D):")
                                input_EL.config( text = "\u00b0D")
                                output_OL.config( text = "\u00b0C")
                            
                            elif tolistbox_get=="Rankine(\u00b0R / \u00b0Ra)":
                                def convert():
                                    D = float(input_entry.get())
                                    Ra = float(671.67 - D * 6/5)
                                    Ra = round(Ra, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ra}")
                                heading_label.config( text = "Delisle(\u00b0D) to Rankine(\u00b0R / \u00b0Ra)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Delisle(\u00b0D):")
                                input_EL.config( text = "\u00b0D")
                                output_OL.config( text = "\u00b0Ra")
                            
                            elif tolistbox_get=="Réaumur(\u00b0Ré / \u00b0Re)":
                                def convert():
                                    D = float(input_entry.get())
                                    Re = float(80 - D * 8/15)
                                    Re = round(Re, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Re}")
                                heading_label.config( text = "Delisle(\u00b0D) to Réaumur(\u00b0Ré / \u00b0Re)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Delisle(\u00b0D):")
                                input_EL.config( text = "\u00b0D")
                                output_OL.config( text = "\u00b0Re")
                            
                            elif tolistbox_get=="Rømer(\u00b0Rø)":
                                def convert():
                                    D = float(input_entry.get())
                                    Rø = float(60 - D * 7/20)
                                    Rø = round(Rø, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Rø}")
                                heading_label.config( text = "Delisle(\u00b0D) to Rømer(\u00b0Rø)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Delisle(\u00b0D):")
                                input_EL.config( text = "\u00b0D")
                                output_OL.config( text = "\u00b0Rø")
                            
                            elif tolistbox_get=="Newton(\u00b0N)":
                                def convert():
                                    D = float(input_entry.get())
                                    N = float(33 - D * 11/50)
                                    N = round(N, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{N}")
                                heading_label.config( text = "Delisle(\u00b0D) to Newton(\u00b0N)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Delisle(\u00b0D):")
                                input_EL.config( text = "\u00b0D")
                                output_OL.config( text = "\u00b0N")
                            
                            elif tolistbox_get=="Wedgwood(\u00b0W)":
                                def convert():
                                    D = float(input_entry.get())
                                    W = float(((100 - D * 2/3) / 72.221) - 8.041)
                                    W = round(W, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{W}")
                                heading_label.config( text = "Delisle(\u00b0D) to Wedgwood(\u00b0W)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Delisle(\u00b0D):")
                                input_EL.config( text = "\u00b0D")
                                output_OL.config( text = "\u00b0W")
                        
                        to_listbox.bind("<<ListboxSelect>>", to_box)


                    elif fromlistbox_get=="Wedgwood(\u00b0W)":                
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Kelvin(K)":    
                                def convert():
                                    W = float(input_entry.get())
                                    K = float((72.221 * W) + 853.95)
                                    K = round(K, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{K}")
                                heading_label.config( text = "Wedgwood(\u00b0W) to Kelvin(K)", foreground = "Black",background = "white", font =(("Times New Roman"), 20),padding = (100,5))
                                heading_label.grid(row = 1)
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Wedgwood(\u00b0W):")
                                input_EL.config( text = "\u00b0W")
                                output_OL.config( text = "K")

                            elif tolistbox_get=="Fahrenheit(\u00b0F)":
                                def convert():
                                    W = float(input_entry.get())
                                    F = float((129.999 * W) + 1077.44)
                                    F = round(F, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{F}")
                                heading_label.config( text = "Wedgwood(\u00b0W) to Fahrenheit(\u00b0F)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Wedgwood(\u00b0W):")
                                input_EL.config( text = "\u00b0W")
                                output_OL.config( text = "\u00b0F")
                            
                            elif tolistbox_get=="Celcius/Centigrade(\u00b0C)":
                                def convert():
                                    W = float(input_entry.get())
                                    C = float((72.221 * W) + 580.8)
                                    C = round(C, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{C}")
                                heading_label.config( text = "Wedgwood(\u00b0W) to Celcius/Centigrade(\u00b0C)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Wedgwood(\u00b0W):")
                                input_EL.config( text = "\u00b0W")
                                output_OL.config( text = "\u00b0C")
                            
                            elif tolistbox_get=="Rankine(\u00b0R / \u00b0Ra)":
                                def convert():
                                    W = float(input_entry.get())
                                    Ra = float((129.999 * W) + 1537.11)
                                    Ra = round(Ra, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ra}")
                                heading_label.config( text = "Wedgwood(\u00b0W) to Rankine(\u00b0R / \u00b0Ra)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Wedgwood(\u00b0W):")
                                input_EL.config( text = "\u00b0W")
                                output_OL.config( text = "\u00b0Ra")
                            
                            elif tolistbox_get=="Réaumur(\u00b0Ré / \u00b0Re)":
                                def convert():
                                    W = float(input_entry.get())
                                    Re = float((57.777 * W) + 464.64)
                                    Re = round(Re, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Re}")
                                heading_label.config( text = "Wedgwood(\u00b0W) to Réaumur(\u00b0Ré / \u00b0Re)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Wedgwood(\u00b0W):")
                                input_EL.config( text = "\u00b0W")
                                output_OL.config( text = "\u00b0Re")
                            
                            elif tolistbox_get=="Rømer(\u00b0Rø)":
                                def convert():
                                    W = float(input_entry.get())
                                    Rø = float((37.916 * W) + 312.42)
                                    Rø = round(Rø, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Rø}")
                                heading_label.config( text = "Wedgwood(\u00b0W) to Rømer(\u00b0Rø)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Wedgwood(\u00b0W):")                                
                                input_EL.config( text = "\u00b0W")
                                output_OL.config( text = "\u00b0Rø")
                            
                            elif tolistbox_get=="Newton(\u00b0N)":
                                def convert():
                                    W = float(input_entry.get())
                                    N = float((23.833 * W) + 191.664)
                                    N = round(N, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{N}")
                                heading_label.config( text = "Wedgwood(\u00b0W) to Newton(\u00b0N)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Wedgwood(\u00b0W):")                                
                                input_EL.config( text = "\u00b0W")
                                output_OL.config( text = "\u00b0N")
                            
                            elif tolistbox_get=="Delisle(\u00b0D)":
                                def convert():
                                    W = float(input_entry.get())
                                    D = float((100 - (72.221 * W) + 580.8) * 3/2)
                                    D = round(D, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{D}")
                                heading_label.config( text = "Wedgwood(\u00b0W) to Delisle(\u00b0D)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Wedgwood(\u00b0W):")
                                input_EL.config( text = "\u00b0W")
                                output_OL.config( text = "\u00b0D")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                def to_snapHighlightToMouse(event):
                    to_listbox.selection_clear(0, END)
                    to_listbox.selection_set(to_listbox.nearest(event.y))

                def to_unhighlight():
                    to_listbox.selection_clear(0, END)    

                to_listbox.delete(0,END)
                for item in range(len(temp_dict)):
                    to_listbox.insert(END, temp_dict[item])

                to_listbox.bind('<Motion>', lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Enter>',  lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Leave>',  lambda _: to_unhighlight())

                def snapHighlightToMouse(event):
                    from_listbox.selection_clear(0, END)
                    from_listbox.selection_set(from_listbox.nearest(event.y))

                def unhighlight():
                    from_listbox.selection_clear(0, END)    

                scientific_heading.config(text = "Temperature", foreground = "red", background = "sky blue")

                from_listbox.delete(0,END)
                for item in range(len(temp_dict)):
                    from_listbox.insert(END, temp_dict[item])
                from_listbox.bind('<<ListboxSelect>>', from_box)
                from_listbox.bind('<Motion>', lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Enter>',  lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Leave>',  lambda _: unhighlight())
        #**************************TEMPERATURE LIST BOX ENDS HERE*************************

        #**************************PRESSURE LIST BOX STARTS HERE*************************
            elif listbox_get=="Pressure":
                
                def from_box(event):
                    
                    fromlistbox_get = str(from_listbox.get(ANCHOR))
                    
                    if fromlistbox_get=="Pascals(Pa)":                
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Standard Atmosphere(atm)":    
                                def convert():
                                    Pa = float(input_entry.get())
                                    atm = float(Pa/101325)
                                    atm = round(atm, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{atm}")
                                heading_label.config( text = "Pascals(Pa) to Standard Atmosphere(atm)", background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pascals(Pa):")
                                input_EL.config( text = "Pa")
                                output_OL.config( text = "atm")
                            
                            elif tolistbox_get=="Torr(Torr)":
                                def convert():
                                    Pa = float(input_entry.get())
                                    torr = float(Pa / 133)
                                    torr = round(torr, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{torr}")
                                heading_label.config( text = "Pasclas(Pa) to Torr(Torr)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pascals(Pa):")
                                input_EL.config( text = "Pa")
                                output_OL.config( text = "torr")
                            
                            elif tolistbox_get=="Bar(bar)":
                                def convert():
                                    Pa = float(input_entry.get())
                                    bar = float(Pa/(100000))
                                    bar = round(bar, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bar}")
                                heading_label.config( text = "Pascals(Pa) to Bar(bar)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pascals(Pa):")
                                input_EL.config( text = "Pa")
                                output_OL.config( text = "bar")

                            elif tolistbox_get=="Pounds per Square Inch (psi or lb/in\u00b2)":
                                def convert():
                                    Pa = float(input_entry.get())
                                    psi = float(Pa/6895)
                                    psi = round(psi, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{psi}")
                                heading_label.config( text = "Pascals(Pa) to PSI(psi or lb/in\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pascals(Pa):")
                                input_EL.config( text = "Pa")
                                output_OL.config( text = "psi")
                            
                            elif tolistbox_get=="Technical Atmosphere (at or kgf/cm\u00b2)":
                                def convert():
                                    Pa = float(input_entry.get())
                                    at = float(Pa/98067)
                                    at = round(at, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{at}")
                                heading_label.config( text = "Pascals(Pa) to Technical Atmosphere (at or kgf/cm\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pascals(Pa):")
                                input_EL.config( text = "Pa")
                                output_OL.config( text = "at")
                            
                            elif tolistbox_get=="Barye(Ba)":
                                def convert():
                                    Pa = float(input_entry.get())
                                    Ba = float(Pa*10)
                                    Ba = round(Ba, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ba}")
                                heading_label.config( text = "Pascals(Pa) to Barye(Ba)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pascals(Pa):")
                                input_EL.config( text = "Pa")
                                output_OL.config( text = "Ba")
                            
                            elif tolistbox_get=="Pièze(pz)":
                                def convert():
                                    Pa = float(input_entry.get())
                                    pz = float(Pa/1000)
                                    pz = round(pz, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{pz}")
                                heading_label.config( text = "Pascals(Pa) to Pièze(pz)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pascals(Pa):")
                                input_EL.config( text = "Pa")
                                output_OL.config( text = "pz")
                            
                            elif tolistbox_get=="mm of Mercury(mmHg)":
                                def convert():
                                    Pa = float(input_entry.get())
                                    Hg = float(Pa/133)
                                    Hg = round(Hg, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{W}")
                                heading_label.config( text = "Pascals(Pa) to mm of Mercury(mmHg)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pascals(Pa):")
                                input_EL.config( text = "Pa")
                                output_OL.config( text = "mmHg")

                        to_listbox.bind("<<ListboxSelect>>", to_box)


                    elif fromlistbox_get=="Standard Atmosphere(atm)":                

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Pascals(Pa)":                                
                                def convert():
                                    atm = float(input_entry.get())
                                    Pa = float(atm*101325)
                                    Pa = round(Pa, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Pa}")
                                heading_label.config( text = "Standard Atmosphere(atm) to Pascals(Pa)", background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Standard Atmosphere(atm):")
                                input_EL.config( text = "atm")
                                output_OL.config( text = "Pa")
                            
                            elif tolistbox_get=="Torr(Torr)":
                                def convert():
                                    atm= float(input_entry.get())
                                    torr = float(atm*760)
                                    torr = round(torr, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{torr}")
                                heading_label.config( text = "Standard Atmosphere(atm) to Torr(Torr)",background = "white")
                                convert_button.config(command = convert)                    
                                enter_label.config(text = "Enter Standard Atmosphere(atm):")
                                input_EL.config( text = "atm")
                                output_OL.config( text = "torr")
                            
                            elif tolistbox_get=="Bar(bar)":
                                def convert():
                                    atm= float(input_entry.get())
                                    bar = float(atm*1.01325)
                                    bar = round(bar, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bar}")
                                heading_label.config( text = "Standard Atmosphere(atm) to Bar(bar)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Standard Atmosphere(atm):")
                                input_EL.config( text = "atm")
                                output_OL.config(text = "bar")

                            elif tolistbox_get=="Pounds per Square Inch (psi or lb/in\u00b2)":
                                def convert():
                                    atm= float(input_entry.get())
                                    psi = float(atm*14.695948775872305152)
                                    psi = round(psi, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{psi}")
                                heading_label.config( text = "Standard Atmosphere(atm) to PSI(psi or lb/in\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Standard Atmosphere(atm):")
                                input_EL.config( text = "atm")
                                output_OL.config( text = "psi")

                            elif tolistbox_get=="Technical Atmosphere (at or kgf/cm\u00b2)":
                                def convert():
                                    atm= float(input_entry.get())
                                    at = float(atm*1.0332274528019851264)
                                    at = round(at, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{at}")
                                heading_label.config( text = "Standard Atmosphere(atm) to Technical Atmosphere (at or kgf/cm\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Standard Atmosphere(atm):")
                                input_EL.config( text = "atm")
                                output_OL.config( text = "at")

                            elif tolistbox_get=="Barye(Ba)":
                                def convert():
                                    atm= float(input_entry.get())
                                    Ba = float(atm*1013250)
                                    Ba = round(Ba, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ba}")
                                heading_label.config( text = "Standard Atmosphere(atm) to Barye(Ba)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Standard Atmosphere(atm):")
                                input_EL.config( text = "atm")
                                output_OL.config( text = "Ba")

                            elif tolistbox_get=="Pièze(pz)":
                                def convert():
                                    atm= float(input_entry.get())
                                    pz = float(atm*101.325)
                                    pz = round(pz, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{pz}")
                                heading_label.config( text = "Standard Atmosphere(atm) to Pièze(pz)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Standard Atmosphere(atm):")
                                input_EL.config( text = "atm")
                                output_OL.config( text = "pz")

                            elif tolistbox_get=="mm of Mercury(mmHg)":
                                def convert():
                                    atm= float(input_entry.get())
                                    Hg = float(atm*760)
                                    Hg = round(Hg, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hg}")
                                heading_label.config( text = "Standard Atmosphere(atm) to mm of Mercury(mmHg)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Standard Atmosphere(atm):")
                                input_EL.config( text = "atm")
                                output_OL.config( text = "mmHg")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Torr(Torr)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Pascals(Pa)":
                                def convert():
                                    torr = float(input_entry.get())
                                    Pa = float(torr*133.3223684)
                                    Pa = round(Pa, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Pa}")
                                heading_label.config( text = "Torr(Torr) to Pascals(Pa)", background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Torr(Torr):")
                                input_EL.config( text = "Torr")
                                output_OL.config( text = "Pa")
                            
                            elif tolistbox_get=="Standard Atmosphere(atm)":
                                def convert():
                                    Torr = float(input_entry.get())
                                    torr = float(Torr/760)
                                    torr = round(torr, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{torr}")
                                heading_label.config( text = "Torr(Torr) to Standard Atmosphere(atm)",background = "white")
                                convert_button.config(command = convert)                    
                                enter_label.config(text = "Enter Torr(Torr):")
                                input_EL.config( text = "Torr")
                                output_OL.config( text = "atm")
                            
                            elif tolistbox_get=="Bar(bar)":
                                def convert():
                                    Torr = float(input_entry.get())
                                    bar = float(Torr/750.06168282261028864)
                                    bar = round(bar, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bar}")
                                heading_label.config( text = "Torr(Torr) to Bar(bar)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Torr(Torr):")
                                input_EL.config( text = "Torr")
                                output_OL.config(text = "bar")

                            elif tolistbox_get=="Pounds per Square Inch (psi or lb/in\u00b2)":
                                def convert():
                                    Torr = float(input_entry.get())
                                    psi = float(Torr/51.715)
                                    psi = round(psi, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{psi}")
                                heading_label.config( text = "Torr(Torr) to PSI(psi or lb/in\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Torr(Torr):")
                                input_EL.config( text = "Torr")
                                output_OL.config( text = "psi")

                            elif tolistbox_get=="Technical Atmosphere (at or kgf/cm\u00b2)":
                                def convert():
                                    Torr = float(input_entry.get())
                                    at = float(Torr/736)
                                    at = round(at, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{at}")
                                heading_label.config( text = "Torr(Torr) to Technical Atmosphere (at or kgf/cm\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Torr(Torr):")
                                input_EL.config( text = "Torr")
                                output_OL.config( text = "at")

                            elif tolistbox_get=="Barye(Ba)":
                                def convert():
                                    Torr = float(input_entry.get())
                                    Ba = float(Torr*1333.22)
                                    Ba = round(Ba, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ba}")
                                heading_label.config( text = "Torr(Torr) to Barye(Ba)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Torr(Torr):")
                                input_EL.config( text = "Torr")
                                output_OL.config( text = "Ba")

                            elif tolistbox_get=="Pièze(pz)":
                                def convert():
                                    Torr = float(input_entry.get())
                                    pz = float(Torr*0.1333223684)
                                    pz = round(pz, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{pz}")
                                heading_label.config( text = "Torr(Torr) to Pièze(pz)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Torr(Torr):")
                                input_EL.config( text = "Torr")
                                output_OL.config( text = "pz")

                            elif tolistbox_get=="mm of Mercury(mmHg)":
                                def convert():
                                    Torr = float(input_entry.get())
                                    Hg = float(Torr/1)
                                    Hg = round(Hg, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hg}")
                                heading_label.config( text = "Torr(Torr) to mm of Mercury(mmHg)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Torr(Torr):")
                                input_EL.config( text = "Torr")
                                output_OL.config( text = "mmHg")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Bar(bar)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Pascals(Pa)":
                                def convert():
                                    bar = float(input_entry.get())
                                    Pa = float(bar*100000)
                                    Pa = round(Pa, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Pa}")
                                heading_label.config( text = "Bar(bar) to Pascals(Pa)", background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Bar(bar):")
                                input_EL.config( text = "bar")
                                output_OL.config( text = "Pa")
                            
                            elif tolistbox_get=="Standard Atmosphere(atm)":
                                def convert():
                                    bar = float(input_entry.get())
                                    torr = float(bar/1.01325)
                                    torr = round(torr, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{torr}")
                                heading_label.config( text = "Bar(bar) to Standard Atmosphere(atm)",background = "white")
                                convert_button.config(command = convert)                    
                                enter_label.config(text = "Enter Bar(bar):")
                                input_EL.config( text = "bar")
                                output_OL.config( text = "atm")
                            
                            elif tolistbox_get=="Torr(Torr)":
                                def convert():
                                    bar = float(input_entry.get())
                                    Torr = float(bar*750.06168282261028864)
                                    Torr = round(Torr, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Torr}")
                                heading_label.config( text = "Bar(bar) to Torr(Torr)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Bar(bar):")
                                input_EL.config( text = "bar")
                                output_OL.config(text = "Torr")

                            elif tolistbox_get=="Pounds per Square Inch (psi or lb/in\u00b2)":
                                def convert():
                                    bar = float(input_entry.get())
                                    psi = float(bar*14.503773773375084544)
                                    psi = round(psi, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{psi}")
                                heading_label.config( text = "Bar(bar) to PSI(psi or lb/in\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Bar(bar):")
                                input_EL.config( text = "bar")
                                output_OL.config( text = "psi")

                            elif tolistbox_get=="Technical Atmosphere (at or kgf/cm\u00b2)":
                                def convert():
                                    bar = float(input_entry.get())
                                    at = float(bar*1.0197162129779281920)
                                    at = round(at, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{at}")
                                heading_label.config( text = "Bar(bar) to Technical Atmosphere (at or kgf/cm\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Bar(bar):")
                                input_EL.config( text = "bar")
                                output_OL.config( text = "at")

                            elif tolistbox_get=="Barye(Ba)":
                                def convert():
                                    bar = float(input_entry.get())
                                    Ba = float(bar*1e+6)
                                    Ba = round(Ba, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ba}")
                                heading_label.config( text = "Bar(bar) to Barye(Ba)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Bar(bar):")
                                input_EL.config( text = "bar")
                                output_OL.config( text = "Ba")

                            elif tolistbox_get=="Pièze(pz)":
                                def convert():
                                    bar = float(input_entry.get())
                                    pz = float(bar*100)
                                    pz = round(pz, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{pz}")
                                heading_label.config( text = "Bar(bar) to Pièze(pz)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Bar(bar):")
                                input_EL.config( text = "bar")
                                output_OL.config( text = "pz")

                            elif tolistbox_get=="mm of Mercury(mmHg)":
                                def convert():
                                    bar = float(input_entry.get())
                                    Hg = float(bar*750.06157584565633024)
                                    Hg = round(Hg, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hg}")
                                heading_label.config( text = "Bar(bar) to mm of Mercury(mmHg)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Bar(bar):")
                                input_EL.config( text = "bar")
                                output_OL.config( text = "mmHg")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Pounds per Square Inch (psi or lb/in\u00b2)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Pascals(Pa)":
                                def convert():
                                    psi = float(input_entry.get())
                                    Pa = float(psi*6894.76)
                                    Pa = round(Pa, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Pa}")
                                heading_label.config( text = "Pounds per Square Inch (psi or lb/in\u00b2) to Pascals(Pa)", background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pounds per Square Inch (psi or lb/in\u00b2):")
                                input_EL.config( text = "psi")
                                output_OL.config( text = "Pa")
                            
                            elif tolistbox_get=="Standard Atmosphere(atm)":
                                def convert():
                                    psi = float(input_entry.get())
                                    torr = float(psi*0.68045963908216135680)
                                    torr = round(torr, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{torr}")
                                heading_label.config( text = "Pounds per Square Inch (psi or lb/in\u00b2) to Standard Atmosphere(atm)",background = "white")
                                convert_button.config(command = convert)                    
                                enter_label.config(text = "Enter Pounds per Square Inch (psi or lb/in\u00b2):")
                                input_EL.config( text = "psi")
                                output_OL.config( text = "atm")
                            
                            elif tolistbox_get=="Torr(Torr)":
                                def convert():
                                    psi = float(input_entry.get())
                                    Torr = float(psi*51.714932578410446848)
                                    Torr = round(Torr, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Torr}")
                                heading_label.config( text = "Pounds per Square Inch (psi or lb/in\u00b2) to Torr(Torr)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pounds per Square Inch (psi or lb/in\u00b2):")
                                input_EL.config( text = "psi")
                                output_OL.config(text = "Torr")

                            elif tolistbox_get=="Bar(bar)":
                                def convert():
                                    psi = float(input_entry.get())
                                    bar = float(psi*0.06894757293)
                                    bar = round(bar, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bar}")
                                heading_label.config( text = "Pounds per Square Inch (psi or lb/in\u00b2) to Bar(bar)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Pounds per Square Inch (psi or lb/in\u00b2):")
                                input_EL.config( text = "psi")
                                output_OL.config( text = "bar")

                            elif tolistbox_get=="Technical Atmosphere (at or kgf/cm\u00b2)":
                                def convert():
                                    psi = float(input_entry.get())
                                    at = float(psi*0.070306957962199121920)
                                    at = round(at, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{at}")
                                heading_label.config( text = "Pounds per Square Inch (psi or lb/in\u00b2) to Technical Atmosphere (at or kgf/cm\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pounds per Square Inch (psi or lb/in\u00b2):")
                                input_EL.config( text = "psi")
                                output_OL.config( text = "at")

                            elif tolistbox_get=="Barye(Ba)":
                                def convert():
                                    psi = float(input_entry.get())
                                    Ba = float(psi*68947.6)
                                    Ba = round(Ba, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ba}")
                                heading_label.config( text = "Pounds per Square Inch (psi or lb/in\u00b2) to Barye(Ba)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pounds per Square Inch (psi or lb/in\u00b2):")
                                input_EL.config( text = "psi")
                                output_OL.config( text = "Ba")

                            elif tolistbox_get=="Pièze(pz)":
                                def convert():
                                    psi = float(input_entry.get())
                                    pz = float(psi*6.894757293)
                                    pz = round(pz, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{pz}")
                                heading_label.config( text = "Pounds per Square Inch (psi or lb/in\u00b2) to Pièze(pz)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Pounds per Square Inch (psi or lb/in\u00b2):")
                                input_EL.config( text = "psi")
                                output_OL.config( text = "pz")

                            elif tolistbox_get=="mm of Mercury(mmHg)":
                                def convert():
                                    psi = float(input_entry.get())
                                    Hg = float(psi*51.714925202609111040)
                                    Hg = round(Hg, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hg}")
                                heading_label.config( text = "Pounds per Square Inch (psi or lb/in\u00b2) to mm of Mercury(mmHg)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Pounds per Square Inch (psi or lb/in\u00b2):")
                                input_EL.config( text = "psi")
                                output_OL.config( text = "mmHg")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Technical Atmosphere (at or kgf/cm\u00b2)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Pascals(Pa)":
                                def convert():
                                    at  = float(input_entry.get())
                                    Pa = float(at *98066.5)
                                    Pa = round(Pa, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Pa}")
                                heading_label.config( text = "Technical Atmosphere (at or kgf/cm\u00b2) to Pascals(Pa)", background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Technical Atmosphere (at or kgf/cm\u00b2):")
                                input_EL.config( text = "at ")
                                output_OL.config( text = "Pa")
                            
                            elif tolistbox_get=="Standard Atmosphere(atm)":
                                def convert():
                                    at  = float(input_entry.get())
                                    torr = float(at *0.96784110535405862912)
                                    torr = round(torr, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{torr}")
                                heading_label.config( text = "Technical Atmosphere (at or kgf/cm\u00b2) to Standard Atmosphere(atm)",background = "white")
                                convert_button.config(command = convert)                    
                                enter_label.config(text = "Enter Technical Atmosphere (at or kgf/cm\u00b2):")
                                input_EL.config( text = "at ")
                                output_OL.config( text = "atm")
                            
                            elif tolistbox_get=="Torr(Torr)":
                                def convert():
                                    at  = float(input_entry.get())
                                    Torr = float(at *735.55924018523521024)
                                    Torr = round(Torr, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Torr}")
                                heading_label.config( text = "Technical Atmosphere (at or kgf/cm\u00b2) to Torr(Torr)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Technical Atmosphere (at or kgf/cm\u00b2):")
                                input_EL.config( text = "at ")
                                output_OL.config(text = "Torr")

                            elif tolistbox_get=="Bar(bar)":
                                def convert():
                                    at  = float(input_entry.get())
                                    bar = float(at *0.980665)
                                    bar = round(bar, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bar}")
                                heading_label.config( text = "Technical Atmosphere (at or kgf/cm\u00b2) to Bar(bar)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Technical Atmosphere (at or kgf/cm\u00b2):")
                                input_EL.config( text = "at ")
                                output_OL.config( text = "bar")

                            elif tolistbox_get=="Pounds per Square Inch (psi or lb/in\u00b2)":
                                def convert():
                                    at  = float(input_entry.get())
                                    psi = float(at *14.223343307466878976)
                                    psi = round(psi, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{psi}")
                                heading_label.config( text = "Technical Atmosphere (at or kgf/cm\u00b2) to Pounds per Square Inch (psi or lb/in\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Technical Atmosphere (at or kgf/cm\u00b2):")
                                input_EL.config( text = "at ")
                                output_OL.config( text = "psi")

                            elif tolistbox_get=="Barye(Ba)":
                                def convert():
                                    at  = float(input_entry.get())
                                    Ba = float(at *980665)
                                    Ba = round(Ba, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ba}")
                                heading_label.config( text = "Technical Atmosphere (at or kgf/cm\u00b2) to Barye(Ba)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Technical Atmosphere (at or kgf/cm\u00b2):")
                                input_EL.config( text = "at ")
                                output_OL.config( text = "Ba")

                            elif tolistbox_get=="Pièze(pz)":
                                def convert():
                                    at  = float(input_entry.get())
                                    pz = float(at *98.0665)
                                    pz = round(pz, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{pz}")
                                heading_label.config( text = "Technical Atmosphere (at or kgf/cm\u00b2) to Pièze(pz)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Technical Atmosphere (at or kgf/cm\u00b2):")
                                input_EL.config( text = "at ")
                                output_OL.config( text = "pz")

                            elif tolistbox_get=="mm of Mercury(mmHg)":
                                def convert():
                                    at  = float(input_entry.get())
                                    Hg = float(at *735.55913527668056064)
                                    Hg = round(Hg, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hg}")
                                heading_label.config( text = "Technical Atmosphere (at or kgf/cm\u00b2) to mm of Mercury(mmHg)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Technical Atmosphere (at or kgf/cm\u00b2):")
                                input_EL.config( text = "at ")
                                output_OL.config( text = "mmHg")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Barye(Ba)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Pascals(Pa)":
                                def convert():
                                    Ba = float(input_entry.get())
                                    Pa = float(Ba*0.1)
                                    Pa = round(Pa, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Pa}")
                                heading_label.config( text = "Barye(Ba) to Pascals(Pa)", background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Barye(Ba):")
                                input_EL.config( text = "Ba")
                                output_OL.config( text = "Pa")
                            
                            elif tolistbox_get=="Standard Atmosphere(atm)":
                                def convert():
                                    Ba = float(input_entry.get())
                                    torr = float(Ba/1013250)
                                    torr = round(torr, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{torr}")
                                heading_label.config( text = "Barye(Ba) to Standard Atmosphere(atm)",background = "white")
                                convert_button.config(command = convert)                    
                                enter_label.config(text = "Enter Barye(Ba):")
                                input_EL.config( text = "Ba")
                                output_OL.config( text = "atm")
                            
                            elif tolistbox_get=="Torr(Torr)":
                                def convert():
                                    Ba = float(input_entry.get())
                                    Torr = float(Ba/1333.22)
                                    Torr = round(Torr, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Torr}")
                                heading_label.config( text = "Barye(Ba) to Torr(Torr)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Barye(Ba):")
                                input_EL.config( text = "Ba")
                                output_OL.config(text = "Torr")

                            elif tolistbox_get=="Bar(bar)":
                                def convert():
                                    Ba = float(input_entry.get())
                                    bar = float(Ba/1e+6)
                                    bar = round(bar, 9)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bar}")
                                heading_label.config( text = "Barye(Ba) to Bar(bar)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Barye(Ba):")
                                input_EL.config( text = "Ba")
                                output_OL.config( text = "bar")

                            elif tolistbox_get=="Pounds per Square Inch (psi or lb/in\u00b2)":
                                def convert():
                                    Ba = float(input_entry.get())
                                    psi = float(Ba*1.4503773773375086592e-5)
                                    psi = round(psi, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{psi}")
                                heading_label.config( text = "Barye(Ba) to Pounds per Square Inch (psi or lb/in\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Barye(Ba):")
                                input_EL.config( text = "Ba")
                                output_OL.config( text = "psi")

                            elif tolistbox_get=="Technical Atmosphere (at or kgf/cm\u00b2)":
                                def convert():
                                    Ba = float(input_entry.get())
                                    at = float(Ba/980665)
                                    at = round(at, 9)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{at}")
                                heading_label.config( text = "Barye(Ba) to Technical Atmosphere (at or kgf/cm\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Barye(Ba):")
                                input_EL.config( text = "Ba")
                                output_OL.config( text = "at")

                            elif tolistbox_get=="Pièze(pz)":
                                def convert():
                                    Ba = float(input_entry.get())
                                    pz = float(Ba/10000)
                                    pz = round(pz, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{pz}")
                                heading_label.config( text = "Barye(Ba) to Pièze(pz)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Barye(Ba):")
                                input_EL.config( text = "Ba")
                                output_OL.config( text = "pz")

                            elif tolistbox_get=="mm of Mercury(mmHg)":
                                def convert():
                                    Ba = float(input_entry.get())
                                    Hg = float(Ba*0.00075006157584565633024)
                                    Hg = round(Hg, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hg}")
                                heading_label.config( text = "Barye(Ba) to mm of Mercury(mmHg)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Barye(Ba):")
                                input_EL.config( text = "Ba")
                                output_OL.config( text = "mmHg")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Pièze(pz)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Pascals(Pa)":
                                def convert():
                                    pz = float(input_entry.get())
                                    Pa = float(pz*1000)
                                    Pa = round(Pa, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Pa}")
                                heading_label.config( text = "Pièze(pz) to Pascals(Pa)", background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pièze(pz):")
                                input_EL.config( text = "pz")
                                output_OL.config( text = "Pa")
                            
                            elif tolistbox_get=="Standard Atmosphere(atm)":
                                def convert():
                                    pz = float(input_entry.get())
                                    torr = float(pz/101.325)
                                    torr = round(torr, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{torr}")
                                heading_label.config( text = "Pièze(pz) to Standard Atmosphere(atm)",background = "white")
                                convert_button.config(command = convert)                    
                                enter_label.config(text = "Enter Pièze(pz):")
                                input_EL.config( text = "pz")
                                output_OL.config( text = "atm")
                            
                            elif tolistbox_get=="Torr(Torr)":
                                def convert():
                                    pz = float(input_entry.get())
                                    Torr = float(pz*7.5006168282261028864)
                                    Torr = round(Torr, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Torr}")
                                heading_label.config( text = "Pièze(pz) to Torr(Torr)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pièze(pz):")
                                input_EL.config( text = "pz")
                                output_OL.config(text = "Torr")

                            elif tolistbox_get=="Bar(bar)":
                                def convert():
                                    pz = float(input_entry.get())
                                    bar = float(pz/100)
                                    bar = round(bar, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bar}")
                                heading_label.config( text = "Pièze(pz) to Bar(bar)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Pièze(pz):")
                                input_EL.config( text = "pz")
                                output_OL.config( text = "bar")

                            elif tolistbox_get=="Pounds per Square Inch (psi or lb/in\u00b2)":
                                def convert():
                                    pz = float(input_entry.get())
                                    psi = float(pz*0.14503773773375084544)
                                    psi = round(psi, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{psi}")
                                heading_label.config( text = "Pièze(pz) to Pounds per Square Inch (psi or lb/in\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pièze(pz):")
                                input_EL.config( text = "pz")
                                output_OL.config( text = "psi")

                            elif tolistbox_get=="Technical Atmosphere (at or kgf/cm\u00b2)":
                                def convert():
                                    pz = float(input_entry.get())
                                    at = float(pz*0.010197162129799999488)
                                    at = round(at, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{at}")
                                heading_label.config( text = "Pièze(pz) to Technical Atmosphere (at or kgf/cm\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter Pièze(pz):")
                                input_EL.config( text = "pz")
                                output_OL.config( text = "at")

                            elif tolistbox_get=="Barye(Ba)":
                                def convert():
                                    pz = float(input_entry.get())
                                    Ba = float(pz*10000)
                                    Ba = round(Ba, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ba}")
                                heading_label.config( text = "Pièze(pz) to Barye(Ba)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Pièze(pz):")
                                input_EL.config( text = "pz")
                                output_OL.config( text = "Ba")

                            elif tolistbox_get=="mm of Mercury(mmHg)":
                                def convert():
                                    pz = float(input_entry.get())
                                    Hg = float(pz*7.5006157584565633024)
                                    Hg = round(Hg, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hg}")
                                heading_label.config( text = "Pièze(pz) to mm of Mercury(mmHg)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Pièze(pz):")
                                input_EL.config( text = "pz")
                                output_OL.config( text = "mmHg")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="mm of Mercury(mmHg)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Pascals(Pa)":
                                def convert():
                                    mmHg = float(input_entry.get())
                                    Pa = float(mmHg*133.322387415)
                                    Pa = round(Pa, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Pa}")
                                heading_label.config( text = "mm of Mercury(mmHg) to Pascals(Pa)", background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter mm of Mercury(mmHg):")
                                input_EL.config( text = "mmHg")
                                output_OL.config( text = "Pa")
                            
                            elif tolistbox_get=="Standard Atmosphere(atm)":
                                def convert():
                                    mmHg = float(input_entry.get())
                                    torr = float(mmHg/760)
                                    torr = round(torr, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{torr}")
                                heading_label.config( text = "mm of Mercury(mmHg) to Standard Atmosphere(atm)",background = "white")
                                convert_button.config(command = convert)                    
                                enter_label.config(text = "Enter mm of Mercury(mmHg):")
                                input_EL.config( text = "mmHg")
                                output_OL.config( text = "atm")
                            
                            elif tolistbox_get=="Torr(Torr)":
                                def convert():
                                    mmHg = float(input_entry.get())
                                    Torr = float(mmHg*1)
                                    Torr = round(Torr, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Torr}")
                                heading_label.config( text = "mm of Mercury(mmHg) to Torr(Torr)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter mm of Mercury(mmHg):")
                                input_EL.config( text = "mmHg")
                                output_OL.config(text = "Torr")

                            elif tolistbox_get=="Bar(bar)":
                                def convert():
                                    mmHg = float(input_entry.get())
                                    bar = float(mmHg/750.06157584565633024)
                                    bar = round(bar, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bar}")
                                heading_label.config( text = "mm of Mercury(mmHg) to Bar(bar)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter mm of Mercury(mmHg):")
                                input_EL.config( text = "mmHg")
                                output_OL.config( text = "bar")

                            elif tolistbox_get=="Pounds per Square Inch (psi or lb/in\u00b2)":
                                def convert():
                                    mmHg = float(input_entry.get())
                                    psi = float(mmHg/51.714925202609111040)
                                    psi = round(psi, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{psi}")
                                heading_label.config( text = "mm of Mercury(mmHg) to Pounds per Square Inch (psi or lb/in\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter mm of Mercury(mmHg):")
                                input_EL.config( text = "mmHg")
                                output_OL.config( text = "psi")

                            elif tolistbox_get=="Technical Atmosphere (at or kgf/cm\u00b2)":
                                def convert():
                                    mmHg = float(input_entry.get())
                                    at = float(mmHg*735.55913527668056064)
                                    at = round(at, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{at}")
                                heading_label.config( text = "mm of Mercury(mmHg) to Technical Atmosphere (at or kgf/cm\u00b2)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config( text = "Enter mm of Mercury(mmHg):")
                                input_EL.config( text = "mmHg")
                                output_OL.config( text = "at")

                            elif tolistbox_get=="Barye(Ba)":
                                def convert():
                                    mmHg = float(input_entry.get())
                                    Ba = float(mmHg*1333.22)
                                    Ba = round(Ba, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Ba}")
                                heading_label.config( text = "mm of Mercury(mmHg) to Barye(Ba)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter mm of Mercury(mmHg):")
                                input_EL.config( text = "mmHg")
                                output_OL.config( text = "Ba")

                            elif tolistbox_get=="Pièze(pz)":
                                def convert():
                                    mmHg = float(input_entry.get())
                                    pz = float(mmHg/7.5006157584565633024)
                                    pz = round(pz, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{pz}")
                                heading_label.config( text = "mm of Mercury(mmHg) to Pièze(pz)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter mm of Mercury(mmHg):")
                                input_EL.config( text = "mmHg")
                                output_OL.config( text = "pz")

                        to_listbox.bind("<<ListboxSelect>>", to_box)
                

                def to_snapHighlightToMouse(event):
                    to_listbox.selection_clear(0, END)
                    to_listbox.selection_set(to_listbox.nearest(event.y))

                def to_unhighlight():
                    to_listbox.selection_clear(0, END)    

                def snapHighlightToMouse(event):
                    from_listbox.selection_clear(0, END)
                    from_listbox.selection_set(from_listbox.nearest(event.y))

                def unhighlight():
                    from_listbox.selection_clear(0, END)    

                scientific_heading.config(text = "Pressure", foreground = "red", background = "sky blue")

                to_listbox.delete(0,END)
                for item in range(len(pressure_dict)):
                    to_listbox.insert(END, pressure_dict[item])

                to_listbox.bind('<Motion>', lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Enter>',  lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Leave>',  lambda _: to_unhighlight())

                from_listbox.delete(0,END)
                for item in range(len(pressure_dict)):
                    from_listbox.insert(END, pressure_dict[item])

                from_listbox.bind('<<ListboxSelect>>', from_box)
                from_listbox.bind('<Leave>',  lambda _: unhighlight())
                from_listbox.bind('<Motion>', lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Enter>',  lambda event: snapHighlightToMouse(event))
            #*******************Pressure Converter Ends here********************************************

            #*******************Time Converter Starts here**********************************************

            elif listbox_get=="Time":
                
                def from_box(event):
                    
                    fromlistbox_get = str(from_listbox.get(ANCHOR))
                    
                    if fromlistbox_get=="Centuries":                
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Days":
                                def convert():
                                    centuries = float(input_entry.get())
                                    days = float(centuries*36500)
                                    days = round(days, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{days}")
                                heading_label.config( text = "Centuries to Days",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Centuries:")
                                input_EL.config( text = "Centuries")
                                output_OL.config( text = "Days")

                            elif tolistbox_get=="Decades":
                                def convert():
                                    centuries = float(input_entry.get())
                                    decades = float(centuries*10)
                                    decades = round(decades, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{decades}")
                                heading_label.config( text = "Centuries to Decades",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Centuries:")
                                input_EL.config( text = "Centuries")
                                output_OL.config( text = "Decades")

                            elif tolistbox_get=="Hours":
                                def convert():
                                    centuries = float(input_entry.get())
                                    hours = float(centuries*876000)
                                    hours = round(hours, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hours}")
                                heading_label.config( text = "Centuries to Hours",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Centuries:")
                                input_EL.config( text = "Centuries")
                                output_OL.config( text = "Hours")

                            elif tolistbox_get=="Minutes":
                                def convert():
                                    centuries = float(input_entry.get())
                                    Minutes = float(centuries*5.256e+7)
                                    Minutes = round(Minutes, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Minutes}")
                                heading_label.config( text = "Centuries to Minutes",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Centuries:")
                                input_EL.config( text = "Centuries")
                                output_OL.config( text = "Minutes")

                            elif tolistbox_get=="Months":
                                def convert():
                                    centuries = float(input_entry.get())
                                    Months = float(centuries*1200)
                                    Months = round(Months, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Months}")
                                heading_label.config( text = "Centuries to Months",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Centuries:")
                                input_EL.config( text = "Centuries")
                                output_OL.config( text = "Months")

                            elif tolistbox_get=="Seconds":
                                def convert():
                                    centuries = float(input_entry.get())
                                    Seconds = float(centuries*3.154e+9)
                                    Seconds = round(Seconds, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Seconds}")
                                heading_label.config( text = "Centuries to Seconds",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Centuries:")
                                input_EL.config( text = "Centuries")
                                output_OL.config( text = "Seconds")

                            elif tolistbox_get=="Tropical Year":
                                def convert():
                                    centuries = float(input_entry.get())
                                    tropical_year = float(centuries*99.933633115979972608)
                                    tropical_year = round(tropical_year, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{tropical_year}")
                                heading_label.config( text = "Centuries to Tropical Year",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Centuries:")
                                input_EL.config( text = "Centuries")
                                output_OL.config( text = "Tropical Year")

                            elif tolistbox_get=="Weeks":
                                def convert():
                                    centuries = float(input_entry.get())
                                    Weeks = float(centuries*5214.29)
                                    Weeks = round(Weeks, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Weeks}")
                                heading_label.config( text = "Centuries to Weeks",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Centuries:")
                                input_EL.config( text = "Centuries")
                                output_OL.config( text = "Weeks")

                            elif tolistbox_get=="Years":
                                def convert():
                                    centuries = float(input_entry.get())
                                    Years = float(centuries*100)
                                    Years = round(Years, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Years}")
                                heading_label.config( text = "Centuries to Years",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Centuries:")
                                input_EL.config( text = "Centuries")
                                output_OL.config( text = "Years")
                                
                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Days":                
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Centuries":
                                def convert():
                                    days = float(input_entry.get())
                                    centuries = float(days/36500)
                                    centuries = round(centuries, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{centuries}")
                                heading_label.config( text = "Days to Centuries",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Days:")
                                input_EL.config( text = "Days")
                                output_OL.config( text = "Centuries")

                            elif tolistbox_get=="Decades":
                                def convert():
                                    days = float(input_entry.get())
                                    decades = float(days/3650)
                                    decades = round(decades, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{decades}")
                                heading_label.config( text = "Days to Decades",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Days:")
                                input_EL.config( text = "Days")
                                output_OL.config( text = "Decades")

                            elif tolistbox_get=="Hours":
                                def convert():
                                    days = float(input_entry.get())
                                    hours = float(days*24)
                                    hours = round(hours, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hours}")
                                heading_label.config( text = "Days to Hours",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Days:")
                                input_EL.config( text = "Days")
                                output_OL.config( text = "Hours")

                            elif tolistbox_get=="Minutes":
                                def convert():
                                    days = float(input_entry.get())
                                    Minutes = float(days*1440)
                                    Minutes = round(Minutes, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Minutes}")
                                heading_label.config( text = "Days to Minutes",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Days:")
                                input_EL.config( text = "Days")
                                output_OL.config( text = "Minutes")

                            elif tolistbox_get=="Months":
                                def convert():
                                    days = float(input_entry.get())
                                    Months = float(days/30.417)
                                    Months = round(Months, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Months}")
                                heading_label.config( text = "Days to Months",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Days:")
                                input_EL.config( text = "Days")
                                output_OL.config( text = "Months")

                            elif tolistbox_get=="Seconds":
                                def convert():
                                    days = float(input_entry.get())
                                    Seconds = float(days*86400)
                                    Seconds = round(Seconds, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Seconds}")
                                heading_label.config( text = "Days to Seconds",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Days:")
                                input_EL.config( text = "Days")
                                output_OL.config( text = "Seconds")

                            elif tolistbox_get=="Tropical Year":
                                def convert():
                                    days = float(input_entry.get())
                                    tropical_year = float(days/365.24219)
                                    tropical_year = round(tropical_year, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{tropical_year}")
                                heading_label.config( text = "Days to Tropical Year",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Days:")
                                input_EL.config( text = "Days")
                                output_OL.config( text = "Tropical Year")

                            elif tolistbox_get=="Weeks":
                                def convert():
                                    days = float(input_entry.get())
                                    Weeks = float(days/7)
                                    Weeks = round(Weeks, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Weeks}")
                                heading_label.config( text = "Days to Weeks",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Days:")
                                input_EL.config( text = "Days")
                                output_OL.config( text = "Weeks")

                            elif tolistbox_get=="Years":
                                def convert():
                                    days = float(input_entry.get())
                                    Years = float(days/365)
                                    Years = round(Years, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Years}")
                                heading_label.config( text = "Days to Years",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Days:")
                                input_EL.config( text = "Days")
                                output_OL.config( text = "Years")
                                
                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Decades":
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Centuries":
                                def convert():
                                    decades = float(input_entry.get())
                                    centuries = float(decades/10)
                                    centuries = round(centuries, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{centuries}")
                                heading_label.config( text = "Decades to Centuries",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Decades:")
                                input_EL.config( text = "Decades")
                                output_OL.config( text = "Centuries")

                            elif tolistbox_get=="Days":
                                def convert():
                                    decades = float(input_entry.get())
                                    days = float(decades*3650)
                                    days = round(days, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{days}")
                                heading_label.config( text = "Decades to Days",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Decades:")
                                input_EL.config( text = "Decades")
                                output_OL.config( text = "Days")

                            elif tolistbox_get=="Hours":
                                def convert():
                                    decades = float(input_entry.get())
                                    hours = float(decades*87600)
                                    hours = round(hours, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{hours}")
                                heading_label.config( text = "Decades to Hours",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Decades:")
                                input_EL.config( text = "Decades")
                                output_OL.config( text = "Hours")

                            elif tolistbox_get=="Minutes":
                                def convert():
                                    decades = float(input_entry.get())
                                    Minutes = float(decades*5.256e+6)
                                    Minutes = round(Minutes, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Minutes}")
                                heading_label.config( text = "Decades to Minutes",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Decades:")
                                input_EL.config( text = "Decades")
                                output_OL.config( text = "Minutes")

                            elif tolistbox_get=="Months":
                                def convert():
                                    decades = float(input_entry.get())
                                    Months = float(decades*120)
                                    Months = round(Months, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Months}")
                                heading_label.config( text = "Decades to Months",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Decades:")
                                input_EL.config( text = "Decades")
                                output_OL.config( text = "Months")

                            elif tolistbox_get=="Seconds":
                                def convert():
                                    decades = float(input_entry.get())
                                    Seconds = float(decades*3.154e+8)
                                    Seconds = round(Seconds, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Seconds}")
                                heading_label.config( text = "Decades to Seconds",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Decades:")
                                input_EL.config( text = "Decades")
                                output_OL.config( text = "Seconds")

                            elif tolistbox_get=="Tropical Year":
                                def convert():
                                    decades = float(input_entry.get())
                                    tropical_year = float(decades*9.9933633115979972608)
                                    tropical_year = round(tropical_year, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{tropical_year}")
                                heading_label.config( text = "Decades to Tropical Year",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Decades:")
                                input_EL.config( text = "Decades")
                                output_OL.config( text = "Tropical Year")

                            elif tolistbox_get=="Weeks":
                                def convert():
                                    decades = float(input_entry.get())
                                    Weeks = float(decades*521.42857142857146368)
                                    Weeks = round(Weeks, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Weeks}")
                                heading_label.config( text = "Decades to Weeks",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Decades:")
                                input_EL.config( text = "Decades")
                                output_OL.config( text = "Weeks")

                            elif tolistbox_get=="Years":
                                def convert():
                                    decades = float(input_entry.get())
                                    Years = float(decades*10)
                                    Years = round(Years, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Years}")
                                heading_label.config( text = "Decades to Years",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Decades:")
                                input_EL.config( text = "Decades")
                                output_OL.config( text = "Years")
                                
                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Hours":
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Centuries":
                                def convert():
                                    hours = float(input_entry.get())
                                    centuries = float(hours/876000)
                                    centuries = round(centuries,10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{centuries}")
                                heading_label.config( text = "Hours to Centuries",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Hours:")
                                input_EL.config( text = "Hours")
                                output_OL.config( text = "Centuries")

                            elif tolistbox_get=="Days":
                                def convert():
                                    hours = float(input_entry.get())
                                    days = float(hours/24)
                                    days = round(days, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{days}")
                                heading_label.config( text = "Hours to Days",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Hours:")
                                input_EL.config( text = "Hours")
                                output_OL.config( text = "Days")

                            elif tolistbox_get=="Decades":
                                def convert():
                                    hours = float(input_entry.get())
                                    decades = float(hours/87600)
                                    decades = round(decades, 9)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{decades}")
                                heading_label.config( text = "Hours to Decades",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Hours:")
                                input_EL.config( text = "Hours")
                                output_OL.config( text = "Decades")

                            elif tolistbox_get=="Minutes":
                                def convert():
                                    hours = float(input_entry.get())
                                    Minutes = float(hours*60)
                                    Minutes = round(Minutes, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Minutes}")
                                heading_label.config( text = "Hours to Minutes",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Hours:")
                                input_EL.config( text = "Hours")
                                output_OL.config( text = "Minutes")

                            elif tolistbox_get=="Months":
                                def convert():
                                    hours = float(input_entry.get())
                                    Months = float(hours/730.0008)
                                    Months = round(Months, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Months}")
                                heading_label.config( text = "Hours to Months",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Hours:")
                                input_EL.config( text = "Hours")
                                output_OL.config( text = "Months")

                            elif tolistbox_get=="Seconds":
                                def convert():
                                    hours = float(input_entry.get())
                                    Seconds = float(hours*3600)
                                    Seconds = round(Seconds, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Seconds}")
                                heading_label.config( text = "Hours to Seconds",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Hours:")
                                input_EL.config( text = "Hours")
                                output_OL.config( text = "Seconds")

                            elif tolistbox_get=="Tropical Year":
                                def convert():
                                    hours = float(input_entry.get())
                                    tropical_year = float(hours*0.00011407948985842460672)
                                    tropical_year = round(tropical_year, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{tropical_year}")
                                heading_label.config( text = "Hours to Tropical Year",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Hours:")
                                input_EL.config( text = "Hours")
                                output_OL.config( text = "Tropical Year")

                            elif tolistbox_get=="Weeks":
                                def convert():
                                    hours = float(input_entry.get())
                                    Weeks = float(hours/168)
                                    Weeks = round(Weeks, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Weeks}")
                                heading_label.config( text = "Hours to Weeks",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Hours:")
                                input_EL.config( text = "Hours")
                                output_OL.config( text = "Weeks")

                            elif tolistbox_get=="Years":
                                def convert():
                                    hours = float(input_entry.get())
                                    Years = float(hours/8760)
                                    Years = round(Years, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Years}")
                                heading_label.config( text = "Hours to Years",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Hours:")
                                input_EL.config( text = "Hours")
                                output_OL.config( text = "Years")
                                
                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Minutes":
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Centuries":
                                def convert():
                                    minutes = float(input_entry.get())
                                    centuries = float(minutes/5.256e+7)
                                    centuries = round(centuries,12)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{centuries}")
                                heading_label.config( text = "Minutes to Centuries",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Minutes:")
                                input_EL.config( text = "Minutes")
                                output_OL.config( text = "Centuries")

                            elif tolistbox_get=="Days":
                                def convert():
                                    minutes = float(input_entry.get())
                                    days = float(minutes/1440)
                                    days = round(days, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{days}")
                                heading_label.config( text = "Minutes to Days",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Minutes:")
                                input_EL.config( text = "Minutes")
                                output_OL.config( text = "Days")

                            elif tolistbox_get=="Decades":
                                def convert():
                                    minutes = float(input_entry.get())
                                    decades = float(minutes/5.256e+6)
                                    decades = round(decades, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{decades}")
                                heading_label.config( text = "Minutes to Decades",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Minutes:")
                                input_EL.config( text = "Minutes")
                                output_OL.config( text = "Decades")

                            elif tolistbox_get=="Hours":
                                def convert():
                                    minutes = float(input_entry.get())
                                    Hours = float(minutes/60)
                                    Hours = round(Hours, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hours}")
                                heading_label.config( text = "Minutes to Hours",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Minutes:")
                                input_EL.config( text = "Minutes")
                                output_OL.config( text = "Hours")

                            elif tolistbox_get=="Months":
                                def convert():
                                    minutes = float(input_entry.get())
                                    Months = float(minutes/43800)
                                    Months = round(Months, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Months}")
                                heading_label.config( text = "Minutes to Months",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Minutes:")
                                input_EL.config( text = "Minutes")
                                output_OL.config( text = "Months")

                            elif tolistbox_get=="Seconds":
                                def convert():
                                    minutes = float(input_entry.get())
                                    Seconds = float(minutes*60)
                                    Seconds = round(Seconds, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Seconds}")
                                heading_label.config( text = "Minutes to Seconds",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Minutes:")
                                input_EL.config( text = "Minutes")
                                output_OL.config( text = "Seconds")

                            elif tolistbox_get=="Tropical Year":
                                def convert():
                                    minutes = float(input_entry.get())
                                    tropical_year = float(minutes/525949)
                                    tropical_year = round(tropical_year, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{tropical_year}")
                                heading_label.config( text = "Minutes to Tropical Year",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Minutes:")
                                input_EL.config( text = "Minutes")
                                output_OL.config( text = "Tropical Year")

                            elif tolistbox_get=="Weeks":
                                def convert():
                                    minutes = float(input_entry.get())
                                    Weeks = float(minutes/10080)
                                    Weeks = round(Weeks, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Weeks}")
                                heading_label.config( text = "Minutes to Weeks",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Minutes:")
                                input_EL.config( text = "Minutes")
                                output_OL.config( text = "Weeks")

                            elif tolistbox_get=="Years":
                                def convert():
                                    minutes = float(input_entry.get())
                                    Years = float(minutes/525600)
                                    Years = round(Years, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Years}")
                                heading_label.config( text = "Minutes to Years",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Minutes:")
                                input_EL.config( text = "Minutes")
                                output_OL.config( text = "Years")
                                
                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Months":
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Centuries":
                                def convert():
                                    months = float(input_entry.get())
                                    centuries = float(months/1200)
                                    centuries = round(centuries, 7)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{centuries}")
                                heading_label.config( text = "Months to Centuries",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Months:")
                                input_EL.config( text = "Months")
                                output_OL.config( text = "Centuries")

                            elif tolistbox_get=="Days":
                                def convert():
                                    months = float(input_entry.get())
                                    days = float(months*30.417)
                                    days = round(days, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{days}")
                                heading_label.config( text = "Months to Days",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Months:")
                                input_EL.config( text = "Months")
                                output_OL.config( text = "Days")

                            elif tolistbox_get=="Decades":
                                def convert():
                                    months = float(input_entry.get())
                                    decades = float(months/120)
                                    decades = round(decades, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{decades}")
                                heading_label.config( text = "Months to Decades",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Months:")
                                input_EL.config( text = "Months")
                                output_OL.config( text = "Decades")

                            elif tolistbox_get=="Hours":
                                def convert():
                                    months = float(input_entry.get())
                                    Hours = float(months*730.0008)
                                    Hours = round(Hours, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hours}")
                                heading_label.config( text = "Months to Hours",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Months:")
                                input_EL.config( text = "Months")
                                output_OL.config( text = "Hours")

                            elif tolistbox_get=="Minutes":
                                def convert():
                                    months = float(input_entry.get())
                                    minutes = float(months/43800)
                                    minutes = round(minutes, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{minutes}")
                                heading_label.config( text = "Months to Minutes",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Months:")
                                input_EL.config( text = "Months")
                                output_OL.config( text = "Minutes")

                            elif tolistbox_get=="Seconds":
                                def convert():
                                    months = float(input_entry.get())
                                    Seconds = float(months*2.628e+6)
                                    Seconds = round(Seconds, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Seconds}")
                                heading_label.config( text = "Months to Seconds",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Months:")
                                input_EL.config( text = "Months")
                                output_OL.config( text = "Seconds")

                            elif tolistbox_get=="Tropical Year":
                                def convert():
                                    months = float(input_entry.get())
                                    tropical_year = float(months/12.008)
                                    tropical_year = round(tropical_year, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{tropical_year}")
                                heading_label.config( text = "Months to Tropical Year",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Months:")
                                input_EL.config( text = "Months")
                                output_OL.config( text = "Tropical Year")

                            elif tolistbox_get=="Weeks":
                                def convert():
                                    months = float(input_entry.get())
                                    Weeks = float(months*4.3452428571428569088)
                                    Weeks = round(Weeks, 2)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Weeks}")
                                heading_label.config( text = "Months to Weeks",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Months:")
                                input_EL.config( text = "Months")
                                output_OL.config( text = "Weeks")

                            elif tolistbox_get=="Years":
                                def convert():
                                    months = float(input_entry.get())
                                    Years = float(months/12)
                                    Years = round(Years, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Years}")
                                heading_label.config( text = "Months to Years",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Months:")
                                input_EL.config( text = "Months")
                                output_OL.config( text = "Years")
                                
                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Seconds":
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Centuries":
                                def convert():
                                    seconds = float(input_entry.get())
                                    centuries = float(seconds/3.154e+9)
                                    centuries = round(centuries, 13)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{centuries}")
                                heading_label.config( text = "Seconds to Centuries",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Seconds:")
                                input_EL.config( text = "Seconds")
                                output_OL.config( text = "Centuries")

                            elif tolistbox_get=="Days":
                                def convert():
                                    seconds = float(input_entry.get())
                                    days = float(seconds/86400)
                                    days = round(days, 8)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{days}")
                                heading_label.config( text = "Seconds to Days",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Seconds:")
                                input_EL.config( text = "Seconds")
                                output_OL.config( text = "Days")

                            elif tolistbox_get=="Decades":
                                def convert():
                                    seconds = float(input_entry.get())
                                    decades = float(seconds/3.154e+8)
                                    decades = round(decades, 13)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{decades}")
                                heading_label.config( text = "Seconds to Decades",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Seconds:")
                                input_EL.config( text = "Seconds")
                                output_OL.config( text = "Decades")

                            elif tolistbox_get=="Hours":
                                def convert():
                                    seconds = float(input_entry.get())
                                    Hours = float(seconds/3600)
                                    Hours = round(Hours, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hours}")
                                heading_label.config( text = "Seconds to Hours",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Seconds:")
                                input_EL.config( text = "Seconds")
                                output_OL.config( text = "Hours")

                            elif tolistbox_get=="Minutes":
                                def convert():
                                    seconds = float(input_entry.get())
                                    minutes = float(seconds/60)
                                    minutes = round(minutes, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{minutes}")
                                heading_label.config( text = "Seconds to Minutes",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Seconds:")
                                input_EL.config( text = "Seconds")
                                output_OL.config( text = "Minutes")

                            elif tolistbox_get=="Months":
                                def convert():
                                    seconds = float(input_entry.get())
                                    Months = float(seconds/2.628e+6)
                                    Months = round(Months, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Months}")
                                heading_label.config( text = "Seconds to Months",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Seconds:")
                                input_EL.config( text = "Seconds")
                                output_OL.config( text = "Months")

                            elif tolistbox_get=="Tropical Year":
                                def convert():
                                    seconds = float(input_entry.get())
                                    tropical_year = float(seconds/3.156e+7)
                                    tropical_year = round(tropical_year, 12)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{tropical_year}")
                                heading_label.config( text = "Seconds to Tropical Year",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Seconds:")
                                input_EL.config( text = "Seconds")
                                output_OL.config( text = "Tropical Year")

                            elif tolistbox_get=="Weeks":
                                def convert():
                                    seconds = float(input_entry.get())
                                    Weeks = float(seconds/604800)
                                    Weeks = round(Weeks, 10)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Weeks}")
                                heading_label.config( text = "Seconds to Weeks",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Seconds:")
                                input_EL.config( text = "Seconds")
                                output_OL.config( text = "Weeks")

                            elif tolistbox_get=="Years":
                                def convert():
                                    seconds = float(input_entry.get())
                                    Years = float(seconds/3.154e+7)
                                    Years = round(Years, 12)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Years}")
                                heading_label.config( text = "Seconds to Years",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Seconds:")
                                input_EL.config( text = "Seconds")
                                output_OL.config( text = "Years")
                                
                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Tropical Year":
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Centuries":
                                def convert():
                                    tropical_Year = float(input_entry.get())
                                    centuries = float(tropical_Year/99.933633115979972608)
                                    centuries = round(centuries, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{centuries}")
                                heading_label.config( text = "Tropical Year to Centuries",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Tropical Year:")
                                input_EL.config( text = "Tropical Year")
                                output_OL.config( text = "Centuries")

                            elif tolistbox_get=="Days":
                                def convert():
                                    tropical_Year = float(input_entry.get())
                                    days = float(tropical_Year*365.24219)
                                    days = round(days, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{days}")
                                heading_label.config( text = "Tropical Year to Days",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Tropical Year:")
                                input_EL.config( text = "Tropical Year")
                                output_OL.config( text = "Days")

                            elif tolistbox_get=="Decades":
                                def convert():
                                    tropical_Year = float(input_entry.get())
                                    decades = float(tropical_Year/9.993)
                                    decades = round(decades, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{decades}")
                                heading_label.config( text = "Tropical Year to Decades",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Tropical Year:")
                                input_EL.config( text = "Tropical Year")
                                output_OL.config( text = "Decades")

                            elif tolistbox_get=="Hours":
                                def convert():
                                    tropical_Year = float(input_entry.get())
                                    Hours = float(tropical_Year/0.00011407948985842460672)
                                    Hours = round(Hours, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hours}")
                                heading_label.config( text = "Tropical Year to Hours",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Tropical Year:")
                                input_EL.config( text = "Tropical Year")
                                output_OL.config( text = "Hours")

                            elif tolistbox_get=="Minutes":
                                def convert():
                                    tropical_Year = float(input_entry.get())
                                    minutes = float(tropical_Year*525949)
                                    minutes = round(minutes, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{minutes}")
                                heading_label.config( text = "Tropical Year to Minutes",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Tropical Year:")
                                input_EL.config( text = "Tropical Year")
                                output_OL.config( text = "Minutes")

                            elif tolistbox_get=="Months":
                                def convert():
                                    tropical_Year = float(input_entry.get())
                                    Months = float(tropical_Year*12.008)
                                    Months = round(Months, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Months}")
                                heading_label.config( text = "Tropical Year to Months",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Tropical Year:")
                                input_EL.config( text = "Tropical Year")
                                output_OL.config( text = "Months")

                            elif tolistbox_get=="Seconds":
                                def convert():
                                    tropical_Year = float(input_entry.get())
                                    seconds = float(tropical_Year*3.156e+7)
                                    seconds = round(seconds, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{seconds}")
                                heading_label.config( text = "Tropical Year to Seconds",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Tropical Year:")
                                input_EL.config( text = "Tropical Year")
                                output_OL.config( text = "Seconds")

                            elif tolistbox_get=="Weeks":
                                def convert():
                                    tropical_Year = float(input_entry.get())
                                    Weeks = float(tropical_Year*52.177485714285715456)
                                    Weeks = round(Weeks, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Weeks}")
                                heading_label.config( text = "Tropical Year to Weeks",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Tropical Year:")
                                input_EL.config( text = "Tropical Year")
                                output_OL.config( text = "Weeks")

                            elif tolistbox_get=="Years":
                                def convert():
                                    tropical_Year = float(input_entry.get())
                                    Years = float(tropical_Year*1.0006641095890411520)
                                    Years = round(Years, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Years}")
                                heading_label.config( text = "Tropical Year to Years",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Tropical Year:")
                                input_EL.config( text = "Tropical Year")
                                output_OL.config( text = "Years")
                                
                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Weeks":
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Centuries":
                                def convert():
                                    weeks = float(input_entry.get())
                                    centuries = float(weeks/99.933633115979972608)
                                    centuries = round(centuries, 5)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{centuries}")
                                heading_label.config( text = "Weeks to Centuries",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Weeks:")
                                input_EL.config( text = "Weeks")
                                output_OL.config( text = "Centuries")

                            elif tolistbox_get=="Days":
                                def convert():
                                    weeks = float(input_entry.get())
                                    days = float(weeks*365.24219)
                                    days = round(days, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{days}")
                                heading_label.config( text = "Weeks to Days",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Weeks:")
                                input_EL.config( text = "Weeks")
                                output_OL.config( text = "Days")

                            elif tolistbox_get=="Decades":
                                def convert():
                                    weeks = float(input_entry.get())
                                    decades = float(weeks/9.993)
                                    decades = round(decades, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{decades}")
                                heading_label.config( text = "Weeks to Decades",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Weeks:")
                                input_EL.config( text = "Weeks")
                                output_OL.config( text = "Decades")

                            elif tolistbox_get=="Hours":
                                def convert():
                                    weeks = float(input_entry.get())
                                    Hours = float(weeks/0.00011407948985842460672)
                                    Hours = round(Hours, 6)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hours}")
                                heading_label.config( text = "Weeks to Hours",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Weeks:")
                                input_EL.config( text = "Weeks")
                                output_OL.config( text = "Hours")

                            elif tolistbox_get=="Minutes":
                                def convert():
                                    weeks = float(input_entry.get())
                                    minutes = float(weeks*525949)
                                    minutes = round(minutes, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{minutes}")
                                heading_label.config( text = "Weeks to Minutes",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Weeks:")
                                input_EL.config( text = "Weeks")
                                output_OL.config( text = "Minutes")

                            elif tolistbox_get=="Months":
                                def convert():
                                    weeks = float(input_entry.get())
                                    Months = float(weeks*12.008)
                                    Months = round(Months, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Months}")
                                heading_label.config( text = "Weeks to Months",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Weeks:")
                                input_EL.config( text = "Weeks")
                                output_OL.config( text = "Months")

                            elif tolistbox_get=="Seconds":
                                def convert():
                                    weeks = float(input_entry.get())
                                    seconds = float(weeks*3.156e+7)
                                    seconds = round(seconds, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{seconds}")
                                heading_label.config( text = "Weeks to Seconds",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Weeks:")
                                input_EL.config( text = "Weeks")
                                output_OL.config( text = "Seconds")

                            elif tolistbox_get=="Tropical Year":
                                def convert():
                                    weeks = float(input_entry.get())
                                    tropical_Year = float(weeks*52.177485714285715456)
                                    tropical_Year = round(tropical_Year, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{tropical_Year}")
                                heading_label.config( text = "Weeks to Tropical Year",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Weeks:")
                                input_EL.config( text = "Weeks")
                                output_OL.config( text = "Tropical Year")

                            elif tolistbox_get=="Years":
                                def convert():
                                    weeks = float(input_entry.get())
                                    Years = float(weeks*1.0006641095890411520)
                                    Years = round(Years, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Years}")
                                heading_label.config( text = "Weeks to Years",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Weeks:")
                                input_EL.config( text = "Weeks")
                                output_OL.config( text = "Years")
                                
                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Years":
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Centuries":
                                def convert():
                                    years = float(input_entry.get())
                                    centuries = float(years/100)
                                    centuries = round(centuries, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{centuries}")
                                heading_label.config( text = "Years to Centuries",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Years:")
                                input_EL.config( text = "Years")
                                output_OL.config( text = "Centuries")

                            elif tolistbox_get=="Days":
                                def convert():
                                    years = float(input_entry.get())
                                    days = float(years*365)
                                    days = round(days, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{days}")
                                heading_label.config( text = "Years to Days",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Years:")
                                input_EL.config( text = "Years")
                                output_OL.config( text = "Days")

                            elif tolistbox_get=="Decades":
                                def convert():
                                    years = float(input_entry.get())
                                    decades = float(years/10)
                                    decades = round(decades, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{decades}")
                                heading_label.config( text = "Years to Decades",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Years:")
                                input_EL.config( text = "Years")
                                output_OL.config( text = "Decades")

                            elif tolistbox_get=="Hours":
                                def convert():
                                    years = float(input_entry.get())
                                    Hours = float(years*8760)
                                    Hours = round(Hours, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Hours}")
                                heading_label.config( text = "Years to Hours",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Years:")
                                input_EL.config( text = "Years")
                                output_OL.config( text = "Hours")

                            elif tolistbox_get=="Minutes":
                                def convert():
                                    years = float(input_entry.get())
                                    minutes = float(years*525600)
                                    minutes = round(minutes, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{minutes}")
                                heading_label.config( text = "Years to Minutes",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Years:")
                                input_EL.config( text = "Years")
                                output_OL.config( text = "Minutes")

                            elif tolistbox_get=="Months":
                                def convert():
                                    years = float(input_entry.get())
                                    Months = float(years*12)
                                    Months = round(Months, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{Months}")
                                heading_label.config( text = "Years to Months",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Years:")
                                input_EL.config( text = "Years")
                                output_OL.config( text = "Months")

                            elif tolistbox_get=="Seconds":
                                def convert():
                                    years = float(input_entry.get())
                                    seconds = float(years*3.154e+7)
                                    seconds = round(seconds, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{seconds}")
                                heading_label.config( text = "Years to Seconds",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Years:")
                                input_EL.config( text = "Years")
                                output_OL.config( text = "Seconds")

                            elif tolistbox_get=="tropical_Year":
                                def convert():
                                    year = float(input_entry.get())
                                    tropical_Year = float(year*0.99933633115979972608)
                                    tropical_Year = round(tropical_Year, 4)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{tropical_Year}")
                                heading_label.config( text = "Years to Tropical Year",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Years:")
                                input_EL.config( text = "Year")
                                output_OL.config( text = "Tropical Year")

                            elif tolistbox_get=="Weeks":
                                def convert():
                                    years = float(input_entry.get())
                                    weeks = float(years*52.142857142857146368)
                                    weeks = round(weeks, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{weeks}")
                                heading_label.config( text = "Years to Weeks",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Years:")
                                input_EL.config( text = "Years")
                                output_OL.config( text = "Weeks")
                                
                        to_listbox.bind("<<ListboxSelect>>", to_box)

                        
                def to_snapHighlightToMouse(event):
                    to_listbox.selection_clear(0, END)
                    to_listbox.selection_set(to_listbox.nearest(event.y))

                def to_unhighlight():
                    to_listbox.selection_clear(0, END)    

                def snapHighlightToMouse(event):
                    from_listbox.selection_clear(0, END)
                    from_listbox.selection_set(from_listbox.nearest(event.y))

                def unhighlight():
                    from_listbox.selection_clear(0, END)    

                scientific_heading.config(text = "Pressure", foreground = "red", background = "sky blue")

                to_listbox.delete(0,END)
                for item in range(len(time_dict)):
                    to_listbox.insert(END, time_dict[item])

                to_listbox.bind('<Motion>', lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Enter>',  lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Leave>',  lambda _: to_unhighlight())

                from_listbox.delete(0,END)
                for item in range(len(time_dict)):
                    from_listbox.insert(END, time_dict[item])

                from_listbox.bind('<<ListboxSelect>>', from_box)
                from_listbox.bind('<Leave>',  lambda _: unhighlight())
                from_listbox.bind('<Motion>', lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Enter>',  lambda event: snapHighlightToMouse(event))

            #*****************************Time Converter End here************************************


            #****************************Current Converter Starts Here******************************
            elif listbox_get=="Current":
                
                def from_box(event):
                    
                    fromlistbox_get = str(from_listbox.get(ANCHOR))
                    
                    if fromlistbox_get=="Abamperes(abA)":                
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Amperes(A)":
                                def convert():
                                    abA = float(input_entry.get())
                                    amp = float(abA*10)
                                    amp = round(amp, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{amp}")
                                heading_label.config( text = "Abamperes(abA) to Amperes(A)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Abamperes(abA):")
                                input_EL.config( text = "abA")
                                output_OL.config( text = "A")

                            elif tolistbox_get=="Biots(Bi)":
                                def convert():
                                    abA = float(input_entry.get())
                                    bio = float(abA*10)
                                    bio = round(bio, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bio}")
                                heading_label.config( text = "Abamperes(abA) to Biots(Bi)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Abamperes(abA):")
                                input_EL.config( text = "abA")
                                output_OL.config( text = "Bi")

                            elif tolistbox_get=="EMUs of Current":
                                def convert():
                                    abA = float(input_entry.get())
                                    EMUs = float(abA*1)
                                    EMUs = round(EMUs, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{EMUs}")
                                heading_label.config( text = "Abamperes(abA) to EMUs of Current",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Abamperes(abA):")
                                input_EL.config( text = "abA")
                                output_OL.config( text = "EMU")

                            elif tolistbox_get=="ESUs of Current":
                                def convert():
                                    abA = float(input_entry.get())
                                    ESUs = float(abA*2.9979245368431e+10)
                                    ESUs = round(ESUs, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ESUs}")
                                heading_label.config( text = "Abamperes(abA) to ESUs of Current",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Abamperes(abA):")
                                input_EL.config( text = "abA")
                                output_OL.config( text = "ESU")

                            elif tolistbox_get=="Statamperes(stA)":
                                def convert():
                                    abA = float(input_entry.get())
                                    stA = float(abA*2.9979245368431e+10)
                                    stA = round(stA, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{stA}")
                                heading_label.config( text = "Abamperes(abA) to Statamperes(stA)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Abamperes(abA):")
                                input_EL.config( text = "abA")
                                output_OL.config( text = "stA")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Amperes(A)":
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Abamperes(abA)":
                                def convert():
                                    amp = float(input_entry.get())
                                    abA = float(amp/10)
                                    abA = round(abA, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{abA}")
                                heading_label.config( text = "Amperes(A) to Abamperes(abA)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Amperes(A):")
                                input_EL.config( text = "A")
                                output_OL.config( text = "abA")

                            elif tolistbox_get=="Biots(Bi)":
                                def convert():
                                    amp = float(input_entry.get())
                                    bio = float(amp/10)
                                    bio = round(bio, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bio}")
                                heading_label.config( text = "Amperes(A) to Biots(Bi)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Amperes(A):")
                                input_EL.config( text = "A")
                                output_OL.config( text = "Bi")

                            elif tolistbox_get=="EMUs of Current":
                                def convert():
                                    amp = float(input_entry.get())
                                    EMUs = float(amp/10)
                                    EMUs = round(EMUs, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{EMUs}")
                                heading_label.config( text = "Amperes(A) to EMUs of Current",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Amperes(A):")
                                input_EL.config( text = "A")
                                output_OL.config( text = "EMU")

                            elif tolistbox_get=="ESUs of Current":
                                def convert():
                                    amp = float(input_entry.get())
                                    ESUs = float(amp*2.9979245368431e+9)
                                    ESUs = round(ESUs, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ESUs}")
                                heading_label.config( text = "Amperes(A) to ESUs of Current",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Amperes(A):")
                                input_EL.config( text = "A")
                                output_OL.config( text = "ESU")

                            elif tolistbox_get=="Statamperes(stA)":
                                def convert():
                                    amp = float(input_entry.get())
                                    stA = float(amp*2.9979245368431e+9)
                                    stA = round(stA, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{stA}")
                                heading_label.config( text = "Amperes(A) to Statamperes(stA)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Amperes(A):")
                                input_EL.config( text = "A")
                                output_OL.config( text = "stA")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Biots(Bi)":
                        
                        def to_box(event):
                            
                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Abamperes(abA)":
                                def convert():
                                    bio = float(input_entry.get())
                                    abA = float(bio*1)
                                    abA = round(abA, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{abA}")
                                heading_label.config( text = "Biots(Bi) to Abamperes(abA)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Biots(Bi):")
                                input_EL.config( text = "Bi")
                                output_OL.config( text = "abA")

                            elif tolistbox_get=="Amperes(A)":
                                def convert():
                                    bio = float(input_entry.get())
                                    amp = float(bio*10)
                                    amp = round(amp, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{amp}")
                                heading_label.config( text = "Biots(Bi) to Amperes(A)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Biots(Bi):")
                                input_EL.config( text = "Bi")
                                output_OL.config( text = "A")

                            elif tolistbox_get=="EMUs of Current":
                                def convert():
                                    bio = float(input_entry.get())
                                    EMUs = float(bio*1)
                                    EMUs = round(EMUs, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{EMUs}")
                                heading_label.config( text = "Biots(Bi) to EMUs of Current",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Biots(Bi):")
                                input_EL.config( text = "Bi")
                                output_OL.config( text = "EMU")

                            elif tolistbox_get=="ESUs of Current":
                                def convert():
                                    bio = float(input_entry.get())
                                    ESUs = float(bio*2.9979245368431e+10)
                                    ESUs = round(ESUs, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ESUs}")
                                heading_label.config( text = "Biots(Bi) to ESUs of Current",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Biots(Bi):")
                                input_EL.config( text = "Bi")
                                output_OL.config( text = "ESU")

                            elif tolistbox_get=="Statamperes(stA)":
                                def convert():
                                    bio = float(input_entry.get())
                                    stA = float(bio*2.9979245368431e+10)
                                    stA = round(stA, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{stA}")
                                heading_label.config( text = "Biots(Bi) to Statamperes(stA)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Biots(Bi):")
                                input_EL.config( text = "Bi")
                                output_OL.config( text = "stA")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="EMUs of Current":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Abamperes(abA)":
                                def convert():
                                    EMUs = float(input_entry.get())
                                    abA = float(EMUs*1)
                                    abA = round(abA, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{abA}")
                                heading_label.config( text = "EMUs of Current to Abamperes(abA)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter EMUs of Current:")
                                input_EL.config( text = "EMU")
                                output_OL.config( text = "abA")

                            elif tolistbox_get=="Amperes(A)":
                                def convert():
                                    EMUs = float(input_entry.get())
                                    amp = float(EMUs*10)
                                    amp = round(amp, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{amp}")
                                heading_label.config( text = "EMUs of Current to Amperes(A)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter EMUs of Current:")
                                input_EL.config( text = "EMU")
                                output_OL.config( text = "A")

                            elif tolistbox_get=="Biots(Bi)":
                                def convert():
                                    EMUs = float(input_entry.get())
                                    bio = float(EMUs*1)
                                    bio = round(bio, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bio}")
                                heading_label.config( text = "EMUs of Current to Biots(Bi)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter EMUs of Current:")
                                input_EL.config( text = "EMU")
                                output_OL.config( text = "EMU")

                            elif tolistbox_get=="ESUs of Current":
                                def convert():
                                    EMUs = float(input_entry.get())
                                    ESUs = float(EMUs*2.9979245368431e+10)
                                    ESUs = round(ESUs, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ESUs}")
                                heading_label.config( text = "EMUs of Current to ESUs of Current",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter EMUs of Current:")
                                input_EL.config( text = "EMU")
                                output_OL.config( text = "Bi")

                            elif tolistbox_get=="Statamperes(stA)":
                                def convert():
                                    EMUs = float(input_entry.get())
                                    stA = float(EMUs*2.9979245368431e+10)
                                    stA = round(stA, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{stA}")
                                heading_label.config( text = "EMUs of Current to Statamperes(stA)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter EMUs of Current:")
                                input_EL.config( text = "EMU")
                                output_OL.config( text = "stA")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="ESUs of Current":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Abamperes(abA)":
                                def convert():
                                    ESUs = float(input_entry.get())
                                    abA = float(ESUs/2.9979245368431e+10)
                                    abA = round(abA, 15)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{abA}")
                                heading_label.config( text = "ESUs of Current to Abamperes(abA)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter ESUs of Current:")
                                input_EL.config( text = "ESU")
                                output_OL.config( text = "abA")

                            elif tolistbox_get=="Amperes(A)":
                                def convert():
                                    ESUs = float(input_entry.get())
                                    amp = float(ESUs/2.9979245368431e+9)
                                    amp = round(amp, 13)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{amp}")
                                heading_label.config( text = "ESUs of Current to Amperes(A)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter ESUs of Current:")
                                input_EL.config( text = "ESU")
                                output_OL.config( text = "A")

                            elif tolistbox_get=="Biots(Bi)":
                                def convert():
                                    ESUs = float(input_entry.get())
                                    bio = float(ESUs/2.9979245368431e+10)
                                    bio = round(bio, 15)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bio}")
                                heading_label.config( text = "ESUs of Current to Biots(Bi)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter ESUs of Current:")
                                input_EL.config( text = "ESU")
                                output_OL.config( text = "Bi")

                            elif tolistbox_get=="EMUs of Current":
                                def convert():
                                    ESUs = float(input_entry.get())
                                    EMUs = float(ESUs/2.9979245368431e+10)
                                    EMUs = round(EMUs, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{EMUs}")
                                heading_label.config( text = "ESUs of Current to EMUs of Current",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter ESUs of Current:")
                                input_EL.config( text = "ESU")
                                output_OL.config( text = "EMU")

                            elif tolistbox_get=="Statamperes(stA)":
                                def convert():
                                    ESUs = float(input_entry.get())
                                    stA = float(ESUs*1)
                                    stA = round(stA, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{stA}")
                                heading_label.config( text = "ESUs of Current to Statamperes(stA)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter ESUs of Current:")
                                input_EL.config( text = "ESU")
                                output_OL.config( text = "stA")

                        to_listbox.bind("<<ListboxSelect>>", to_box)

                    elif fromlistbox_get=="Statamperes(stA)":

                        def to_box(event):

                            tolistbox_get = str(to_listbox.get(ANCHOR))

                            if tolistbox_get=="Abamperes(abA)":
                                def convert():
                                    stA = float(input_entry.get())
                                    abA = float(stA/2.9979245368431e+10)
                                    abA = round(abA, 15)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{abA}")
                                heading_label.config( text = "Statamperes(stA) to Abamperes(abA)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Statamperes(stA):")
                                input_EL.config( text = "stA")
                                output_OL.config( text = "abA")

                            elif tolistbox_get=="Amperes(A)":
                                def convert():
                                    stA = float(input_entry.get())
                                    amp = float(stA/2.9979245368431e+9)
                                    amp = round(amp, 13)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{amp}")
                                heading_label.config( text = "Statamperes(stA) to Amperes(A)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Statamperes(stA):")
                                input_EL.config( text = "stA")
                                output_OL.config( text = "A")

                            elif tolistbox_get=="Biots(Bi)":
                                def convert():
                                    stA = float(input_entry.get())
                                    bio = float(stA/2.9979245368431e+10)
                                    bio = round(bio, 15)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{bio}")
                                heading_label.config( text = "Statamperes(stA) to Biots(Bi)",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Statamperes(stA):")
                                input_EL.config( text = "stA")
                                output_OL.config( text = "stA")

                            elif tolistbox_get=="EMUs of Current":
                                def convert():
                                    stA = float(input_entry.get())
                                    EMUs = float(stA/2.9979245368431e+10)
                                    EMUs = round(EMUs, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{EMUs}")
                                heading_label.config( text = "Statamperes(stA) to EMUs of Current",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Statamperes(stA):")
                                input_EL.config( text = "stA")
                                output_OL.config( text = "EMU")

                            elif tolistbox_get=="ESUs of Current":
                                def convert():
                                    stA = float(input_entry.get())
                                    ESUs = float(stA*1)
                                    ESUs = round(ESUs, 3)
                                    output_entry.delete(0, END)
                                    output_entry.insert(1, f"{ESUs}")
                                heading_label.config( text = "Statamperes(stA) to ESUs of Current",background = "white")
                                convert_button.config(command = convert)
                                enter_label.config(text = "Enter Statamperes(stA):")
                                input_EL.config( text = "stA")
                                output_OL.config( text = "ESU")

                        to_listbox.bind("<<ListboxSelect>>", to_box)


                def to_snapHighlightToMouse(event):
                    to_listbox.selection_clear(0, END)
                    to_listbox.selection_set(to_listbox.nearest(event.y))

                def to_unhighlight():
                    to_listbox.selection_clear(0, END)    

                def snapHighlightToMouse(event):
                    from_listbox.selection_clear(0, END)
                    from_listbox.selection_set(from_listbox.nearest(event.y))

                def unhighlight():
                    from_listbox.selection_clear(0, END)    

                scientific_heading.config(text = "Pressure", foreground = "red", background = "sky blue")

                to_listbox.delete(0,END)
                for item in range(len(current_dict)):
                    to_listbox.insert(END, current_dict[item])

                to_listbox.bind('<Motion>', lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Enter>',  lambda event: to_snapHighlightToMouse(event))
                to_listbox.bind('<Leave>',  lambda _: to_unhighlight())

                from_listbox.delete(0,END)
                for item in range(len(current_dict)):
                    from_listbox.insert(END, current_dict[item])

                from_listbox.bind('<<ListboxSelect>>', from_box)
                from_listbox.bind('<Leave>',  lambda _: unhighlight())
                from_listbox.bind('<Motion>', lambda event: snapHighlightToMouse(event))
                from_listbox.bind('<Enter>',  lambda event: snapHighlightToMouse(event))
                #****************************Current Converter Starts Here******************************

        def snapHighlightToMouse(event):
            listbox.selection_clear(0, END)
            listbox.selection_set(listbox.nearest(event.y))

        def unhighlight():
            listbox.selection_clear(0, END)


        science_dict = ["Temperature", "Pressure", "Time", "Current"]
        temp_dict = ["Kelvin(K)","Fahrenheit(\u00b0F)","Celcius/Centigrade(\u00b0C)","Rankine(\u00b0R / \u00b0Ra)","Réaumur(\u00b0Ré / \u00b0Re)","Rømer(\u00b0Rø)","Newton(\u00b0N)","Delisle(\u00b0D)","Wedgwood(\u00b0W)",]
        pressure_dict =["Pascals(Pa)", "Standard Atmosphere(atm)", "Torr(Torr)", "Bar(bar)", "Pounds per Square Inch (psi or lb/in\u00b2)", "Technical Atmosphere (at or kgf/cm\u00b2)", "Barye(Ba)", "Pièze(pz)", "mm of Mercury(mmHg)"]
        time_dict = ["Centuries", "Days", "Decades", "Hours", "Minutes", "Months", "Seconds", "Tropical Year", "Weeks", "Years"]
        current_dict = ["Abamperes(abA)", "Amperes(A)", "Biots(Bi)", "EMUs of Current", "ESUs of Current", "Statamperes(stA)"]
        
        root["background"] = "#C0FF00"

        science_frame = md.Frame(root, background="#C0FF00")
        science_frame.pack()        

        science_heading_label= Label(science_frame, background="#C0FF00", text = "Scientific Converter", foreground = "Blue",  font = ("Bookman Old Style", 30, "bold"),padding = (100,5))
        science_heading_label.grid()

#All frames here**************************************************************************************
        scientific_heading_frame = md.Frame(science_frame, background="#C0FF00")
        scientific_heading_frame.grid()

        listbox_frame = md.Frame(science_frame, background="#C0FF00")
        listbox_frame.grid()
        
        conversion_frame = md.Frame(science_frame, background="#C0FF00")
        conversion_frame.grid()
     
#*************************************************Headings*********************************************
        scientific_heading = Label(scientific_heading_frame, background="#C0FF00", font =("Bookman Old Style", 25, "bold"),padding = (100,1))
        scientific_heading.grid(row = 0)

        heading_label= Label(scientific_heading_frame, background="#C0FF00",  font =(("Times New Roman"), 20),padding = (100,5))
        heading_label.grid(row = 1, pady = 5)


#********************************Main List Box****************************************
        listbox = md.Listbox(listbox_frame, width = 20, height = 10, font ="verdana 11 bold")
        listbox.grid(row = 1, column = 1,)
        for item in range(len(science_dict)):
            listbox.insert(END, science_dict[item])
        listbox.bind('<<ListboxSelect>>', nextbox)
        listbox.bind('<Motion>', lambda event: snapHighlightToMouse(event))
        listbox.bind('<Enter>',  lambda event: snapHighlightToMouse(event))
        listbox.bind('<Leave>',  lambda _: unhighlight())

#From Label, listbox and its scrollbar******************************************
        from_label= Label(listbox_frame, text = "From",anchor='s', font =("Times New Roman", 20), background="#C0FF00")
        from_label.grid(row = 0, column = 3)

        symbol_label = Label(listbox_frame, text = "→", font =("Algerian", 50, "bold"), background="#C0FF00")
        symbol_label.grid(row = 1, column = 2)
        
        from_listbox = md.Listbox(listbox_frame, width = 20, height = 10, font ="verdana 11")
        from_listbox.grid(row = 1, column = 3)
        
        scrollbar = Scrollbar(listbox_frame, orient="horizontal",command=from_listbox.xview)
        scrollbar.grid(row = 1, column = 3, sticky= S + E + W)

#To label, listbox and tis scrollbar******************************************
        symbol_label = Label(listbox_frame, text = "→", font =("Algerian", 50, "bold"), background="#C0FF00")
        symbol_label.grid(row = 1, column = 5)

        to_label= Label(listbox_frame, text = "To",anchor = 's', font =("Times New Roman", 20), background="#C0FF00")
        to_label.grid(row = 0, column = 6, sticky='s')
        
        to_listbox = md.Listbox(listbox_frame, width = 20, height = 10, font ="verdana 11")
        to_listbox.grid(row = 1, column = 6)

        scrollbar = Scrollbar(listbox_frame, orient="horizontal",command=to_listbox.xview,)
        scrollbar.grid(row = 1, column = 6, sticky= E + W + S)


#Convertion Part*************************************************************

        enter_label = md.Label(conversion_frame, font = "Verdana 16", padx = 30, background="#C0FF00")
        enter_label.grid(row = 3, column = 2, pady =5)

        input_entry = md.Entry(conversion_frame,justify="center", width=30, font = "Verdana 16")
        input_entry.grid(row = 4, column = 2, pady =5, sticky =(E, W))
        input_EL = md.Label(conversion_frame,  font = "verdana 16", padx = 10, background="#C0FF00")
        input_EL.grid(row = 4, column = 3, padx =3, sticky =(E, W))

        convert_button = md.Button(conversion_frame, text = "Convert To", font = ("Bookman Old Style", 18, "bold"))
        convert_button.grid(row = 5, column = 2, ipadx=10)

        output_entry = md.Entry(conversion_frame, width= 20,justify="center", font = "Verdana 16")
        output_entry.grid(row = 6, column = 2, pady = 5, sticky =(E, W))
        output_OL = md.Label(conversion_frame, font = "verdana 16", padx = 10, background="#C0FF00")
        output_OL.grid(row = 6, column = 3, padx =3, sticky =(E, W))



        button_frame = md.Frame(science_frame, background="#C0FF00")
        button_frame.grid(pady=20, sticky=S)
        
        back_button = md.Button(button_frame,background="#C0FF00",bd = 0, command = self.main_screen)
        back_button.grid(row = 1, column = 1, padx=50)
        def back_button_enter(e):
            back_button["bg"] = "grey"
            back_label.config(text = "Home", font = ("Bookman Old Style", 13))
            statusvar.set("Go to Home!")

        def back_button_leave(e):
            back_button["bg"] = '#C0FF00'
            back_label.config(text = "")
            statusvar.set("Status is good.")

        back_label = Label(button_frame,background="#C0FF00", font = ("Bookman Old Style", 13))
        back_label.grid(row = 0, column = 1, sticky=S)
        back_button.bind("<Enter>", back_button_enter)
        back_button.bind("<Leave>", back_button_leave)
        
        image = Image.open("img/home.png")
        resize_image = image.resize((60,58), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        back_button.img_ref = img
        back_button.config(image = img, justify=LEFT)


        standard_button = md.Button(button_frame, bg = '#C0FF00', bd = 0, padx = 20, command = self.standard_converter)
        standard_button.grid(row = 1, column = 2, padx = 50)
        def standard_entry(e):
            standard_button["bg"] = "grey"
            standard_label.config(text = "Standard", font = ("Bookman Old Style", 13))
            statusvar.set("Standard Converter")
        def standard_leave(e):
            statusvar.set("Status is good.")
            standard_button["bg"] = '#C0FF00'
            standard_label.config(text = "")
        standard_label = Label(button_frame, background="#C0FF00")
        standard_label.grid(row = 0, column = 2, sticky=S)
        standard_button.bind("<Enter>", standard_entry)
        standard_button.bind("<Leave>", standard_leave)

        image = Image.open("img/standard.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        standard_button.img_ref = img
        standard_button.config(image = img, justify=LEFT)


        currency_button = md.Button(button_frame,bg = '#C0FF00', bd = 0, padx = 20, command = self.currency_converter)
        currency_button.grid(row = 1, column = 3, padx = 50)
        def binary_entry(e):
            currency_button["bg"] = "grey"
            currency_label.config(text = "Currency", font = ("Bookman Old Style", 13))
            statusvar.set("Currency Converter")
        def binary_leave(e):
            currency_button["bg"] = '#C0FF00'
            currency_label.config(text = "")
            statusvar.set("Status is good.")
        currency_label = Label(button_frame, background="#C0FF00")
        currency_label.grid(row = 0, column = 3, sticky=S)
        currency_button.bind("<Enter>", binary_entry)
        currency_button.bind("<Leave>", binary_leave)

        image = Image.open("img/currency.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        currency_button.img_ref = img
        currency_button.config(image = img, justify=LEFT)


        binary_button = md.Button(button_frame,bg = '#C0FF00', bd = 0, padx = 20, command = self.binary_to_decimal)
        binary_button.grid(row = 1, column = 4, padx = 50)
        def binary_entry(e):
            binary_button["bg"] = "grey"
            binary_label.config(text = "B ⇌ D", font = ("Bookman Old Style", 13))
            statusvar.set("Binary Converter")
        def binary_leave(e):
            binary_button["bg"] = '#C0FF00'
            binary_label.config(text = "")
            statusvar.set("Status is good.")
        binary_label = Label(button_frame, background="#C0FF00")
        binary_label.grid(row = 0, column = 4, sticky=S)
        binary_button.bind("<Enter>", binary_entry)
        binary_button.bind("<Leave>", binary_leave)

        image = Image.open("img/binary.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        binary_button.img_ref = img
        binary_button.config(image = img, justify=LEFT)


        calculator_button = md.Button(button_frame,bg = '#C0FF00', bd = 0, padx = 20, command = open_Calculator)
        calculator_button.grid(row = 1, column = 5, padx = 50)
        def binary_entry(e):
            calculator_button["bg"] = "grey"
            calculator_label.config(text = "Calculator", font = ("Bookman Old Style", 13))
            statusvar.set("Calculator")
        def binary_leave(e):
            calculator_button["bg"] = '#C0FF00'
            calculator_label.config(text = "")
            statusvar.set("Status is good.")
        calculator_label = Label(button_frame, background="#C0FF00")
        calculator_label.grid(row = 0, column = 5, sticky=S)
        calculator_button.bind("<Enter>", binary_entry)
        calculator_button.bind("<Leave>", binary_leave)

        image = Image.open("img/calculator.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize_image)
        calculator_button.img_ref = img
        calculator_button.config(image = img, justify=LEFT)

        self.frame = science_frame





#*********************************BINARY CONVERTER STARTS HERE************************************************
#*************************************************************************************************************

    def binary_to_decimal(self, *args):
        from numpy import binary_repr
        import itertools
        self.frame.destroy()
        width = root.winfo_width()
        height = root.winfo_height()
        root.update()
        root.background_image = background_image = PhotoImage(file = r"img/binary_wall.png")


        mainframe = Canvas(root, height =height, width=width)
        mainframe.pack(fill = 'both', expand=True)
        mainframe.create_image(0, 0, image = background_image, anchor = 'nw')

        def decimal_2_bin(*args):
            try:
                value = int(decimal.get())
                binary.set(binary_repr(value, None))
            except ValueError:
                pass

        def BtoD():
            global info_button

            def main_function():
                value = 0
                binary = list(decimal_entry.get())
                for i in range(len(binary)):
                    digit = binary.pop()

                    if digit == '1':
                        value = value + pow(2, i)
                binary_output.delete(0, END)
                binary_output.insert(1, value)

            binary_output.delete(0, END)
            decimal_entry.delete(0, END)

            def info_button_leave(e, *args):
                info_enter.pack_forget()
            def info_button_enter(e):
                info_enter.pack(pady = 100,padx =50, anchor='e')

            note_var="Note: In Binary to Decimal\nconverter if you put any\ndecimal number in Binary\nfield, it will treat that\nnumber as zero!"
            info_enter = md.Text(mainframe,width = 23,height=5, font = ("Bookman Old Styel", 11,'bold'))
            info_enter.insert(INSERT,note_var)
            info_enter.configure(state='disabled')
            
            i_image = Image.open("img/info_button.png")
            resized_image = i_image.resize((40,38), Image.ANTIALIAS)
            root.img_info = img_info = ImageTk.PhotoImage(resized_image)

            info_button = mainframe.create_image(f'{width/2+230}', 150, image = img_info)
            mainframe.tag_bind(info_button, "<Leave>", info_button_leave)
            mainframe.tag_bind(info_button, "<Enter>", info_button_enter)

            mainframe.itemconfig(main_head, text = "Binary To Decimal",font = ("Bookman Old Style",40,"bold"), fill = 'red')

            mainframe.itemconfig(first_head, text="Enter Binary Number:",font = ("Bookman Old Style", 25, "bold"), fill ='BLue')

            mainframe.itemconfig(second_head, text="Decimal", font = ("Bookman Old Style", 25, "bold"), fill = 'blue')

            calculat_button.configure(command = main_function)


        def DtoB():

            def decimal_2_bin(*args):
                try:
                    value = int(decimal.get())
                    binary.set(binary_repr(value, None))
                except ValueError:
                    pass

            binary_output.delete(0, md.END)
            decimal_entry.delete(0, md.END)
            
            mainframe.delete(info_button)

            mainframe.itemconfig(main_head, text = "Decimal To Binary",font = ("Bookman Old Style",40,"bold"), fill = 'red')

            mainframe.itemconfig(first_head, text="Enter Decimal Number:",font = ("Bookman Old Style", 25, "bold"), fill ='BLue')

            mainframe.itemconfig(second_head, text="Binary", font = ("Bookman Old Style", 25, "bold"), fill = 'blue')

            calculat_button.configure(command = decimal_2_bin)


        main_head = mainframe.create_text(f'{width/2}', 40, text = "Decimal To Binary",font = ("Bookman Old Style",40,"bold"), fill = 'red')


        first_head = mainframe.create_text(f'{width/2}', 110, text="Enter Decimal Integer:",font = ("Bookman Old Style", 25, "bold"), fill = 'blue')

        decimal = StringVar()
        decimal_entry = md.Entry(mainframe, width=30, justify=CENTER,textvariable=decimal, font = ("Bookman Old Style", 15, "bold"))
        mainframe.create_window(f'{width/2}', 150, window = decimal_entry)

        second_head = mainframe.create_text(f'{width/2}',220, text="Binary", font = ("Bookman Old Style", 25, "bold"), fill = 'blue')

        binary = StringVar()
        binary_output = md.Entry(mainframe, width=30,justify=CENTER, textvariable=binary, font = ("Bookman Old Style", 20, "bold"))
        mainframe.create_window(f'{width/2}',260, window = binary_output)


        calculat_button = md.Button(mainframe, text="Calculate", command=decimal_2_bin,font = ("Bookman Old Style", 15, "bold"))
        calculat_button.pack()
        mainframe.create_window(f'{width/2}',320, window = calculat_button)

        decimal_entry.focus()
        root.bind("<Return>", decimal_2_bin)


        toggle_funcs = itertools.cycle((BtoD, DtoB))

        def toggle():
            func = next(toggle_funcs)
            func()

        cycle_button = md.Button(mainframe,font = ("Bookman Old Style", 15, "bold"), text = "Binary ⇌ Decimal", command = toggle)
        cycle_button_window = mainframe.create_window(f'{width/2}', 420, window = cycle_button)



        def home_button_enter(e):
            mainframe.itemconfig(blink_home, text = "Home", font = ("Bookman Old Style", 13, "bold"),fill = 'red')
            statusvar.set("Go to Home!")
        def home_button_leave(e):
            mainframe.itemconfig(blink_home, text = " ")
            statusvar.set("Status is good.")

        image = Image.open("img/home.png")
        resize_image = image.resize((60,58), Image.ANTIALIAS)
        root.img_home = img_home = ImageTk.PhotoImage(resize_image)

        blink_home = mainframe.create_text(f'{width/6.4+5}', 550,anchor="nw")
        home_button = mainframe.create_image(f'{width/6.4}', 580, image = img_home, anchor = 'nw')
        mainframe.tag_bind(home_button, "<Button-1>", self.main_screen)
        mainframe.tag_bind(home_button, "<Leave>", home_button_leave)
        mainframe.tag_bind(home_button, "<Enter>", home_button_enter)



        def standard_button_enter(e):
            mainframe.itemconfig(blink_standard, text = "Standard", font = ("Bookman Old Style", 13, "bold"),fill = 'red')
            statusvar.set("Standard Converter")
        def standard_button_leave(e):
            mainframe.itemconfig(blink_standard, text = " ")
            statusvar.set("Status is good.")

        image = Image.open("img/standard.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        root.img_standard = img_standard = ImageTk.PhotoImage(resize_image)

        blink_standard = mainframe.create_text(f'{width/6.4*2-10}', 550,anchor="nw")
        standard_button = mainframe.create_image(f'{width/6.4*2}', 580, image = img_standard, anchor = 'nw')
        mainframe.tag_bind(standard_button, "<Button-1>", self.standard_converter)
        mainframe.tag_bind(standard_button, "<Leave>", standard_button_leave)
        mainframe.tag_bind(standard_button, "<Enter>", standard_button_enter)



        def scientific_button_enter(e):
            mainframe.itemconfig(blink_scientific, text = "Scientific", font = ("Bookman Old Style", 13, "bold"),fill = 'red')
            statusvar.set("Scientific Converter")
        def scientific_button_leave(e):
            mainframe.itemconfig(blink_scientific, text = " ")
            statusvar.set("Status is good.")

        image = Image.open("img/scientific.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        root.img_scientific = img_scientific = ImageTk.PhotoImage(resize_image)

        blink_scientific = mainframe.create_text(f'{width/6.4*3-10}', 550,anchor="nw")
        scientific_button = mainframe.create_image(f'{width/6.4*3}', 580, image = img_scientific, anchor = 'nw')
        mainframe.tag_bind(scientific_button, "<Button-1>", self.scientific_converter)
        mainframe.tag_bind(scientific_button, "<Leave>", scientific_button_leave)
        mainframe.tag_bind(scientific_button, "<Enter>", scientific_button_enter)



        def currency_button_enter(e):
            mainframe.itemconfig(blink_currency, text = "Currency", font = ("Bookman Old Style", 13, "bold"),fill = 'red')
            statusvar.set("Currency Converter")
        def currency_button_leave(e):
            mainframe.itemconfig(blink_currency, text = " ")
            statusvar.set("Status is good.")

        image = Image.open("img/currency.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        root.img_currency = img_currency = ImageTk.PhotoImage(resize_image)

        blink_currency = mainframe.create_text(f'{width/6.4*4-10}', 550,anchor="nw")
        currency_button = mainframe.create_image(f'{width/6.4*4}', 580, image = img_currency, anchor = 'nw')
        mainframe.tag_bind(currency_button, "<Button-1>", self.currency_converter)
        mainframe.tag_bind(currency_button, "<Leave>", currency_button_leave)
        mainframe.tag_bind(currency_button, "<Enter>", currency_button_enter)



        def calculator_button_enter(e):
            mainframe.itemconfig(blink_calculator, text = "Calculator")
            statusvar.set("Calculator")
        def calculator_button_leave(e):
            mainframe.itemconfig(blink_calculator, text = " ")
            statusvar.set("Status is good.")
        image = Image.open("img/calculator.png")
        resize_image = image.resize((58,58), Image.ANTIALIAS)
        root.img_calculator = img_calculator = ImageTk.PhotoImage(resize_image)

        blink_calculator = mainframe.create_text(f'{width/6.4*5-10}', 550,anchor="nw", font = ("Bookman Old Style", 13, "bold"),fill = 'red')
        calculator_button = mainframe.create_image(f'{width/6.4*5}', 580, image = img_calculator, anchor = 'nw')
        mainframe.tag_bind(calculator_button, "<Button-1>", open_Calculator)
        mainframe.tag_bind(calculator_button, "<Leave>", calculator_button_leave)
        mainframe.tag_bind(calculator_button, "<Enter>", calculator_button_enter)



        self.frame = mainframe

#***********************************************BINARY CONVERTER ENDS HERE*******************************************************
#********************************************************************************************************************************





#***********************************************Currency Converter starts here*******************************************
#************************************************************************************************************************

    def currency_converter(self, *args):
        import webbrowser
        try:
            from tkinter import Tk, Frame
        except ImportError:
            from tkinter import Tk, Frame

        
        iExit = tmsg.askquestion("Currency", "You will be directed to Online Currency Converter for current Updates of currencies!\nDo you want to go to Currency Converter?\n\nNote: Please make sure you are connected to Internet.")
        root.wm_iconbitmap("img/unit converter.ico")
        if iExit=="yes":
            webbrowser.open_new(r"https://www.xe.com/currencyconverter/")

#***********************************************Currency Converter ends here*******************************************
#**********************************************************************************************************************

        
        

#Menu Bar start Here.

mainmenu = md.Menu(root)

#File Menu Start here.
def saveMenu():
    pass

def openMenu():
    pass

def historyMenu():
    pass

def exit_window(): 
    iExit = tmsg.askquestion("Converter", "Do you want to exit ?")
    root.wm_iconbitmap("img/unit converter.ico")
    if iExit=="yes":
        root.destroy()
fileMenu = md.Menu(mainmenu, tearoff = 0)

fileMenu.add_command(label = "Save", state='disabled')
fileMenu.add_command(label = "Open", state='disabled')
fileMenu.add_separator()
fileMenu.add_command(label = "History", state='disabled')
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command = exit_window)
root.config(menu = mainmenu)
mainmenu.add_cascade(menu = fileMenu, label = "File")



#viewMenu Starts Here.
def fullsize():
    root.state(newstate = 'zoomed')

def originalSize():
    root.state(newstate='normal')

def zoomIn():
    pass

def zoomOut():
    pass

def fullScreen():
    pass

def lowQuality():
    pass

def mediumQuality():
    pass

def highQuality():
    pass

viewMenu= md.Menu(mainmenu, tearoff = 0)
viewMenu.add_command(label = "Original Size", command = originalSize)
viewMenu.add_separator()
viewMenu.add_command(label = "Zoom In", state='disabled')
viewMenu.add_command(label = "Zoom Out", state='disabled')
viewMenu.add_separator()
viewMenu.add_command(label = "Full Screen", command = fullsize)
viewMenu.add_separator()
#Adding SubMenu to viewMenu.
qualityMenu = md.Menu(viewMenu, tearoff = 0)
qualityMenu.add_command(label = "Low", state='disabled')
qualityMenu.add_command(label = "Medium", state='disabled')
qualityMenu.add_command(label = "High", state='disabled')
viewMenu.add_cascade(menu = qualityMenu, label = "Quality")
#to here.
root.config(menu = mainmenu)
mainmenu.add_cascade(menu = viewMenu, label = "View")


#Control Menu Starts Here.
def windowSize():
    def release():
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())
        root.geometry(f'{new_width}x{new_height}')
        window_pop.destroy()
    
    window_pop = md.Toplevel(root)
    window_pop.wm_iconbitmap("img/unit converter.ico")
    window_pop.grab_set()
    window_pop.geometry("370x170")


    width_label = md.Label(window_pop, text = "Enter the width of window (in pixels):", font = 'Helvetica 12')
    width_label.grid(row = 1, column=1, pady = 10)
    width_entry = md.Entry(window_pop, width = 10,font = 'Helvetica 12')
    width_entry.grid(row = 1, column = 2, padx = 2)
    height_label = md.Label(window_pop, text = "Enter the Height of window (in pixels):", font = 'Helvetica 12')
    height_label.grid(row = 2, column=1, pady = 10)
    height_entry = md.Entry(window_pop, width = 10,font = 'Helvetica 12')
    height_entry.grid(row = 2, column = 2, padx = 2)
    
    md.Label(window_pop, text = "\"Minimum Size of Window is 1000x750\"", fg="red", font = "Helvetica 12").grid(row = 3, column =1, columnspan=2)
    
    change_button = md.Button(window_pop, text = 'Change', command = release, font = ("Georgia", 14, "bold"), bg = 'light gray')
    change_button.grid(row = 4, column = 1, columnspan=2)

    window_pop.mainloop()

def backgroundColor():
    pass

def download():
    pass

def find():
    pass

def replace():
    pass

controlMenu= md.Menu(mainmenu, tearoff = 0)
controlMenu.add_command(label = "Window Size", command = windowSize)
controlMenu.add_command(label = "Background Color", state = 'disabled')
controlMenu.add_separator()
#Adding subMenu to control Menu from here.
downloadMenu = md.Menu(controlMenu, tearoff =0)
downloadMenu.add_command(label = "Basic Converter")
downloadMenu.add_command(label = "Scientific Converter")
controlMenu.add_cascade(menu = downloadMenu, label = "Download Data", state = 'disabled')
#to here
controlMenu.add_separator()
controlMenu.add_command(label = "Find", state = 'disabled')
controlMenu.add_command(label = "Replace", state = 'disabled')
root.config(menu = mainmenu)
mainmenu.add_cascade(menu = controlMenu, label = "Contol")

def about_us():
    tmsg.showinfo("About!", "This converter is made, to fulfil the purpose of mini project in 2nd year B.Tech. Which is made in *Python* using tkinter module.")
def contact_us():
    tmsg.showinfo("Contact", "E-mail: danish.00@gmail.com\nMobile No: 2245248765\n\nIf you have any suggestions or facing any issue related to the app, feel free to contact us.\n\nThank you for choosing us.")
helpMenu = md.Menu(mainmenu, tearoff = 0)
helpMenu.add_command(label = "About", command=about_us)
helpMenu.add_command(label = "Contact", command=contact_us)
root.config(menu = mainmenu)
mainmenu.add_cascade(menu = helpMenu, label="Help")


from tkinter.ttk import *
style = Style()
 
style.configure('TButton', font =
                ('Georgia', 30 , 'bold'),
                    borderwidth = '4')
 

style.map('TButton', foreground = [('active', '!disabled', '#0C00FF')],
                     background = [('active', 'red')])

#status bar.......
statusvar = md.StringVar()
statusvar.set("Status is good.")
sbar = md.Label(root, textvariable = statusvar, relief = SUNKEN, anchor = "w")
sbar.pack(side = BOTTOM, fill = X)


#Sub title bar**********************************
def shift():
    x1,y1,x2,y2 = sub_Title.bbox("marquee")
    if(x2<0 or y1<0): 
        x1 = sub_Title.winfo_width()
        y1 = sub_Title.winfo_height()//2
        sub_Title.coords("marquee",x1,y1)
    else:
        sub_Title.move("marquee", -2, 0)
    sub_Title.after(1000//fps,shift)

sub_Title = md.Canvas(root,background='yellow',)
sub_Title.pack(side = BOTTOM, fill = X)     
text_var="Made by MD.DANISH (B.Tech IInd Year)"
text=sub_Title.create_text(0,-2000,text=text_var,fill = 'red',font=('Times New Roman',15,'bold'),tags=("marquee"),anchor='w')
x1,y1,x2,y2 = sub_Title.bbox("marquee")
width1 = x2-x1
height1 = y2-y1
sub_Title['width']=width1
sub_Title['height']=height1
fps=40
shift()
#Sub title bar ends here************************

screen = Screens()

root.mainloop()