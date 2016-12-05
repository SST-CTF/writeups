# Black Suprematic Square
###### 100 Points

### Problem
The problem gives us a scary looking black square with no information except the fact this is a 'web' problem.
![Black Square](http://i.imgur.com/pg07hJL.jpg)

### Writeup
Seeing as this is a web problem the first step is to look into the HTML source. Inspecting element on the black square we see the following:
```html
<div id="task_body">
    <center>
        <div style="width: 478px;">
            <img src = "http://i.imgur.com/pg07hJL.jpg" >
            <img src = "http://i.imgur.com/YyHPw50.jpg" width="0">
        </div>
        <br>
        M.Iu.Lupanov<br><br>
    </center>
</div>
```
I can see that there is a hidden image behind the black square with width of 0. Modifying the HTML to see that image:
```html
<div id="task_body">
    <center>
        <div style="width: 478px;">
            <img src = "http://i.imgur.com/pg07hJL.jpg" width="0">
            <img src = "http://i.imgur.com/YyHPw50.jpg" width="500">
        </div>
        <br>
        M.Iu.Lupanov<br><br>
    </center>
</div>
```
![Image of Flag](http://i.imgur.com/YyHPw50.jpg)
We now transcribe the image, that was painful, but we have the flag.

###### Flag: aima0AiwahsidupaiToehoong1PhieruqueivahphieKah7uceetair9aiGae1eSsaedoo4becooShohhu8eifahXi7EJoh2gaephechei5chiP9
