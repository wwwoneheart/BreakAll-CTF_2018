#!/usr/bin/env python3

from pwn import *

r=remote("140.110.112.29", 5123)

r.recvline()

def caesar(s,n):
	a = ""
	for i in range(len(s)):
		if s[i] <> " " and ord(s[i])>64 and ord(s[i])<91:		
			q = ord(s[i]) + n
			if q < 65:
				q = 91 - (65 - q)
			elif q > 90:
				q = 64 + (q - 90)
			a += chr(q)
		else:
			a += s[i]
	return a

for i in range(100):
	r.recvline()
	k = r.recvuntil("\n").strip()
	s = k.split(" : ")[1]
	n = int((k.split(" : ")[0].split("by "))[1])
	r.sendline(caesar(s,n))


r.interactive()