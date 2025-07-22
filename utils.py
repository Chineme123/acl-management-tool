import subprocess
from _logger import logger
from _mongo import collection
from rich import print
import os
import json
import re

#directory
log_dir = log_dir = os.path.join(os.path.expanduser("~"), "acl_tool_logs")
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"access.json")

# convert to json
def parse_acl_output(acl_text):
    print(acl_text)
    lines = acl_text.strip().splitlines()
    result = {
        "path": "",
        "acls": []
    }

    for i, line in enumerate(lines):
        # First line has the path and the first ACE
        if i == 0:
            parts = line.strip().split(" ", 1)
            result["path"] = parts[0]
            ace_part = parts[1].strip()
        else:
            ace_part = line.strip()

        match = re.match(r'(.+?):\(([^)]+)\)', ace_part)
        if match:
            identity = match.group(1).strip()
            permissions = match.group(2).strip()
            result["acls"].append({
                "identity": identity,
                "permissions": permissions
            })

    return result

# Defining common windows rights
rights_definitions = {
    "R": "Read",
    "W": "Write",
    "F": "Full Control",
    "D": "Delete",
    "M": "Modify",
    "RX": "Read and Execute",
    "N": "No",
}

# This is to view are users and access rights on a particular file
def view_acl(path: str):
    result = subprocess.run(["icacls", path], capture_output=True, text=True)
    parsed_acl = parse_acl_output(result.stdout)

    # # Load existing JSON entries
    # data = []
    # if os.path.exists(log_file):
    #     with open(log_file, "r") as f:
    #         try:
    #             data = json.load(f)
    #         except json.JSONDecodeError:
    #             data = []

    # # Remove any existing record with the same path
    # data = [entry for entry in data if entry.get["path"] != parsed_acl["path"]]

    # # Append the new one
    # data.append(parsed_acl)

    # # Write back to file
    # with open(log_file, "w") as f:
    #     json.dump(data, f, indent=4)

    # Optional: Upsert into DB
    collection.replace_one({"path": parsed_acl["path"]}, parsed_acl, upsert=True)

    print(result.stdout)

# This is grants specified permissions on a file
def grant_access(path: str, user: str, permission: str):
    command = ["icacls", path, "/grant", f"{user}:({permission})"]
    permissions = permission.split(',')

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"[cyan]Access granted for {user} on {path}:[/cyan] \n{result.stdout}")
        for i in permissions:
            logger.info(f"{rights_definitions[i]} Access was granted for {user} on {path}")
    else:
        print(f"[red]Failed to grant access for {user} on {path}:[/red] \n{result.stderr}")
        logger.error(f"Grant Access Failed: {result.stderr}")

# This removes all access a user has on file
def remove_access(path: str, user: str):
    command = ["icacls", path, "/remove", user]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"[cyan]Access removed for {user} on {path}:[/cyan] \n{result.stdout}")
        logger.info(f"All Access Removed for {user} on {path}")
    else:
        print(f"[red]Failed to remove access for {user} on {path}:[/red] \n{result.stderr}")
        logger.error(f"Remove Access Failed: {result.stderr}")
