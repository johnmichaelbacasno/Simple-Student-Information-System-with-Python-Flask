from flask import Blueprint, render_template

from .. manage import count_students, count_courses, count_colleges

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@dashboard.route('/home')
def dashboard_content():
    return render_template('dashboard/dashboard.html',
                            count_students=count_students(),
                            count_courses=count_courses(),
                            count_colleges=count_colleges())