import tkinter as tk

class Front_End():
    '''Class that implements the GUI (Front-End) for the Project'''
    
    def __init__(self):
        self.base = tk.Tk()
        
    def setup(self):
        '''Sets the basic attributes for the Window'''
        self.base.geometry("550x500+480+120")
        self.base.resizable(0,0)
        self.base.title("Tic-Tac-Toe GUI Game ")
        
    def end(self):
        self.base.mainloop()
        
    def test(self):
        '''Used to test the GUI'''
        self.setup()
        self.program()
        self.end()
