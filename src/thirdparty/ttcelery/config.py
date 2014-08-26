# -*- coding: utf-8 -*-
# @Date    : 2014-08-26 16:31:33
# @Author  : Your Name (you@example.org)
# @Link    : (http://docs.celeryproject.org/en/latest/configuration.html#database-backend-settings)
# @Version : $Id$

#======================basic Celery set-up================================
## Broker settings.
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
# List of modules to import when celery starts.
CELERY_IMPORTS = ('myapp.tasks', )
## Using the database to store task state and results.
CELERY_RESULT_BACKEND = 'db+sqlite:///results.db'
CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}


#=====================Time and date settings=================================
CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True

#======================Task settings================================
CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}


#=====================Concurrency settings=================================
CELERYD_CONCURRENCY =
CELERYD_PREFETCH_MULTIPLIER =

#======================Task result backend settings================================
CELERY_RESULT_BACKEND = 'amqp://'
CELERY_RESULT_SERIALIZER = 'json'

#=======================Database backend settings===============
CELERY_RESULT_BACKEND = 'db+scheme://user:password@host:port/dbname'
CELERY_RESULT_DBURI =
CELERY_RESULT_ENGINE_OPTIONS = {'echo': True}
CELERY_RESULT_DB_TABLENAMES = {
    'task': 'myapp_taskmeta',
    'group': 'myapp_groupmeta',
}

#=======================AMQP backend settings===============================
CELERY_RESULT_EXCHANGE =
CELERY_RESULT_EXCHANGE_TYPE =
CELERY_RESULT_PERSISTENT =
# CELERY_RESULT_BACKEND = 'amqp'
# CELERY_TASK_RESULT_EXPIRES = 18000  # 5 hours.



#=======================Redis backend settings===============================
#CELERY_RESULT_BACKEND = 'redis://:password@host:port/db'
#CELERY_REDIS_MAX_CONNECTIONS = 

#=======================MongoDB backend settings===============================
# CELERY_RESULT_BACKEND = 'mongodb://192.168.1.100:30000/'
# CELERY_MONGODB_BACKEND_SETTINGS = {
#     'database': 'mydb',
#     'taskmeta_collection': 'my_taskmeta_collection',
# }

#========================Message Routing==============================
CELERY_QUEUES =
CELERY_ROUTES = {
    'tasks.add': {'exchange': 'C.dq', 'routing_key': 'w1@example.com'}
}
CELERY_QUEUE_HA_POLICY = 'all'
CELERY_WORKER_DIRECT =
CELERY_CREATE_MISSING_QUEUES =
CELERY_DEFAULT_QUEUE =
CELERY_DEFAULT_EXCHANGE =
CELERY_DEFAULT_EXCHANGE_TYPE =
CELERY_DEFAULT_ROUTING_KEY =
CELERY_DEFAULT_DELIVERY_MODE =

#=========================Broker Settings=============================
# using serializer name
CELERY_ACCEPT_CONTENT = ['json']
# or the actual content-type (MIME)
CELERY_ACCEPT_CONTENT = ['application/json']
BROKER_FAILOVER_STRATEGY =
BROKER_TRANSPORT =
BROKER_URL =
BROKER_HEARTBEAT =
BROKER_HEARTBEAT_CHECKRATE =
BROKER_USE_SSL =
BROKER_POOL_LIMIT =
BROKER_CONNECTION_TIMEOUT =
BROKER_CONNECTION_RETRY =
BROKER_CONNECTION_MAX_RETRIES =
BROKER_LOGIN_METHOD =
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 18000}  # 5 hours

#==========================Task execution settings============================
CELERY_ALWAYS_EAGER =
CELERY_EAGER_PROPAGATES_EXCEPTIONS =
CELERY_IGNORE_RESULT =
CELERY_MESSAGE_COMPRESSION =
CELERY_TASK_RESULT_EXPIRES =
CELERY_MAX_CACHED_RESULTS =
CELERY_CHORD_PROPAGATES =
CELERY_TRACK_STARTED =
CELERY_TASK_SERIALIZER = 'json'
CELERY_TASK_PUBLISH_RETRY =
CELERY_TASK_PUBLISH_RETRY_POLICY =
CELERY_DEFAULT_RATE_LIMIT =
CELERY_DISABLE_RATE_LIMITS =
CELERY_ACKS_LATE =

#=========================Worker=============================
CELERY_IMPORTS =
CELERY_INCLUDE =
CELERYD_FORCE_EXECV =
CELERYD_WORKER_LOST_WAIT =
CELERYD_MAX_TASKS_PER_CHILD =
CELERYD_TASK_TIME_LIMIT =
CELERYD_TASK_SOFT_TIME_LIMIT =
CELERY_STORE_ERRORS_EVEN_IF_IGNORED =
CELERYD_STATE_DB =
CELERYD_TIMER_PRECISION =
CELERY_ENABLE_REMOTE_CONTROL =

#========================Error E-Mails==============================
# Enables error emails.
CELERY_SEND_TASK_ERROR_EMAILS = True
# Name and email addresses of recipients
ADMINS = (
    ('George Costanza', 'george@vandelay.com'),
    ('Cosmo Kramer', 'kosmo@vandelay.com'),
)
# Email address used as sender (From field).
SERVER_EMAIL = 'no-reply@vandelay.com'
# Mailserver configuration
EMAIL_HOST = 'mail.vandelay.com'
EMAIL_PORT = 25
# EMAIL_HOST_USER = 'servers'
# EMAIL_HOST_PASSWORD = 's3cr3t'

#=========================Events=============================
CELERY_SEND_EVENTS =
CELERY_SEND_TASK_SENT_EVENT =
CELERY_EVENT_QUEUE_TTL =
CELERY_EVENT_QUEUE_EXPIRES =
CELERY_EVENT_SERIALIZER =


#========================Broadcast Commands==============================
CELERY_BROADCAST_QUEUE =
CELERY_BROADCAST_EXCHANGE =
CELERY_BROADCAST_EXCHANGE_TYPE =

#========================Logging==============================
CELERYD_HIJACK_ROOT_LOGGER =
CELERYD_LOG_COLOR =
CELERYD_LOG_FORMAT =
CELERYD_TASK_LOG_FORMAT = '[%(asctime)s: %(levelname)s/%(processName)s] [%(task_name)s(%(task_id)s)] %(message)s'
CELERY_REDIRECT_STDOUTS =
CELERY_REDIRECT_STDOUTS_LEVEL = 

#=========================Security=============================
CELERY_SECURITY_KEY =
CELERY_SECURITY_CERTIFICATE =
CELERY_SECURITY_CERT_STORE =

#=========================Custom Component Classes (advanced)=============================
CELERYD_POOL =
CELERYD_POOL_RESTARTS =
CELERYD_AUTOSCALER =
CELERYD_AUTORELOADER =
CELERYD_CONSUMER =
CELERYD_TIMER =

#=========================Periodic Task Server: celery beat=============================
CELERYBEAT_SCHEDULE =
CELERYBEAT_SCHEDULER =
CELERYBEAT_SCHEDULE_FILENAME =
CELERYBEAT_SYNC_EVERY =
CELERYBEAT_MAX_LOOP_INTERVAL =

#=========================Monitor Server: celerymon=============================
CELERYMON_LOG_FORMAT =  '[%(asctime)s: %(levelname)s/%(processName)s] %(message)s'