# Development Setup

Setting up to develop PyGears requires a few steps. The exact steps are
largely OS dependent; see instructions for Ubuntu 10.10+, OS X 10.6,
and Windows 7 below.

## Everyone

After following your OS-specific instructions, follow these instructions to
set up your SSH keys so you can push code to github.com.

Check to see if you already have an private/public key pair.

    $ cat ~/.ssh/id_rsa.pub
    cat: /home/russ/.ssh/id_rsa.pub: No such file or directory

If the file doesn't exist, execute the following commands to generate a new
public/private key pair.

    $ ssh-keygen -t rsa -b 1024
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/russ/.ssh/id_rsa):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/russ/.ssh/id_rsa.
    Your public key has been saved in /home/russ/.ssh/id_rsa.pub.
    ...

_NB: the only reason to include a password for this if you think someone that
has physical access to your computer is going to try pushing code to
github.com. I recommend leaving the passphrase blank for convenience's sake._

Now, navigate to github.com > Account Settings > [SSH Public Keys](https://github.com/account/ssh)
and click "Add another public key".

Give it a name useful to you (you're the only one that will see this screen.
The name of your computer plus the Operating System you're using is probably
the most straightforward name.

Copy and paste your __public__ key into the box on the github page.


### OS X users:

    $ cat ~/.ssh/id_rsa.pub

Copy and paste as normal and you're good.


### Linux users:

Same as above, but you'll have to use the right click menu instead of ctrl+c
to copy.


### Windows users:

The Windows shell sucks. Open a text editor, and navigate to your home folder.
It's the folder with your name on it to the left. Make sure to enable viewing
hidden files in your Folder Options. Open the .ssh/id_rsa.pub file, then copy
and paste normally.


### Continuing on

Once you save your __public__ key on github, verify it's working with the
following. (Accept the RSA fingerprint, when prompted)

    $ ssh -T git@github.com
    Hi <user>! You've successfully authenticated, but GitHub does not provide
    shell access.

If you see a message about authentication failure ("Permission denied
(publickey)."), you've got a problem. This will likely happen if you copied
from the Windows shell, for example. You do not need to generate a new
public/private key pair. Verify that you have copied the public key (not the
private key!) and pasted it exactly as shown -- there should be no line breaks
or leading/trailing whitespace.


## Ubuntu 10.10+

Open up a terminal and execute the following.

    $ sudo apt-get update
    $ sudo apt-get python-pip git-core python-opengl python-pyside

Rejoice in the simplicity!


## Mac OS X 10.6

_NB: I've no idea how these instructions will differ in different OS versions,
or whether the libraries we're using are even supported. We should be good
from 10.5-7, but, again, I can't test personally anything except 10.6.
 -- Russ_

There are two different paths to take to install everything you need to
develop PyGears on your Mac. If you plan on doing development in future (in
any language), or already have Xcode installed, I recommend using the Homebrew
method. It's simpler and does not mess with your system install (beyond the
Xcode install, which is Apple's doing anyway).


### Manual

Download and install [the latest Git](http://code.google.com/p/git-osx-installer/downloads/list?can=3)
for your OS version.

Download and install [the latest Qt](http://qt.nokia.com/downloads/qt-for-open-source-cpp-development-on-mac-os-x).
(Yes, it says "C++ development")

Download and install [the latest PySide](http://developer.qt.nokia.com/wiki/PySide_Binaries_MacOSX)
for your python version (Determine your version with ``python --version``).

Execute the following to install pip and PyOpenGL.

    $ sudo easy_install pip
    $ sudo pip install PyOpenGL


### Homebrew

_NB: This requires Xcode with X11 support._

Execute the following to install and update [Homebrew](http://mxcl.github.com/homebrew/),
then install all of the PyGears tools and dependencies.

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"
    $ brew update
    $ brew install python git
    $ pip install --update pip PySide PyOpenGL

Find some time during which you can leave your computer on and unattended.

_NB: Compilation took 90 minutes on my i5 MBP, maxing both cores. YMMV. --Russ_

Execute the following to compile and install Qt.

    $ brew install qt


## Windows 7

Download and install ActiveState's [ActivePython](http://www.activestate.com/activepython/downloads).
Download the 32-bit/x86 .msi for Python 2.7.

_NB: Don't use 64-bit, even on 64-bit machines. We shouldn't hit 4Gb memory
usage in a 2d engine anyway, but, more importantly, ActiveState's PyPM binary
package installer is __not free__ for 64-bit ActivePython._

Download and install Nokia's [Qt libraries](http://qt.nokia.com/downloads/downloads#qt-lib).
Make sure to download the "libraries", not the "sdk", or you'll be downloading
all night. Use the VS 2008 version.

Open a terminal (Start > "cmd.exe") and run the following to install the
other libraries.

    > pypm install PyOpenGL
    > easy_install -U PySide
    > python c:\Python27\Scripts\pyside_postinstall.py -install

Download [Git for Windows](http://code.google.com/p/msysgit/downloads/list?can=3).
Make sure to use the package labelled "Git.*.exe", not "msysGit.*" or
"PortableGit.*".

__Read the next step before installing Git.__

During the install for Git for Windows, you are given several options for
how Git will integrate with your computer. Make sure the following options
are set.

On the _"Adjusting your PATH environment"_ screen, select "Run Git and
included Unix tools from the Windows Command Path."

The warning means
that certain commands will be preferred over Windows built-in commands for
as long as Git is installed, not that they are being replaced. This will only
affect Windows scripts that use commands such as "find.exe"; if you don't use
Windows shell scripts, this won't affect you. More importantly, fixing it if
it turns out to be a problem for you is dead simple; simple remove Git entirely
or remove the appropriate directory from your [PATH environment variable](http://geekswithblogs.net/renso/archive/2009/10/21/how-to-set-the-windows-path-in-windows-7.aspx).

On the _"Configuring the line ending conversions"_ screen, ensure that
"Checkout Windows-style, commit Unix-style line endings" is selected, so that
the POSIX-compliant operating system users don't pull their hair out when you
commit code.
