from Front_End import Front_End 

class Back_End(Front_End):
    '''Class that implements the Back-End for the Project'''
    
    marker1, marker2 = "X", "O"
    marker = marker1
    count = 0
    
    def __init__(self):
        Front_End.__init__(self)
        Front_End.test(self)
      
    
    def program(self):
        global buttons
        
        banner1 = tk.LabelFrame(self.base, height=70, width=550, bg="#084B83")
        banner1.place(x=0, y=0)

        banner2 = tk.LabelFrame(self.base, height=320, width=550, bg="#BBE6E4")
        banner2.place(x=0, y=70)
        
        banner3 = tk.LabelFrame(self.base, height=110, width=550, bg="#F1D9A7")
        banner3.place(x=0, y=390)

        welcomeNote = tk.Label(banner1, text="Welcome to TIC-TAC-TOE Game", font=("Cambria", 14), padx=15, pady=4)
        welcomeNote.place(x=120, y=18)
        
        instrn = tk.Label(banner3, text="Player 1 will start the Game\nClick any box to place \'X\'", font=('Cambria', 12),
                          padx=10, fg="#145C9E")
        instrn.place(x=150, y=30)
        
        p1note = tk.Label(banner2, text="Player 1 : "+self.marker1, font=('Arial', 10), padx=10)
        p1note.place(x=400, y=20)
        p2note = tk.Label(banner2, text="Player 2 : "+self.marker2, font=('Arial', 10), padx=10)
        p2note.place(x=400, y=50)
    
        b_x, b_y = 144, 40
        
        button1 = tk.Button(banner2, text=" ", command=lambda: self.click(button1, self.marker, instrn), height=1, width=1, font=("Arial", 24), padx=14)
        button1.place(x=b_x, y=b_y+160)
        button2 = tk.Button(banner2, text=" ", command=lambda: self.click(button2, self.marker, instrn), height=1, width=1, font=("Arial", 24), padx=14)
        button2.place(x=b_x+80, y=b_y+160)
        button3 = tk.Button(banner2, text=" ", command=lambda: self.click(button3, self.marker, instrn), height=1, width=1, font=("Arial", 24), padx=14)
        button3.place(x=b_x+160, y=b_y+160)
        
        button4 = tk.Button(banner2, text=" ", command=lambda: self.click(button4, self.marker, instrn), height=1, width=1, font=("Arial", 24), padx=14)
        button4.place(x=b_x, y=b_y+80)
        button5 = tk.Button(banner2, text=" ", command=lambda: self.click(button5, self.marker, instrn), height=1, width=1, font=("Arial", 24), padx=14)
        button5.place(x=b_x+80, y=b_y+80)
        button6 = tk.Button(banner2, text=" ", command=lambda: self.click(button6, self.marker, instrn), height=1, width=1, font=("Arial", 24), padx=14)
        button6.place(x=b_x+160, y=b_y+80)
        
        button7 = tk.Button(banner2, text=" ", command=lambda: self.click(button7, self.marker, instrn), height=1, width=1, font=("Arial", 24), padx=14)
        button7.place(x=b_x, y=b_y)
        button8 = tk.Button(banner2, text=" ", command=lambda: self.click(button8, self.marker, instrn), height=1, width=1, font=("Arial", 24), padx=14)
        button8.place(x=b_x+80, y=b_y)
        button9 = tk.Button(banner2, text=" ", command=lambda: self.click(button9, self.marker, instrn), height=1, width=1, font=("Arial", 24), padx=14)
        button9.place(x=b_x+160, y=b_y)
        
        buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
        replay = tk.Button(banner3, text="Replay", command=lambda: self.reset_game(buttons, instrn), height=1, font=('Arial', 9), padx=10, bg="#DEBA6F")
        replay.place(x=450, y=20)
        
        exitB = tk.Button(banner3, text="Exit", command=self.exit_game, bg="#77BFA3", font=('Arial', 9), padx=14)
        exitB.place(x=450, y=60)
    
    
    
    
    def click(self, button, marker, instrn): 
        button['text'] = marker
        button['state'] = 'disabled'
        
        if marker == self.marker1:
            self.marker = self.marker2
            button['bg'] = "#0AD3FF"
            instrn['text'] = "Player 2 will click now..\nClick any box to place \'O\'"
            instrn['fg'] = "#290628"
            self.count+=1
            
        else:
            self.marker = self.marker1
            button['bg'] = '#F2BB05'
            instrn['text'] = "Player 1 will click now..\nClick any box to place \'X\'"
            instrn['fg'] = "#145C9E"
            self.count+=1
        self.display_result(buttons, instrn)
    
    
    
    
    def display_result(self, buttons, instrn):
        if 9>self.count>4:
            if self.check_win(buttons, self.marker1):
                instrn['text'] = "Congratulations\nPlayer 1 won the Game...!!!!"
                instrn['fg'] = "#290628"
                instrn['bg'] = '#66C3FF'
                for i in buttons: i['state'] = 'disabled'
                
            elif self.check_win(buttons, self.marker2):
                instrn['text'] = "Congratulations\nPlayer 2 won the Game...!!!!"
                instrn['fg'] = "#290628"
                instrn['bg'] = '#F2BB05'
                for i in buttons: i['state'] = 'disabled'
                
        elif self.count == 9:
            instrn['text'] = "Match Drawn...!!!!"
            instrn['fg'] = "#290628"
            instrn['bg'] = 'light blue'
    
    
    
    
    def check_win(self, buttons, marker):
        return ((buttons[0]['text']==marker and buttons[1]['text']==marker and buttons[2]['text']==marker) or
        (buttons[3]['text']==marker and buttons[4]['text']==marker and buttons[5]['text']==marker) or
        (buttons[6]['text']==marker and buttons[7]['text']==marker and buttons[8]['text']==marker) or
        (buttons[0]['text']==marker and buttons[3]['text']==marker and buttons[6]['text']==marker) or
        (buttons[1]['text']==marker and buttons[4]['text']==marker and buttons[7]['text']==marker) or 
        (buttons[2]['text']==marker and buttons[5]['text']==marker and buttons[8]['text']==marker) or 
        (buttons[0]['text']==marker and buttons[4]['text']==marker and buttons[8]['text']==marker) or 
        (buttons[6]['text']==marker and buttons[4]['text']==marker and buttons[2]['text']==marker))

    
    
    
    def reset_game(self, buttons, instrn):
        self.count = 0
        instrn['bg'] = '#F0F0F0'
        instrn['text'] = "Player 1 will start the Game\nClick any box to place \'X\'"
        for i in buttons:
            i['text'] = ' '
            i['state'] = 'active'
            i['bg'] = "#F0F0F0"
            self.marker = self.marker1
    
    
    def exit_game(self):
        self.base.destroy()
        
Back_End()
