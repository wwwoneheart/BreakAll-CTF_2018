#!/usr/bin/env python3

from pwn import *

r=remote("140.110.112.29", 5126)

r.recvlines(10)

ans=""

for p in range(121):
	g = r.recvline().strip()
	a = [0 for i in range(9)]
	while True:
		if a[0] == a[1] and a[1] == a[2] or a[1] == a[4] and a[4] == a[7]:
			if a[1]<>0:
				break
		if a[3] == a[4] and a[4] == a[5] or a[2] == a[4] and a[4] == a[6] or a[0] == a[4] and a[4] == a[8]:
			if a[4]<>0:
				break
		if a[6] == a[7] and a[7]== a[8] or a[0] == a[3] and a[3] == a[6]:
			if a[6]<>0:
				break
		if a[2] == a[5] and a[5] == a[8]:
			if a[5]<>0:
				break
		k = r.recvline().strip()
		s = int(k.strip().split(" : ")[1])
		if g <> "":
			ans += str(s)
		g = ""
		r.recvlines(9)
		a[s] = 2
		if a[0] == a[1] and a[1] == a[2] or a[1] == a[4] and a[4] == a[7]:
			if a[1]<>0:
				break
		if a[3] == a[4] and a[4] == a[5] or a[2] == a[4] and a[4] == a[6] or a[0] == a[4] and a[4] == a[8]:
			if a[4]<>0:
				break
		if a[6] == a[7] and a[7]== a[8] or a[0] == a[3] and a[3] == a[6]:
			if a[6]<>0:
				break
		if a[2] == a[5] and a[5] == a[8]:
			if a[5]<>0:
				break
		c=0
		for i in range(9):
			if a[i] <> 1 and a[i] <> 2:
				a[i]=1
				c=1
				r.sendline(str(i))
				r.recvlines(9)
				break
		if c==0:
			break


r.interactive()

print(ans)
