# Hot Sun?
###### 100 Points


### Problem
Surfing in the Shallowweb, we have discovered a new algorithm that promises to be the newest substituition cipher. The algorithm to encrypt works as following: the user informs the text to be encrypted and a number N. Initially, the algorithm shift all letters one position to the right (e.g. 'A' tuns into 'B'). With this result, in the next step, the algorithm now shift the text two positions to the right. And with the text from the previous output, it repeats the shift procedure until N. Your task is quite simple: given an encrypted flag and an N number, discover the flag. 
Encrypted flag: 3RG{hv1g_f0h_1g_b0h_g0_V0h}


### Writeup
Looks like a Ceasar Cipher to me!
[Using our handy tool](https://gchq.github.io/CyberChef/?recipe=%5B%7B%22op%22%3A%22ROT13%22%2C%22args%22%3A%5Btrue%2Ctrue%2C%2212%22%5D%7D%5D&input=M1JHe2h2MWdfZjBoXzFnX2IwaF9nMF9WMGh9IA)
The key looks to be twelve, and we have the flag.

###### Flag: 3DS{th1s_r0t_1s_n0t_s0_H0t} 
