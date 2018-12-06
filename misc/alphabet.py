#!/usr/bin/env python3

from pwn import *

r=remote("140.110.112.29", 5128)

r.recvlines(3)

for p in range(100):
    a = r.recvline()
    s = r.recvline().strip().split(" ")
    ans = 0
    for i in range(len(s[4])):
        if s[4][i] == s[2]:
            ans += 1
    r.sendline(str(ans))

r.interactive()
