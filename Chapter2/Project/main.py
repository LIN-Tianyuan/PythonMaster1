from file_define import TextFileReader, JSONFileReader
from pymysql import Connection

text_file_reader = TextFileReader('January2023SalesData.txt')
json_file_reader = JSONFileReader('February2023SalesData.txt')

jan_data:list = text_file_reader.read_data()
feb_data:list = json_file_reader.read_data()
all_data:list = jan_data + feb_data


# Création d'objets de connexion MySQL
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='',
    autocommit=True
)
cursor = conn.cursor()
# cursor.execute('create database sales')
conn.select_db('sales')
# cursor.execute('create table orders(order_date DATE, order_id varchar(255), money int, province varchar(10))')
cursor.execute('show tables')
"""
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) " \
          f"values ('{record.date}', '{record.order_id}', '{record.money}', '{record.province}')"
    cursor.execute(sql)
"""
cursor.execute('select * from orders')
print(cursor.fetchall())
conn.close()