#!/usr/bin/python3

import binascii

# c = ciphertext
# e = public key
# p and q = factors of modulus N

#---#
c = 369408011835106754994592140032812953837627 
e = 65537
p = 476086083120737490439
q = 857366660267409414053 
N = p * q
phi = (p-1)*(q-1)
#---#

# Greatest common divisor finder

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Modular inverse finder

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No mod inverse')
    else:
        return x % m

# RSA formula

def rsa(c,e,phi):
    phi = (p-1)*(q-1)
    d = modinv(e, phi)
    m = pow(c, d, N)
    return m

# Message to ascii decode

def flag(m):
    decoded_flag = binascii.unhexlify(hex(m).strip('0x'))
    return decoded_flag

def main():
    m = rsa(c,e,phi)
    decoded_flag = flag(m)
    print(decoded_flag)

main()
