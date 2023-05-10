Danish-English Sentence Pair Dataset Cleaner
This guide will walk you through the process of pulling a GitHub repository to Visual Studio Code (VS Code) using Git commands.

Prerequisites
Git: If you haven't already, download and install Git on your computer. You can find the official Git installer at https://git-scm.com/.
Steps
Clone the repository: Open a terminal or command prompt and navigate to the directory where you want to clone the repository. Use the following command to clone the repository:

bash
Copy code
git clone <repository_url>
Replace <repository_url> with the URL of the GitHub repository you want to clone. This will create a local copy of the repository on your computer.

Open the repository in VS Code: Open VS Code and go to "File" > "Open Folder" (or use the shortcut Ctrl+K Ctrl+O). Navigate to the directory where you cloned the repository and select it. VS Code will open the repository in a new window.

Pull changes from the remote repository: To update your local repository with the latest changes from the remote repository, use the following command in the terminal within VS Code:

css
Copy code
git pull origin main
This command fetches the latest commits from the remote repository's main branch and merges them into your local branch.

Start working with the code: Now you can start working with the code in the repository. Make changes, create new files, or modify existing ones using VS Code's features.

Commit and push changes: Once you've made changes to the code, use the following commands to commit and push your changes to the remote repository:

sql
Copy code
git add .
git commit -m "Your commit message"
git push origin main
The git add . command stages all the changes you made. Replace "Your commit message" with a meaningful description of your changes. The git commit command creates a new commit with the staged changes, and git push pushes the commit to the remote repository.

That's it! You have successfully pulled the GitHub repository to your local machine, opened it in VS Code, and learned how to pull and push changes using Git commands.

Note: Make sure you have the necessary permissions to pull and push changes to the remote repository.