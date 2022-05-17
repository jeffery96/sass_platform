LANGUAGE_CODE = 'zh-hans'

# 短信模板
SMS = 0

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'saas_platform',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}
