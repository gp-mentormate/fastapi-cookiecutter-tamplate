#!/bin/sh
set -e

if [ "$ENV" = "dev" ]
then
    uvicorn src.main:app --host 0.0.0.0 --port 8001 --reload
else
    uvicorn src.main:app --host 0.0.0.0 --port 8001 --workers=2
fi

exec "$@"
