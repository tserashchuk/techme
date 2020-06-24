import client6
#не оформил ошибки

class User(object):
   id: int
   name: str
   messages = []

   def get_users_request(self):
       data = 'GET /users/1/name HTTP/1.0\r\n\r\n'
       answ = client6.request(data, '127.0.0.1', 8080)
       print(answ)


class Message(object):
   id: int
   author: int  # user id
   text: str

   def send_message_request(self):
       data = 'GET / HTTP/1.0\r\n\r\n'
       client6.request(data, '127.0.0.1', 8080)



a = User()
a.get_users_request()


