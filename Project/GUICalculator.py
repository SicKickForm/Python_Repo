from tkinter import *
from tkinter import messagebox

# GUI Calculator

class Calc(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("Calculator")
        self.master.configure(background='white')
        self.master.resizable(width=False, height=False)
        self.master.geometry("465x540+540+120")
        self.master = master

        self.Screen = Text(master, height=2, width=30, pady=6, padx=6,
                           bg="#000000", fg="#dddddd", font=('Helvetica', 20, 'bold'))
        self.Screen.grid(row=0, column=0, columnspan=4)
        self.Screen.insert(INSERT, "0")

        Btn_1 = Button(master, text="1", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(1))
        Btn_1.grid(row=2, column=0)

        Btn_2 = Button(master, text="2", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(2))
        Btn_2.grid(row=2, column=1)

        Btn_3 = Button(master, text="3", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(3))
        Btn_3.grid(row=2, column=2)

        Btn_4 = Button(master, text="4", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(4))
        Btn_4.grid(row=3, column=0)

        Btn_5 = Button(master, text="5", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(5))
        Btn_5.grid(row=3, column=1)

        Btn_6 = Button(master, text="6", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(6))
        Btn_6.grid(row=3, column=2)

        Btn_7 = Button(master, text="7", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(7))
        Btn_7.grid(row=4, column=0)

        Btn_8 = Button(master, text="8", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(8))
        Btn_8.grid(row=4, column=1)

        Btn_9 = Button(master, text="9", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(9))
        Btn_9.grid(row=4, column=2)

        Btn_0 = Button(master, text="0", width=6, height=2, bd=4,
                       bg='#000000', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                       command=lambda: self.Num_Input(0))
        Btn_0.grid(row=5, column=1)

        Btn_Plus = Button(master, text="+", width=6, height=2, bd=4,
                          bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                          command=lambda: self.Num_Input("+"))
        Btn_Plus.grid(row=1, column=3)

        Btn_Minus = Button(master, text="-", width=6, height=2, bd=4,
                           bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                           command=lambda: self.Num_Input("-"))
        Btn_Minus.grid(row=2, column=3)

        Btn_Multi = Button(master, text="*", width=6, height=2, bd=4,
                            bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                            command=lambda: self.Num_Input("*"))
        Btn_Multi.grid(row=3, column=3)

        Btn_Divide = Button(master, text="/", width=6, height=2, bd=4,
                            bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                            command=lambda: self.Num_Input("/"))
        Btn_Divide.grid(row=4, column=3)

        Btn_LeftP = Button(master, text="(", width=6, height=2, bd=4,
                           bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                           command=lambda: self.Num_Input("("))
        Btn_LeftP.grid(row=1, column=1)

        Btn_RightP = Button(master, text=")", width=6, height=2, bd=4,
                            bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                            command=lambda: self.Num_Input(")"))
        Btn_RightP.grid(row=1, column=2)

        Btn_Dot = Button(master, text=".", width=6, height=2, bd=4,
                         bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                         command=lambda: self.Num_Input("."))
        Btn_Dot.grid(row=5, column=2)

        Btn_Calculate = Button(master, text="=", width=6, height=2, bd=4,
                               bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                               command=self.Output)
        Btn_Calculate.grid(row=5, column=3)

        Btn_Clear = Button(master, text="Clear", width=6, height=2, bd=4,
                           bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                           command=self.C)
        Btn_Clear.grid(row=1, column=0)

        Btn_Exit = Button(master, text="Exit", width=6, height=2, bd=4,
                          bg='#0011cc', fg="#dddddd", font=('Helvetica', 20, 'bold'),
                          command=self.Exit)
        Btn_Exit.grid(row=5, column=0)

    def Num_Input(self, num):
        if self.Screen.get("0.0", END) == "0\n":
            self.Screen.delete("0.0", END)
        self.Screen.insert(INSERT, str(num))

    def Output(self):
        res = self.Calculation(self.Screen.get("0.0", END)[:-1])
        self.Screen.delete("0.0", END)
        self.Screen.insert(INSERT, str(res))

    def Calculation(self, Exp):
        if Exp == "ERROR":
            return "ERROR"
        try:
            return (float(Exp))
        except ValueError:
            if ")" in Exp:
                Index = 0
                StartIndex = 0
                EndIndex = 0
                for i in range(0, len(Exp)):
                    if Exp[i] == "(":
                        Index += 1
                        StartIndex = i
                    if Exp[i] == ")":
                        Index -= 1
                if Index != 0:
                    messagebox.showerror(
                        "Error", "Brackets don't match!")
                    return "ERROR"
                for i in range(StartIndex, len(Exp)):
                    if Exp[i] == ")":
                        EndIndex = i
                        break
                New_Exp = Exp[:StartIndex] + str(self.Calculation(
                    Exp[StartIndex+1:EndIndex])) + Exp[EndIndex+1:]
                return self.Calculation(New_Exp)
            elif "+" in Exp:
                New_Exp2 = Exp.split("+")
                Rest = self.Calculation(New_Exp2[0])
                for j in New_Exp2[1:]:
                    Rest += self.Calculation(j)
                return Rest
            elif "-" in Exp:
                New_Exp2 = Exp.split("-")
                Rest = self.Calculation(New_Exp2[0])
                for j in New_Exp2[1:]:
                    Rest -= self.Calculation(j)
                return Rest
            elif "*" in Exp:
                New_Exp2 = Exp.split("*")
                Rest = self.Calculation(New_Exp2[0])
                for j in New_Exp2[1:]:
                    Rest *= self.Calculation(j)
                return Rest
            elif "/" in Exp:
                New_Exp2 = Exp.split("/")
                Rest = self.Calculation(New_Exp2[0])
                for j in New_Exp2[1:]:
                    try:
                        Rest /= self.Calculation(j)
                    except ZeroDivisionError:
                        messagebox.showerror("Error", "ERROR: Division by 0!")
                        return "ERROR"
                return Rest
            else:
                messagebox.showerror("Error", "ERROR: Invalid expression!")
                return "ERROR"

    def C(self):
        self.Screen.delete("0.0", END)
        self.Screen.insert(INSERT, "0")

    def Exit(self):
        Exit_Req = messagebox.askyesno("Calculator", "Do You want to exit?")
        if Exit_Req == True:
            Root.destroy()

Root = Tk()
App = Calc(Root)
Root.mainloop()
