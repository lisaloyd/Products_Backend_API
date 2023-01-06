# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$#u&wf_)%1af4)$_3rvdjbgp4ec#s0e&ef0vz@)cu)7c#zy($)'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}
