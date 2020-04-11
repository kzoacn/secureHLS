key=0123456789123456aaaaaaaaaaaaaaab
iv=a1234567891234560123456789123456

for((i=0;i<=10;i++));  
do   

openssl sm4 -e -in out$i.ts -out out$i.enc -K $key -iv $iv 2> /dev/null

if [ $? -eq 0 ]; then
	echo Enc $i
else
	break
fi

done 
