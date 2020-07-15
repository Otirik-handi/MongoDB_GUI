import pymongo

class Functions(object):

    def __init__(self,path):
        self.mongo = pymongo.MongoClient(path)

#=============================[数据库操作]=====================================#
    def load_db_names(self):#加载数据库名称
        return self.mongo.list_database_names()

    def create_db(self):#创建数据库
        pass

    def delete_db(self):#删除数据库
        pass
#=============================[集合操作]=======================================#
    def load_collection_names(self,db):#加载集合名称
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
#=============================[其他功能]=======================================#
    pass
