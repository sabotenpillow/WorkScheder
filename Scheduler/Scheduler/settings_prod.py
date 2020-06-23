import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = [ 'localhost' ]

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'formatters': {
#        'production': {
#            'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
#                      '%(pathname)s:%(lineno)d %(message)s'
#        },
#    },
#    'handlers': {
#        'file': {
#            'class': 'logging.FileHandler',
#            'filename': 'logs/django.log',  #環境に合わせて変更
#            'formatter': 'production',
#            'level': 'INFO',
#        },
#    },
#    'loggers': {
#        # 自作したログ出力
#        '': {
#            'handlers': ['file'],
#            'level': 'INFO',
#            'propagate': False,
#        },
#        # Djangoの警告・エラー
#        'django': {
#            'handlers': ['file'],
#            'level': 'INFO',
#            'propagate': False,
#        },
#    },
#}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    # setting of django
    'django': {
        'handlers': ['file'],
        'level'   : 'INFO',
    },
    # setting of WorkScheder App
    'WorkScheder': {
        'handlers': ['file'],
        'level'   : 'INFO',
    },
    # setting of 'handlers'
    'handlers': {
        'file': {
            'level'   : 'INFO',
            'class'   : 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),  #環境に合わせて変更
            'formatter': 'prod',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
        },
    },
    # setting of 'formatters'
    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    },
}
