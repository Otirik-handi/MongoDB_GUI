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
        #标签
        pass
        #文本框
        pass
        #按钮
        pass
        #列表盒子
        self.db_list = Listbox(self.root)
        for db_name in self.func.load_db_names():
            self.db_list.insert('end',db_name)
        self.db_list.grid(row=1,column=1,padx=10,pady=10,ipadx=10,ipady=10)
        self.TABLE_LIST = Listbox(self.root)
        #滑条
        pass
        #etc...


if __name__ == '__main__':
    root = Tk()
    GUI = MongoDB_GUI(root)
    GUI.set_root_window()
    root.mainloop()
        
