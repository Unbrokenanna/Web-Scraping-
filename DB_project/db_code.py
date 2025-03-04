import sqlite3
import pandas as pd
conn = sqlite3.connect('STAFF.db')
table_name = 'INSTRUCTOR'
attribute_list = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']
file_path = '/home/project/DB_project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

data_dict = {'ID' : [101],
            'FNAME' : ['Anna'],
            'LNAME' : ['Fedosova'],
            'CITY' : ['Luhansk'],
            'CCODE' : ['UA']}
data_append = pd.DataFrame(data_dict)
data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

table_name = 'DEPARTMENTS'
attribute_list = ['DEPT_ID', 'DEPT_NAME', 'MANAGER_ID', 'LOC_ID']
file_path = '/home/project/DB_project/Departments.csv'
df = pd.read_csv(file_path, names = attribute_list)
df.to_sql(table_name, conn, if_exists = 'replace', index =False)
print('Table is ready')
query_statement = f"SELECT * FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
query_statement = f"SELECT DEPT_NAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)
conn.close()