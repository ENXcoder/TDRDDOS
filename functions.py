import random
import socket
import time
import threading
def start(m,x,y,z,w):
  for y in range(m):
      
          th = threading.Thread(target =x)
          th.start()
          th = threading.Thread(target = y)
          th.start()
          th = threading.Thread(target = z)
          th.start()
          th = threading.Thread(target = w)
          th.start()
