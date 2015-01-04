# shell script that runs the mist monitor pythong script.
# Expects a username and password parameters.
# Usage:
# 	mist_monitor_runner.sh <mist_username> <mist_password>

if [ -d mist_venv ];
then
    echo "Activating existing virtual env"
    . mist_venv/bin/activate
else
    mkdir mist_venv
    echo "Creating new virtual env"
    virtualenv mist_venv
    . mist_venv/bin/activate
fi

pip install mist

PATH_TO_SCRIPT=`dirname $0`

python $PATH_TO_SCRIPT/mist_monitor.py $1 $2
