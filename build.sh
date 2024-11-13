set -o errexit

pip install -r requirements.txt

cd ProntaEntregaDjango

./manage.py makemigrations
./manage.py migrate    