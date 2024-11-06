import socket
#from textblob import TextBlob
from googletrans import Translator

s= socket.socket()
host = socket.gethostname()
print('server will start a host:',host)
port=8080
s.bind((host,port))
print("waiting for connection \n")
s.listen(1)
conn,addr=s.accept()
while 1:
    message=input(str('you>>'))
    message=message.encode()
    conn.send(message)
    print("send \n")
    incomming_message = conn.recv(1024)
    incomming_message=incomming_message.decode()
   # blob=TextBlob("incomming_message")
    translator = Translator()
    #incomming_message=blob.translate(to='en')
    incomming_message = translator.translate(incomming_message, dest='en').text
    print('friend>>',incomming_message,'\n')