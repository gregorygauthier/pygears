# Development Setup

Setting up to develop PyGears requires a few steps. The exact steps are
largely OS dependent; see instructions for Ubuntu 10.10+, OS X 10.6,
and Windows 7 below.

## Everyone

[Install Git](http://help.github.com/set-up-git-redirect)!

Windows users: during installation, make sure
to select "Run Git and included Unix tools from the Windows Command Path" on the
_"Adjusting your PATH environment"_ screen, and "Checkout Windows-style, commit
Unix-style line endings" on the _"Configuring the line ending conversions"_ screen.

Linux users: use your packaging tool (i.e. synaptic/apt on Ubuntu,
yum on RHEL/Fedora, etc.).

Optionally, follow the instructions on the Github page to set up SSH keys
for Github. This will allow you to interact with your remote repository without
constantly re-entering your password.


## Ubuntu 10.10+

Open up a terminal and execute the following.

    $ sudo apt-get update
    $ sudo apt-get install python-pip git-core python-opengl python-pyside

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

Download and install Nokia's [PySide Qt bindings for Python](http://developer.qt.nokia.com/wiki/PySide_Binaries_Windows).
Make sure to select the 32-bit version for Python 2.7.

Open a terminal (Start > "cmd.exe") and run the following to install the
last library.

    > pypm install PyOpenGL
