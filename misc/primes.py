#!/usr/bin/env python3

from pwn import *
from Crypto.Util import number
import math

r=remote("140.110.112.29", 5131)

r.recvlines(7)
for p in range(100):
    a = r.recvline().strip()
    s = r.recvline().strip().split(" ")
    for i in range(1,1000000):
        ans = ""
        k = str(number.getPrime(i))
        if len(k) == int(s[2]):
            while True:
                c = 0
                for j in range(len(k)):
                    c += int(k[j])
                if number.isPrime(c):
                    ans = k
                    break
                else:
                    k = str(number.getPrime(i+1))
        if ans != "":
            break
    r.sendline(ans)

r.interactive()
