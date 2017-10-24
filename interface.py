import matplotlib
matplotlib.use('TkAgg')

from tkinter import *
import tkinter as tk
import time
from datetime import datetime
from PIL import ImageTk, Image

class Janela_Principal():

    def __init__(self):
        self.user = "Gabriel"
        self.window = tk.Tk()
        self.window.geometry("600x500+100+100")
        self.window.title("MSN")
        self.window.configure(background = 'white')
        self.window.resizable(True, True)

        # Geometria da pagina
        self.window.rowconfigure(0, minsize = 120)
        self.window.rowconfigure(1, minsize = 10)
        self.window.rowconfigure(2, minsize = 60)
        self.window.rowconfigure(3, minsize = 10)
        self.window.columnconfigure(0, minsize = 40)
        self.window.columnconfigure(1, minsize = 20)




        #Label
        self.Logo = ImageTk.PhotoImage(Image.open("chat3.jpg"))
        self.Logo_label = tk.Label(self.window, image = self.Logo, height = 1, width = 1, borderwidth=2)
        self.Logo_label.grid(row = 0, column = 0, sticky = "nsew")

        self.textView = Text(self.window, height=15, width=85)
        self.textView.grid(row=1 ,column = 0, sticky = "nsew")
        # quote = """Conversa"""
        # self.textView.insert(END, quote)

        # Botoes
        self.textField = Text(self.window, height=1, width = 1)
        self.textField.grid(row = 2 ,column = 0,sticky = "nsew")
        quoteq = "Escreva aqui"
        self.textField.insert(END, quoteq)

        self.button_treinar = tk.Button(self.window, text = "SEND", height = 3, width = 10)
        self.button_treinar.grid(row = 3, column = 0,sticky = "nsew")
        self.button_treinar.configure(command = self.Send)

        

        self.var = StringVar(self.window)
        self.var.set("Choose your port") # initial value


        # self.text = "Waiting"
        # self.w = Label(self.window, text=self.text,font=("Helvetica", 20))
        # self.w.grid(row = 5, columnspan = 1)

        
        # w.pack()


    def Send(self):
        input_text = self.textField.get("1.0",END)
        
        show_string = self.user + ": " + input_text
        self.textView.insert(END, show_string)
        


    #Loop do codigo
    def iniciar(self):
        self.window.mainloop()


#Loop do codigo
app = Janela_Principal()
app.iniciar()