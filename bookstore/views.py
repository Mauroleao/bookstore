import os
import sys

# assuming your django settings file is at '/home/drsantos20/mysite/mysite/settings.py'
# and your manage.py is is at '/home/drsantos20/mysite/manage.py'
path = '/home/Mauroleao/bookstore'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'bookstore.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
