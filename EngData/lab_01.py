import json
import csv

def t2():
    js = {
        'sex': {
            'female': {
                'class': {
                    '1': {
                        'SurvivedCount': 0
                    },
                    '2': {
                        'SurvivedCount': 0
                    },
                    '3': {
                        'SurvivedCount': 0
                    },

                }
            },
        }
    }
    with open('data.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            if line['Survived'] == '1' and line['Sex'] == 'female':
                js['sex']['female']['class'][line['Pclass']]['SurvivedCount'] += 1

            # passId = line['PassengerId']
        print(js)

def t1():
    js = {"Date": "01.01.2021", 'name': 'Foreign Currecy Market',
          'Valute': {}
          }

    valutes = {}
    headers = ["ID", "NumCode", "CharCode", "Nominal", "Name", "Value"]

    with open('data_bank.csv', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            valuteName = line["Valute"]
            valute = {}
            for h in headers:
                if h == 'Valute':
                    continue
                if h == "Nominal":
                    valute[h] = int(line[h])
                    continue
                if h == "Value":
                    valute[h] = float(line[h])
                    continue
                valute[h] = line[h]
            valutes[valuteName] = valute

    js['Valute'] = valutes
    jso = json.dumps(js, ensure_ascii=False)

    fo = open('json.json', 'w+', encoding='utf-8')
    fo.writelines(jso)

    print(jso)

