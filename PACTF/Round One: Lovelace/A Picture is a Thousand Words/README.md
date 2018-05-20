# A Picture is a Thousand Words
###### 10 Points

### Problem
Apparently there is something hidden in this [image](problem.jpg)

### Hint
You're looking for text--how might you look at the text of the image?

### Writeup
As the first problem on the list of problems, this one should be fairly straight forward. We are looking for the text in the files. Also, if we want to find the flag, we can pipe it with grep to function as an ascii search in the image.

`strings problem.jpg | grep "flag"`

Our flag is in the resultant line.

###### Flag: flag_is_DjKVIXXQRZZrrAd
