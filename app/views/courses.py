from flask import Blueprint, render_template, request, redirect, flash

from extensions import db

from .. forms import CourseForm
from .. manage import *

courses = Blueprint('courses', __name__, url_prefix='/courses')

@courses.route('/courses_content')
def courses_content():
    return render_template('courses/courses.html', data=available_courses())

@courses.route('/add_course', methods=['GET', 'POST'])
def add_course():
    form = CourseForm()
    form.college.choices += college_options()
    try:
        if form.validate_on_submit():

            query = """
                INSERT INTO `Course`(`code`, `name`, `college`)
                VALUES(%s, %s, %s)
                """

            data = (
                form.code.data,
                form.name.data,
                form.college.data,
                )

            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()

            flash('Course added successfully!', 'success')

            return redirect('/courses/courses_content')
        
        return render_template('courses/add_course.html', form=form)
    except Exception as exception:
        return str(exception)


@courses.route('/edit_course/<string:code>', methods=['GET', 'POST'])
def edit_course(code):
    try:
        conn = db.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM `Course` WHERE `code` = %s", (code,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        form = CourseForm(data=row)
        form.college.choices += college_options()

        if form.validate_on_submit():		
            query = """
                UPDATE `Course` SET `name` = %s, `college` = %s
                WHERE `code` = %s
                """
			
            data = (
                form.name.data,
                form.college.data,
                form.code.data
                )
			
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()
			
            flash('Course updated successfully!', 'success')

        return render_template('courses/edit_course.html', form=form)
    except Exception as exception:
        return str(exception)

@courses.route('/delete_course/<string:code>')
def delete_course(code):
    conn = None
    cursor = None
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM `course` WHERE `code` = %s", (code,))
        conn.commit()
        cursor.close() 
        conn.close()
        flash('Course deleted successfully!', 'success')
        return redirect('/courses/courses_content')
    except Exception as e:
        print(e)