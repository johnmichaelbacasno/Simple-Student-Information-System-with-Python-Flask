from flask import Blueprint, render_template, request, redirect, flash

from extensions import db

from .. forms import CollegeForm
from .. manage import *

colleges = Blueprint('colleges', __name__, url_prefix='/colleges')

@colleges.route('/colleges_content')
def colleges_content():
    return render_template('colleges/colleges.html', data=available_colleges())

@colleges.route('/add_college', methods=['GET', 'POST'])
def add_college():
    form = CollegeForm()
    try:
        if form.validate_on_submit():
            query = """
                INSERT INTO `College`(`code`, `name`)
                VALUES(%s, %s)
                """

            data = (
                form.code.data,
                form.name.data
                )

            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()

            flash('College added successfully!', 'success')

            return redirect('/colleges/colleges_content')
        
        return render_template('colleges/add_college.html', form=form)
    except Exception as exception:
        return str(exception)


@colleges.route('/edit_college/<string:code>', methods=['GET', 'POST'])
def edit_college(code):
    try:
        conn = db.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM `College` WHERE `code` = %s", (code,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        form = CollegeForm(data=row)

        if form.validate_on_submit():		
            query = """
                UPDATE `College` SET `name` = %s
                WHERE `code` = %s
                """
            
            data = (
                form.name.data,
                form.code.data
                )

            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()
			
            flash('College updated successfully!', 'success')

        return render_template('colleges/edit_college.html', form=form)
    except Exception as exception:
        return str(exception)

@colleges.route('/delete_college/<string:code>')
def delete_college(code):
    conn = None
    cursor = None
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM `College` WHERE `code` = %s", (code,))
        conn.commit()
        cursor.close() 
        conn.close()

        flash('College deleted successfully!', 'success')

        return redirect('/colleges/colleges_content')
    except Exception as e:
        print(e)