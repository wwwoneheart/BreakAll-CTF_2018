# code.py
#!/usr/bin/env python
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA
import libnum
import random

priv = DSA.importKey(open("privkey.pem").read())
pub = DSA.importKey(open("public.pem").read())
m = open("signed.txt","rb").read()



def nonce(alice, bob):
	a = libnum.s2n(alice[:8]) 
	s = libnum.s2n(bob[:4]) 
	random.seed(a^s) 
	return a*s + random.randint(a+s,a*s)


def sign_msg(msg):
	alice = open("./alice.png","rb").read()
	bob = open("./bob.jpg","rb").read()
	k = nonce(alice, bob)
	h = SHA.new(msg).digest()
	r = pow(pub.g,k,pub.p) % pub.q
	s = libnum.invmod(k,pub.q)*(libnum.s2n(h) + priv.x * r) % pub.q
	sig = (r,s)
	return sig

sign_file = sign_msg(m)

with open("signature","wb") as f:
	f.write(str(sign_file).encode())