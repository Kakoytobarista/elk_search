#!/bin/bash

wait_for_elasticsearch() {
  until nc -z elasticsearch 9200; do
    echo "Waiting for Elasticsearch to start..."
    sleep 1
  done
}

wait_for_elasticsearch

python -m config.elk.startup

python -m config.elk.data_migration

exec "$@"

echo "Migration finished"
