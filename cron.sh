#!/bin/sh

##Example usage: . ./cron.sh python3
sh start.sh -d
$1 -m venv venv
source venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/run_scripts.py scripts/ga_main.py,scripts/twitter_main.py,scripts/slack_main.py,scripts/parquet_writer.py,scripts/scheduler.py,scripts/writer.py localhost 10000 30
docker-compose down
deactivate
rm -rf venv
