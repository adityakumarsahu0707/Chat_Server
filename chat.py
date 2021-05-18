import threading
import socket
import time


def send():

  while True:
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text=input()
    text=text.encode()
    s.sendto(text, ("192.168.43.114", 1234))  #Current system's IP
    print("\n")
#    time.sleep(5)

def recieve():
  while True:
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip="192.168.43.193"
    port=1235
    s.bind((ip,port))
    x=s.recvfrom(100)
    rep=x[0].decode()
    print("Reply recieved from " + x[1][0] + " : " + rep + "\n")

t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recieve)

t1.start()
t2.start()
