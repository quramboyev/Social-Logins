from pathlib import Path

from environ import Env
env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-rj#-z^kx3j+1ay397otg6j8m_8#v^$^$jys6&41vy^&6le)ezc'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

CSRF_TRUSTED_ORIGINS = [ 'https://*' ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
    'django_htmx',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.facebook',

    # My apps
    'a_home',
    'a_users',
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('OAUTH_GOOGLE_CLIENT_ID'),
            'secret': env('OAUTH_GOOGLE_SECRET'),
            'key': ''
        },
        'SCOPE': [
            'profile', 'email'
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
            'prompt': 'consent'
        },
    },
    'github': {
        'APP': {
            'client_id': env('OAUTH_GITHUB_CLIENT_ID'),
            'secret': env('OAUTH_GITHUB_SECRET'),
        },
        'AUTH_PARAMS': {
            'prompt': 'consent',
        },
    },
    'facebook': {
        'APP': {
            'client_id': env('OAUTH_FACEBOOK_CLIENT_ID'),
            'secret': env('OAUTH_FACEBOOK_SECRET'),
        },
        'AUTH_PARAMS': {
            'auth_type': 'reauthenticate'
        },
    },

}

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django_htmx.middleware.HtmxMiddleware',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]


ROOT_URLCONF = 'a_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'a_core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media' 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 
LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_LOGIN_METHODS = {'email'}
ACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_UNIQUE_email = True 
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True
SOCIALACCOUNT_EMAIL_VERIFICATION = "none"

ACCOUNT_ADAPTER = "a_users.adapters.CustomAccauntAdapter"
ACCOUNT_ADAPTER = "a_users.adapters.SocialAccountAdapter"