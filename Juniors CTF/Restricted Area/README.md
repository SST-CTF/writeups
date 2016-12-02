# Restricted Area
###### 400 Points

### Problem
You are given a trial run as an admin in the Mystery Shack. 
Your first task is to define access permissions to the critical information, according to the matrix
The information is stored on the special storage disk. There is also information about system users and a program, which checks, if the settings are correct. If you do it right according to the matrix, you`ll receive a flag.

### Description
We first get an external filesystem. We can mount this to our machine.

```
gzip -d image.bin.gz
sudo mount image.bin mount1/
```

We see that we need to make 5 users, with specific user ids (according to the passwd file).

```
useradd -u 1004 dipper
useradd -u 1005 mabel
useradd -u 1006 soos
useradd -u 1007 wendy
useradd -u 1008 stan
```

The binary checks the permissions for each of the users. Each user controls 8 digits of the flag.
We can fix permissions for one user at a time by changing owner permissions according to the matrix.

EX:
```
chown dipper lazy_black_cat
chown dipper lazy_red_cat
.
.
.
```
Running the binary ./check_32 after fixing permissions for each user, we get the following results:
```
Dipper: 09D240FD00000000000000000000000000000000
Mabel: 0000000060442F6C000000000000000000000000
Soos: 0000000000000000D3F45E470000000000000000
Wendy: 000000000000000000000000704D9DCB00000000
Stan: 00000000000000000000000000000000F0344B0D
```
Putting the results together gives us the flag.

Flag: 09D240FD60442F6CD3F45E47704D9DCBF0344B0D
