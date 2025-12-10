#!/bin/sh

celery -A backend.celery.worker worker -l debug
