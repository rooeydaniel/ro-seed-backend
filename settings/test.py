DEBUG = False

# This should be set to the test domain (e.g. test.django-angular-pt.com)
ALLOWED_HOSTS = ['cc-ro-seed-frontend.herokuapp.com', 'daniel-angular.com']

# Make this unique, and don't share it with anybody.
SECRET_KEY = '4444444444444444444'

CORS_ORIGIN_WHITELIST = (
    'cc-ro-seed-frontend.herokuapp.com',
    'localhost/',
)

from base import *