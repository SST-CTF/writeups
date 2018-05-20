
# Letter to a Machine 
###### 25 Points


### Problem
You intercepted a [letter.rar](letter.c5e1ae35c726.rar)—but to read it, you have to prove that you are not a human. The password is `NOT BAD` + `FACE`.


### Hint
I’m sure it’s just coincidence that `BAD` and `FACE` can be spelled with just the letters `ABCDEF`…

### Writeup
If it wasn't obvious already, the hint informs us that both `BAD` and `FACE` are hexadecimals. This means that the password to the archive file is likely the result of the `NOT` operation applied to `BAD` added with `FACE`. This can be done with a simple line in python:


```python
print(hex(~0xbad+0xface)[2:].upper())
```

    EF20


I decided to turn the output to uppercase to stay consistent with the input. When we use the password `EF20` to open the archive, we recieve a `flag.txt` file with the flag in it.

###### Flag: lIZORZaOkWrIuNB
