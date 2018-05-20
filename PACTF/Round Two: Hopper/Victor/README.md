# Victor
###### 50 Points


### Problem
Привет, меня зовут Рейно, иначе известный как Виктор. Пожалуйста, расшифруйте это секретное сообщение - у меня нет времени для этого. Я предоставляю вам ключ.

Note: the flag contains Cyrillic characters.

[необходимая информация](https://2018.pactf.com/static/ctfproblems/d18474ee-1fbe-44d5-b55e-7fb3d9de99fb/key.490c9f36a766.png)


### Hint
Google Translate is your friend—but you might want to familiarize yourself with Russian Nihilism, too.


### Writeup
Before we start solving the problem, we should translate the text. Putting it in Google Translate, we get:
```
Hello, my name is Reynaud, otherwise known as Victor. Please, decipher this secret message - I do not have time for this. I give you the key.
```
After some simple Googling about Nihilism, Reino, and Victor, we find that the cipher provided is a so-called [VIC Cipher](https://en.wikipedia.org/wiki/VIC_cipher). Great, we have the ciphertext, the secret shift key, and the mapping table. All we need to do is use this information to decrypt the message.

First, we will reverse the substitution by subtracting each element of the message with the corresponding element of the key modulo 10.


```python
#!/usr/bin/env python3

key = '12261991' * 5
ciphertext = '7264160199640987865519282923616105'

message = [str((int(c)-int(k)) % 10) for c, k in zip (ciphertext, key)]
print(message)
```

    ['6', '0', '4', '8', '0', '7', '1', '0', '8', '7', '4', '8', '9', '0', '9', '6', '7', '4', '3', '9', '0', '0', '3', '7', '1', '7', '0', '7', '5', '2', '7', '0', '9', '3']


If we wanted to, we could already decrypt this by hand by just following the table. For this problem, however, I decided to go a step further. Since each element of the message array does not necessarily correspond to a single characters of the message, I decided to group together the ones that do.


```python
answer = []
extra = False
extra_char = ""

for x in message:
    if extra:
        extra = False
        answer.append(extra_char+x)
    elif x in ("079"):
        extra_char = x
        extra = True
    else:
        answer.append(x)

print(answer)
```

    ['6', '04', '8', '07', '1', '08', '74', '8', '90', '96', '74', '3', '90', '03', '71', '70', '75', '2', '70', '93']


At this point in the problem, I considered recreating the table in the form of a dictionary. However, I decided against it, as the message is quite short and can quickly and comfortably be done by hand. In order to type out the Cyrillic characters, I used this [website](http://translit.net/). Going through the table element by element, we get the flag, which translates to "do it by hand".


###### Flag: СДЕЛАЙТЕ\_ЭТО\_ВРУЧНУЮ
