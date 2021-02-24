#!/bin/bash
# No more than 100 lines of code
wait_for () {
    for _ in `seq 0 100`; do
        (echo > /dev/tcp/$1/$2) >/dev/null 2>&1
        if [[ $? -eq 0 ]]; then
            echo "$1:$2 accepts connections!^_^"
            break
        fi
        sleep 1
    done
}
populate_env_variables () {
  set -o allexport
  [[ -f /src/core/.env ]] && source /src/core/.env
  set +o allexport
  echo "env variables are populated!^_^"
}
populate_env_variables
case "$PROCESS" in
"LINT")
    wait_for "${DB_HOST}" "${DB_PORT}"
    python manage.py migrate \
    && mypy . && flake8 . && bandit -r . --exclude tests && safety check
    ;;
"DEV_DJANGO")
    wait_for "${DB_HOST}" "${DB_PORT}"
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    python manage.py migrate && python manage.py runserver 0.0.0.0:8000
    ;;
"DEV_CELERY")
    wait_for "${DB_HOST}" "${DB_PORT}"
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A core worker -B --loglevel=INFO --concurrency=1
    ;;
"TEST")
    wait_for "${DB_HOST}" "${DB_PORT}"
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    pytest -v --cov . --cov-report term-missing --cov-fail-under=100 \
    --color=yes -n 4 --no-migrations --reuse-db -W error \
    -W ignore::django.utils.deprecation.RemovedInDjango40Warning \
    -W ignore::ResourceWarning
    ;;
"DJANGO")
    wait_for "${DB_HOST}" "${DB_PORT}"
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    python manage.py collectstatic --noinput && python manage.py migrate
    gunicorn -c core/gunicorn.py core.wsgi
    ;;
"CELERY_SCHEDULER")
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A core beat --loglevel=INFO
    ;;
"CELERY_CONSUMER")
    wait_for "${DB_HOST}" "${DB_PORT}"
    wait_for "${BROKER_HOST}" "${BROKER_PORT}"
    celery -A core worker --loglevel=INFO \
    --concurrency=12 --max-tasks-per-child=2048
    ;;
*)
    echo "NO PROCESS SPECIFIED!>_<"
    exit 1
    ;;
esac
