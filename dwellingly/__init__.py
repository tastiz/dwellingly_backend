from flask import Flask
from dwellingly.home.views import home
from dwellingly.admin.views import admin
from dwellingly.staff.views import staff
from dwellingly.tenant.views import tenant
from dwellingly.property_manager.views import property_manager

app = Flask(__name__)

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(tenant, url_prefix='/tenant')
app.register_blueprint(staff, url_prefix='/staff')
app.register_blueprint(property_manager, url_prefix='/property_manager')