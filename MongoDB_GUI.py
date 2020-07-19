from gui_settings import Settings
from functions import Functions as Func
from tkinter import *


class MongoDB_GUI(object):

    def __init__(self,root):
        self.root = root
        self.func = Func(Settings.MongoDB_Path)

    def set_root_window(self):
        self.root.title(Settings.root_window_Title)
        self.root.geometry(Settings.root_window_Size)
        self.root["bg"] = Settings.root_window_BackgroundColor

    def set_menu(self):
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.helpmenu = Menu(self.menubar,tearoff=0)

        self.filemenu.add_command(label='Exit',command=self.root.quit)
        self.helpmenu.add_command(label='For Help',command=self.func.get_help)
        #待添加
        self.menubar.add_cascade(label='File',menu=self.filemenu)
        self.menubar.add_cascade(label='Help',menu=self.helpmenu)
        self.root.config(menu=self.menubar)

    def set_text(self):
        self.input_text = Text(self.root,width=60,height=18)
        self.data_text = Text(self.root,height=43)

        self.input_text.place(x=0,y=298,anchor='nw')
        self.data_text.place(x=430,y=25,anchor='nw')

    def set_label(self):
        self.db_label = Label(self.root,text='Datebases',bg='white',font=('Arial',12),)
        self.col_label = Label(self.root,text='Collections',bg='white',font=('Arial',12))
        self.data_label = Label(self.root,text='Data',bg='white',font=('Arial',12))
        self.input_label = Label(self.root,text='Input Here:(e.g.{"name":"LiHua"})',bg='white',font=('Arial',15))

        self.db_label.place(x=30,y=0,anchor='nw')
        self.col_label.place(x=180,y=0,anchor='nw')
        self.data_label.place(x=700,y=0,anchor='nw')
        self.input_label.place(x=0,y=268,anchor='nw')
        
    def set_listbox(self):
        self.db_list = Listbox(self.root)
        self.col_list = Listbox(self.root)

        self.load_listbox()

    def load_listbox(self):
        for db_name in self.func.load_db_names():
            self.db_list.insert('end',db_name)

        self.db_list.place(x=0,y=25,anchor='nw')

        for col in self.func.load_col_names(self.db_list):
            self.col_list.insert('end',col)

        self.col_list.place(x=150,y=25,anchor='nw')

    def set_button(self):
        self.b_create_db = Button(self.root,width=15,height=1,text='create database',command=self.func.create_db())
        self.b_delete_db = Button(self.root,width=15,height=1,text='delete database',command=lambda:self.func.delete_db(self.db_list))
        self.b_create_col = Button(self.root,width=15,height=1,text='create collection')
        self.b_delete_col = Button(self.root,width=15,height=1,text='delete collection')
        self.b_commit_data = Button(self.root,width=25,height=2,text='commit')
        self.b_delete_data = Button(self.root,width=25,height=2,text='delete')

        self.b_create_db.place(x=300,y=25,anchor='nw')
        self.b_delete_db.place(x=300,y=70,anchor='nw')
        self.b_create_col.place(x=300,y=135,anchor='nw')
        self.b_delete_col.place(x=300,y=180,anchor='nw')
        self.b_commit_data.place(x=5,y=537,anchor='nw')
        self.b_delete_data.place(x=239,y=537,anchor='nw')
        
    def set_all(self):
        self.set_root_window()
        self.set_menu()
        #self.set_frame()
        self.set_text()
        self.set_label()
        self.set_listbox()
        self.set_button()

if __name__ == '__main__':
    root = Tk()
    GUI = MongoDB_GUI(root)
    GUI.set_all()
    root.mainloop()
        
