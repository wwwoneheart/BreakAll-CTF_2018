#!/usr/bin/env python3

from pwn import *
import random

r=remote("140.110.112.29", 5129)

r.recvlines(7)
for p in range(100):
    a = r.recvline().strip()
    s = r.recvline().strip().split(" ")
    while True:
        k=""
        for i in range(int(s[2])):
            k += str(random.randint(1,9)).strip()
        c=0
        for j in range(len(k)):
            c += int(k[j])
        if int(k) % c == 0:
            ans = k
            break
    r.sendline(ans)

r.interactive()
