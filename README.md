# High Level Programming

This is the official repository of the course, and contains the Jupyter Notebooks guiding students through the world of data analysis with python.
The notebooks will be added few hours before each lecture / exercise.

This repo should be forked by each individual student. Exercises should be committed to the student's repo. Before each deadline, a pull request (PR) should be prepared to integrate the changes into this (*upstream*) repository. Those pull requests should point to the appropriate student branch. PRs pointing to the *main* branch will be closed.

## IPython notebooks instructions and tips
Notebooks are extremely powerful tools, you may find useful to discover some of their functionalities on this tutorial [page](https://nbviewer.jupyter.org/github/ipython/ipython/blob/3.x/examples/Notebook/Index.ipynb) or by checking these tips [list](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

## Git Instructions

To begin with, you need to have a GitHub account. If you don't already have one, go to [github](github.com) and sign up. Follow instructions on the screen. Tip: use a reasonable username that resembles your actual name.  

Once you have your github account, fork this repository clicking on the top-right button *Fork*.

### Setting up a local repository

The following instructions need to be followed any time a new local repository is created. If you are working in a location where such repo already exists, what follows doesn't need to be repeated every time.

   * Clone your (forked) repository (i.e. create a local repository cloned from your remote repository)

   `git clone https://github.com/<YourUsername>/HighLevelProgramming_Y1.git`

   where <YourUsername> it your GitHub username. A new directory will appear in your current directory. Get into it:

   `cd HighLevelProgramming_Y1/`

   * Configure your username and email:

   `git config --global user.name "<YourUsername>"`

   `git config --global user.email "<YourEmail>"`

   Your git configuration is stored in `.gitconfig`, a file that you can alwasy edit by hand or via the `git config ..` commands.

   * Define the central HighLevelProgramming repo as the upstream repository (you may need to set the url too):

   `git remote add upstream https://github.com/PhysicsOfData/LaboratoryOfComputationalPhysics_Y3.git`

   `git remote set-url origin https://YOUR_GIT_ACCOUNT@github.com/YOUR_GIT_ACCOUNT/LaboratoryOfComputationalPhysics_Y3.git`

   * Check that the previous commands succeeded:

   `git remote -v`

   * Get (fetch) the updates that have been done on the remote repository:

   `git fetch upstream`

  * The default branch is `main`. You should now create your development branch where you can edit and run the code. Note that you have a branch corresponding to your name in the upstream repository (`upstream/<NameSurname>`): that is the branch you should point the pull request to. In order to set up a proper development cycle, you must create a branch (in the example below called <BranchName>) that *tracks* `upstream/<NameSurname>`:

   `git branch -vv`

   `git checkout -b <BranchName> upstream/<NameSurname>`

   Note: in case you decide to develop your code in a branch that does **not** track `upstream/<NameSurname>`, you'll eventually need to merge your changes into the branch tracking `upstream/<NameSurname>` which is the one to which your pull request will point to.



### Standard development cycle

   * Before starting to edit on the machine that you are using, type the follow command in order to update the directory with the last changes:
  
   `git pull`

   * Before starting with the development you could check whether the upstream repository has been updated with respect to your forked version (that's likely to be the case prior to every lab class). If it had, then merge the chances into your master.

   `git fetch upstream`

   `git checkout main`

   `git merge upstream/main`

   The idea is that your main always reflects `upstream/main`, i.e. it keeps a local copy of the reference code as a starting point for your developments (i.e. solving the assigned problems).
  Note that in order to update your repository on GitHub, you need to push the local version to your remote repository.

   * In the case your pull request has been recently approved, you also need to synch your development branch:

   `git checkout <BranchName>`

   `git merge upstream/<NameSurname>`

   * You may also need to get the updates from the main, i.e. need to merge the main:

   `git merge main`

   * Now develop some code. Image you create a <NewFile>. Add the file to your local repository and stage it for commit (to unstage a file, use `git reset HEAD <NewFile>`)

   `git add <NewFile>`

   * Commits the (tracked) changes you made to the file(s) and commit them local repository on github

   `git commit -m "Add existing file"`

   (what follows after `-m` is a comment to keep track of the reason of the commit)

   * Now propagate (push) your local changes to your remote repository on github (`origin`)

   `git push origin <BranchName>`

   * When appropriate, propagate your development also to the repo you originally forked (upstream). For that you need to go for a pull request, which is done from GitHub. Pay attention to set the correct starting and destination branches.
