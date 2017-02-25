#!/usr/bin/env python
from Crypto.Cipher import AES
import os
import sys 
import re 

sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

class FlagGetter:
  def __init__(self):
    
    self.key = os.urandom(16)
    self.blocksize = 16
  
  def _pad(self,string):
    padlen = self.blocksize - (len(string) % self.blocksize)
    return string + ( chr(padlen) * padlen)
  
  def _unpad(self,string):
    padlen = string[-1]
    return string[:-ord(padlen)]

  def getUserInput(self):
    line = sys.stdin.readline()
    return re.sub("[^A-Za-z0-9]","",line)

  def auth_token(self):
    print "Input your username"
    username = self.getUserInput()
    
    print "Input your password"
    password = self.getUserInput()
    
    iv = os.urandom(16)
    cipher = AES.new( self.key, AES.MODE_CBC, iv)
    string = self._pad( "username:" + username + ";password:" + password + ";type:user" )
    return (iv + cipher.encrypt(string)).encode('hex')

  def getFlag(self):
    with open('/home/gf/flag', 'r') as f:
      flag = f.readline().strip()
    if self.checkAdmin():
      print "Flag: '" + flag + "'"
      return True
   
    print "Sorry only admins can get flags"
    return False

  def checkAdmin(self):
    print "What was your profile again?"
    enc = self.getUserInput()
    if ( len(enc) < 32 ) or ( len(enc) % 32 > 0 ):
      print "Profile not valid"
      return False
    enc = enc.decode('hex')
    iv = enc[:16]
    profile = enc[16:]
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    plain = cipher.decrypt(profile)
    parts = self._unpad(plain).split(";")
    for p in parts:
      pair = p.split(':')
      if pair[0] == 'type' and pair[1] == 'admin':
        return True
    
    return False

fg = FlagGetter()
print fg.auth_token()

NumTries = 10
for i in range(0, NumTries):
  if fg.getFlag():
    break
  print "Let's try that again... (" + str(9 - i) + " Attempts remaining)" 

