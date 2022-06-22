#!/bin/bash

NAME="Gunicorn-Server"                                           # Name of the application
DJANGODIR=/home/ubuntu/passataDjango                             # Django project directory
SOCKFILE=/home/ubuntu/passataDjango/passata/wsgi.sock            # we will communicate using this unix socket
USER=ubuntu                                                      # the user to run as
GROUP=ubuntu                                                     # the group to run as
NUM_WORKERS=2                                                    # how many worker processes should Gunicorn spawn
# timeout for uploads https://stackoverflow.com/questions/6816215/gunicorn-nginx-timeout-problem
TIMEOUT=300
DJANGO_SETTINGS_MODULE=passata.settings                         # which settings file should Django use
DJANGO_WSGI_MODULE=passata.wsgi                                 # WSGI module name

echo "Starting $NAME as `whoami` at: `date +%H:%M:%S--%m-%d-%Y`"

# Activate the virtual environment
cd $DJANGODIR
# Load env variables
. /home/ubuntu/Passata/passataDjango/.secrets
# activate virtual env
source /home/ubuntu/Passata/passata-env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH


# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER \
  --group=$GROUP \
  --timeout=$TIMEOUT \
  --bind=unix:$SOCKFILE \
  --log-level=critical \
  --log-file=$DJANGODIR/backend/logs/gunicorn.log
  # --error-logfile=$DJANGODIR/logs/gunicorn-error.log \
