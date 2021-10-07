from flaskext.mysql import MySQL
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect

db = MySQL()
bootstrap = Bootstrap()
csrf = CSRFProtect()