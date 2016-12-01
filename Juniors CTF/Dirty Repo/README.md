# Dirty Repo
###### 400 Points

### Problem
Gruncle Stan loves money very much and doesn't shun to use unacceptable tricks to get it. Not so far he started a new project with an aim to embezzlement of public funds. He hired some developers and decided to "borrow" source code. But one liberal-minded young man didn't like, that Stan's project is a plagiarism. This zealous fighter for justice decided to spoil one developer's project. Try to find out, what the malefactor added.
Here are all developers' projects -> WORKDIRS or > WORKDIRS 

### Description
We are given a tar archive of several computers.

```
tar xf gStproject.tar.gz
tar xf comp_1.tar.gz
tar xf comp_2.tar.gz
tar xf comp_5.tar.gz 
```
We need to find the difference in one of the computers.
Using diff, we see the comp_1 and comp_2 are the exact same.

```
diff -r comp_1 comp_2
```

After testing a few computers, we see that comp_5 has the difference.

```
diff -r comp_1 comp_5
```

Output:
```
diff -r comp_1/openvpn/src/openvpn/forward.c comp_5/openvpn/src/openvpn/forward.c
132a133
> //FLAG -> gRunCle_StAn_tHe_woRsT_coDeR
```

Flag: gRunCle_StAn_tHe_woRsT_coDeR
