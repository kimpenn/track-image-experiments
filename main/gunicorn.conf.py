accesslog = "-"
access_log_format = '%(t)s [%({x-forwarded-for}i)s %(M)sms] "%(m)s %(U)s?%(q)s" %(s)s %(b)s'
preload_app = True
timeout = 60
bind = "0.0.0.0:8000"
workers = 4
module = "main.wsgi"
# used this for Docker
# chdir = "/app/"


def post_fork(server, worker):
    from django.core.management import call_command

    call_command("collectstatic", interactive=False)
