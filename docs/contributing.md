# Contributing to PyGears

When you've made a working change (for example, perhaps you've made a bug fix),
you should commit your code with a short, relevant commit message.

```bash
pygears: russ$ git status
# On branch master
# Changed but not updated:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#	modified:   gears/core.py
#
no changes added to commit (use "git add" and/or "git commit -a")
pygears: russ$ git add gears/core.py
pygears: russ$ git commit -m "Altered the redraw timer to improve performance on Windows"
[master 9d2e1a8] Altered the redraw timer to improve performance on Windows
 1 files changed, 4 insertions(+), 2 deletions(-)
```

## Pushing your code

At this point, your change has been recorded and, at any point in the future,
you will be able to come back to this point in your history, or undo this
specific change if it turns out to cause new problems. However, you want
to share your bug fix with your fellow PyGears coders. To do so, you must 
"push" your changes to your github repository.

```bash
pygears: russ$ git status
# On branch master
# Your branch is ahead of 'origin/master' by 1 commit.
#
nothing to commit (working directory clean)
pygears: russ$ git push
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (2/2), 255 bytes, done.
Total 2 (delta 1), reused 0 (delta 0)
To git@github.com:russ-/pygears.git
   0037dd3..856d7c0  master -> master
```

## Pulling others' code

Now, the only remaining step is occasionally updating your repository
to keep pace with the code that everyone else is writing. To do so,
you need to add the main repository as a second "remote", from which
you can pull new commits and branches. Note that, when pulling from
the main repository, you have to explicitly tell git which remote
(here, "vandycs") and branch (here, "master") to pull. Git will then
attempt to merge the remote branch with your current local branch.

```bash
pygears: russ$ git remote add vandycs http://github.com/vandycs/pygears.git
pygears: russ$ git remote show vandycs
dh-10-20-65-242:pygears russ$ git pull vandycs master
From http://github.com/vandycs/pygears
 * branch            master     -> FETCH_HEAD
Already up-to-date.
```
