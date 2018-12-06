#!/usr/bin/env python3

from pwn import *

r=remote("140.110.112.29", 5132)

r.recvlines(5)
L=0
R=100000000000
while True:
    r.recvuntil(">")
    r.sendline("4")
    r.recvuntil(" :")
    r.sendline(str((L+R)/2))
    a = r.recvline().strip()
    if a == "that's not enough money (vending machine is angry)":
        L = (L+R)/2 + 1
    elif a == "you give me too much money (money spitting out of vending machine)":
        R = (L+R)/2 - 1
    else:
        print(a)
        break

r.interactive()
