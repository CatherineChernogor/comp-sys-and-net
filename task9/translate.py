import requests
import json

key = "82e622ccc27b4ad0af0918182329a742"
region = 'westeurope'


def extract(obj, arr, key):
    """Recursively search for values of key in JSON tree."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                extract(v, arr, key)
            elif k == key:
                arr.append(v)
    elif isinstance(obj, list):
        for item in obj:
            extract(item, arr, key)
    return arr


def translate(string, lang):
    json = [{'Text': string}]

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': region,
        'Content-Type': 'application/json'
    }

    url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=" + lang
    request = requests.post(url, headers=headers, json=json)

    values = extract(request.json(), [], 'text')

    return ''.join(values)


file = open("task9/in.txt", "r", encoding="utf-8")
lang = input('choose language: ')

fout = open("task9/out.txt", "a+")

for line in file.readlines(): 
    string = translate(line, lang)
    fout.write(string)
    print('prosessing')
print('done')
