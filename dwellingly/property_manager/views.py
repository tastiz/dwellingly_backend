from flask import Blueprint, render_template
property_manager = Blueprint('property_manager', __name__, template_folder='templates')

@property_manager.route("/")
def index():
    return render_template('property_manager/index.html')