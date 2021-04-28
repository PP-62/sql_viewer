import pymysql
 
con = pymysql.connect(host='localhost', user='root', 
    password='test_db_password_123', db='world')
 
with con:
 
    cur = con.cursor()

    # show tables names
    cur.execute("show tables")
    tables = cur.fetchall()
    for i in tables:
        print(i[0])

    #first table
    first_table = tables[0][0]

    print("-"*10)
    
    #show columns names
    cur.execute("select * from %s" % (first_table))
    desc = cur.description
    for i in desc:
        print(i[0])
    
    #first column
    first_column = desc[0][0]