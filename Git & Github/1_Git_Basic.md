# Git

## Git

What is Git?
* a program that manages codes (especially version control)
* 공부 = 나의 문제 * 상상력 > 공부의 어려움 ? 구원 : 지옥


## Download & Install

[git-scm] https://git-scm.com/

[source tree] https://www.sourcetreeapp.com/

[visual studio code] https://code.visualstudio.com/

## Setting Environment in Sourcetree

1. create a folder in file explorer
2. File - > New Clone -> Create -> Choose a directory

## 개념

### Master

마지막 버전이 무엇인지를 가르키는것

### Head

나의 working directory 가 어느 버전에서 유래했는지를 의미함

(working directory 를 head 가 가르키는 버전이 만들어진 시점으로 옮김)

### Checkout (시간여행)

헤드를 옮긴다는 의미

(시간여행을 끝낸 후 마스터를 더블클릭 = checkout 한다는 의미)

Head != Master => called detetched head

**마스터로 체크아웃을 안할 경우 (head를 바꾼후 마스터로 되돌리지 않고 그상태에서 working directory에서 수정을 할 경우) -> 현재 head가 새로운 버전의 head 가 됨**


### Reset (삭제)

마스터의 위치를 바꿈

## Command Line

### git init
initializing a git repository

### git status
* show untracked / modified / uncommitted files

### git add
* untracked file -> stage area
* adding untracted file to stage area
* git add index.html

### git commit
* tracked file & uncommitted file -> repository
* commit files in the stage area to the repository
* commit changes
* git commit -m "work 1"
* -m indicates that the git message will be written together

### git diff
* shows changes by comparing with the last committed file

### git log
* show log
* git log --oneline (show online summary)
* git log --oneline --all (shows everything including master when in detecthed mode)

### git checkout commit_ID
* move head
* change working copy

### git reset commit_ID
* change branches that the head points to (**헤드가 가르키는 브랜치**)
* change the position of master
* can reverse by using commit_ID

### git reflog
* effect (git version that the head points to after the operation) : cause (operation)

### making files private
* make a directory called ".gitignore"
* list out all the files that needs to be private inside .gitignroe


## Branch

### git branch
* list out all the branches

### git branch branch_name
* creating a new branch called branch_name	
    ![branch](./git_branch.png)


### git checkout branch_name || git checkout master
* switch branch

### git log --all --oneline --graph
* shows branches in graph

### git branch -d branch_name
* delete branch

### git branch -D branch_name
* force to delete branch

## git merge exp
* 마스터로 exp 병합
* git merge exp
* creating a node that points to both of the branch as parents & indicate the new node as a master
    ![merge conflict](./git_merge.png)

### merge conflict

#### TWO WAY MERGE
master | new_branch | expectation | result  
-------|------------|-------|--
-|-|-|-
m1|-|?|m1
-|e1|?|e1
m2|e2|?|?
 | | 1/4|3/4

![merge conflict](./git_merge_conflict.png)

* accept current change = keep master's work
* accept incoming change = accept exp's work
![merge conflict](./git_merge_conflict2.png)


#### THREE WAY MERGE
master |base| new_branch | 2 way merge | 3 way merge  
-------|--|------------|-------|--
-|-|-|-|-
m1|-|-|?|m1
-|-|e1|?|e1
m2|-|e2|?|?
 -|-|-| 1/4|3/4

 1. compare master & base
 2. compare base & new_branch
 3. if only one of the comparison has a change -> apply the change
4. if two changes, don't know which one will be chosen

* git merge --abort : 병합 취소