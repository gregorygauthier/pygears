# Installing Python

There are a few different ways of installing Python on every platform, but you'll likely have the most
success for PyGears (with respect to our dependencies) for the least effort if you follow the instructions
below for your Operating System.


## Windows

1. Download [ActivePython, x86, v2.7.x](http://activestate.com/activepython/downloads)
2. Run the installer


## Linux

Most distributions come with Python installed. If you're not sure, open up a terminal and type the
following. If you don't get a version number (or the version number is not 2.6.x or 2.7.x), search for
"<distro> <distro version> python 2.7" and you should find what you need.

```bash
$ python -V
Python 2.7.1
```


## OS X

Mac OS X comes with Python, but if you're on OS X 10.5 or older, it's too old a version. On those
versions, you can take a few different paths: upgrading your OS, using a VM, or installing
ActivePython (see the Windows instructions above), installing (the official Python)[http://python.org/download/releases/2.7.2], or installing [Homebrew](http://mxcl.github.com/homebrew/) and using Homebrew to install Python.

I personally use Homebrew, and can heartily recommend it as an OS X package manager oriented to developers.

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"
$ brew update
$ brew install python
```
