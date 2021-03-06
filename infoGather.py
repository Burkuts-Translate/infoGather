# this is my Information Gathering miniProject
import socket
import requests
import sys , os
import urllib.request

try:
	os.system("figlet infoGather") #created  in exception for some users where figlet isnot present
except:
	pass
print(f"\nversiyon: v1.2")
try:
	domain = str(sys.argv[1])
	port = int(sys.argv[2])

except (IndexError , ValueError):
	print(f"\033[33mBir Argüman Geçmeli!!!\033[37m")
	sys.exit(2)

try:
	sock = socket.create_connection((domain,port))
	sock.settimeout(50) #50secs , socket will wait 50 sec to try connecting with the  server
 
except:
	print(f"\033[33mAna Makine Ulaşılamaz!!!");
	sys.exit(2)

req = None #no requests

if sock.fileno() != -1: # if domain is up  , then analyse further
	print(f"\033[32mAlan Adı {socket.gethostbyname(domain)} Doldu... \033[37m")
	if port == 443:
		req = requests.get(f"https://{domain}")
		print(f"Durum Kodu : {req.status_code}")
		print(f"Servis Port'u : {socket.getservbyport(port)}")

	if port == 80:
		req = requests.get(f"http://{domain}:{port}")
		print(f"Durum Kodu : {req.status_code}")
		print(f"Servis Port'u : {socket.getservbyport(port)}")

print(f"Hizmet Veren : {req.headers['Server']}")
for i in range(0,1000):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # only dicovers TCP ports i repeat only discovers TCP ports
	s.settimeout(0.2) 
	result = s.connect_ex((domain,i))
	if result == 0:
		print(f"Keşfedilen Port {i}")
      
# request's  headers 
for i in req.headers:
	print(req.headers[i])

 


