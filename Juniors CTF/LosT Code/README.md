# LosT Code!!!
###### 200 Points

### Problem
Given the LosT Programs

### Description
We are given a LosT bruteforce program.
We need to guess a 32 digit alphanumeric string.
If a digit of the guess string matches the actual string, the program returns 1. 
Otherwise, the program returns 0.

EX:
Actual: ABABCDEFGA
Guess: AAAAAAAAAA

Returns: 1010000001

The below program bruteforces the flag.
```shell
#!/bin/bash

COUNTER=1

function brute {

    default='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    for x in {0..9} {a..f}; do
        new=$(echo $default | sed s/A/$x/$1)
        if [[ $(./LosT.x32 -b $new) == *1* ]]; then
            echo $x
            break
        fi
    done
}

answer=""

for x in {1..32}; do
    answer=$answer$(brute $x)
done

echo $answer
```
Flag: 616dc3888a99170c5b8aa721d925ac68
