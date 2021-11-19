# Guido van Rossum <guido@python.org>
import json
import urllib.request
import os
API_URL = 'https://zeapi.yandex.net/lab/api/yalm/text3'
option = ''
answer = ['Утка-маляр 🦆 решила выпить зайти в бар.\nВзять ей зонтик? ☂️']
options = {'да': True, 'нет': False}

def step2_umbrella(api,data_to_send):
    payload = {"query": data_to_send, "intro": 0, "filter": 1}
    params = json.dumps(payload).encode('utf8')
    req = urllib.request.Request(api, data=params, headers= {'Content-Type': 'application/json'})
    response = urllib.request.urlopen(req)
    json_data = json.loads(response.read().decode('utf8'))
    answer.append(json_data['text'])
    return step1(option,options,answer)


def step2_no_umbrella():
    print('Сохранить рассказ?: {}/{}'.format(*options))
    option = input()
    if options[option]:
        with open('omd.txt', 'w', encoding='utf-8') as f:
            for string in answer:
                f.write(string) 
    
def step1(option,options,answer):
    print(answer[-1])
    while option not in options:
        print('Балабобим дальше?: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella(API_URL,answer[-1].split('\n')[-1])
    return step2_no_umbrella()

if __name__ == '__main__':

    step1(option,options,answer)

