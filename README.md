python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py


git push <remote> <branch> # send changes
git push origin master

git pull <remote> <branch>
git pull origin master # get changes

git remote -v # info about remote repositories

git checkout -b <new_branch_name>
git checkout -b new_branch_name_1 # checkout branch

git checkout master 

git branch
git branch -D <name_branch> # remove branch
 
git clone 