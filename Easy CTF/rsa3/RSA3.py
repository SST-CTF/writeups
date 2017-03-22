#!/usr/bin/python3

import binascii

# c = ciphertext
# e = public key
# p and q = factors of modulus N

#---#
c = 2907995727224121244474109148869412603986746589983095760953378907471772983106265015352351411281256847387789301815094608746590512178894738862276459859204020010443067567963450732279228357933677075986407 
e = 65537
p = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780869
q = 3423616853305296708261404925903697485956036650315221001507285374258954087994492532947084586412780871 
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
