from os import environ
from flaskext.mysql import MySQL
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
import cloudinary

db = MySQL()
bootstrap = Bootstrap()
csrf = CSRFProtect()

cloudinary.config(
    cloud_name = environ.get('CLOUDINARY_CLOUD_NAME'), 
    api_key = environ.get('CLOUDINARY_API_KEY'), 
    api_secret = environ.get('CLOUDINARY_API_SECRET'),
    secure = environ.get('CLOUDINARY_API_SECRET')
)