import typer
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os

HOME = os.getenv("HOME")

app = typer.Typer()

@app.command()
def dots(ctx: typer.Context):
    os.chdir(f"{HOME}/dots")
    subprocess.run(["cp", "-vr", f"{HOME}/.config/nvim", f"{HOME}/dots/.config"])
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "'sync'"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    app()
