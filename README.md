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

1. Check Python installation on Windows:
   ```bash
   python --version
   # or
   py --version
   ```

2. Create a virtual environment:
   ```bash
   # Using Python's venv
   python -m venv venv
   # or
   py -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # On Windows Command Prompt
   venv\Scripts\activate.bat
   
   # On Windows PowerShell
   venv\Scripts\Activate.ps1
   ```

4. If you get a PowerShell execution policy error:
   ```powershell
   # Run PowerShell as Administrator and execute:
   Set-ExecutionPolicy RemoteSigned
   # Select 'Y' when prompted
   ```

5. Verify activation:
   ```bash
   # You should see (venv) at the start of your prompt
   # Check Python location
   where python
   # Should point to your venv directory
   ```

6. Install packages:
   ```bash
   pip install package_name
   # or from requirements file
   pip install -r requirements.txt
   ```

7. Deactivate when done:
   ```bash
   deactivate
   ```

Tips:
- Add these to .gitignore:
  ```text
  venv/
  __pycache__/
  *.pyc
  ```
- Create requirements.txt:
  ```bash
  pip freeze > requirements.txt
  ```
- Common issues:
  - If 'python' isn't recognized, try 'py' instead
  - Make sure to run activate.bat for Command Prompt or Activate.ps1 for PowerShell
  - Use backslashes (\) not forward slashes (/) on Windows paths

## Managing Virtual Environment Files

1. Create or update your .gitignore file:
   ```text:.gitignore
   # Virtual Environment
   venv/
   env/
   .env/
   .venv/
   ENV/
   
   # Python
   __pycache__/
   *.py[cod]
   *$py.class
   *.so
   .Python
   
   # IDE settings
   .vscode/
   .idea/
   *.swp
   
   # Environment variables
   .env
   ```

2. What to push instead:
   ```bash
   # Generate requirements file
   pip freeze > requirements.txt
   
   # Push only the requirements.txt file
   git add requirements.txt
   git commit -m "Update dependencies"
   ```

3. For other developers to recreate the environment:
   ```bash
   # Create and activate their own venv first
   python -m venv venv
   venv\Scripts\activate  # Windows
   
   # Install from requirements
   pip install -r requirements.txt
   ```

Tips:
- Never commit virtual environment folders
- Always keep requirements.txt updated
- Each developer should create their own virtual environment locally
- Make sure requirements.txt is in version control
- Consider using different requirement files for dev and production:
  - requirements.txt (production)
  - requirements-dev.txt (development dependencies)

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

## Understanding Git Changes Status

1. "Changes to be committed" (staged changes):
   - These are files that have been added to the staging area using:
     ```bash
     git add filename
     # or
     git add .  # for all files
     ```
   - These changes are ready to be committed
   - They appear in green when you run `git status`

2. Different states of files:
   ```bash
   git status
   ```
   Shows:
   - 🟢 Green: Changes to be committed (staged)
   - 🔴 Red: Changes not staged for commit
   - 🔴 Red: Untracked files

3. Managing staged changes:
   ```bash
   # Remove file from staging area (unstage)
   git restore --staged filename
   
   # Commit staged changes
   git commit -m "Your message"
   
   # View staged changes
   git diff --staged
   ```

Tips:
- Think of staging as a preparation area for your next commit
- You can stage multiple files and commit them together
- Use `git add -p` to stage specific parts of a file
- To unstage all changes: `git restore --staged .`
- Always add a meaningful commit message describing your changes

## Committing All Changes at Once

1. Stage and commit all changes in one go:
   ```bash
   # Method 1: Stage all + commit
   git add .
   git commit -m "Your message"
   
   # Method 2: Stage and commit in one command
   # (Only works for tracked files)
   git commit -am "Your message"
   ```

2. What gets included:
   - `git add .` stages:
     - Modified files
     - New files
     - Deleted files
     - Files in current directory and subdirectories

3. Check what will be committed:
   ```bash
   # Before staging
   git status
   
   # After staging, before commit
   git diff --staged
   ```

Tips:
- Use `git status` before committing to verify what will be included
- Be careful with `git add .` as it stages ALL changes
- `git commit -am` only works for already tracked files (won't include new files)
- Always write clear commit messages explaining what changes were made
- To exclude specific files, add them to .gitignore before using `git add .`

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

## Activating Virtual Environment on Windows

1. Open Command Prompt or PowerShell:
   ```bash
   # For Command Prompt
   venv\Scripts\activate.bat
   
   # For PowerShell
   venv\Scripts\Activate.ps1
   ```

2. Verify activation:
   ```bash
   # You should see (venv) at the start of your prompt like this:
   # (venv) C:\Your\Project\Path>
   
   # Verify Python location
   where python
   # Should show path inside your venv folder
   ```

3. Common activation issues on Windows:
   - If using PowerShell and getting permission errors:
     ```powershell
     # Run PowerShell as Administrator and execute:
     Set-ExecutionPolicy RemoteSigned
     # Type 'Y' when prompted
     ```
   - If 'python' isn't recognized:
     ```bash
     # Try using 'py' instead
     py -m venv venv
     ```
   - If activation fails, ensure you're in the correct directory:
     ```bash
     # Check current directory
     cd
     # Navigate to project directory if needed
     cd path\to\your\project
     ```

4. To deactivate when done:
   ```bash
   deactivate
   ```

Tips:
- Always check for (venv) in your prompt to confirm activation
- Use backslashes (\) not forward slashes (/) in Windows paths
- Run scripts from the project root directory
- If using VS Code, select the correct Python interpreter:
  1. Press Ctrl + Shift + P
  2. Type "Python: Select Interpreter"
  3. Choose the one in your venv folder

## Troubleshooting Virtual Environment Activation

1. Check your current directory:
   ```bash
   # First, check where you are
   cd
   # Make sure you're in the directory that contains the 'venv' folder
   dir
   # You should see 'venv' listed
   ```

2. Try these alternative activation methods:
   ```bash
   # Method 1: Use full path
   .\venv\Scripts\activate
   
   # Method 2: Use activate without .bat
   venv\Scripts\activate
   
   # Method 3: Use forward slashes
   ./venv/Scripts/activate
   ```

3. If none of those work:
   ```bash
   # Check if the activate file exists
   dir venv\Scripts
   # You should see 'activate', 'activate.bat', and 'Activate.ps1'
   ```

4. Common fixes:
   - If the venv folder is empty or missing activate scripts:
     ```bash
     # Remove the old venv
     rmdir /s /q venv
     
     # Create a new one
     python -m venv venv
     ```
   
   - If using PowerShell, try:
     ```powershell
     # Enable script execution
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     
     # Then activate using
     .\venv\Scripts\Activate.ps1
     ```

Tips:
- Make sure you created the venv using `python -m venv venv`
- Check if Python is in your PATH (try `python --version`)
- Try using Command Prompt instead of PowerShell
- Look for error messages when activating
- Make sure you didn't accidentally create venv inside another folder

## Setting Up Jupyter Notebook

1. Install Jupyter (with venv activated):
   ```bash
   # Install jupyter
   pip install jupyter notebook
   
   # Install common data science packages
   pip install numpy pandas matplotlib seaborn
   
   # Save to requirements
   pip freeze > requirements.txt
   ```

2. Launch Jupyter Notebook:
   ```bash
   # Start the notebook server
   jupyter notebook
   ```
   This will:
   - Open your default browser
   - Show Jupyter's file navigator
   - Default to http://localhost:8888

3. Create a new notebook:
   - Click "New" → "Python 3 (ipykernel)"
   - Or navigate to notebooks/ directory first
   - Save notebook with .ipynb extension

4. Working with notebooks:
   ```python
   # Test your setup with:
   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   import seaborn as sns
   
   print("Setup complete!")
   ```

5. Installing packages from within Jupyter:
   ```python
   # Method 1: Using system command
   !pip install package_name
   
   # Method 2: For multiple packages
   !pip install package1 package2 package3
   
   # Example:
   !pip install scikit-learn
   ```

6. After installing new packages:
   ```python
   # Restart the kernel to use new packages
   # Click: Kernel → Restart Kernel
   
   # Or import your new package
   import sklearn
   ```

Tips:
- Keep notebooks in the `notebooks/` directory
- Use `Ctrl + S` to save frequently
- Use `Ctrl + Enter` to run current cell
- Use `Shift + Enter` to run and move to next cell
- Install additional packages as needed with `pip install`
- Install packages as you need them using `!pip install`
- Remember to update requirements.txt after adding packages:
  ```python
  !pip freeze > requirements.txt
  ```
- Some packages might need kernel restart to work properly
- Use `!pip list` to see installed packages

## Understanding pip freeze and Requirements

1. What is pip freeze:
   ```bash
   # pip freeze shows all installed packages and their versions
   pip freeze
   # Output example:
   # numpy==1.21.0
   # pandas==1.3.0
   # jupyter==1.0.0
   ```

2. Using pip freeze:
   ```bash
   # Save all installed packages to requirements.txt
   pip freeze > requirements.txt
   
   # View current requirements
   cat requirements.txt  # on Unix/macOS
   type requirements.txt # on Windows
   ```

3. Why use pip freeze:
   - Captures exact versions of all packages
   - Includes both direct and dependency packages
   - Ensures reproducible environments
   - Helps team members use identical package versions

4. Managing requirements:
   ```bash
   # Install specific versions
   pip install numpy==1.21.0
   
   # Install latest version
   pip install numpy
   
   # Install all requirements
   pip install -r requirements.txt
   ```

Tips:
- Run pip freeze after installing new packages
- Keep requirements.txt in version control
- Don't manually edit requirements.txt
- Use `pip list` to see installed packages in a readable format
- Consider using separate requirements files:
  ```bash
  # Development requirements
  pip freeze > requirements-dev.txt
  
  # Production requirements (minimal needed packages)
  pip freeze > requirements.txt
  ```

## Managing requirements.txt Changes

1. When to update requirements.txt:
   ```bash
   # After installing new packages
   pip install new-package
   pip freeze > requirements.txt
   
   # After upgrading packages
   pip install --upgrade package-name
   pip freeze > requirements.txt
   ```

2. When to commit requirements.txt:
   ```bash
   # After updating requirements.txt
   git add requirements.txt
   git commit -m "Update requirements: Add new-package"
   git push
   ```

3. Best practices:
   - Commit requirements.txt changes immediately
   - Use descriptive commit messages mentioning added/updated packages
   - Test your code with the new requirements before pushing
   - Inform team members about significant package changes

4. For team members:
   ```bash
   # Before starting work, pull latest changes
   git pull
   
   # Update their virtual environment
   pip install -r requirements.txt
   ```

Tips:
- Always push requirements.txt changes to keep team in sync
- Include what packages were added/updated in commit message
- Consider creating a changelog for major dependency updates
- Test your application after updating packages
- Use `pip list --outdated` to check for package updates

## Managing Data Files

1. Update .gitignore for data:
   ```text:.gitignore
   # Data files
   data/
   *.csv
   *.xlsx
   *.xls
   *.db
   *.sqlite
   *.json
   *.xml
   *.parquet
   *.feather
   *.pkl
   *.h5
   
   # Large files
   *.zip
   *.tar
   *.gz
   *.7z
   
   # Sensitive data
   *credentials*
   *secret*
   *.env
   ```

2. Data management best practices:
   - Keep small, sample data in version control
   - Store large datasets elsewhere:
     ```bash
     # Create a data directory structure
     data/
     ├── raw/          # Original, immutable data
     ├── processed/    # Cleaned, transformed data
     ├── interim/      # Intermediate data
     └── external/     # Data from external sources
     ```
   - Include a data/README.md explaining:
     - Data sources
     - How to obtain the data
     - Data structure
     - Update frequency

3. Sample data handling:
   ```bash
   # Create sample data for testing
   data/
   ├── sample/
   │   ├── test_data.csv    # Small subset for testing
   │   └── README.md        # Document sample data creation
   ```

Tips:
- Never commit sensitive or private data
- Document data sources and preprocessing steps
- Consider using Git LFS for large files if needed
- Keep sample data small (< 100KB)
- Share data download instructions in README
- Use relative paths in your code

## Accessing Data with .gitignore

1. Data storage options:
   ```bash
   # Local data structure
   project/
   ├── data/                  # Gitignored, but exists locally
   │   ├── raw/              # Original data
   │   ├── processed/        # Cleaned data
   │   └── sample/           # Small sample data (in git)
   ├── src/                  # Code (in git)
   └── README.md            # Instructions (in git)
   ```

2. Share data access instructions in README:
   ```markdown
   ## Data Setup
   1. Download data files from [shared location]
   2. Place files in the `data/raw/` directory
   3. Run preprocessing scripts:
      ```bash
      python src/data/preprocess.py
      ```
   ```

3. Common data sharing methods:
   - Cloud storage (provide access instructions):
     ```markdown
     1. Download from Google Drive: [link]
     2. Download from S3: `aws s3 cp s3://bucket/data ./data/`
     3. Download from Azure: `az storage blob download...`
     ```
   - Data download scripts:
     ```python
     # src/data/download.py
     import requests
     
     def download_data():
         url = "https://your-data-source.com/data.csv"
         response = requests.get(url)
         with open("data/raw/data.csv", "wb") as f:
             f.write(response.content)
     ```

4. Sample data for testing:
   ```bash
   # Keep small sample in git
   !data/sample/           # Exception in .gitignore
   !data/sample/*.csv     # Allow sample CSV files
   
   # Create sample from full dataset
   python src/data/create_sample.py
   ```

Tips:
- Document data sources and access methods
- Provide sample data for quick testing
- Use relative paths in code:
  ```python
  from pathlib import Path
  
  # Good - relative path
  data_dir = Path("data/raw")
  
  # Bad - absolute path
  data_dir = "C:/Users/name/project/data"
  ```
- Consider automated data download scripts
- Include data validation checks
- Keep sensitive data credentials in .env file

## Working with CSV Files

1. Local CSV file structure:
   ```bash
   project/
   ├── data/
   │   ├── raw/
   │   │   └── dataset.csv     # Original CSV (gitignored)
   │   ├── processed/
   │   │   └── cleaned.csv     # Processed CSV (gitignored)
   │   └── sample/
   │       └── sample.csv      # Small sample (in git)
   └── src/
       └── data/
           ├── load_data.py    # Data loading functions
           └── process_data.py # Data processing functions
   ```

2. Loading CSV files in Python:
   ```python
   import pandas as pd
   from pathlib import Path
   
   # Load data using relative paths
   data_dir = Path("data/raw")
   df = pd.read_csv(data_dir / "dataset.csv")
   
   # Save processed data
   output_dir = Path("data/processed")
   output_dir.mkdir(exist_ok=True)  # Create directory if it doesn't exist
   df.to_csv(output_dir / "cleaned.csv", index=False)
   ```

3. Creating sample data:
   ```python
   # Create a small sample for git
   sample = df.head(100)  # First 100 rows
   # or
   sample = df.sample(n=100, random_state=42)  # Random 100 rows
   
   sample_dir = Path("data/sample")
   sample_dir.mkdir(exist_ok=True)
   sample.to_csv(sample_dir / "sample.csv", index=False)
   ```

4. Data loading instructions in README:
   ```markdown
   ## Data Setup
   1. Download dataset.csv from [source]
   2. Place dataset.csv in the data/raw directory
   3. Run data processing:
      ```bash
      python src/data/process_data.py
      ```
   4. For quick testing, use sample data in data/sample/sample.csv
   ```

Tips:
- Keep original CSV files in data/raw/
- Use pandas for CSV operations
- Always include column descriptions in data/README.md
- Consider data validation:
  ```python
  def validate_csv(file_path):
      df = pd.read_csv(file_path)
      assert all(df.columns == ['expected', 'columns']), "Missing columns"
      assert len(df) > 0, "Empty dataset"
      return df
  ```
- Use encoding parameter if needed:
  ```python
  df = pd.read_csv("data.csv", encoding='utf-8')
  # or for Excel-exported CSVs
  df = pd.read_csv("data.csv", encoding='latin1')
  ```

## Closing Jupyter Notebook

1. Save your work:
   - Click the save icon (💾) or press `Ctrl + S`
   - Or use File → Save and Checkpoint

2. Close Jupyter Notebook:
   - Method 1: Browser
     ```text
     1. Save all notebooks
     2. Close browser tabs
     3. Go to terminal where Jupyter is running
     4. Press Ctrl + C twice
     5. Type 'y' when prompted
     ```

   - Method 2: Terminal command
     ```bash
     # If Ctrl+C doesn't work, use:
     jupyter notebook stop
     ```

3. Verify shutdown:
   - Terminal prompt should return
   - Browser tabs should show "No Connection to Kernel"
   - Port 8888 should be released

Tips:
- Always save your work before closing
- Make sure all notebooks are properly closed
- If browser keeps reconnecting, check for other notebook instances
- Use `jupyter notebook list` to see running servers
- Kill specific port if needed:
  ```bash
  # Windows
  netstat -ano | findstr :8888
  taskkill /PID <PID> /F
  ```
