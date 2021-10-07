import pymysql

from extensions import db

def available_students():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM `Student`")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

def available_courses():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM `Course`")
    courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return courses

def available_colleges():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM `College`")
    colleges = cursor.fetchall()
    cursor.close()
    conn.close()
    return colleges

def count_students():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT COUNT(*) AS `Count`  FROM `Student`")
    students = cursor.fetchone()
    cursor.close()
    conn.close()
    return students['Count']

def count_courses():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT COUNT(*) AS `Count`  FROM `Course`")
    courses = cursor.fetchone()
    cursor.close()
    conn.close()
    return courses['Count']

def count_colleges():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT COUNT(*) AS `Count`  FROM `College`")
    colleges = cursor.fetchone()
    cursor.close()
    conn.close()
    return colleges['Count']

def course_options():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT code, name FROM `Course`")
    courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return courses

def college_options():
    conn = db.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT code, name FROM `College`")
    colleges = cursor.fetchall()
    cursor.close()
    conn.close()
    return colleges