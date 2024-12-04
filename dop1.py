import json
import yaml

def convert(file):
    parsed_data = yaml.safe_load(file)

    json_output = json.dumps(parsed_data, ensure_ascii=False)
    return json_output

if __name__ == '__main__':
    file = open("schedule.yaml", encoding="utf-8")

    with open('output1.json', 'w', encoding='utf-8') as json_file:
        json_file.write(convert(file))