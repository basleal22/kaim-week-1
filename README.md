# My Repository

## Setting up the Main Branch

1. Initialize a new Git repository (if not already done):
   ```bash
   git init
   ```

2. Create and switch to the main branch:
   ```bash
   git checkout -b main
   ```

3. Add your files to the repository:
   ```bash
   git add .
   ```

4. Make your first commit:
   ```bash
   git commit -m "Initial commit"
   ```

5. If you're connecting to a remote repository (like GitHub):
   ```bash
   git remote add origin <repository-url>
   git push -u origin main
   ```

Note: If you're converting an existing repository from `master` to `main`, use these commands:

## Virtual Environment Setup

1. Create a virtual environment:
   ```bash
   # Using venv (Python 3)
   python -m venv venv
   
   # Or using virtualenv
   virtualenv venv
   ```

2. Activate the virtual environment:
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Verify activation - you should see (venv) in your terminal:
   ```bash
   # Check Python location
   which python  # macOS/Linux
   where python  # Windows
   ```

4. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Deactivate when done:
   ```bash
   deactivate
   ```

Tips:
- Add `venv/` to your .gitignore file
- Create requirements.txt with:
  ```bash
  pip freeze > requirements.txt
  ```
- Always activate the virtual environment before working on the project
- Install new packages only when the virtual environment is activated

## Creating a New Branch

There are several ways to create a new branch:

1. Create and switch to a new branch in one command:
   ```bash
   git checkout -b new-branch-name
   ```

2. Alternative method:
   ```bash
   # Create a new branch
   git branch new-branch-name
   
   # Switch to the new branch
   git checkout new-branch-name
   ```

3. Push the new branch to remote repository:
   ```bash
   git push -u origin new-branch-name
   ```

Tips:
- Use descriptive names for your branches (e.g., `feature/login`, `bugfix/header`)
- Always create new branches from an updated main branch
- To ensure you're up to date before creating a branch:
  ```bash
  git checkout main
  git pull
  git checkout -b new-branch-name
  ```
- Branch naming rules:
  - Cannot contain spaces (use hyphens or underscores instead)
  - Cannot begin with a hyphen (-) or a dot (.)
  - Cannot end with a period (.)
  - Valid examples: 
    - `git switch new-task-1`
    - `git switch feature_login`
    - `git switch bugfix/task-1`
  - Invalid examples:
    - `git switch -task-1`
    - `git switch .task1`
    - `git switch new task1`
    - `git switch task-1.`
  - Can include numbers, hyphens (in the middle), and underscores
  - Should not include special characters like ?, !, @, #, etc.
  - The -m flag is a command option, not part of the branch name

## Switching Between Branches

1. Switch to any branch:
   ```bash
   git checkout branch-name
   ```
   or using the newer command:
   ```bash
   git switch branch-name
   ```
   For example:
   ```bash
   git checkout feature/login
   # or
   git switch feature/login
   ```

2. Before switching branches, it's good practice to:
   - Save and commit your current changes:
     ```bash
     git add .
     git commit -m "Your commit message"
     ```
   - Or stash your changes if you're not ready to commit:
     ```bash
     git stash
     ```

3. To see all branches and identify your current branch:
   ```bash
   git branch
   ```
   The current branch will be marked with an asterisk (*)

## Viewing Branch Contents and Status

1. Check branch status (modified files, staged changes):
   ```bash
   git status
   ```

2. View commit history of current branch:
   ```bash
   # Simple log
   git log
   
   # Compact single-line format
   git log --oneline
   
   # With branch graph
   git log --graph --oneline --all
   ```

3. See changes in working directory:
   ```bash
   # Show all changes
   git diff
   
   # Show staged changes
   git diff --staged
   ```

4. List all files in the branch:
   ```bash
   # List tracked files
   git ls-files
   
   # List all files including untracked
   ls  # On Unix/macOS
   dir # On Windows
   ```

5. View specific file content:
   ```bash
   # Current version
   cat filename.txt  # Unix/macOS
   type filename.txt # Windows
   
   # Git's version
   git show HEAD:filename.txt
   ```

Tips:
- Use `git status` frequently to track your changes
- `git log` shows commits from newest to oldest
- Press 'q' to exit from git log view
- Add `--pretty=format:"%h %an %ar - %s"` to git log for custom formatting

## Understanding Branch File Behavior

1. Files Following Branch Switches:
   - Files remain visible in your workspace when switching branches if:
     - They are identical between branches
     - They haven't been committed to either branch
     - They have uncommitted changes

2. To ensure clean branch switching:
   ```bash
   # Commit your changes before switching
   git add .
   git commit -m "Your message"
   git switch other-branch
   
   # Or stash changes temporarily
   git stash
   git switch other-branch
   git stash pop  # to retrieve changes later
   ```

3. Check if files are tracked:
   ```bash
   # See tracked and untracked files
   git status
   
   # See only tracked files
   git ls-files
   ```

Tips:
- Always commit or stash changes before switching branches
- Use `git status` to see which files are tracked/untracked
- Untracked files will remain visible across all branches until:
  - They are committed to a specific branch
  - They are added to .gitignore
  - They are manually deleted
- Use `git clean -n` to see which untracked files would be removed
- Use `git clean -f` to remove untracked files (use with caution!)

## Renaming Branches

1. To rename your current branch:
   ```bash
   git branch -m new-name
   ```

2. To rename a branch while on a different branch:
   ```bash
   git branch -m old-name new-name
   ```

3. If you've already pushed the branch to remote, you'll need to:
   ```bash
   # Delete the old remote branch
   git push origin --delete old-name
   
   # Push the renamed branch
   git push origin -u new-name
   ```

Tips:
- Be careful when renaming branches that others might be using
- Always inform your team when renaming shared branches
- Consider creating a new branch instead of renaming if others are actively using it
