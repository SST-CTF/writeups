# Open Sourcery 2018
###### 30 Points


### Problem
The solution to this problem lies within the Chromium source code. Literally. There is some string in there that mentions a flag and PACTF...

### Hint
This problem builds off of a similarly named problem in PACTF 2017.

### Writeup
Following the hint, we found a writeup on the last years problem, [Open Sourcery 2](https://writeups.amosng.com/2017/pactf_2017/boole/open-sourcery-2_40/). Their specific search function on the Chromium Source Code leads us directly to the page with our flag, with the lines
```JSON
{ "name": "packetcrash.net", "policy": "bulk-18-weeks", "mode": "force-https", "include_subdomains": true },
    { "name": "pactf-flag-4boxdpa21ogonzkcrs9p.com", "policy": "bulk-18-weeks", "mode": "force-https", "include_subdomains": true },
    { "name": "pactocore.org", "policy": "bulk-18-weeks", "mode": "force-https", "include_subdomains": true },
```

###### Flag: pactf-flag-4boxdpa21ogonzkcrs9p.com
