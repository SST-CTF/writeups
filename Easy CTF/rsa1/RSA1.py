#!/usr/bin/python3

import binascii

# c = ciphertext
# e = public key
# p and q = factors of modulus N

#---#
c = 1178032235671904796069257732084448576634823834226462879114286008635793582812470569423832126675102093900618353133532512419270939491860517027175253727624531742226 
e = 65537
p = 36215951468512094769516636400468720236765133100802364573722318478684491531537517 
q = 34015312748391565779234192349552883558194401709266906558140707229972491648342001 
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
