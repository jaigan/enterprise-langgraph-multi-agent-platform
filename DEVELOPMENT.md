\# Development Guide

Welcome to the **Enterprise LangGraph Multi-Agent Platform** development guide.

This document explains how to set up your local development environment, contribute to the project, run tests, and follow engineering best practices.

\---

\# Table of Contents

\- Prerequisites

\- Repository Setup

\- Python Environment

\- Dependency Management

\- Environment Variables

\- Project Structure

\- Running the Application

\- Running Tests

\- Code Quality

\- Debugging

\- Git Workflow

\- Development Best Practices

\- Troubleshooting

\---

\# Prerequisites

Install the following tools before starting.

\## Required

\- Git

\- Python 3.12+

\- uv

\- Docker Desktop

\- Visual Studio Code

\---

\## Recommended

\- Kubernetes

\- kubectl

\- Helm

\- Terraform

\- Make

\- AWS CLI

\---

\# Clone Repository

\`\`\`bash

git clone <https://github.com/jaigan/enterprise-langgraph-multi-agent-platform.git>

cd enterprise-langgraph-multi-agent-platform

\`\`\`

\---

\# Python Environment

Create a virtual environment.

\`\`\`bash

uv venv

\`\`\`

Activate it.

Windows

\`\`\`bash

.venv\\Scripts\\activate

\`\`\`

Linux / macOS

\`\`\`bash

source .venv/bin/activate

\`\`\`

\---

\# Install Dependencies

\`\`\`bash

uv sync

\`\`\`

or

\`\`\`bash

uv pip install -e .

\`\`\`

\---

\# Environment Variables

Copy the example configuration.

\`\`\`bash

cp .env.example .env

\`\`\`

Update values as needed.

Never commit:

\`\`\`

.env

\`\`\`

\---

\# Project Structure

\`\`\`

src/

docs/

tests/

docker/

kubernetes/

terraform/

scripts/

\`\`\`

See `README.md` for the complete repository layout.

\---

\# Running the Application

Development mode:

\`\`\`bash

uv run python src/[main.py](http://main.py)

\`\`\`

When the FastAPI application is available:

\`\`\`bash

uv run uvicorn src.main:app --reload

\`\`\`

\---

\# Running Tests

Run all tests.

\`\`\`bash

pytest

\`\`\`

Run a specific file.

\`\`\`bash

pytest tests/test\_[graph.py](http://graph.py)

\`\`\`

Measure test coverage.

\`\`\`bash

pytest --cov=src

\`\`\`

\---

\# Code Quality

\### Format

\`\`\`bash

ruff format .

\`\`\`

\---

\### Lint

\`\`\`bash

ruff check .

\`\`\`

\---

\### Type Checking

\`\`\`bash

mypy src

\`\`\`

\---

\# Pre-Commit Hooks

Install hooks.

\`\`\`bash

pre-commit install

\`\`\`

Run manually.

\`\`\`bash

pre-commit run --all-files

\`\`\`

\---

\# Docker

Build the image.

\`\`\`bash

docker build -t enterprise-langgraph .

\`\`\`

Run the container.

\`\`\`bash

docker run enterprise-langgraph

\`\`\`

\---

\# Kubernetes

Validate manifests.

\`\`\`bash

kubectl apply --dry-run=client -f kubernetes/

\`\`\`

Deploy.

\`\`\`bash

kubectl apply -f kubernetes/

\`\`\`

\---

\# Git Workflow

Create a feature branch.

\`\`\`bash

git checkout -b feature/my-feature

\`\`\`

Commit changes.

\`\`\`bash

git commit -m "feat(graph): add planner node"

\`\`\`

Push branch.

\`\`\`bash

git push origin feature/my-feature

\`\`\`

Open a Pull Request.

\---

\# Development Best Practices

\- Follow Clean Architecture.

\- Write small, focused commits.

\- Keep pull requests manageable.

\- Write tests for new functionality.

\- Update documentation alongside code.

\- Use descriptive commit messages.

\- Avoid hardcoded configuration.

\- Never commit secrets.

\---

\# Debugging

Useful commands.

Check Python version.

\`\`\`bash

python --version

\`\`\`

Check installed packages.

\`\`\`bash

uv pip list

\`\`\`

Verify dependencies.

\`\`\`bash

uv sync

\`\`\`

\---

\# Troubleshooting

\## Virtual environment issues

Recreate the environment.

\`\`\`bash

rm -rf .venv

uv venv

uv sync

\`\`\`

\---

\## Dependency conflicts

Synchronize dependencies.

\`\`\`bash

uv sync

\`\`\`

\---

\## Import errors

Ensure the virtual environment is activated.

Verify package installation.

\---

\## Docker issues

Rebuild without cache.

\`\`\`bash

docker build --no-cache -t enterprise-langgraph .

\`\`\`

\---

\# Related Documentation

\- [README.md](http://README.md)

\- [CONTRIBUTING.md](http://CONTRIBUTING.md)

\- [SECURITY.md](http://SECURITY.md)

\- [ARCHITECTURE.md](http://ARCHITECTURE.md)

\- [TROUBLESHOOTING.md](http://TROUBLESHOOTING.md)

\---

\# Development Philosophy

This project follows enterprise software engineering practices.

Every change should prioritize:

\- Maintainability

\- Reliability

\- Scalability

\- Security

\- Observability

\- Testability

\- Simplicity

The goal is not just to build a working AI platform, but to build one that is production-ready, well-documented, and easy for other engineers to understand and extend.