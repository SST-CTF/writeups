# ROFL
###### 400 Points

### Problem
Given is a cypher text, and a link that leads to a "Base64" wikipedia page

### Writeup
We need to decode the text file a certain amount of times using Base64 in order to get the flag.
The amount of times was experimentally found to be '33'

The below program decodes the cypher text and returns the flag.
```shell
#!/bin/bash

cp rofl old.txt
touch new.txt

for i in {1..33}
do
    cat old.txt | base64 -d -i > new.txt
    cp new.txt old.txt
done

rm old.txt
cat new.txt | less

```

If the script returns a string similar to 'E8 C9 F6 C9 CE E1 _ DE F5 C4 C5 F3' it must be decoded on https://2cyr.com/decode/?lang=ru

###### Flag: ХиЖинА_чУдеС

