# Go Git It
###### 25 Points


### Problem
The <i>code samurai</i> (also known by his pseudonym <i>Nicholas</i>) was making some final optimizations on his program when... he accidentally decapitated it.

Download the samurai's repository [go git it.tar.bz2](https://2018.pactf.com/static/ctfproblems/1c4e67a4-9fd7-4d11-b8e1-5f528344c01b/go_git_it.tar.427f1b62f4aa.bz2)

### Hint
Perhaps 'chopping a branch off a tree' would be the more precise analogy.

### Writeup
First, after downloading the tar.bz2 file, we see that the initial file extension is obfuscated ending in `.tar.427f1b62f4aa.bz2`. Rename the file to just end in `.tar` and run `tar xf filename.tar`. You will find that there is a git repository called "WaveFunctionCollapse/" out of the zipped file.

From our hint, it is implied that there was a branch that was deleted from the repository. We can check the logs with `git reflog` and we see
```git
fad1066 HEAD@{0}: checkout: moving from 01ab3947246a08dcddf71056c330473bbb58d0ed to master
01ab394 HEAD@{1}: commit: I AM THE CODE SAMURAI
116ec49 HEAD@{2}: checkout: moving from master to 116ec4958d68f844d480f50c2bd4dcbe6aa0b909
fad1066 HEAD@{3}: clone: from https://github.com/mxgmn/WaveFunctionCollapse.git
```

The interesting line here is the commit that states "I AM THE CODE SAMURAI" with the specific commit hash `01ab394`.

We check out that specific commit with the command `git show 01ab394` and get:
```git
commit 01ab3947246a08dcddf71056c330473bbb58d0ed
Author: Miles McCain <milesmcc@users.noreply.github.com>
Date:   Fri Apr 6 20:58:41 2018 -0400

    I AM THE CODE SAMURAI

diff --git a/README.md b/README.md
index 3ee1001..b5fff7b 100644
--- a/README.md
+++ b/README.md
@@ -107,3 +107,5 @@ Some samples are taken from the games Ultima IV and [Dungeon Crawl](https://gith

 <p align="center"><img alt="second collage" src="http://i.imgur.com/CZsvnc7.png"></p>
 <p align="center"><img alt="voxel perspective" src="http://i.imgur.com/RywXCHn.png"></p>
+
+The flag is `3x3rc1z3_caut10n_wh3n_d3tach1ng_ur_h3ad`!
```

###### Flag: 3x3rc1z3_caut10n_wh3n_d3tach1ng_ur_h3ad
