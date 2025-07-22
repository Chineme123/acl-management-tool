import json
import csv
import os
from utils import grant_access, remove_access
from rich import print

def apply_batch_file(batch_file: str, action: str):
    if not os.path.exists(batch_file):
        print(f"[red]Batch file not found: {batch_file}[/red]")
        return
    
    ext = os.path.splitext(batch_file)[1].lower()
    entries = []

    if ext == ".json":
        with open(batch_file, "r") as file:
            entries = json.load(file)
    elif ext == ".csv":
        with open(batch_file, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                entries.append(row)
    else:
        print(f"[red]Unsupported file type: {ext}[/red]")
        return
    
    for entry in entries:
        try:
            if action == "grant":
                if "path" in entry and "user" in entry and "perm" in entry:
                    path = entry["path"]
                    user = entry["user"]
                    perm = entry["perm"]
                    print(f"[green]Processing: {path} for {user} with {perm}[/green]")
                    grant_access(path, user, perm)
            elif action == "remove":
                if "path" in entry and "user" in entry:
                    path = entry["path"]
                    user = entry["user"]
                    print(f"[green]Processing: {path} for {user} with {perm}[/green]")
                    remove_access(path, user)
            else:
                print(f"[red]Invalid action: {action}[/red]")
        except Exception as e:
            print(f"[red]Error processing {entry}: {e}[/red]")
    
    print("[green]Batch processing complete[/green]")