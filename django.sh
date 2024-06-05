#!/bi/bash
echo "Create migrations"
python manage.py makemigrations djangoapp
echo "=========================="

echo "Migrate"
python manage.py migrate
echo "=========================="

echo "Start server"
python manager.py runserver 0.0.0.0:8000
