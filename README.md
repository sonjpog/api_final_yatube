# Учебный проект «API для Yatube»

## Описание проекта

Yatube — учёбный проект курса «backend-python» от [Яндекс.Практикума](https://practicum.yandex.ru), предоставляющий API для социальной сети с базовыми функциями: пользователи могут публиковать, редактировать и удалять свои записи, просматривать контент других участников, оставлять комментарии и подписываться на других авторов.

Контент доступен для просмотра всем пользователям, но для создания и редактирования собственного требуется пройти аутентификацию с помощью JWT-токена.


### Стек технологий:
![phyton](https://camo.githubusercontent.com/26a0e33a85ddbcd406bb08d8156ed000f0ce3b37e0fa9b709ce266fb718444f8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d4646464646463f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d333737364142) ![django](https://camo.githubusercontent.com/69aeb85bd99470605532b2d8029f1d5f4db8982e0aba648e54720192bc1a62ea/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646a616e676f2d4646464646463f7374796c653d666f722d7468652d6261646765266c6f676f3d646a616e676f266c6f676f436f6c6f723d303832453038) ![django rest framework](https://camo.githubusercontent.com/7201b78bcadecbe742d7f2e3be84b0688ca18d4af76c97a3c9b12fb58dcbc27a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446a616e676f2052455354204672616d65776f726b2d4646464646463f7374796c653d666f722d7468652d6261646765266c6f676f3d266c6f676f436f6c6f723d333631353038) ![sqlite](https://camo.githubusercontent.com/9129552136a7b150d218a831da826862017927b5bfe7cb3d9eaa2b1ba8c24ce6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53514c6974652d4646464646463f7374796c653d666f722d7468652d6261646765266c6f676f3d53514c697465266c6f676f436f6c6f723d303033423537)

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/sonjpog/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
### Примеры запросов к API:
#### Получение публикаций: 

Метод GET к эндпоинту http://127.0.0.1:8000/api/v1/posts/{id}/

Пример ответа:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

#### Создание публикации:

Метод POST к эндпоинту http://127.0.0.1:8000/api/v1/posts/
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Пример ответа:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
Подробную версию запросов можно посмотреть по адресу: http://127.0.0.1:8000/redoc/

Автор: [Софья Погосян](https://github.com/sonjpog)
