#! /bin/bash
set -e

YGENIUS_HOME=${1:-$HOME/ygenius-brain}
echo "updating training-data index..."
cd $YGENIUS_HOME
docker rm -f ygenius-builder || true
docker run --env-file=.env --name ygenius-builder --entrypoint "/app/build_index.sh" ghcr.io/yearn/ygenius-brain
docker cp ygenius-builder:/app/index_new.json .
docker rm -f ygenius-builder || true
docker-compose down
mv index_new.json index.json
docker-compose up -d
