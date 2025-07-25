import os
import subprocess
import datetime

# Your project directory
project_path = "D:/Coding/The Ultimate Pyrthon/practice/file handling"

# Commit message with current timestamp
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
commit_message = f"Backup on {timestamp}"

def auto_git_backup():
    try:
        os.chdir(project_path)

        # Stage changes
        subprocess.run(["git", "add", "."], check=True)

        # Check if there are changes to commit
        status_output = subprocess.check_output(["git", "status", "--porcelain"]).decode().strip()

        if status_output == "":
            print("⚠️  Nothing to commit. Working directory clean.")
        else:
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("✅ Backup pushed successfully!")

    except subprocess.CalledProcessError as e:
        print("❌ Error during Git operation:", e)

auto_git_backup()
