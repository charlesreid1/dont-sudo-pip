# dont-sudo-pip

running `sudo pip install` is dangerous:

* typesquatting
* malicious packages
* system commands

it's basically the same as giving a stranger
on the internet sudo access to your computer.

don't believe me? go ahead and try it:

```
sudo pip install russian_roulette
```

