import os
import sys
import re
import shutil
from pathlib import Path

def validate_project_name(name):
    """Valida o nome do projeto."""
    if not name:
        print("⚠️ Nome do projeto não pode ser vazio!")
        sys.exit(1)
    if not re.match(r'^[a-zA-Z0-9_-]+$', name):
        print("⚠️ Nome do projeto só pode conter letras, números, _ ou -!")
        sys.exit(1)
    if os.path.exists(name):
        print(f"⚠️ O diretório '{name}' já existe!")
        sys.exit(1)

def check_requirements():
    """Verifica se Python e pip estão instalados."""
    if not shutil.which('python'):
        print("❌ Python não encontrado! Instale o Python antes de continuar.")
        sys.exit(1)
    if not shutil.which('pip'):
        print("❌ pip não encontrado! Instale o pip antes de continuar.")
        sys.exit(1)

def create_project_structure(project_name, framework, db, auth, frontend):
    """Cria a estrutura de diretórios e arquivos do projeto."""
    directories = [
        "",
        "static/css",
        "static/js",
        "static/images",
        "tests",
        "docs"
    ]

    # Carregar templates de uma pasta externa (simulado aqui)
    templates_dir = Path(__file__).parent / "templates"
    framework_files = {
        "flask": {
            "app.py": (templates_dir / "flask/app.py").read_text(),
            "templates/index.html": (templates_dir / "flask/templates/index.html").read_text(),
            "static/css/style.css": (templates_dir / "flask/static/css/style.css").read_text(),
            "static/js/main.js": (templates_dir / "flask/static/js/main.js").read_text(),
        },
        "fastapi": {
            "main.py": (templates_dir / "fastapi/main.py").read_text(),
            "static/css/style.css": (templates_dir / "fastapi/static/css/style.css").read_text(),
            "static/js/main.js": (templates_dir / "fastapi/static/js/main.js").read_text(),
        },
        "common": {
            "requirements.txt": (templates_dir / "common/requirements.txt").read_text(),
            ".gitignore": (templates_dir / "common/.gitignore").read_text(),
            "Dockerfile": (templates_dir / "common/Dockerfile").read_text(),
            "tests/test_app.py": (templates_dir / "common/tests/test_app.py").read_text(),
            "config.py": (templates_dir / "common/config.py").read_text(),
            ".env": (templates_dir / "common/.env").read_text(),
            "mkdocs.yml": (templates_dir / "common/mkdocs.yml").read_text(),
        }
    }

    if db:
        framework_files[framework]["models.py"] = (templates_dir / f"{framework}/models.py").read_text()
    if auth:
        framework_files[framework]["auth.py"] = (templates_dir / f"{framework}/auth.py").read_text()

    main_file = "app.py" if framework == "flask" else "main.py"
    framework_requirements = {
        "flask": "flask>=2.3.0\nwerkzeug>=3.0.0\n",
        "fastapi": "fastapi>=0.100.0\nuvicorn>=0.20.0\n"
    }
    if db:
        framework_requirements[framework] += "sqlalchemy>=2.0.0\n" if framework == "flask" else "sqlmodel>=0.0.8\nasyncpg>=0.27.0\n"
    if auth:
        framework_requirements[framework] += "python-jose[cryptography]>=3.3.0\npasslib[bcrypt]>=1.7.4\n"

    framework_files["common"]["requirements.txt"] += framework_requirements[framework]
    test_imports = {
        "flask": "from flask import Flask\n",
        "fastapi": "from fastapi.testclient import TestClient\nfrom main import app\nclient = TestClient(app)\n"
    }
    framework_files["common"]["tests/test_app.py"] = framework_files["common"]["tests/test_app.py"].replace("{{ test_imports }}", test_imports[framework])

    try:
        for dir_path in directories:
            os.makedirs(os.path.join(project_name, dir_path), exist_ok=True)

        for file_path, content in framework_files[framework].items():
            full_path = os.path.join(project_name, file_path)
            with open(full_path, 'w') as f:
                f.write(content.replace("{{ project_name }}", project_name))

        for file_path, content in framework_files["common"].items():
            full_path = os.path.join(project_name, file_path)
            with open(full_path, 'w') as f:
                f.write(content.replace("{{ project_name }}", project_name).replace("{{ main_file }}", main_file))

        if frontend:
            frontend_dir = os.path.join(project_name, "frontend")
            os.makedirs(frontend_dir, exist_ok=True)
            for file_path in (templates_dir / "frontend/react").rglob("*"):
                rel_path = file_path.relative_to(templates_dir / "frontend/react")
                dest_path = os.path.join(frontend_dir, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                with open(dest_path, 'w') as f:
                    f.write(file_path.read_text().replace("{{ project_name }}", project_name))

        print(f"✅ Projeto '{project_name}' criado com sucesso para {framework.upper()}!")
        print(f"📁 Estrutura gerada:")
        for root, dirs, files in sorted(os.walk(project_name)):
            level = root.replace(project_name, '').count(os.sep)
            indent = '│   ' * level
            print(f"{indent}├── {os.path.basename(root)}/")
            for file in sorted(files):
                subindent = '│   ' * (level + 1)
                print(f"{subindent}├── {file}")

        print("\n🚀 Próximos passos:")
        print(f"cd {project_name}")
        print(f"python {main_file}")

    except PermissionError:
        print("❌ Sem permissão para criar arquivos no diretório atual!")
        sys.exit(1)
    except OSError as e:
        print(f"❌ Erro no sistema de arquivos: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
        sys.exit(1)