**Settings.py**
-
1) SECRET_KEY - секретный ключ (в случае, чего его можно сгенерировать)
2) BASE_DIR - корневая папка проекта
3) DEBUG - если указан True, то в случае ошибки будет выводить подробную информацию, на продакшене нужно менять на False, потому что пользователь не должен знать о деталях, в случае ошибки
4) ALLOWED_HOSTS -  хосты, на которых разрешен запуск вашего проекта, если список пуст, то запустить можно только на локальном хосте (localhost, 127.0.0.1)
5) INSTALLED_APPS - все приложения, которые будет использовать наш проект
6) MIDDLEWARE - функции/классы которые обрабатывают входящий запрос
7) ROOT_URLCONF - главный файл urls.py
8) DATABASES - настройка баз данных, которые будет использовать наш проект


**Как проходит запрос**
-
1) wsgi/asgi - те, кто принимает запрос и возвращает ответ
2) settings.py - MIDDLEWARE (функции/классы который отрабатывают запрос)
3) urls.py - маршрутизатор, который проверяет часть url и если находит совпадения, передает запрос нужный функции/классу
4) views - функции/классы которые возвращает данные в нужном формате
5) serializers - классы, которые преобразуют данные из json в объекты от модели и наоборот
6) models - классы, которые представляют нашу таблицу в БД
7) manager (objects) - классы, которые работают с ORM, у них есть методы для создания обновления, чтения, удаления, фильтрации и тд. записей из таблицы в БД
8) db - база данных 
