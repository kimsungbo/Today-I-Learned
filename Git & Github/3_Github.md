# Github

## git address
* address that I can download git open source 

## Communication Method
* http
* ssh

## Download Open Source
* git clone https://github.com/git/git.git .
* "." represents current directory

## Create New Repository
* git init
* git add README.md
* git commit -m "first commit"
* git remote add origin git_address 
* git push -u origin master

## Push Existing Repository
* git remote add origin git_address
* git push -u origin master

### verification (first time only)
* ssh-keygen
* cat id_rsa.pub to get password
* github -> settings -> SSH and GPG keys -> new ssh key

### git remote add origin git_address
* tell local repo about remote repo's address and its nickname is called "origin"
* "add" indicates that one local repo can have multiple remote repos

### git push --set-upstream origin master or git push -u origin master
* process of matching git's branch with local repo's branch
* local master branch = git master branch

### git push
* ask to push files to origin as a master

## Clone

1. ssh-keygen
2. save the password on github website
3. git clone git_address .

* clone = init + add + paring

## Pull

* git pull
* pull = fetch + merge
* download and then local & remote repo paring

### use git pull to resolve push conflict

* 다른사람이 수정한걸 가져와서 merge 하고 새롭게 만들어진걸 push 하여라

    ![push conflict -> use pull](./git_push_conflict.png)

    ![push conflict -> use pull](./git_push_conflict_pull.png)