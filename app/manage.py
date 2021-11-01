import pymysql

from extensions import db

def available_students():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT Student.id, Student.first_name, Student.middle_name, Student.last_name, Course.name AS `course`, Student.year, Student.birth_date, Student.birth_place, Student.sex, Student.gender, Student.civil_status, Student.citizenship, Student.address, Student.contact_number, Student.image_url
        FROM `Student`
        LEFT JOIN `Course` ON Student.course = Course.code
        ORDER BY Student.id;
        """)
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

def available_courses():
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("""
        SELECT Course.code, Course.name, College.name AS `college`
        FROM `Course`
        LEFT JOIN `College` ON Course.college = College.code
        ORDER BY Course.code;
        """)
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

def student_exists(id):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM `Student` where id=%s", (id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return bool(student)

def course_exists(code):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM `Course` where code=%s", (code,))
    course = cursor.fetchone()
    cursor.close()
    conn.close()
    return bool(course)

def college_exists(code):
    conn = db.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM `College` where code=%s", (code,))
    college = cursor.fetchone()
    cursor.close()
    conn.close()
    return bool(college)

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