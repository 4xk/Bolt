import socket
import threading
class Bolt():
    class newInstance():
        def __init__(self):
            print('initiated bolt object!')
            self.threads = {}
            self.sockets = []
        def connect(self, **kwargs):
            
            s = socket.socket()
            s.connect(("irc.chat.twitch.tv", 6667))
            s.send("PASS {}\r\n".format(kwargs["token"]).encode("utf-8"))
            s.send("NICK {}\r\n".format(kwargs["botname"]).encode("utf-8"))
            s.send("JOIN #{}\r\n".format(kwargs['channel']).encode("utf-8"))
            self.sockets.append(s)
        def recieve(self, socket):
            while True:
                recv = socket.recv(2048)
                print(recv.decode('utf-8'))
        def go(self):
            for s in self.sockets:
                t = threading.Thread(target=self.recieve, args = (s,))
                t.start()
                print(s)
            

