# Django-REST-framework example project

## Как начать работу

```
git clone https://github.com/volodya-leveryev/msa1-drf.git
cd msa1-drf
python -m venv venv
venv\scripts\activate.bat
pip install -r requirements.txt
python manage.py runserver
```

Для внесения изменений в структуру БД:

```
python manage.py makemigrations
python manage.py migrate
```

Для создания администратора:

```
python manage.py createsuperuser
```

## Задание

Создать модель StudyGroup со следующими полями:

- name — название группы, строка длиной не более 50 символов
- year — год поступления, целое число

Добавить в студента ссылку на группу в которой он учится.

Внести соответствующие изменения в файлы `admin.py`, `urls.py`, `viewsets.py`, `serializers.py` и т.п.
