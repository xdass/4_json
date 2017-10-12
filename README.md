# JSON-форматер

Программа форматирует JSON-формат в удобочитаемый вид и выводит в консоль.<br>
load_data(filepath) - Загружает данные из файла и преобразовывает в json обьект<br>
pretty_print_json(data) - Форматирует JSON-обьект в удобочитаемый формат<br>

# Как пользоваться
filepath - Путь до json-файла с данными
```
python pprint_json.py <filepath>
```

# Примеры

###### Пример запуска скрипта на windows 7 из командной строки, Python 3.5
**Запуск скрипта**
```
python pprint_json.py 'alco_shops.json'
```
**Результат работы скрипта**
```
{
    "features": [
        {
            "geometry": {
                "coordinates": [
                    37.39703804817934,
                    55.740999719549094
                ],
                "type": "Point"
            },
            "properties": {
                "Attributes": {
.... Часть данных обрезана для удобочитаемости
```
###### Запуск скрипта с указанием не существующего файла
**Запуск скрипта**
```
python pprint_json.py 'alco_shops11.json'
```
**Результат работы скрпта**
```
Файл alco_shop1s.json не найден
```

###### Запуск скрипта с указанием пустого файла
**Запуск скрипта**
```
python pprint_json.py 'emtpy.json'
```

**Результат работы скрипта**
```
Файл пустой
```

###### Запуск скрипта без указания файла
**Запуск скрипта**
```
python pprint_json.py
```

**Результат работы скрипта**
```
Укажите имя файла: python pprint_json.py <filename>
```

# Цели проекта

Код написан в образовательных целях. Учебный курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
