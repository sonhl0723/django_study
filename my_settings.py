import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   # engine
        'NAME': 'django_study', # db
        'USER': 'root',         # user
        'PASSWORD': 'ghddlf7626#',  # user password
        'HOST': 'localhost',    # host
        'PORT': '3306',         # port
    }
}
SECRET_KEY = 'z-5z9bw_j_*0#u4qjez7fd9#t9pc0%$^xko)e1a*!k*u66vu=-'