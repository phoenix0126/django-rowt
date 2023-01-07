from pathlib import Path
import os, sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qs@!3ee%+9!o)m!7yavxu%o$*&s!hm9uh1r-_$44p9yfbo5hj='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['rowt.co.uk','localhost','127.0.0.1','seal-app-tamk6.ondigitalocean.app']


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rowt',
    'app',
    'form',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rowt.urls'

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

WSGI_APPLICATION = 'rowt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# constants for rowt calculations
ROWT_REDIRECT_URL = "thanks"
ROWT_ESTIMATED_CRAWL = 85
ROWT_ESTIMATED_VISIT = 5000
ROWT_ESTIMATED_CONVERSIONS = 2.5

MAILERSEND_API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiY2MwYWRkYTdkYTM3NWM5Yzg4Y2UwNGI4OTYwNjkyMzU5Y2Q1ZjQwNGE3ZThhNDIxNDBhZTk1OWUyZGY0NGZlYjA4MGNhNzg1NTg0ZjFlYzYiLCJpYXQiOjE2NTI4Njk1MDEuMTc5NTAzLCJuYmYiOjE2NTI4Njk1MDEuMTc5NTA2LCJleHAiOjQ4MDg1NDMxMDEuMTc1MjYsInN1YiI6IjI2NDgzIiwic2NvcGVzIjpbImVtYWlsX2Z1bGwiLCJkb21haW5zX2Z1bGwiLCJhY3Rpdml0eV9mdWxsIiwiYW5hbHl0aWNzX2Z1bGwiLCJ0b2tlbnNfZnVsbCIsIndlYmhvb2tzX2Z1bGwiLCJ0ZW1wbGF0ZXNfZnVsbCIsInN1cHByZXNzaW9uc19mdWxsIiwic21zX2Z1bGwiXX0.gQF7mYiYpvTt9P9x3g1_eE4ySwmStviC8jCST9wxwAnJCYa3cSgTWOfSYddqPM69rJ6nzKf9kEXZzOWiffRzv56hyhXefv-eWhKQ1bTTlMdU7hJtAVAyxuymhLMF_PWj44P_F2HWEnnNGN-sfPfpPIfYTRjKMyIgAACSo_luZEiW1VQ_9rnfYZJDOmGAYgH3mInFLFyoXGKxjTGg7wBAgcRaLp86qtx5ClVzlz176udlh7sIvOWic0Y83qnRtbc-UeJ18l96qwiWCuYVIYWefA_BnWyZX_odwAwpkzbnKYO-9ZKgiGahjKxpjO6iFyzQ3Aj0_rURd9MqTW-YHuWKFa3TB7uVuVkuKEZaJ6pFT699fuwvsVABSJtb9lbejDkaH13a95ovCRujGrRJfm3yGscYeyyioBM5lxqm7pJNXOrRu_ZNngH_7ge0bX4M5flf0bKFlvbyxO-WPQPU3Z1DfFHjBLUGNE713ILCAaa3Kxtj9XiH6JMchJCQ74m46ClXS0-FF9GxEpBt2yRSYkY-1yKUUiEljuxkBIEQzdbMwhSpT_Q3MJueeOvOhOh0ZAoTJD1S-7UJgdVroOlrDpOOQTZwIrpuFDBFNmE0LT6PrXaIs9HJjkcdngzRd9s1uXhndFNPOdTYtYobC9D1_VbZQifZSlaIbOh7sfQ-JNp0-mg"
MAILERLITE_API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiNjZkMDdjNjFlMWRjNGRjMDlmMjEzNDFhZTgxOWE1MzE3ZTA5MjA5N2MzZjcxMTU4ODI0NWU5Njg5NDFiZWM3NDQ4MDgzNmJiNzg3MzNhYjQiLCJpYXQiOjE2NTI4Njk1MzQuMTQzMjY2LCJuYmYiOjE2NTI4Njk1MzQuMTQzMjcsImV4cCI6NDgwODU0MzEzNC4xMzg3NTEsInN1YiI6IjYxNDQwIiwic2NvcGVzIjpbXX0.Ao1MaF5ItlzSqxCTV_9RyPfqCJIxYGpiZE3j9YNxArj3rUo1Ap2wQ8MkoWUGw0gReXWUQTnq-NWCYEi8ec3Ak0uAFxlDcHULuQzSPwwgjNn_4lH8Zwp4_6_smauBs8dWLKjlUB5j_FHMJCEEMePbBPxjExGJkCpHeN5XeFEjOFJgPdIW8BTRUibEgkfUOQ8UUJPpHmQ3cwF3mq4u4X13y0vLMRJ1QW-5zJRcRYjaLKHb1txSb8T4S3BjocF6XeSu_R3yhKznL8yRrpkhEQrOrqUBDenaSUnYsyFcNq8oT7ICjwCWE-1YMj8ClctO6ItOMAGelz8U9npAA2Ws0-Nx__91oUTlM_Qkj331sx-YB9pzYmR6ku2kzCFb_4cyhL77Lc_pkeQW21ucwRihWF5E9qdaLNttZKwbhtN6sxCjeUYhZpwRWsUxG50FVI92uIPTzNqEB3hGdyXlTuUkmJMdmjWCFHvVTMNUMiE-YbJbvK4tyZSNtAwMhaVi-IgQdEggT4v9meARRrHNZCZfvAXeAKFfyFj0M4nmhDr67e2F5LOHWJeLk4ff_KhHjm-_fCeQ5TBNShRLjT7hNl60Ndi6cUlS79o0dN0Xvc8hGgSaE5jXRNhrlBZNBaSAL-4_QNchff35KTvc24_LnjQLnYvEJcBsx9URn16DPx-gQqApcw4"
