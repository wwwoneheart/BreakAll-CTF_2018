#!/usr/bin/env python3

from pwn import *

r=remote("140.110.112.29", 5127)

r.recvlines(5)

for i in range(100):
	r.recvline()
	F = int(r.recvline().strip().split(" : ")[1])
	r.recvuntil(" : ")
	C = (F - 32) * 5
	r.sendline(str(C) + "/9")

r.interactive()
