import mysql.connector as conn
from flask import Flask , request , jsonify

app=Flask(__name__)

mydb=conn.connect(host = 'localhost',user = 'root' , passwd= 'password')

cursor=mydb.cursor()

def show_database():
	cursor.execute('show databases')
	databases = cursor.fetchall()

	for x in databases:
		print(x)

def createdb():
	cursor.execute('create database db1')

def create_table():
	cursor.execute("create table db1.dbai(studentid INT(10) , fname VARCHAR(30) , lname VARCHAR(30) , regid INT(10) , classname VARCHAR(30))")

def show_tables():
	cursor.execute('use db1')
	cursor.execute('show tables')
	tables=cursor.fetchall()
	for x in tables:
		print(x)


def insert_data():
	cursor.execute("insert into db1.dbai values(333654,'Deepak','Mohanty',245546652,'Full Stack Data Science')")
	cursor.execute("insert into db1.dbai values(656654,'Chandrakanta','Satapathy',245546543,'Full Stack Web Dev')")
	mydb.commit()

@app.route('/fetch',methods=['POST'])
def fetch():
	if request.method=='POST':
		cursor.execute('use db1')
		table=request.json['name']
		cursor.execute(f'select * from {table}')
		data=cursor.fetchall()
	return jsonify(data)


if __name__ == '__main__':
	app.run()



