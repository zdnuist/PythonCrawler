#安装驱动
#pip install mysql-connector-python --allow-external mysql-connector-python
import mysql.connector

conn = mysql.connector.connect(user='zd' , password='root',database='py_datas')

cursor = conn.cursor()

cursor.close()