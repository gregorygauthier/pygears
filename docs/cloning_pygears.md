# Cloning PyGears

If you haven't already, you'll want to [install Python](cloning_pygears.md)
and [set up the development environment](development.md).

To actually write code for PyGears, you first need to "Fork" the PyGears
respository on Github. Near the top left of the
[main repository's page](http://github.com/vandycs/pygears), find and
press the "Fork" button. Github will redirect to a clone of the main
repository, at github.com/[yourusername]/pygears. On this new page,
copy the "SSH"/"Read+Write" access URI. Open a terminal, navigate
to wherever you want the PyGears root directory, and type the following.

```bash
~: russ$ cd dev
dev: russ$ git clone [thegithuburi]
Cloning into pygears...
remote: Counting objects: 42, done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 42 (delta 11), reused 36 (delta 5)
Receiving objects: 100% (42/42), 10.70 KiB, done.
Resolving deltas: 100% (11/11), done.
~: russ$ ls -sal
...
   0 drwxr-xr-x  10 russ  staff     340 Sep 30 09:34 pygears
...
```

You now have a full copy of the repository and its history on your local
computer.

## Testing the set up

Now that we have the code and all of the libraries, we can run a simple
script to test whether everything is working correctly.

```bash
pygears: russ$ python examples/stack_test.py
```

The result should be a large, blue rectangle centered in a 1024x768 black
window. Close the window to exit the script.
