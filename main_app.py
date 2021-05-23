from tkinter import *
from customers import Customers
from dealers import Dealers
from lockscreen import LockScreen
from statementspage import StatementsPage
from lockscreen import fcompany_name

# ------------- MAIN APP ----------#


class MainApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Dealers, StatementsPage, Customers, LockScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame('LockScreen')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == '__main__':
    app = MainApp()
    app.title(fcompany_name)
    try:
        app.state('zoomed')
    except:
        pass
    try:
        app.iconbitmap('logo.ico')
    except:
        print('No icon file found')
    app.mainloop()



