Фотографии в базе данных хранятся в виде url нужно добавить!!!
1. Подключиться к sql_app.db открыть таблицу items
2. Скачиваем фото в формате jpg в папку static
3. Записываем в базу название файла: "cap.jpg"
4. При запросе в базу будет выдавать полный путь к вашим фото, можно будет зайти по 
полному пути в теле ответа "localhost:8000/static/cap.jpg"
Только после того как добавили url фото продолжать!!!
1. Создание контейнера ~$docker build -t fastapi-app .
2. Запуск ~$docker run -p 8000:8000 fastapi-app
3. Swagger localhost:8000/docs