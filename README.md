# Поиск по копрусу анекдотов
## Как устроен GitHub?
1. Есть [тетрадка](/project.ipynb) для запуска сайта через Google Colab.
2. Есть файлы `.py` c классами для [BM-25](/bm.py), [эмбеддингов](/embed.py) и [лемматизации](/lemm.py) и собственно [`main.py`](/main.py) с запуском через командную строку.
3. Есть [zip-архив](/jokes.zip) с корпусом шуток.
4. Надо скачать корпус для предобучения [w2v](http://vectors.nlpl.eu/repository/20/65.zip) и [navec](https://storage.yandexcloud.net/natasha-navec/packs/navec_hudlit_v1_12B_500K_300d_100q.tar) (см. комментарии и wget).
5. Есть файл [`requirements.txt`](/requirements.txt) со всеми требуемыми для установки библиотеками.
6. Есть папки [`static`](/static/) и [`templates`](/templates/) с картинками и страницами соответственно.
## Как пользоваться через CLI?
```python
> python main.py your_query your_indexer --top=n
```
Где вместо:
* `your_query` - поисковый запрос с нижними подчеркиваниями вместо пробелов,
* `your_indexer` - вид индексатора (word2vec, navec, bm25),
* `n` - кол-во анекдотов в выдаче (опционально, дефолтно десять).

## Как запустить сайт?
1. Открыть [тетрадку](/project.ipynb) в Google Colab.
2. Создать на своем Google Drive ярлык с папкой [`projects`](https://drive.google.com/drive/folders/1pcYK6y9qCFIejxxT4QeKp0p6P_rwtQmq?usp=drive_link).
3. Подключить (замаунтить) свой Google Drive к Google Colab'у и скопировать папку `projects` в `content` (первая ячейка тетрадки).
4. Установить все требуемые бибилиотеки
   1. Из файла [`requirements.txt`](/requirements.txt):
    ```python
    !pip install -r requirements.txt
    ```
   2. Раскомментить установки во второй ячейке.
5. Залогиниться или зарегистрироваться в [ngrok](https://ngrok.com/) и получить свой код аутентификации. Запустить код из третьей ячейки, где вместо `your_authtoken` надо подставить аутентификационный токен:
   ```python
   !ngrok authtoken your_authtoken
   ```
7. Последовательно запустить все ячейки.
8. Перейти по ссылке, окачивающейся на `ngrok-free.app`, и нажать **Visit Site**.
9. Описание работы сайта есть в разделе *what's this?* на верхней панели.
