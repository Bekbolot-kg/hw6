import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)

def create_student(conn, student):
    sql = '''INSERT INTO student (name, mark, hobby, b_date, is_married)
    VALUES (?, ?, ?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)

def read_student(conn, student_id):
    sql = '''SELECT * FROM student WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (student_id,))
        row = cursor.fetchone()
        if row:
            return row
        else:
            print("Student not found.")
    except Error as e:
        print(e)

def update_student(conn, student):
    sql = '''UPDATE student SET name=?, mark=?, hobby=?, b_date=?, is_married=? WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)

def delete_student(conn, student_id):
    sql = '''DELETE FROM student WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (student_id,))
        conn.commit()
    except Error as e:
        print(e)


database = r'file.db'
sql_create_table = '''
CREATE TABLE IF NOT EXISTS student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR (104) NOT NULL,
mark FLOAT NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
b_date DATE NOT NULL ,
is_married BOOLEAN DEFAULT FALSE
);
'''

connection = create_connection(database)

if connection is not None:
    create_table(connection, sql_create_table)
    print('everything is ready')

    student1 = ('John Smith', 90.5, 'Swimming', '1999-06-20', 0)
    student1_id = create_student(connection, student1)
    print(f'Student record created with id: {student1_id}')


    student2 = read_student(connection, student1_id)
    print(f'Student record retrieved: {student2}')


    student1 = ('John Doe', 95, 'Reading', '1999-06-20', 1, student1_id)
    update_student(connection, student1)
    print(f'Student record updated with id: {student1_id}')


    delete_student(connection, student1_id)
    print(f'Student record deleted with id: {student1_id}')

else:
    print('failed')