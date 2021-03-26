# Поднятия проекта локально

1. Настроить базу данных. <br>
   Откройте MiniStore/settings.py. <br>
   Укажите свои данные.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'store', 
        'USER': 'maksnurgazy',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

2. Делать миграции. <br>
   Cкопируйте приведенный ниже код и запустите в терминале.
```
python manage.py makemigrations
python manage.py migrate
```
3. Заполнение данными. <br>
   Для этого cкопируйте приведенный ниже код и запустите. <br>
   Или же создайте суперпользователя с помощью ```python manage.py createsuperuser```
   этой команды и
   запускайте проек(шаг 4) и сами заполняйте в админ панеле(добавте /admin в URL адреса и введите свои данные) .
```
python manage.py loaddata fixtures/dump.json
```
4. Запуск проекта. <br>
   Cкопируйте приведенный ниже код и запустите в терминале.
```
python manage.py runserver
```