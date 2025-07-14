import typer
import os
from kobra.generator import create_project_structure, validate_project_name, check_requirements

app = typer.Typer(name="Kobra", help="🐍 Kobra - Gerador de projetos Flask e FastAPI")

@app.command()
def create(
    project_name: str = typer.Argument(..., help="Nome do projeto"),
    framework: str = typer.Option("flask", "--framework", "-f", help="Framework: flask ou fastapi"),
    db: bool = typer.Option(False, "--db/--no-db", help="Incluir suporte a banco de dados"),
    auth: bool = typer.Option(False, "--auth/--no-auth", help="Incluir autenticação JWT"),
    frontend: bool = typer.Option(False, "--frontend/--no-frontend", help="Incluir frontend React")
):
    """Cria um novo projeto web com Flask ou FastAPI."""
    typer.echo("🐍 Kobra - Gerador de Projetos Web")
    typer.echo("---------------------------------------")

    check_requirements()
    validate_project_name(project_name)

    if framework not in ["flask", "fastapi"]:
        typer.echo("⚠️ Framework inválido! Use 'flask' ou 'fastapi'.")
        raise typer.Exit(code=1)

    typer.echo("\n🔄 Gerando estrutura do projeto...")
    create_project_structure(project_name, framework, db, auth, frontend)

if __name__ == "__main__":
    app()