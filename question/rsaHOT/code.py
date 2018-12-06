#!/usr/bin/env python
from Crypto.Util.number import *
import libnum
import random

def enc1(bits, msg):
	p = getPrime(bits)
	q = getPrime(bits)
	e = 3
	n = p*q
	assert msg < n
	msg2 = e*msg+libnum.s2n("BreakALLCTF")
	c1 = pow(msg, e, n)
	c2 = pow(msg2, e, n)
	return (c1, c2, n, msg^msg2)

def trans(num, mix, bits):
	mix = int(pow(2,bits-1)) + mix
	for i in range(10000):
		tmp = mix + i
		if isPrime(tmp) and libnum.gcd(tmp, num) == 1:
			break
	assert tmp > 2**(bits-1) - 2**(bits//2) and tmp < 2**(bits-1) + 2**(bits//2)
	return libnum.invmod(num, tmp)

def cal_ed(p, q, mix):
	phi = (p-1) * (q-1)
	bits = size(p*q)
	while(1):
		r = getPrime(bits // 5)
		if libnum.gcd(r, phi) != 1:
			continue
		x = libnum.invmod(r, phi)
		e = trans(x, mix, bits)
		if libnum.gcd(e, phi) == 1:
			break
	d = libnum.invmod(e, phi)
	return (e, d)

def main():
	result = ""
	bits = 1024
	c1,c2,n,mix = enc1(bits, random.randint(pow(3,bits/4), pow(2,bits/2)))
	result += "c1 = %d\nc2 = %d\nn1 = %d\n\n\n" % (c1, c2, n)
	pqbits = size(mix)*3
	flag = libnum.s2n(open("flag.txt", 'r').read())
	p = getPrime(pqbits)
	q = getPrime(pqbits)
	n = p*q
	e, d = cal_ed(p, q, mix)
	c = pow(flag, e, n)
	result += "c = %d\ne = %d\nn = %d\n" % (c,e,n)
	with open("problem.txt","w") as f:
		f.write(result)

main()