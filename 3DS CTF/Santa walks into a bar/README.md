# Santa walks into a bar
###### 100 Points


### Problem
Santa walks into a bar and creates a friendship bound with you.
After some shots, he spells to you his secrets to delivery all gifts on Christmas: he has a magical linked list that inform the next kiddie to visit.
At the end of the night, he goes alway and left behind his wallet and the bag with the list of gifts to delivery. Try to discover if you will receive something. 


### Writeup
Looking into the folder provided in the problem, we see a jpg with Santa's information, and a folder with 11,001 QR codes.
Checking the Santa ID card first - I can see the barcode is PDF417, scanning it with my phone gives me the same ID that is provided on the card (7ab7df3f4425f4c446ea4e5398da8847). Looking at that corresponding QR code we are told to look for another child and another QR code ID is given, the proccess repeats over and over.
We may assume that the flag or some reference to it is hidden in one of the QR codes, not seeing any real pattern we will scan all of the qr codes using a library called [zbarimg](http://zbar.sourceforge.net).
```shell
sudo apt-get install zbar-tools
touch qr_read.txt
zbarimg * > qr_read.txt
```
After scanning, we look at the text file. The problem wants us to find if *you* will recieve anything. Serching the file for *you* we get six occurences. Scanning all six, and (3ab3b4b87d57315315cbb0259a262177) is our lucky winner.
```shell
otakar@sstctf:~/qr/list$ zbarimg 3ab3b4b87d57315315cbb0259a262177.png
QR-Code:Y0ur gift is in goo.gl/wFGwqO inugky3leb2gqzjanruw42yk
scanned 1 barcode symbols from 1 images in 0.03 seconds
```
Going to the link, we get the flag.

###### Flag: 3DS{I_h0p3_th4t_Y0u_d1d_n0t_h4v3_ch4ck3d_OnE_by_0n3}
