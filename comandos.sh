#iniciando o servidor

python manage.py runserver


#criando mudancas no bd


python manage.py makemigrations core

#migrando mudancas para o banco

python manage.py migrate core


#criando usuario admin

python manage.py createsuperuser