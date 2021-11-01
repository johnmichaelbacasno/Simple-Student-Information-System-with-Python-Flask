from flask import Blueprint, render_template, request, redirect, flash
import pymysql

from extensions import db, cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

from .. forms import StudentAddForm, StudentEditForm
from .. manage import available_students, course_options

STUDENT_IMAGES_FOLDER_URL = f'https://res.cloudinary.com/{cloudinary.config().cloud_name}/image/upload/ssis/student_images'

students = Blueprint('students', __name__, url_prefix='/students')

@students.route('/students_content')
def students_content():
    images = {'alternate_image_url' : f'{STUDENT_IMAGES_FOLDER_URL}/student_image_not_found.jpg'}
    return render_template('students/students.html', data=available_students(), images=images)

@students.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = StudentAddForm()
    form.course.choices += course_options()
    try:
        if form.validate_on_submit():
            query = """
                INSERT INTO `Student`(`id`, `first_name`, `middle_name`, `last_name`, `course`, `year`, `birth_date`, `birth_place`, `sex`, `gender`, `civil_status`, `citizenship`, `address`, `contact_number`, `image_url`)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
            
            image_url = f'{STUDENT_IMAGES_FOLDER_URL}/{form.id.data}.jpg'

            data = (
                form.id.data,
                form.first_name.data,
                form.middle_name.data,
                form.last_name.data,
                form.course.data,
                form.year.data,
                form.birth_date.data,
                form.birth_place.data,
                form.sex.data, 
                form.gender.data,
                form.civil_status.data,
                form.citizenship.data,
                form.address.data,
                form.contact_number.data,
                image_url
                )
            
            if form.image_file.data:
                upload(form.image_file.data.read(), public_id=f"ssis/student_images/{form.id.data}")

            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()

            flash('Student added successfully!', 'success')

            return redirect('/students/students_content')
        
        return render_template('students/add_student.html', form=form)
    except Exception as exception:
        return str(exception)
    
@students.route('/edit_student/<string:id>', methods=['GET', 'POST'])
def edit_student(id):
    try:
        conn = db.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT `id`, `first_name`, `middle_name`, `last_name`, `course`, `year`, `birth_date`, `birth_place`, `sex`, `gender`, `civil_status`, `citizenship`, `address`, `contact_number` FROM `Student` WHERE `id` = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        
        images = {
            'student_image_url': f'{STUDENT_IMAGES_FOLDER_URL}/{id}.jpg',
            'alternate_image_url' : f'{STUDENT_IMAGES_FOLDER_URL}/student_image_not_found.jpg'
            }
        
        form = StudentEditForm(data=row)
        form.course.choices += course_options()
        
        if form.validate_on_submit():
            query = """
                UPDATE `Student` SET `first_name` = %s, `middle_name` = %s, `last_name` = %s, `course` = %s, `year` = %s, `birth_date` = %s, `birth_place` = %s, `sex` = %s, `gender` = %s, `civil_status` = %s, `citizenship` = %s, `address` = %s, `contact_number` = %s
                WHERE `id` = %s
                """
            
            data = (
                form.first_name.data,
                form.middle_name.data,
                form.last_name.data,
                form.course.data,
                form.year.data,
                form.birth_date.data,
                form.birth_place.data,
                form.sex.data, 
                form.gender.data,
                form.civil_status.data,
                form.citizenship.data,
                form.address.data,
                form.contact_number.data,
                form.id.data,
                )
            
            if form.image_file.data:
                upload(form.image_file.data.read(), public_id=f"ssis/student_images/{form.id.data}")
			
            conn = db.connect()
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()
			
            flash('Student updated successfully!', 'success')

        return render_template('students/edit_student.html', form=form, images=images)
    except Exception as exception:
        return str(exception)

@students.route('/delete_student/<string:id>')
def delete_student(id):
    try:
        conn = db.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM `Student` WHERE `id` = %s", (id,))
        conn.commit()
        cursor.close() 
        conn.close()

        flash('Students deleted successfully!', 'success')
        
        return redirect('/students/students_content')
    except Exception as exception:
        print(exception)