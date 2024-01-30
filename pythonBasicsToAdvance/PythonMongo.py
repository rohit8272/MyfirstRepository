from pymongo import MongoClient

conn = MongoClient('localhost' , 27017)

db = conn.testdb.emp

emp_rec = {}

flag = True

while flag:
    emp_name , emp_add, emp_id = input("Enter emp name , add , id:").split(',')
    emp_rec = {"name" : emp_name, "addr" : emp_add , "id": emp_id}
    db.insert(emp_rec)
    flag = input('do you want add another data')
    if flag[0].upper() == 'N':
        flag = False


ret = db.found()

for result in ret:
    print(f"name: {result[name]} ,addr: {result[addr]} , id: {result[id]}")
    print()

conn.close()