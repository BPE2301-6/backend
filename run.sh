#!/bin/sh
set -e

#echo "🔄 applying migrations..."
#python3 -m alembic upgrade head

echo "🚀 starting backend..."
exec python3 -m src.api