# Clone Attack
###### 200 Points

### Problem
Gravity Falls is under clones attack. Find the real Dipper and save the town 

### Description
The problem asks us to find the real Dipper.
After analyzing the files, we see that only the meta data is different between images.
Specifically, the meta data containing the object name.
We can loop through each image and get its object name metadata and try to find the original.
```shell
#!/bin/bash

for x in *.jpg; do
    echo $x " - " $(exiftool $x | grep "Ксерокопия  номер") >> data.log
done
```

We find that atvF2wf1tfB2IkuV.jpg is the original image (not having the object name metadata tag).
We now find the md5sum of the image to get the flag.

```
md5sum atvF2wf1tfB2IkuV.jpg
```

Flag: cd4d19b8471cecbc8ea7544de59db368
