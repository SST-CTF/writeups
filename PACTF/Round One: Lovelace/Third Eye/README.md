
# Third Eye
###### 40 Points


### Problem
Sometimes​‌‌‌​‌‌‌​‌‌​ there‌​​​​‌‌​​​​‌ is ​‌‌‌​‌​​​‌​‌‌‌more ‌‌​‌‌​​‌​‌​‌‌​‌‌​​​‌‌‌​​‌‌​‌‌​​‌​‌​‌​‌‌‌‌‌​‌‌​‌‌​​​‌‌‌​‌​‌​‌‌‌​​‌​​‌‌​‌​‌‌​‌‌‌​​‌‌​‌​‌‌‌‌‌​‌‌​​​‌than ​​‌‌​​‌​‌​‌‌​‌‌meets ‌​​‌‌​​‌​‌​‌‌​​​the ​‌​‌‌‌​‌​​​‌‌​‌​​​​‌​‌‌‌‌‌​‌‌‌eye​‌​​​‌‌​‌​​​​‌‌​​‌​‌​‌​‌‌‌‌‌​‌‌​​‌​‌​‌‌‌‌​​‌​‌‌​​‌​‌.

### Hint
Maybe if you just squint harder...

### Writeup

More than meets the eye huh? Let's copy the string into a [text file](message.txt) and open it with a text editor (e.g. vim).

Looks like we have some invisible characters. Interestingly enough, there are only two types: `<200c>` and `<200b>`. These likely represents the binary digits `1` and `0` respectively. Now all we have to do is write a short script that will convert the invisible characters to ones and zeroes and print out the resulting ascii string:


```python
#!/usr/bin/env python3

import binascii

with open('message.txt', 'r') as f:
    given = f.readline()

solution = ''
for x in given:
    if x == '\u200c':
        solution += '1'
    elif x == '\u200b':
        solution += '0'

print(binascii.unhexlify(hex(int(solution, 2))[2:]).decode())
```

    what_else_lurks_beneath_the_eye


###### Flag: what_else_lurks_beneath_the_eye
