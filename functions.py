import pymongo
from tkinter import *
from tkinter import messagebox
class Functions(object):

    def __init__(self,path):
        self.mongo = pymongo.MongoClient(path)

#=============================[数据库操作]=====================================#
    def load_db_names(self):#加载数据库名称
        return self.mongo.list_database_names()

    def create_db(self,entry):#创建数据库
        try:
            e = Entry(Tk())
            e.pack()
            db_name = e.get()
            db = self.mongo[db_name]
            e.delete(0,'end')
        except Exception as e:
            messagebox.showerror('Error',e)

    def delete_db(self,db_list):#删除数据库
        try:
            db_name = db_list.get('active')
            self.mongo.drop_database(db_name)
            listbox.delete(db_list.index('active'))
            messagebox.showinfo('删除成功','Database %s 已删除'%db_name)
        except Exception as e:
            messagebox.showerror('Error',e)
            
#=============================[集合操作]=======================================#
    def load_col_names(self,db_list):#加载集合名称
        db = self.mongo[db_list.get('active')]
        return db.list_collection_names()

    def create_col(self,db):#创建集合
        pass

    def delete_col(self,db):#删除集合
        pass
#=============================[数据操作]=======================================#
    def read(self,col):#读取数据
        pass

    def write(self,col):#写入数据
        pass

    def delete(self,col):#删除数据
        pass
#=============================[其他功能]=======================================#
    def get_help(self):#打开帮助文档
        pass
