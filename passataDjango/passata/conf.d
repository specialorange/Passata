[program:passata-gunicorn]
directory=/home/ubuntu/Passata/passataDjango/passata
command=/home/ubuntu/Passata/passataDjango/passata/gunicorn.sh                                      ; Command to start app
user=ubuntu                                                                                         ; User to run as
stdout_logfile=/home/ubuntu/Passata/passataDjango/backend/logs/supervisor/gunicorn.log              ; Where to write log messages
stderr_logfile=/home/ubuntu/Passata/passataDjango/backend/logs/supervisor/gunicorn-errors.log
# redirect_stderr=true                                                                              ; Save stderr in the same log
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8                                                     ; Set UTF-8 as default encoding
autostart=true
autorestart=true

; Need to wait for currently executing tasks to finish at shutdown.
; Increase this if you have very long running tasks.
stopwaitsecs = 600

stopasgroup=true

; Set Celery priority higher than default (999)
; so, if rabbitmq is supervised, it will start first.
priority=1000