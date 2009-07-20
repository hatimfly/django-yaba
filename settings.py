# Django settings for django_yaba project.
import os, socket

###############################################
# django-yaba specific settings below         #
###############################################
# GitHub UserName for sidebar GitHub List - Leave blank if you don't want to use it
GITHUB_USERNAME = 'GITHUB_USER_HOLDER'

# Twitter UserName for sidebar Twitter List and Automatic Tweets
TWITTER_USERNAME = 'TWITTER_USER_HOLDER'
TWITTER_PASSWORD = "TWITTER_PASS_HOLDER"

# Blog Name
BLOG_NAME = 'SITE_NAME_HOLDER'

# Blog URL
ROOT_BLOG_URL = 'http://URL_HOLDER/'

# Root system path
PROJECT_DIR = os.path.dirname(__file__)

# Recaptcha keys
RECAPTCHA_PUBLIC_KEY = "PUBLIC_KEY_HOLDER"
RECAPTCHA_PRIVATE_KEY = "PRIVATE_KEY_HOLDER"

# Disqus Settings
DISQUS_API_KEY = "YOUR_API_KEY_HERE"
DISQUS_WEBSITE_SHORTNAME = "YOUR_SITE_SHORTNAME_HERE"

###############################################
# end django-yaba specific settings           #
###############################################

DEBUG = False 
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'DB_ENGINE_HOLDER'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'DB_NAME_HOLDER'             # Or path to database file if using sqlite3.
DATABASE_USER = 'DB_USER_HOLDER'             # Not used with sqlite3.
DATABASE_PASSWORD = 'DB_PASS_HOLDER'         # Not used with sqlite3.
DATABASE_HOST = 'DB_HOST_HOLDER'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = 'DB_PORT_HOLDER'             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = '/home/f4nt/git-repos/personal/django_yaba/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ROOT_BLOG_URL + "/media/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/adminmedia/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'b30u+n8ojd=4a36ivv*2yig#_5vcly#%1j4-v3erg$*8+0u5#9'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'django_yaba.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.comments',
    'tagging',
    'disqus',
    'django_yaba.blog'
)

# Caching Directives
s = socket.socket()
s.settimeout(0.25)
try:
    s.connect(("127.0.0.1", 11211))
    CACHE_BACKEND = "memcached://127.0.0.1:11211/?timeout=60"
    s.close()
except:
    CACHE_BACKEND = "file:///%s/cache/cache_file" % PROJECT_DIR
    
CACHE_MIDDLEWARE_SECONDS = 300
CACHE_MIDDLEWARE_KEY_PREFIX = 'yaba'

try:
    from localsettings import *
except ImportError:
    print 'localsetting could not be imported'
    pass #Or raise
