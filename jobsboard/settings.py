import environ

# django-environ
root = environ.Path(__file__) - 2
env = environ.Env(
    DEBUG=(bool, False),
)
env.read_env(str(root('.env')))

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'pipeline',
    'jobsboard.web',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jobsboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'jobsboard.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = str(root('static'))

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

STATICFILES_DIRS = [
    ('bootstrap', root('node_modules/bootstrap')),
]


# Pipeline
# https://django-pipeline.readthedocs.io/en/latest/configuration.html

PIPELINE = {
    'STYLESHEETS': {
        'bundle': {
            'source_filenames': (
                'bootstrap/scss/bootstrap-flex.scss',
                'scss/app.scss',
            ),
            'output_filename': 'css/bundle.css',
        },
    },
    'JAVASCRIPT': {
        'bundle': {
            'source_filenames': (
                'bootstrap/dist/js/bootstrap.js',
                'js/app.js',
            ),
            'output_filename': 'js/bundle.js',
        },
    },
}

PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
PIPELINE['COMPILERS'] = (
    'jobsboard.web.compilers.SASSCompiler',
)

