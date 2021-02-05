from tkinter import *
from tkinter import messagebox
from math import *

class Trojkat(object):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def pole(self):
        p = (self.a+self.b+self.c)/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def obwod(self):
        return self.a+self.b+self.c

    def wysokoscNaBokA(self):
        return (2*self.pole())/self.a

    def wysokoscNaBokB(self):
        return (2*self.pole())/self.b

    def wysokoscNaBokC(self):
        return (2*self.pole())/self.c


    def katPomiedzyBokamiAB(self):
        alfa = ((self.a*self.a)+(self.b*self.b)-(self.c*self.c))/(2*self.a*self.b)
        return self.radiany_na_stopnie(acos(alfa))

    def katPomiedzyBokamiAC(self):
        alfa = ((self.a*self.a)+(self.c*self.c)-(self.b*self.b))/(2*self.a*self.c)
        return self.radiany_na_stopnie(acos(alfa))

    def katPomiedzyBokamiBC(self):
        alfa = ((self.c*self.c)+(self.b*self.b)-(self.a*self.a))/(2*self.b*self.c)
        return self.radiany_na_stopnie(acos(alfa))

    def radiany_na_stopnie(self, rad):
        return (360 * rad) / (2 * pi)




#t1 = Trojkat(4,5,6)
# print("Pole:",t1.pole())
# print("Obwód:",t1.obwod())
# print("Wysokość na bok a:",t1.wysokoscNaBokA())
# print("Wysokość na bok b:",t1.wysokoscNaBokB())
# print("Wysokość na bok c:",t1.wysokoscNaBokC())
# print("Kąt pomiedzy bokami ab:",t1.katPomiedzyBokamiAB())
# print("Kąt pomiedzy bokami ac:",t1.katPomiedzyBokamiAC())
# print("Kąt pomiedzy bokami bc:",t1.katPomiedzyBokamiBC())

class WrongDataError(Exception):
    pass

class MissingDataError(Exception):
    pass

class Application(object):
    def __init__(self):
        self.okno = Tk()
        self.okno.geometry("600x400")
        self.okno.title("Parametry trójkąta")
        self.frame = Frame(self.okno)
        self.frame.grid()
        self.frame.pack()
        self.dodajWidgety()
        self.okno.mainloop()

    def oblicz(self):
        try:
            a = self.inputBokA.get()
            b = self.inputBokB.get()
            c = self.inputBokC.get()

            if (len(a) == 0 and len(b) == 0 and len(c) == 0):
                raise MissingDataError

            self.messageError = "Błędna długość boku A"
            a = float(a)
            self.messageError = "Błędna długość boku B"
            b = float(b)
            self.messageError = "Błędna długość boku C"
            c = float(c)


            if(a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a):
                trojkat = Trojkat(a,b,c)
            else:
                raise WrongDataError
            
        except WrongDataError:
            messagebox.showinfo("Błąd", "Z podanych danych nie da się utworzyć trójkąta.")
        except MissingDataError:
            messagebox.showinfo("Błąd", "Wpisz długości boków trójkąta aby obliczyć jego parametry.")
        except ValueError:
            messagebox.showinfo("Błąd", self.messageError)
        except:
            messagebox.showerror("Błąd", "Nierozpoznany błąd.")
        else:
            self.precyzja = 5
            ################################
            self.outputPole["state"] = "normal"
            self.outputPole.delete(0.0, END)
            self.outputPole.insert(0.0, str(round(trojkat.pole(),self.precyzja)))
            self.outputPole["state"] = "disable"
            ################################
            self.outputObwod["state"] = "normal"
            self.outputObwod.delete(0.0, END)
            self.outputObwod.insert(0.0,str(round(trojkat.obwod(),self.precyzja)))
            self.outputObwod["state"] = "disable"
            ################################
            self.outputWysokoscNaBokA["state"] = "normal"
            self.outputWysokoscNaBokA.delete(0.0, END)
            self.outputWysokoscNaBokA.insert(0.0, str(round(trojkat.wysokoscNaBokA(),self.precyzja)))
            self.outputWysokoscNaBokA["state"] = "disable"
            ################################
            self.outputWysokoscNaBokB["state"] = "normal"
            self.outputWysokoscNaBokB.delete(0.0, END)
            self.outputWysokoscNaBokB.insert(0.0, str(round(trojkat.wysokoscNaBokB(),self.precyzja)))
            self.outputWysokoscNaBokB["state"] = "disable"
            ################################
            self.outputWysokoscNaBokC["state"] = "normal"
            self.outputWysokoscNaBokC.delete(0.0, END)
            self.outputWysokoscNaBokC.insert(0.0, str(round(trojkat.wysokoscNaBokC(),self.precyzja)))
            self.outputWysokoscNaBokC["state"] = "disable"
            ################################
            self.outputKatMiedzyAB["state"] = "normal"
            self.outputKatMiedzyAB.delete(0.0, END)
            self.outputKatMiedzyAB.insert(0.0, str(round(trojkat.katPomiedzyBokamiAB(),self.precyzja)))
            self.outputKatMiedzyAB["state"] = "disable"
            ################################
            self.outputKatMiedzyAC["state"] = "normal"
            self.outputKatMiedzyAC.delete(0.0, END)
            self.outputKatMiedzyAC.insert(0.0, str(round(trojkat.katPomiedzyBokamiAC(),self.precyzja)))
            self.outputKatMiedzyAC["state"] = "disable"
            ################################
            self.outputKatMiedzyBC["state"] = "normal"
            self.outputKatMiedzyBC.delete(0.0, END)
            self.outputKatMiedzyBC.insert(0.0, str(round(trojkat.katPomiedzyBokamiBC(),self.precyzja)))
            self.outputKatMiedzyBC["state"] = "disable"


    def dodajWidgety(self):
        self.fontSize = ("Helvetica",10)
        ###############################
        tytul = Label(self.frame)
        tytul.config(font=("Courier", 15))
        tytul["text"] = "Aplikacja do obliczania parametrów trójkąta"
        tytul.grid(row=0, columnspan=2, pady=20)
        self.tytul = tytul


        ###############################
        etykietaBokA = Label(self.frame, font=self.fontSize)
        etykietaBokA["text"] = "Podaj długość boku A trójkąta: "
        etykietaBokA.grid(row=1,column=0) #sticky=E
        self.etykietaBokA = etykietaBokA

        inputBokA = Entry(self.frame, font=self.fontSize)
        inputBokA.grid(row=1,column=1)
        self.inputBokA = inputBokA

        ################################
        etykietaBokB = Label(self.frame, font=self.fontSize)
        etykietaBokB["text"] = "Podaj długość boku B trójkąta: "
        etykietaBokB.grid(row=2, column=0)
        self.etykietaBokA = etykietaBokB

        inputBokB = Entry(self.frame, font=self.fontSize)
        inputBokB.grid(row=2, column=1)
        self.inputBokB = inputBokB

        ###############################
        etykietaBokC = Label(self.frame, font=self.fontSize)
        etykietaBokC["text"] = "Podaj długość boku C trójkąta: "
        etykietaBokC.grid(row=3, column=0, pady=(0,20))
        self.etykietaBokC = etykietaBokC

        inputBokC = Entry(self.frame, font=self.fontSize)
        inputBokC.grid(row=3, column=1, pady=(0,20))
        self.inputBokC = inputBokC

        ###############################
        etykietaPole = Label(self.frame, font=self.fontSize)
        etykietaPole["text"] = "Pole trójkąta wynosi: "
        etykietaPole.grid(row=4, column=0)
        self.etykietaPole = etykietaPole

        outputPole = Text(self.frame, width=15, height=1, state=DISABLED, font=self.fontSize)
        outputPole.grid(row=4, column=1)
        self.outputPole = outputPole

        ###############################
        etykietaObwod = Label(self.frame, font=self.fontSize)
        etykietaObwod["text"] = "Obwód trójkąta wynosi: "
        etykietaObwod.grid(row=5, column=0)
        self.etykietaObwod = etykietaObwod

        outputObwod = Text(self.frame, width=15, height=1, state=DISABLED, font=self.fontSize)
        outputObwod.grid(row=5, column=1)
        self.outputObwod = outputObwod

        ###############################
        etykietaWysokoscNaBokA = Label(self.frame, font=self.fontSize)
        etykietaWysokoscNaBokA["text"] = "Wysokość trójkąta poprowadzona na bok A wynosi: "
        etykietaWysokoscNaBokA.grid(row=6, column=0)
        self.etykietaWysokoscNaBokA = etykietaWysokoscNaBokA

        outputWysokoscNaBokA = Text(self.frame, width=15, height=1, state=DISABLED, font=self.fontSize)
        outputWysokoscNaBokA.grid(row=6, column=1)
        self.outputWysokoscNaBokA = outputWysokoscNaBokA

        ###############################
        etykietaWysokoscNaBokB = Label(self.frame, font=self.fontSize)
        etykietaWysokoscNaBokB["text"] = "Wysokość trójkąta poprowadzona na bok B wynosi: "
        etykietaWysokoscNaBokB.grid(row=7, column=0)
        self.etykietaWysokoscNaBokB = etykietaWysokoscNaBokB

        outputWysokoscNaBokB = Text(self.frame, width=15, height=1, state=DISABLED, font=self.fontSize)
        outputWysokoscNaBokB.grid(row=7, column=1)
        self.outputWysokoscNaBokB = outputWysokoscNaBokB

        ###############################
        etykietaWysokoscNaBokC = Label(self.frame, font=self.fontSize)
        etykietaWysokoscNaBokC["text"] = "Wysokość trójkąta poprowadzona na bok C wynosi: "
        etykietaWysokoscNaBokC.grid(row=8, column=0)
        self.etykietaWysokoscNaBokC = etykietaWysokoscNaBokC

        outputWysokoscNaBokC = Text(self.frame, width=15, height=1, state=DISABLED, font=self.fontSize)
        outputWysokoscNaBokC.grid(row=8, column=1)
        self.outputWysokoscNaBokC = outputWysokoscNaBokC

        ###############################
        etykietaKatMiedzyAB = Label(self.frame, font=self.fontSize)
        etykietaKatMiedzyAB["text"] = "Kąt trójkąta pomiędzy bokami A oraz B wynosi: "
        etykietaKatMiedzyAB.grid(row=9, column=0)
        self.etykietaKatMiedzyAB = etykietaKatMiedzyAB

        outputKatMiedzyAB = Text(self.frame, width=15, height=1, state=DISABLED, font=self.fontSize)
        outputKatMiedzyAB.grid(row=9, column=1)
        self.outputKatMiedzyAB = outputKatMiedzyAB

        ###############################
        etykietaKatMiedzyAC = Label(self.frame, font=self.fontSize)
        etykietaKatMiedzyAC["text"] = "Kąt trójkąta pomiędzy bokami A oraz C wynosi: "
        etykietaKatMiedzyAC.grid(row=10, column=0)
        self.etykietaKatMiedzyAC = etykietaKatMiedzyAC

        outputKatMiedzyAC = Text(self.frame, width=15, height=1, state=DISABLED, font=self.fontSize)
        outputKatMiedzyAC.grid(row=10, column=1)
        self.outputKatMiedzyAC = outputKatMiedzyAC

        ###############################
        etykietaKatMiedzyBC = Label(self.frame, font=self.fontSize)
        etykietaKatMiedzyBC["text"] = "Kąt trójkąta pomiędzy bokami B oraz C wynosi: "
        etykietaKatMiedzyBC.grid(row=11, column=0)
        self.etykietaKatMiedzyBC = etykietaKatMiedzyBC

        outputKatMiedzyBC = Text(self.frame, width=15, height=1, state=DISABLED, font=self.fontSize)
        outputKatMiedzyBC.grid(row=11, column=1)
        self.outputKatMiedzyBC = outputKatMiedzyBC


        ###############################
        przycisk = Button(self.frame, font=self.fontSize)
        przycisk["text"] = "Oblicz parametry trójkąta"
        przycisk.grid(row=12, columnspan=2, pady=20)
        przycisk["command"] = self.oblicz
        self.przycisk = przycisk



app = Application()