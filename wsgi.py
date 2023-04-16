import sys
path = '/home/amzhar/mysite'
if path not in sys.path:
    sys.path.append(path)

from flask_app import create_app
application = create_app()