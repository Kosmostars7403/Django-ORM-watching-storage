# Пульт охраны банка

Это пульт охраны банка, созданный чтобы возвести безопасность банка до невиданных высот.

## Применение
- Для начала убедитесь, что у вас установлены все пакеты из файла `requirements.txt`
- Задайте в своём файле `.env` следующие настройки:
    * `DB_ENGINE` - используемый движок базы данных;
    * `DB_HOST` - адрес хоста, на котором располагается база данных
    * `DB_PORT` - порт для подключения к базе данных
    * `DB_NAME` - имя используемой базы данных
    * `DB_USER` - пользователь, от лица которого производится подключение к базе данных
    * `DB_PASSWORD` - пароль для подключения к базе данных
    * `SECRET_KEY` - секретный ключ, используется для криптографической подписи
    * `DEBUG` - включение отладочного режима. 
- Запустите сайт командой `python manage.py runserver 0.0.0.0:8000`
- Переходите по адресу `0.0.0.0:8000` в браузере и наслаждайтесь зашкаливающим уровнем контроля за каждым
входящим человеком.
