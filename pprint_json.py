import json
import sys


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as file:
            raw_data = file.read()
        deserialize_obj = json.loads(raw_data)
        return deserialize_obj
    except FileNotFoundError:
        return None


def pretty_print_json(deserialize_obj):
    return json.dumps(deserialize_obj, indent=4, sort_keys=True,
                      ensure_ascii=False)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
        json_data = load_data(path)
        if json_data is not None:
            pretty_json = pretty_print_json(json_data)
            print(pretty_json)
        else:
            print('Файл не найден')
    else:
        print('Укажите имя файла: python pprint_json.py <filename>')
