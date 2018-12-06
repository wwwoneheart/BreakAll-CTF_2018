#!/usr/bin/env python3

from pwn import *

r=remote("140.110.112.29", 5122)

r.recvlines(5)

for p in range(100):
	a = r.recvline()
	s = r.recvline().strip().split(" : ")[1].strip().split(" ")
	ans = ""
	for i in range(-100,100):
		k = int(s[len(s)-1])
		for j in range(len(s)-1):
			k += int(s[j]) * i ** (len(s)-1-j)
		if k == 0:
			ans = str(i)
			break
	r.recvuntil(" : ")	
	r.sendline(ans)

r.interactive()
