from werkzeug.test import Client
from app_server import app_server, app_client

from pony.orm import *
from pony import orm
import os

choice = ''
while True:
    os.system('CLS')
    print('+'+'='*33+'+\n| Выберите один из вариантов:\n|\n| 1) Создать заметку\n| 2) Вывести все заметки\n| 3) Изметить заметку по id\n| 4) Удалить заметку по id\n| Для выхода нажмите любую кнопку\n'+'+'+'='*33+'+\n')
    print('--->', end='')
    choice = input()
    if (choice == '1'):
        print ('title=', end='')
        _title = input()
        print ('content=', end='')
        _content = input()
        res = app_client.post('/', json={'title': _title, 'content': _content})
        print(res.status_code)
        print(res.get_json())
        print ('Нажмите любую клавишу для продолжения', end='')
        input()
    elif (choice == '2'):
        print(app_client.get('/').get_json())
        print ('Нажмите любую клавишу для продолжения', end='')
        input()

    elif (choice == '3'):
        print ('id=', end='')
        _id = input()
        print ('title=', end='')
        _title = input()
        print ('content=', end='')
        _content = input()
        res = app_client.put('/'+_id, json={'title': _title, 'content': _content})
        print(res.status_code)
        print(res.get_json())
        print ('Нажмите любую клавишу для продолжения', end='')
        input()
    elif (choice == '4'):
        print ('id=', end='')
        _id = input()
        res = app_client.delete('/'+_id)
        res.status_code
        print ('Нажмите любую клавишу для продолжения', end='')
        input()
    else:
        break


