# Southern Cross
###### 300 Points

### Problem
- Wow, what's this, Soos? 
- It's the Confederacy's cipher disk with a help of which southerners encrypted their messages. 
- How does it work? 
- Look, Dipper. We need to encode the phrase MABLE EATS SPRINKLES. We don't need any spaces so just delete them. We get MABLEEATSSPRINKLES. Then we have too choose a key. Let it be GRAVITY. And let's go !!! You see, we've encrypted the phrase and here it is RBZTXYZJSKZBLQCEN 
- Cool! 
- Now I'll encode a famous story and you'll try to decode it. By the way, it's much more interesting to read the whole story over, isn't it? 
- That's complicated. Maybe I have to find a key at first. I'd better look for someone who is able to solve this... 
- Don't forget to reach to the end of the text! **The ending is greatly important.**
- [Famous Encoded Story](https://github.com/SST-CTF/writeups/blob/Tamir-Writeups/Juniors%20CTF/Southern%20Cross/crypt.txt)

### Writeup
Along with the description, there was a video describing basically the process of the Vignere Cipher, so we can assume our task is
something to do with the Vignere Cipher.

The story is very, very long, meaning a statistical analysis attack on the cipher is probably a good idea. From the brute-force, we get
the Vigenere key to be **Bolivar**

The decoded story turns out to be the story [_The Roads We Take_](http://www.online-literature.com/o_henry/1044/)

Since the hint told us that the ending is greatly important, we try out the last sentence, "Bolivar cannot carry double"

######Flag: BOLIVARCANNOTCARRYDOUBLE

