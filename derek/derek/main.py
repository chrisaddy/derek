import typer
import sync

app = typer.Typer()
app.add_typer(sync.app, name="sync")

if __name__ == "__main__":
    app()
