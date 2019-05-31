from flask import Blueprint, render_template
tenant = Blueprint('tenant', __name__, template_folder='templates')


@tenant.route('/')
def index():
    return render_template('tenant/index.html')