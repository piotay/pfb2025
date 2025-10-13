# Unix 2 Problem Set

## Git/GitHub setup.  You may have completed this while following along with lecture. You don't need to do this again.

1. Go to GitHub and create a free accout.

2. You may have completed this while following along with lecture. You don't need to do this again. Look back at the notes and create your SSH key and add it to your github account.
   [Notes for key creation](https://github.com/prog4biol/pfb2025/blob/master/unix.md#generating-a-new-ssh-key)
 
 #### Skip if you already completed this: Create Key and passphrase
```
$ ssh-keygen -t ed25519 -C "your_email@example.com"
```

```
> Enter a file in which to save the key (/Users/YOU/.ssh/id_ALGORITHM: [Press enter]
```

```
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```

#### Skip if you already completed this:  Adding your SSH key to the ssh-agent
```
$ eval "$(ssh-agent -s)"
> Agent pid 59566
```

#### Skip if you already completed this:  Add Key info to ssh configuration file with a text editor
```
$ vi ~/.ssh/config
```
##### Skip if you already completed this:  Add
```
Host *
  IdentityFile ~/.ssh/id_ed25519
```

#### Skip if you already completed this:  Add to your GitHub.com account: Settings --> SSH and GPC Keys --> Click "New SSH Key"
Paste the contents of your public "Lock" to GitHub with a title
```
cat ~/.ssh/id_ed25519.pub
```

3. You may have completed this while following along with lecture. You don't need to do this again.
   Create your first repository for your problem set code. [Notes for repository creation](https://github.com/prog4biol/pfb2025/blob/master/unix.md#git-for-beginners).
   **NOTE: Don't create a repository inside of another repostitory.**
   - Move to your home directory (`cd ~`), then create a new Repository by clicking "New" on the repository github page. https://github.com/YOURUSERNAME/repositories 
   - Create a local (your machine) directory with `mkdir PFB_problemsets`.  
   - move into the new directory with `cd PFB_problemsets` 
   - start setting up your repository with the code produced by github. Start with `git init`. 
   - **Don't `git init` in your home directory. Make a new directory mentioned above (PFB_problemsets), change directory into PFB_problemsets, then `git init`** 
   - Now link it to your remote repository with `git remote add` using the ssh URL.
   
## Once Git/Github set up is complete, do these:

1. Move any files you created for Unix_01 Problem set that are not already in your local problemset git repository to your local repository (PFB_problemsets). You can use the `mv` command.

2. **Push** all the new files in your local repository to your remote repository
   - `git status` to see all the files you need to add
   - `git add <filename>`  or  `git add <filename1> <filename2> <filename3> ...`  
   - `git commit -m 'adding unix01 problem set files'`
   - `git push`
   - Visit the your GitHub repository website (on github.com) and see the files from your local repository that you just pushed up to your remote repository.



3. Create a directory call `files` in your PFB_problemsets directory. 

4. Move the file you renamed (in Unix01 problem set) from `sequences.nt.fa` to `cancer_genes.fasta` to your `files` directory

5. ADD/COMMIT/PUSH `cancer_genes.fasta` to your remote repository
  - `git add files/cancer_genes.fasta`
  - `git commit -m 'adding cancer_genes.fasta'`
  - `git push`
  - Visit the your GitHub repository website (on github.com) and see the file from your local repository that you just pushed up to your remote repository.

6. Using your **vi** text editor create a fasta file and name it `mysequences.txt`. Make sure it ends up in your problem sets files directory.

This is fasta file format:
```
>seqName description
ATGGCGTCTTGGCCTTAAAAGCTC
GGCGTCTTGGCCTTAAAAGCTCAT
ATTCTTGGCCTTAAATTGGCCTTG
```
  - add 10 lines of sequence
  - delete a line
  - insert a new line at line 4
  - Copy line 5
  - Paste this line above line 2
  - set to view line numbers
  - Cut line 3 and paste below line 6
  - Go to line 4
  - delete a line
  - undo your last delete
  - search for `CTT`
  - find next occurance of `CTT`
  - Save and exit


7. ADD/COMMIT/PUSH `mysequences.txt` to your remote.


8. Create a directory called `fastas` inside your problem_sets directory.     (Hint: use mkdir)
9. Copy the fasta file that you renamed to `cancer_genes.fasta` to the fasta directory.
10. Verify that the file is within the fasta directory.  
11. Delete the the original file that you used for copying.  
12. Sync your remote repo with your local repo. Make sure to add each file you changed or use `git add <filename>`. Don't forget to commit and push.
13. Practice with `git rm`
  - Create a file named `oops` and add a few characters of content.
  - Save and Exit. 
  - Add/Commit/Push this file 
  - `git rm oops` 
  - `git commit -m 'removing oops'`
  - `git push`
14. Practice with `rm`. Can you spot the little difference from `git rm`
  - Create a file named `oops2`. add some content. save and exit
  - Add/Commit/Push this file
  - `rm oops2`
  - `git add oops2`
  - `git commit -m 'removing oops2'`
  - `git push`
15. Imagine this: You created a file, `git add` it, but then realize you don't want to commit it. What do you do? [from google search](https://stackoverflow.com/questions/348170/how-do-i-undo-git-add-before-commit)
  - Create a file named `never`. 
  - `git add never`
  - `git reset never`
16. Read the man page for `rm` and `cp` to find out how to remove and copy a directory.
17. Print out your history and redirect it to a file called `unixBasics.history.txt`
18. Open your history file with your text editor and delete any lines you do not want to keep. See this [google search](https://www.google.com/search?rlz=1C5CHFA_enUS596US596&q=vi+delete+entire+line&oq=vi+delete+entire+line&gs_l=psy-ab.3..0j0i5i30k1.28765.29854.0.30351.7.6.0.0.0.0.186.526.0j3.3.0....0...1.1.64.psy-ab..5.2.362...0i13k1j0i7i5i30k1.0.Ub2zfH_lp_o) for info on deleting entire lines in vi.
19. Make sure all your files are synced with your remote repository. (`git status`)
20. Here is a way to ENSURE that you don't mistakenly commit a large file. Get help from TA if you do not know where your .git directory is
```
cd ~/PFB_problemsets/.git/hooks/
curl -O https://raw.githubusercontent.com/prog4biol/pfb2025/master/setup/pre-commit
```
