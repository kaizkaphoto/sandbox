# Color chart

![output.png](output.png)


# Contact

Twitter: https://twitter.com/kaizkaphoto

----

# Memo

## Developing environment 

* Python3.9
* skia-python

```sh
# sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

# curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

Add to .bashrc follows:

```sh
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init - zsh --no-rehash)"
eval "$(pyenv virtualenv-init -)"
```

```sh
$ pyenv -v
$ pyenv install 3.9.2
$ pyenv global 3.9.2
$ python --version
$ which python
```

```sh
$ git clone git@github.com:kaizkaphoto/sandbox.git
$ cd ~/sandbox
$ python -m venv sandbox
$ source sandbox/bin/activate
$ python -m pip install --upgrade pip
Collecting pip
  Downloading pip-21.0.1-py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 758 kB/s
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.2.3
    Uninstalling pip-20.2.3:
      Successfully uninstalled pip-20.2.3
Successfully installed pip-21.0.1

$ pip install pycodestyle

# apt-get install libfontconfig1 libgl1-mesa-glx libgl1-mesa-dri
$ pip install skia-python numpy scipy
```
