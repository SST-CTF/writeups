# Ogrewatch
##### 100 Points

### Problem
My friend was out watching ogres when he heard a strange sound. Could you figure out what it means? [ogreman](https://github.com/SST-CTF/writeups/tree/master/Easy%20CTF/Ogreman/ogreman)

### Hint
If you're having trouble with the file format, Gary Kessler might help.

### Writeup
In console, if we 
```
file ogreman
```

We find that the file has Matroska data, or is a .mkv file. If you have mkvtoolnix installed, you can run the command
```
mkvinfo ogreman
```


We see three tracks in the ogreman file: a video track, an audo track, and a subtitle track. We can look at the subtitle with the command
```
mkvextract tracks ogreman 2:subtitle.txt
```

And when we finally read the subtitle file, we see the flag hidden in the subtitles.

###### Flag: [ easyctf{subs_r_b3tt3r_th@n_dub5} ]

