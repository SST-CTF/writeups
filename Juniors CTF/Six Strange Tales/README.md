# Six Strange Tales
###### 300 Points

### Problem
- Gruncle Stan, what`s the secret of the six fingered hand? 
- Can you see these codes? When the six fingered hand touches them, one of the Gravity Falls secrets opens! 
- Gruncle, but how should we read the secret? From left to right or right to left? Or maybe upside down? 
- It depends on whether you are a Christian, a Muslim or a Taoist... 
![Problem Image](https://github.com/SST-CTF/writeups/blob/Tamir-Writeups/Juniors%20CTF/Six%20Strange%20Tales/StrangeTalesProblem.PNG)

### Writeup
Since this problem was under the **Web** category, it was safe to assume that we would need to look at the source code of the problem.
We find this interesting script element, with a lot of functions in JavaScript that changes the image.

```javascript
window.addEventListener('load', function () {
var b = document.getElementById('img');
var a = b.getContext('2d');
var d = new Image();
d.src = "http://i.imgur.com/GIYH3fA.png";
d.addEventListener('load', function () {
a.drawImage(this, 0, 0);
k = 174;
l = 345;
m = 12; 
n = 89; 
o = 671;
p = 18;
q = 222;
r = q-1;
c="rgba(0,0,0,0)"; 
if (navigator.userAgent == "Gravity Falls") 
c=c.replace(/(0)(\))/,"$1.5$2");
a.fillStyle = c;         
a.fillRect(q%m-6, k-3, n+r-q-2, 5-(p-q));
a.fillRect(2*(q+1), p+1, n+r-q+2, l+16);
a.fillRect(l+r-30, o%p-5, 2*l-600, q+5-p);
a.fillRect(q%n+42, o%p-5, o-600+p+1, 2*(p+1));
a.fillRect(176, o%p-5, 2*l-600, q/2*3+47);
a.fillRect(2*k+p-100, q%m-6, o-600+p+1, n+r-m/2);
a.fillRect(o%p-5, q%m-6, 2*l-604, k-p-4);
a.fillRect(2*k+p-100, q/2*3-10, 3*m+p*3, (p+1)*3);
a.fillRect(2*k+p-m+2, q%m-6,2*l-600, q+n+m-190);
a.fillRect(2*k+p-10, k-p-m/3, o-600+p+1, r+m*2/3+p);
a.fillRect(n-3, q-k+9, 2*(l-300), q+n+m);
a.fillRect(l+q-31, q+m/2,2*l-600, k-p-m/3);
a.fillRect(o-2*p-p/2, q%m-6, 2*l-600, q/2*3+47);
},false);},false);
```

In this jumble, we find that all of the fillRect functions only work under the if-statement where our navigator.userAgent is "Gravity Falls".
Through some research, we can change our userAgent.
On Google Chrome, you need to open your web inspector, and on the bottom tab where the Console appears, next to it are additional options,
and bring out the _Network Conditions_, and you are able to customize your user agent to be "Gravity Falls".

![Solution Image](https://github.com/SST-CTF/writeups/blob/master/Juniors%20CTF/Six%20Strange%20Tales/StrangeTalesSolution.PNG)

From this image, we can test out all of the combinations (top-down, left-right... etc) as it gave us in the original problem
```
Gruncle, but how should we read the secret? From left to right or right to left? Or maybe upside down? 
```

The main thing to look out here is that there is a difference in the **0s** and **Os** in this image, so it's important to pay extra attention.

Eventually, we find that the flag is read under the top-down direction

```
Flag: Maiy2au0Is4feeh3aej8eeThAhWae2Ohdawu0Aebud2juD9a
```
