import requests
import os
import time

key='0123456789123456aaaaaaaaaaaaaaab'
iv='a1234567891234560123456789123456'

url='http://192.168.1.105:8000/'
tmp_file='tmp.m3u8'
with open(tmp_file,'w+') as f:
    f.write('#EXTM3U\n')
    f.write('#EXT-X-VERSION:3\n')
    f.write('#EXT-X-MEDIA-SEQUENCE:1\n')
    f.write('#EXT-X-TARGETDURATION:10\n')

buffer=[]

while True:
    m3u8=requests.get(url+'playlist.m3u8')  
    lines=m3u8.text.split()
    if lines[0][0]!='#':
        continue
    for i in range(0,len(lines)):
        l=lines[i]
        enc=l.replace('.ts','.enc')
        if l[0]=='#':
            continue
        if l in buffer:
            continue
        ts=requests.get(url+enc)  
        with open(enc,'wb') as f:
            f.write(ts.content)
        os.system('openssl sm4 -d -in %s -out %s -K %s -iv %s' % (enc,l,key,iv) )
        buffer.append(l)
        if len(buffer)>100:
            f=buffer.pop(0)
            os.remove(f)
        print(l)
        with open(tmp_file,'a+') as f:
            f.write(lines[i-1]+'\n')
            f.write(lines[i]+'\n')
    time.sleep(2)
