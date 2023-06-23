# Flask Test application

Для начала работы нужно скачать и установить MS Code и Git Bash

После установки, открыть MS Code, далее открыть терминал gitbash

В терминале gitbash ввести
> git clone https://github.com/mar0ve/flask_test.git

Далее следовать

- python -m venv venv
- source venv/Sctipts/activate - активируем виртуальную среду
- нажимаем Ctrl+Shift+P - выбираем интерпретатор Python, который расположен в папке venv/Scripts/python.exe
- pip install -r requirements.txt - устанавливаем необходимые модули
- export FLASK_APP=microblog.py
- flask db upgrade (для работы нужен сервер mysql c базой данных)
    > параметры для бд указаны в файле app/__init__.py строка app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://<username>:<db_passwpord>@<host url(localhost)>:3306/<db_name>")

- flask run - запускает проект


# Запуск в Docker Container

> docker build -t microblog:latest .
> docker run --name microblog -d -p 8000:5000 --rm -e SECRET_KEY=test_key -e MAIL_SERVER=smtp.gmail.com -e MAIL_PORT=587 -e MAIL_USE_TLS=true -e MAIL_USERNAME=your_mail@gmail.com -e MAIL_PASSWORD=your_password microblog:latest
