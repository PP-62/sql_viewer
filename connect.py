import pymysql

# pyuic5 gui.ui -o gui.py
 
# con = pymysql.connect(host='localhost', user='root', 
#     password='test_db_password_123', db='world')
 
# with con:
 
#     cur = con.cursor()

#     # show tables names
#     cur.execute("show tables")
#     tables = cur.fetchall()
#     # for i in tables:
#     #     print(i[0])

#     #first table
#     first_table = tables[0][0]

#     # print("-"*10)
    
#     #show columns names
#     cur.execute("select * from %s" % (first_table))
#     desc = cur.description
#     # for i in desc:
#     #     print(i[0])
    
#     #first column
#     first_column = desc[0][0]
#     # print(cur.fetchall())

class Connect:
    def __init__(self,host,user,password,db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.con = pymysql.connect(host=self.host, user=self.user, 
        password=self.password, db=self.db)

    def get_table_names(self):
        self.con = pymysql.connect(host=self.host, user=self.user, 
        password=self.password, db=self.db)
        with self.con:
            cur = self.con.cursor()
            cur.execute("show tables")
            content =  list(cur.fetchall()).copy()
        # self.con.close()
        return content
        
    def get_columns(self,table_name):
        self.con = pymysql.connect(host=self.host, user=self.user, 
        password=self.password, db=self.db)
        with self.con:
            cur = self.con.cursor()
            cur.execute("select * from %s" % (table_name))
            content = list(cur.description).copy()
        # self.con.close()
        return content

    def get_table(self,table_name):
        self.con = pymysql.connect(host=self.host, user=self.user, 
        password=self.password, db=self.db)
        with self.con:
            cur = self.con.cursor()
            cur.execute("select * from %s" % (table_name))
            content = list(cur.fetchall()).copy()
        # self.con.close()
        return content

    def get_content(self,table_name,column_a):
        self.con = pymysql.connect(host=self.host, user=self.user, 
        password=self.password, db=self.db)
        with self.con:
            cur = self.con.cursor()
            cur.execute("select %s from %s" % (column_a,table_name))
            content = list(cur.fetchall()).copy()
        # self.con.close()
        return content

    def get_column(self,table_name,column_a):
        self.con = pymysql.connect(host=self.host, user=self.user, 
        password=self.password, db=self.db)
        with self.con:
            cur = self.con.cursor()
            cur.execute("select %s,%s from %s" % (column_a,table_name))
            content = list(cur.fetchall()).copy()
        # self.con.close()
        return content

    def get_two_columns(self,table_name,column_a,column_b):
        self.con = pymysql.connect(host=self.host, user=self.user, 
        password=self.password, db=self.db)
        with self.con:
            cur = self.con.cursor()
            cur.execute("select %s,%s from %s" % (column_a,column_b,table_name))
            content = list(cur.fetchall()).copy()
        # self.con.close()
        return content

a = Connect(host='localhost', user='root', password='test_db_password_123', db='world')
x = a.get_table_names()
for i in x:
    print(i[0])
print(a.get_columns("country"))
print(a.get_content("country","name"))
