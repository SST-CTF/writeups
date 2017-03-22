# SQL Injection 2
###### 150 Points


### Problem
I've told my friend a billion times that the user called leet1337 doesn't exist on this website, but he won't listen. Could you please login as this user, even though it doesn't exist in the database? Oh and also, make sure that the user has a power level over 9000!!!!

Running sqlmap or the likes will earn you an IP ban.

### Hint
The columns in the table are (not in order) username, password, power_level, and a unique id.

### Writeup
We know that the columns in the database are username, password, power_level, and id.
The most likely order of the columns is id, username, password, power_level.
We can UNION our own user into the table. After some trial and error, this query worked.

```
" UNION SELECT 10, "leet1337", "leet1337", 9999 #
```

###### Flag: easyctf{reUNI0Ns_are_alw4ys_s0_em0t1onal!} 
