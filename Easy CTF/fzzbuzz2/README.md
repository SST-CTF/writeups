# Fzz Buzz 2
###### 200 Points


### Problem
Oh no! Two of my keys are broken! Please help me make the same Fzz Buzz program, sans that one letter and queston marks.
As a side note, use of eval() and exec() is also frowned upon and will be marked invalid.

### Hint
Have fun!

### Writeup
Here is the program I used to solve the problem.
```python
def l():global k;o='F%czz'%105;vars(globals().values()[0])['pr%cnt'%105](str(k%3//2*o+k%5//4*'Buzz'or-~k));k+=1
j=vars(globals().values()[0])['%cnt'%105](vars(globals().values()[0])['raw_%cnput'%105]());k=0;m=map(lambda n:l(),range(j))
```
There were two main obstacles I needed to overcome. Calling builtin functions, and looping.
```python
vars(globals().values()[0])
```
contains a dictionary of all builtin functions. We can call print and raw_input by doing:
```python
vars(globals().values()[0])['pr%cnt'%105]
vars(globals().values()[0])['%cnput'%105]
```
We can loop by mapping a lambda function to range(). Note that l() contains the line
we want to loop.
```python
m=map(lambda n:l(),range(j))
```
Everything else should be self explanatory. A casting hack was used for fizzbuzz itself.
```python
str(k%3//2*o+k%5//4*'Buzz'or-~k))
```
Here is the program with better indentation.
```python
def l():
    global k
    o='F%czz'%105
    vars(globals().values()[0])['pr%cnt'%105](str(k%3//2*o+k%5//4*'Buzz'or-~k))
    k+=1

j=vars(globals().values()[0])['%cnt'%105](vars(globals().values()[0])['raw_%cnput'%105]())
k=0
m=map(lambda n:l(),range(j))
```
###### Flag: N/A 
