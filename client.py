import socket
#from textblob import TextBlob
from googletrans import Translator

s=socket.socket()
host=input(str('enter the host name to connect :'))
port =8080
s.connect((host,port))
print('connected to chat server')
while 1:
    incomming_message=s.recv(1024)
    incomming_message=incomming_message.decode()
   # blob=TextBlob("incomming_message")
    translator = Translator()
    #incomming_message=blob.translate(to='es')
    incomming_message = translator.translate(incomming_message, dest='kn').text
    print('friend>>',incomming_message,'\n')
    message=input(str('you>>'))
    message=message.encode()
    s.send(message)
    print("send \n")