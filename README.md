# Поиск по копрусу анекдотов
## Как устроен GitHub?
1. Есть [тетрадка](/project.ipynb) для запуска сайта через Google Colab.
2. Есть файлы `.py` c классами для [BM-25](/bm.py), [эмбеддингов](/embed.py) и [лемматизации](/lemm.py) и собственно [`main.py`](/main.py) с запуском через командную строку.
3. Есть [zip-архив](/jokes.zip) с корпусом шуток.
4. Надо скачать корпус для предобучения [w2v](http://vectors.nlpl.eu/repository/20/65.zip) и [navec](https://storage.yandexcloud.net/natasha-navec/packs/navec_hudlit_v1_12B_500K_300d_100q.tar) (см. комментарии и wget).
5. Есть файл [`requirements.txt`](/requirements.txt) со всеми требуемыми для установки библиотеками.
6. Есть папки [`static`](/static/) и [`templates`](/tamplates/) с картинками и страницами соответственно.
## Как пользоваться через CLI?
```
> main.py your_query your_indexer --top=n
```
Где вместо:
* `your_query` - поисковый запрос,
* `your_indexer` - вид индексатора (word2vec, navec, bm25),
* `n` - кол-во анекдотов в выдаче (опционально, дефолтно десять).

## Как запустить сайт?
1. Открыть [тетрадку](/project.ipynb) в Google Colab.
2. Создать на своем Google Drive ярлык с папкой [`projects`](https://drive.google.com/drive/folders/1pcYK6y9qCFIejxxT4QeKp0p6P_rwtQmq?usp=drive_link).
3. Подключить (замаунтить) свой Google Drive к Google Colab'у.
4. Установить все требуемые бибилиотеки из файла [`requirements.txt`](/requirements.txt):
```python
!pip install -r requirements.txt
```
5. Последовательно запустить все ячейки.
6. Перейти по ссылке, окачивающейся на `ngrok-free.app`, и нажать **Visit Site**.
7. Описание работы сайта есть в разделе *what's this?* на верхней панели.
