# dev:stage:prod app-repo

This repository contains a simple Python service and GitHub Actions CI workflow
that builds and pushes a Docker image to ECR, then updates the GitOps repo for
ArgoCD sync on Minikube.

## Local run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/app.py
```

Service endpoints:
- `GET /`
- `GET /health`

## Branch to environment mapping

- `dev` branch -> `dev` overlay
- `staging` branch -> `stage` overlay
- `main` branch -> `prod` overlay

## Required GitHub secrets

- `AWS_ACCESS_KEY`
- `AWS_SECRET_KEY`
- `AWS_ACCOUNT_ID`
- `GIT_TOKEN` (token with push access to `dev-stage-prod-CD`)
