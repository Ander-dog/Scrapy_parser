# Краткое описание
Это простенький парсер документов PEP на базе фреймворка Scrapy. По результатам работы в папке results/ создаётся два csv файла: один содержит номер, заголовок и статус каждого PEP, а второй -- сколько документов с каждым статусом всего существует

# Работа с парсером

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Ander-dog/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить парсер

```
scrapy crawl pep
```
# Системные требования
- Python3.9
# Автор
[Андрей А.](https://github.com/Ander-dog)
