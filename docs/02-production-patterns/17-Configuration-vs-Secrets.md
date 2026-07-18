\# Lesson 17 - Configuration vs Secrets

&gt; Repository: `enterprise-langgraph-multi-agent-platform`

\---

\# Learning Objectives

By the end of this lesson, you should understand:

\## Beginner

\- What is configuration?

\- What is a secret?

\- Why they should be separated

\## Intermediate

\- Environment variables

\- `.env`

\- ConfigMap

\- Kubernetes Secret

\## Advanced

\- Secret Managers

\- Secret Rotation

\- Encryption

\- Least Privilege Access

\## Production

\- AWS Secrets Manager

\- AWS Systems Manager Parameter Store

\- Azure Key Vault

\- Google Secret Manager

\- HashiCorp Vault

\- AI API Key Management

\---

\# Why This Topic Exists

One of the biggest security mistakes developers make is treating **configuration** and **secrets** as the same thing.

They are not.

A production system manages them differently.

\---

\# What is Configuration?

Configuration controls how an application behaves.

Examples:

\- Application Port

\- Log Level

\- Model Name

\- Region

\- Timeout

\- Retry Count

\- Feature Flags

Configuration is generally **not confidential**.

\---

\# What is a Secret?

A secret grants access to a protected resource.

Examples:

\- OpenAI API Key

\- Anthropic API Key

\- PostgreSQL Password

\- Redis Password

\- JWT Signing Key

\- OAuth Client Secret

\- AWS Access Keys

\- TLS Private Keys

Secrets must always be protected.

\---

\# Simple Comparison

| Configuration | Secret |

|---------------|--------|

| Model Name | API Key |

| Port | Password |

| Timeout | Private Key |

| Region | OAuth Secret |

| Log Level | Database Password |

Rule of thumb:

&gt; If someone else should not know it, it's a secret.

\---

\# Why Separate Them?

Imagine you need to change:

\`\`\`

LOG_LEVEL

INFO

↓

DEBUG

\`\`\`

No security risk.

Now imagine changing:

\`\`\`

OPENAI_API_KEY

\`\`\`

This requires careful handling because exposing it could allow unauthorized access and incur costs.

\---

\# Local Development

Typical setup:

\`\`\`

.env

\`\`\`

Example:

\`\`\`

MODEL_NAME=gpt-4.1-mini

LOG_LEVEL=INFO

OPENAI_API_KEY=xxxxxxxx

\`\`\`

The `.env` file is convenient for local development but should **never** be committed to Git.

\---

\# Production Environment

In production:

Configuration and secrets usually come from different sources.

\`\`\`

Configuration

        ↓

ConfigMap / Environment Variables

Secrets

        ↓

Secret Manager / Kubernetes Secret

\`\`\`

\---

\# Kubernetes

\## ConfigMap

Stores non-sensitive values.

Examples:

\- Port

\- Environment

\- Model Name

\- Feature Flags

\- Timeout

\---

\## Secret

Stores sensitive values.

Examples:

\- API Keys

\- Passwords

\- Certificates

\- Tokens

\---

\# Kubernetes Architecture

\`\`\`

Application

↓

ConfigMap

↓

Configuration

Application

↓

Secret

↓

Credentials

\`\`\`

Both can be exposed as environment variables or mounted as files.

\---

\# AWS Options

\## Systems Manager Parameter Store

Best for:

\- Configuration

\- Small secrets

\- Simple applications

Examples:

\- Environment Name

\- Feature Flags

\- Region

Can also store encrypted values.

\---

\## AWS Secrets Manager

Designed specifically for secrets.

Examples:

\- Database Passwords

\- OpenAI Keys

\- API Tokens

Benefits:

\- Automatic rotation

\- Encryption

\- IAM integration

\- Audit logging

\---

\# Azure

Use:

Azure Key Vault

Stores:

\- Secrets

\- Certificates

\- Keys

\---

\# Google Cloud

Use:

Google Secret Manager

\---

\# HashiCorp Vault

Large enterprises often use Vault.

Provides:

\- Dynamic Secrets

\- Secret Rotation

\- Encryption

\- Audit Logs

\- Fine-grained Access Control

\---

\# Secret Rotation

Never use the same API key forever.

Good practice:

\`\`\`

Old Key

↓

New Key

↓

Update Application

↓

Delete Old Key

\`\`\`

Regular rotation reduces risk.

\---

\# Encryption

Secrets should be encrypted:

At Rest

\- Database

\- Secret Manager

\- Kubernetes Secret Store

In Transit

\- HTTPS

\- TLS

Encryption protects data even if storage is compromised.

\---

\# Access Control

Follow the Principle of Least Privilege.

Example:

A service that only needs an OpenAI API key should **not** have access to database credentials.

\---

\# AI Platform Example

Your AI platform may use:

\- OpenAI

\- Anthropic

\- Pinecone

\- PostgreSQL

\- Redis

\- AWS

Each service should receive only the credentials it needs.

\---

\# Secret Lifecycle

\`\`\`

Generate

↓

Store Securely

↓

Retrieve

↓

Use

↓

Rotate

↓

Revoke

↓

Delete

\`\`\`

Every secret should follow a managed lifecycle.

\---

\# What Should Never Be Done?

❌ Commit `.env` to Git

❌ Store API keys in source code

❌ Log secrets

❌ Email credentials

❌ Share credentials in chat messages

❌ Hardcode passwords

❌ Reuse secrets across environments

\---

\# Environment Separation

Development

\`\`\`

OpenAI Development Key

\`\`\`

Staging

\`\`\`

OpenAI Staging Key

\`\`\`

Production

\`\`\`

OpenAI Production Key

\`\`\`

Never reuse the same secret across environments.

\---

\# Logging Considerations

Good:

\`\`\`

OpenAI request started

\`\`\`

Bad:

\`\`\`

OpenAI API Key:

sk-xxxxxxxxxxxxxxxx

\`\`\`

Secrets must never appear in logs.

\---

\# CI/CD

Use secure secret storage.

Examples:

\- GitHub Actions Secrets

\- GitLab CI Variables

\- Azure DevOps Library

\- Jenkins Credentials

Never hardcode credentials into pipeline definitions.

\---

\# Common Mistakes

❌ `.env` committed to Git

❌ Secrets stored in README

❌ API keys inside source code

❌ Logging credentials

❌ Sharing production credentials

❌ Using one secret for every environment

❌ No secret rotation

\---

\# Production Best Practices

\- Separate configuration from secrets.

\- Encrypt secrets.

\- Rotate secrets regularly.

\- Follow least privilege.

\- Use Secret Managers.

\- Never commit secrets.

\- Audit secret access.

\- Use different secrets per environment.

\---

\# Interview Questions

\## What is the difference between Configuration and Secrets?

Configuration controls application behavior.

Secrets provide authenticated access to protected resources.

\---

\## Why shouldn't `.env` be committed?

It often contains sensitive credentials that could be exposed publicly.

\---

\## When should ConfigMap be used?

For non-sensitive configuration such as ports, feature flags, model names, and log levels.

\---

\## When should Kubernetes Secret be used?

For API keys, passwords, certificates, and tokens.

\---

\## Why rotate secrets?

Regular rotation limits the impact of credential compromise and follows security best practices.

\---

\## Why follow Least Privilege?

Each application should have access only to the resources it requires, reducing the potential impact of a security breach.

\---

\# Homework

Answer the following:

1\. What is the difference between configuration and secrets?

2\. Why shouldn't `.env` be committed?

3\. When should you use ConfigMap instead of Secret?

4\. Why is secret rotation important?

5\. What does the Principle of Least Privilege mean?

\---

\# Summary

Configuration and secrets are both essential to application deployment, but they serve different purposes.

A production-ready AI Platform should:

\- Store configuration separately from secrets

\- Use dedicated Secret Managers

\- Encrypt sensitive information

\- Rotate credentials regularly

\- Follow least privilege

\- Prevent accidental exposure through logs, source code, or version control

Strong secret management is a fundamental requirement for secure AI platforms and cloud-native applications.