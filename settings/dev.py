DEBUG = True
SANDBOX = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ro-seed',
        'USER': 'dstephenson',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'X-REQUESTED-WITH',
    'CONTENT-TYPE',
    'ACCEPT',
    'ORIGIN',
    'AUTHORIZATION'
)

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'localhost:8001',
    'localhost/',
    'cc-ro-seed-frontend.herokuapp.com',
    'cc-ro-seed-backend.herokuapp.com/',
    'cc-ro-seed-backend.herokuapp.com'
)

ALLOWED_HOSTS = ['127.0.0.1', 'localhost:8001', 'localhost']

#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_USER = 'username@googlemail.com'
#EMAIL_HOST_PASSWORD = 'xxxxxxxx'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587

#ADMINS = (
#    ('Your Name', 'username@googlemail.com'),
#)
#MANAGERS = ADMINS

# Absolute path to the directory that holds the project sources
# Make sure to use a training slash
STATIC_APP_NAME = 'static'
MEDIA_APP_NAME = 'media'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '^+huj2wtmaob37@6l0csq6lu!&c8@=d@&le%*hb_yg249t-d7n'