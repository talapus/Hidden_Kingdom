Hey Jacob! I'd like to collaborate with you on your game if that's OK? Schoolwork needs to come first, but I'd love to write some code with you when time allows. 

I put it here to give you a taste of what it's like to be on a distributed development team. 

In addition to improving your game and python skills, using this repository will teach you the tools you'll need to work on teams with other developers - specifically, the git tools and git repositories. 

For now, lets focus on basic commands. 

First - to get the game repository on your hard disk (so you can continue to make changes), navigate into the directory where you keep your repositories and paste in this command exactly as it's written. Let me know if you get any errors:

```git clone https://github.com/talapus/Hidden_Kingdom.git```

I chose the name 'Hidden Kingdom' because it came to mind while I was making your repo. The game is yours though, name it whatever you want and I'll change the repository to match. 

Also, this code is yours. I'm just collaborating with you. I'll give you the repository (or show you how to set up your own) any time you want. 

Ok, here's the four git commands you'll need. If you don't understand how or why these are used, ask anytime. 

1. To check the status of your repository, use git status. Try this now in the Hidden Kingdoms directory. If you've changed nothing you should see these results displayed:

```git status```

```
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

2. if you create a new file or make changes to an existing file, you need to 'add' the file to tell git that there is new stuff in there. I added this README file like this:

```
git add README.md 
```

3. Once you've told git which files need to be added, you need to stage a commit. Always add a commit message with the -m switch:

```
git commit -m 'Added a README'
```

4. Not always, but often multiple file changes will be staged in one commit if those changes are related. 

5. Push your new stuff up to the remote repository with this:

```git push```

After pushing, I'll be able to see and download the new code in the repo. Theres more around this (and feel free to ask questions if I'm not going fast enough in any area), but lets start with these commands. 

Also, take a few minutes to look around the web-based interface for the repository. See '4 Commits'? Click on that. Those are the commits where I pushed up your game file and the readme. 