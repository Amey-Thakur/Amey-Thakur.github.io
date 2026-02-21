import subprocess
import sys
import os

os.chdir(r"D:\GitHub\Amey-Thakur.github.io")

# Get all commits from oldest to newest
result = subprocess.run(
    ["git", "rev-list", "--reverse", "HEAD"],
    capture_output=True, text=True
)
commits = result.stdout.strip().split('\n')
print(f"Total commits to rewrite: {len(commits)}")

# The commit message (exact same format as ACC)
message = "Amey's Arc\n\nCo-authored-by: Mega Satish <mega.modha@gmail.com>"

# Write message to a temp file to avoid shell escaping issues
msg_file = os.path.join(os.getcwd(), "_commit_msg.txt")
with open(msg_file, "w", newline="\n") as f:  # Force Unix line endings
    f.write(message)
    f.write("\n")

# Map old hash -> new hash
hash_map = {}

for i, old_hash in enumerate(commits):
    # Get tree
    tree = subprocess.run(
        ["git", "rev-parse", f"{old_hash}^{{tree}}"],
        capture_output=True, text=True
    ).stdout.strip()

    # Get parents
    parents_result = subprocess.run(
        ["git", "rev-list", "--parents", "-n", "1", old_hash],
        capture_output=True, text=True
    ).stdout.strip().split()
    old_parents = parents_result[1:]  # First element is the commit itself

    # Map old parents to new hashes
    new_parents = [hash_map[p] for p in old_parents]

    # Get author info
    author_name = subprocess.run(
        ["git", "log", "-1", "--format=%an", old_hash],
        capture_output=True, text=True
    ).stdout.strip()
    author_email = subprocess.run(
        ["git", "log", "-1", "--format=%ae", old_hash],
        capture_output=True, text=True
    ).stdout.strip()
    author_date = subprocess.run(
        ["git", "log", "-1", "--format=%ai", old_hash],
        capture_output=True, text=True
    ).stdout.strip()

    # Set environment: author AND committer must match, dates must match
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = author_name
    env["GIT_AUTHOR_EMAIL"] = author_email
    env["GIT_AUTHOR_DATE"] = author_date
    env["GIT_COMMITTER_NAME"] = author_name
    env["GIT_COMMITTER_EMAIL"] = author_email
    env["GIT_COMMITTER_DATE"] = author_date

    # Build git commit-tree command with signing
    cmd = ["git", "commit-tree", tree, "-S", "-F", msg_file]
    for p in new_parents:
        cmd.extend(["-p", p])

    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    new_hash = result.stdout.strip()

    if result.returncode != 0 or not new_hash:
        print(f"ERROR at commit {i+1}/{len(commits)}: {old_hash[:7]}")
        print(f"stderr: {result.stderr}")
        sys.exit(1)

    hash_map[old_hash] = new_hash
    print(f"  [{i+1}/{len(commits)}] {old_hash[:7]} -> {new_hash[:7]}")

# Update branch ref to point to new HEAD
new_head = hash_map[commits[-1]]
subprocess.run(["git", "update-ref", "refs/heads/main", new_head])
print(f"\nDone! Updated main to {new_head}")

# Cleanup
os.remove(msg_file)
print("Cleaned up temp files.")
