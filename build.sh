set -o errexit

pip install -r requirements.txt

cd ProntaEntregaDjango

./manage.py makemigrations
./manage.py migrate    

../end_cron.sh
../start_cron.sh 
