import typer
from utils import view_acl, grant_access, remove_access
from batch import apply_batch_file

app = typer.Typer()

@app.command()
def view(path: str):
    view_acl(path)

@app.command()
def grant(path: str, user: str, permission: str):
    grant_access(path, user, permission)

@app.command()
def remove(path: str, user: str):
    remove_access(path, user)

@app.command()
def batch(batch_file: str, action: str):
    apply_batch_file(batch_file, action)

if __name__ == "__main__":
    app()