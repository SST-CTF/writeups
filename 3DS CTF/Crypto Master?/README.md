# Crypto Master?
###### 100 Points


### Problem
John says that he is the master of his personal server. He created a script that talks to him as if it was his disciple. The problem is that in order to access the server, one needs to know the logic used by the script. Access the server and get the flag. 
Server: 54.175.35.248:8002 

### Writeup
```shell
nc 54.175.35.248 8002
Hi! Are you my master?
YES
So prove it! We have a secret code so we can talk secretly.
I will give you a couple of hints!
If you give me a C, I give you a W.
If you give me a F, I give you a T.
If you give me a Z, I give you a 0(zero).
So, what if I give you an I? What should you give me?
```
Looking at the given input, we realize that the sum of the ascii values in decimal for the two letters is 154. Assuming this pattern holds true, I &rarr; Q.
```shell
Q
Nice! But this doesnt prove much.
Translate the following and I shall give to you what youre looking for:
```
Continuing the pattern we get QYMFRUMYGFUHKTWQJRUHG &rarr; IAMTHEMASTEROFCIPHERS.
```shell
QYMFRUMYGFUHKTWQJRUHG
IAMTHEMASTEROFCIPHERS
Hello my master! Here is what you seek: 3DS{M4st3r_My_455}.
```
And just like that, we have the flag.


###### Flag: 3DS{M4st3r_My_455}
