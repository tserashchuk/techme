import server6
import re

users = [{'id': '1', 'name': 'Валера', 'messages': 'asdasd'}]
messages = [{'id': '11', 'author': '1', 'message': 'это вам не мать кувыркать'}]


class DataWorker(object):

    def get_user_data(self, id, type):
        result = 'элемент не найден'
        if type == 'user':
            for item in users:
                if item['id'] == id:
                    result = item
        elif type == 'message':
            for item in messages:
                if item['id'] == id:
                    result = item
        return result

    def get_attr(self, id, attr, type):
        result = 'элемент не найден'
        if type == 'user':
            for item in users:
                if item['id'] == id:
                    result = item
                    try:
                        result = result[attr]
                    except IndexError:
                        result = 'не найден соответствующий атрибут'
        elif type == 'message':
            for item in messages:
                if item['id'] == id:
                    result = item
                    try:
                        result = result[attr]
                    except IndexError:
                        result = 'не найден соответствующий атрибут'
        return result

def handle_request(request: str) -> str:

    uri = re.search(r'/.* ', request)
    uri = uri.group(0)[0:len(uri.group(0))-1]
    uri = re.split('/', uri)
    prot = re.search(r'\w*/\d.\d', request)
    prot = prot.group(0)
    body = re.split(r'\r\n\r\n', request)
    body = body[1]
    worker = DataWorker()

    if uri[1] == 'users':
        try:
            return 'HTTP/1.0 200 OK\r\n\r\n' + str(worker.get_attr(uri[2], uri[3], 'user'))
        except IndexError:
            try:
                return 'HTTP/1.0 200 OK\r\n\r\n' + str(worker.get_user_data(uri[2], 'user'))
            except IndexError:
                return 'HTTP/1.0 200 OK\r\n\r\n' + str(users)
    elif uri[1] == 'messages':
        try:
            return 'HTTP/1.0 200 OK\r\n\r\n' + str(worker.get_attr(uri[2], uri[3], 'message'))
        except IndexError:
            try:
                return 'HTTP/1.0 200 OK\r\n\r\n' + str(worker.get_user_data(uri[2], 'message'))
            except IndexError:
                return 'HTTP/1.0 200 OK\r\n\r\n' + str(messages)
    else:
        return 'HTTP/1.0 400 Bad Request\r\n\r\n'


server6.serve(handle_request, '127.0.0.1', 8080)