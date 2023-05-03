import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        # the main window of app / top lvl of app
        self.root=tk.Tk() 
        self.root.geometry("450x300")
        self.root.title("Text App")

        # creation of frame
        self.mainframe=tk.Frame(self.root) # defining the main from, where all widges will be placed
        self.mainframe.pack(fill="both",expand=True)
        
        # just defining the txt but not defining where to place it
        self.text=ttk.Label(self.mainframe,text="Welcome!",font=("Brass Mono",40),background="white")
        # placing this defined txt
        self.text.grid(row=0,column=0)

        # A new widget, entry, where enter the txt 
        self.set_text_field=ttk.Entry(self.mainframe)
        # where to place this entry widget
        self.set_text_field.grid(row=1,column=0,pady=10,sticky="NWES")
        # Creating a button
        self.txt_btn=ttk.Button(self.mainframe,text='Set Text',command=self.set_txt) # command var is linked with the method, telling us what to do with txt
        # where to place this button
        self.txt_btn.grid(row=1, column=1,pady=10,padx=10)

        color_options=['red','green','blue','black','pink']
        # creating a new widget where I can select some values
        self.set_color_field=ttk.Combobox(self.mainframe,values=color_options)
        # where to place this widget with the options
        self.set_color_field.grid(row=2,column=0,sticky="NWES",pady=10)

        # Creating a button to apply these options/color
        self.color_btn=ttk.Button(self.mainframe,text='Set Color',command=self.set_color) # command var is linked with the method, telling us what to do with txt
        # where to place this button
        self.color_btn.grid(row=2, column=1,pady=10,padx=10)

        # Adding a btn which reverses the txt
        self.reverse_txt=ttk.Button(self.mainframe,text='Reverse Text', command=self.reverse)
        self.reverse_txt.grid(row=3,column=0,sticky="NWES",pady=10)
        self.root.mainloop() # part of the self.root=tk.Tk() 
        return
    
    # ---- Methods ----

        # display a new text
    def set_txt(self):
        new_txt=self.set_text_field.get()
        self.text.config(text=new_txt)

        # change color
    def set_color(self):
        new_color=self.set_color_field.get()
        self.text.config(foreground=new_color)

        # reverse text
    def reverse(self):
        new_text=self.text.cget('text') # here we're getting the txt from label 
        reversed=new_text[::-1]
        self.text.config(text=reversed)

if __name__=="__main__":
    App()