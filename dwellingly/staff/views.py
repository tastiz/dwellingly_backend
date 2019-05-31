from flask import Blueprint, render_template
staff = Blueprint('staff', __name__, template_folder='templates')


@staff.route('/')
def index():
    return render_template('staff/index.html')