import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# Ensure settings module is set
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datingapp.settings')

# Get the WSGI application first
application = get_wsgi_application()

# Configure WhiteNoise to serve static files from the source static/ directory
# (which is tracked in git and deployed to Vercel) rather than from STATIC_ROOT
# (staticfiles/ which is not deployed to Vercel)
import django
from django.conf import settings

# Serve from the source static directory at /static/ URL prefix
static_dir = settings.STATICFILES_DIRS[0]
application = WhiteNoise(application, root=static_dir, prefix='/static/')

# Also serve root-level files (favicon.ico) from static_root
root_dir = settings.WHITENOISE_ROOT
if os.path.isdir(root_dir):
    application.add_files(root_dir, prefix='/')

app = application
