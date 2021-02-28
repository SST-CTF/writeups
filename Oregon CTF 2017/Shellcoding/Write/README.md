Write
100

Do you know how syscalls work? Let's find out!

The flag is in memory (specifically, there's a pointer to it in esi). It's yours for the taking, but you have EXACTLY 16 bytes to steal it with. (Remember, this is x86, and you may pad your shellcode with NOPs if it is shorter. Please provide raw bytes as input (no ASCII representations).


Host: 54.89.227.20

Port: 10080
