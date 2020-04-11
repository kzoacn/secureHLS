import requests
 

url = 'http://192.168.1.105:8000'

files = {'file': ('playlist.m3u8',open('playlist.m3u8', 'rb'),'application/octet-stream')}           
response = requests.post(url, files=files )
print('Pushing playlist')
for i in range(0,10):
	name='out'+str(i)+'.enc'
	try:
		files = {'file': (name,open(name, 'rb'),'application/octet-stream')}           
		response = requests.post(url, files=files )
		print('Pushing '+str(i))
	except:
		break
