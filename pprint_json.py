import json
import sys
from pathlib import Path


def load_data(filepath):
    if Path(filepath).exists():
        if Path(filepath).stat().st_size == 0:
            return None
        with open(filepath, encoding='utf-8') as file:
            raw_data = file.read()
        json_obj = json.loads(raw_data)
        return json_obj
    else:
        print('Файл {} не найден'.format(filepath))


def pretty_print_json(data):
    if data is not None:
        print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    else:
        print('Файл пустой')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
        json_data = load_data(path)
        pretty_print_json(json_data)
    else:
        print('Укажите имя файла: python pprint_json.py <filename>')

