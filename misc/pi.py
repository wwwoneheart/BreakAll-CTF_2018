#!/usr/bin/env python3

from pwn import *

g=0
while g==0:
    try:
        r=remote("140.110.112.29", 5130)
        r.recvlines(5)
        b="3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745"
        for p in range(100):
            a = r.recvline().strip()
            print(a)
            s = r.recvline().strip().split(" ")
            ans = b[0:int(s[2])+1]
            if int(b[int(s[2])+1:int(s[2])+2])>=5:
                t=1
                for i in range(int(s[2])+1,0,-1):
                    if int(b[i-1:i])+t >=10:
                        ans = ans[:i-1] + str(int(b[i-1:i])+t) + ans[i+1:]
                        t = 1
                    else:
                        ans = ans[:i-1] + str(int(b[i-1:i])+t) + ans[i+1:]
                        t=0
                        break
            r.sendline(ans)
        r.interactive()
    except:
        print("continue")
g=1
