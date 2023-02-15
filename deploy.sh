#! /bin/bash
set -e

YGENIUS_HOME=${1:-$HOME/ygenius-brain}
cd $YGENIUS_HOME
docker pull ghcr.io/yearn/ygenius-brain
docker-compose down
docker-compose up -d
