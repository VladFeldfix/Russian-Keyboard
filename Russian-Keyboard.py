import keyboard
import tkinter
from tkinter import *
import os
from threading import *


class RussianKeboard:
    def __init__(self):
        # set global variables
        
        # setup GUI
        # setup main window
        self.root = tkinter.Tk()
        self.root.minsize(640,240)
        self.root.title("Russian Keyboard v1.0")
        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        self.root.wm_attributes("-topmost" , 2)
        
        #self.root.iconbitmap("favicon.ico")

        # draw main menu
        main_frame = Frame(self.root, bg='red', padx=5, pady=5, takefocus=0)
        main_frame.grid(row=0,column=0, sticky=NSEW)
        btn1 = Button(main_frame, text = "btn", command = lambda:self.type_it("Ё"), width=2, height=1, takefocus=0)
        btn1.grid(row=0, column=0, sticky="news")
        
        """
        menuFrame = Frame(self.root)
        menuFrame.grid(column=0, row=0, sticky="news")
        self.loadButton = Button(menuFrame, text="Load", command=lambda: self.load())
        self.loadButton.grid(column=0, row=0, padx=5, pady=5, sticky="nw")
        self.loadButton.config(width = 10)
        self.startButton = Button(menuFrame, text="Start", command=lambda: self.start())
        self.startButton.grid(column=1, row=0, padx=5, pady=5, sticky="nw")
        self.startButton.config(width = 10)
        self.startButton.config(state=DISABLED)
        

        # darw maze
        self.canvas = Canvas(self.root,bg='white', width=500, height=500)
        self.canvas.grid(column=0, row=1, padx=5, pady=5, columnspan=3, sticky="news")
        """
        # run GUI
        self.root.mainloop()
        

    def type_it(self, char):
        # Call work function 
        self.root.wm_attributes('-topmost', False)
        keyboard.write(char)

    def exit(self):
        self.root.destroy()
        os._exit(1)
    """
    def load(self):
        # stop current thread
        try:
            self.thread._stop()
        except:
            pass
        
        # load a maze file
        file = tkinter.filedialog.askopenfile(mode ='r', filetypes =[('PNG Files', '*.png')])
        if file:
            self.startButton.config(state=DISABLED)
            self.fun.reset()
            test = self.fun.create_maze(file.name)
            if not test[0]:
                tkinter.messagebox.showerror("Error", test[1])
                self.loadButton.config(state=NORMAL)
            else:
                # load selected image to bord
                self.img= ImageTk.PhotoImage(Image.open(file.name))
                self.canvas.create_image(5, 5, image=self.img, anchor=NW)
                self.startButton.config(state=NORMAL)
    """
RussianKeboard()