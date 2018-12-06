#!/usr/bin/env python3

from pwn import *

r=remote("140.110.112.29", 5125)

r.recvlines(5)

for i in range(100):
	r.recvline()
	s = r.recvline().strip().split(" : ")[1]
	r.recvuntil(" : ")
	r.sendline(str(int(s.encode('hex'),16)))

r.interactive()
