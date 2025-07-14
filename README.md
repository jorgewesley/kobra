# Kobra 🐍

![PyPI](https://img.shields.io/pypi/v/kobra)
![License](https://img.shields.io/pypi/l/kobra)
![Python](https://img.shields.io/pypi/pyversions/kobra)
![Build Status](https://github.com/yourusername/kobra/actions/workflows/ci.yml/badge.svg)

Kobra é uma ferramenta CLI para gerar projetos web com Flask ou FastAPI, pronta para projetos pequenos e grandes. Suporta banco de dados, autenticação JWT, frontend React opcional, Docker, testes e documentação com MkDocs.

## Funcionalidades
- Gera projetos Flask ou FastAPI com um comando.
- Suporte opcional a bancos de dados (SQLAlchemy, SQLModel).
- Autenticação JWT integrada (opcional).
- Frontend React básico (opcional).
- Inclui Docker, testes, `.gitignore`, `.env` e documentação.
- CLI moderna com Typer.

## Instalação
```bash
pip install kobra
```

## Uso
```bash
kobra my_project --framework flask --db --auth --frontend
```
ou
```bash
kobra my_project --framework fastapi
```

### Estrutura gerada
```
my_project/
├── app.py (ou main.py para FastAPI)
├── config.py
├── .env
├── models.py (se --db)
├── auth.py (se --auth)
├── static/
│   ├── css/style.css
│   ├── js/main.js
│   ├── images/
├── templates/ (apenas para Flask)
│   ├── index.html
├── frontend/ (se --frontend)
│   ├── src/App.jsx
│   ├── package.json
├── tests/
│   ├── test_app.py
├── docs/
│   ├── mkdocs.yml
├── .gitignore
├── Dockerfile
├── requirements.txt
```

### Como rodar o projeto gerado
1. Entre no diretório: `cd my_project`
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative: `source venv/bin/activate` (Linux/Mac) ou `venv\Scripts\activate` (Windows)
4. Instale dependências: `pip install -r requirements.txt`
5. Execute: `python app.py` (Flask) ou `python main.py` (FastAPI)

### Com Docker
```bash
docker build -t my_project .
docker run -p 8000:8000 my_project
```

### Documentação
```bash
pip install mkdocs mkdocs-material
mkdocs serve
```

## Contribuição
Veja [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre como contribuir.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato
- Autor: Jorge Wesley
- Email: wesleycardozoo@gmail.com
- GitHub: [jorgewesley/kobra](https://github.com/jorgewesley/kobra)
