# shell script that runs the mist monitor pythong script.
# Expects a username and password parameters.
# Usage:
# 	mist_monitor_runner.sh <mist_username> <mist_password>

pip install mist
python ./mist_monitor.py $1 $2
