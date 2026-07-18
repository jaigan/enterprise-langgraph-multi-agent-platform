
\# Learning Objectives

By the end of this lesson, you should understand:

\## Beginner

\- What is configuration?

\- Why not hardcode values?

\- Difference between configuration and business logic.

\## Intermediate

\- Environment variables

\- `.env` files

\- Configuration hierarchy

\- Configuration validation

\## Advanced

\- Centralized configuration

\- Singleton configuration

\- Typed configuration

\- Environment-specific configuration

\## Production

\- Secret management

\- Cloud secret managers

\- Kubernetes ConfigMaps & Secrets

\- Configuration versioning

\- Configuration validation at startup

\- Dynamic configuration (when appropriate)

\---

\# Why Configuration Exists

Consider the following code:

\`\`\`python

llm = ChatOpenAI(

    api_key="sk-xxxx",

    model="gpt-4.1-mini",

    temperature=0

)

\`\`\`

This works.

Now imagine you have multiple environments:

\- Development

\- QA

\- Staging

\- Production

Each environment has different:

\- API Keys

\- Model Names

\- Database URLs

\- Logging Levels

\- Feature Flags

Would you modify your source code every time?

No.

Configuration exists to separate **environment-specific values** from **business logic**.

\---

\# Business Problem

Without configuration management:

\- Developers edit source code for deployments.

\- Secrets leak into Git repositories.

s- Switching environments becomes difficult.

\- Deployments become error-prone.

\- Scaling across environments becomes harder.

\---

\# Technical Problem

Hardcoded values create:

\- Tight coupling

\- Poor portability

\- Difficult testing

\- Security risks

\- Difficult deployments

\---

\# Twelve-Factor App Principle

One of the core Twelve-Factor App principles states:

&gt; Store configuration in the environment.

Never hardcode secrets or deployment-specific values into the application.

\---

\# Bad Example

\`\`\`python

DATABASE_URL = "postgres://[localhost](http://localhost)"

OPENAI_API_KEY = "sk-xxxx"

MODEL_NAME = "gpt-4"

\`\`\`

Problems:

\- Credentials stored in source code

\- Difficult to deploy

\- Security risk

\- Cannot support multiple environments easily

\---

\# Good Example

\`\`\`

.env

OPENAI_API_KEY=...

MODEL_NAME=gpt-4.1-mini

LOG_LEVEL=INFO

DATABASE_HOST=db

DATABASE_PORT=5432

\`\`\`

The application loads these values during startup.

\---

\# Configuration Hierarchy

A typical production application loads configuration in this order:

\`\`\`

Command-Line Arguments

        ↓

Environment Variables

        ↓

.env File

        ↓

Configuration File (Optional)

        ↓

Default Values

\`\`\`

Higher-priority sources override lower-priority sources.

\---

\# Repository Structure

\`\`\`

src/

└── config/

    ├── **init**.py

    ├── [settings.py](http://settings.py)

    ├── [logging.py](http://logging.py)

    └── [constants.py](http://constants.py)

\`\`\`

\---

\# File Responsibilities

\## [settings.py](http://settings.py)

Responsible for:

\- Reading environment variables

\- Validation

\- Typed configuration

\- Creating a singleton settings object

No business logic.

\---

\## [logging.py](http://logging.py)

Responsible for:

\- Logging configuration

\- Log format

\- Log level

\- Structured logging configuration

\---

\## [constants.py](http://constants.py)

Contains:

\- Application constants

\- Default timeout values

\- Retry limits

\- Application metadata

Never store secrets here.

\---

\# Configuration Flow

\`\`\`

Application Starts

        ↓

Load .env

        ↓

Read Environment Variables

        ↓

Validate Configuration

        ↓

Create Settings Object

        ↓

Inject Settings Across Application

\`\`\`

\---

\# Runtime Flow

\`\`\`

[main.py](http://main.py)

      ↓

[settings.py](http://settings.py)

      ↓

LLM Client

      ↓

Database

      ↓

API

      ↓

Graph

\`\`\`

Every component reads configuration from a single source.

\---

\# Why Not Use os.getenv Everywhere?

Bad:

\`\`\`python

api_key = os.getenv("OPENAI_API_KEY")

\`\`\`

Repeated in every file.

Problems:

\- Duplication

\- No validation

\- Easy to introduce typos

\- Difficult to test

\- Hard to maintain

Instead:

\`\`\`python

settings.OPENAI_API_KEY

\`\`\`

One source of truth.

\---

\# Why Typed Configuration?

Instead of:

\`\`\`python

MODEL = os.getenv("MODEL")

\`\`\`

Use a typed configuration object:

\`\`\`python

settings.model_name

\`\`\`

Benefits:

\- IDE autocomplete

\- Type checking

\- Validation

\- Easier refactoring

\- Better developer experience

\---

\# Configuration vs Secrets

\## Configuration

Examples:

\- Model Name

\- Region

\- Logging Level

\- Timeout

\- Port Number

\## Secrets

Examples:

\- API Keys

\- Database Passwords

\- OAuth Tokens

\- Certificates

Secrets require stronger protection.

\---

\# Production Secret Management

\## Local Development

\`\`\`

.env

\`\`\`

\## Production

Use dedicated secret managers:

\- AWS Secrets Manager

\- Azure Key Vault

\- Google Secret Manager

\- HashiCorp Vault

\- Kubernetes Secrets

Never commit production secrets.

\---

\# Kubernetes

\## ConfigMap

Stores:

\- Configuration

\- Feature flags

\- Environment variables

\## Secret

Stores:

\- Passwords

\- Tokens

\- Certificates

\- API Keys

Pods consume both as environment variables or mounted files.

\---

\# Docker

Example:

\`\`\`dockerfile

ENV LOG_LEVEL=INFO

\`\`\`

Or inject values during runtime:

\`\`\`bash

docker run \\

  -e OPENAI_API_KEY=... \\

  -e MODEL_NAME=gpt-4.1-mini

\`\`\`

\---

\# CI/CD

GitHub Actions should use:

\- Repository Secrets

\- Organization Secrets

\- Environment Secrets

Never hardcode credentials inside workflow files.

\---

\# Design Pattern

Configuration follows the **Singleton Pattern**.

One configuration object.

Shared across the application.

\---

\# SOLID Principles

\## Single Responsibility Principle

The configuration module should only:

\- Load configuration

\- Validate configuration

\- Expose configuration

It should never contain business logic.

\---

\# Common Mistakes

❌ Hardcoding API keys

❌ Calling `os.getenv()` throughout the codebase

❌ Multiple configuration modules

❌ No validation

❌ Secrets committed to Git

❌ Mixing configuration with business logic

❌ Different configuration loading strategies across modules

\---

\# Production Best Practices

\- Keep one configuration module.

\- Validate configuration during startup.

\- Fail fast if required values are missing.

\- Separate configuration from secrets.

\- Use immutable configuration after startup.

\- Support multiple environments cleanly.

\- Never commit sensitive information.

\---

\# Interview Questions

\## Why centralize configuration?

A centralized configuration provides a single source of truth, improves maintainability, simplifies testing, and reduces duplication.

\---

\## Why validate configuration during startup?

Failing fast prevents runtime failures caused by missing or invalid configuration.

\---

\## Why shouldn't API keys be committed?

Committed credentials can be leaked, abused, or accidentally exposed, creating significant security risks.

\---

\## Why use environment variables?

Environment variables separate deployment-specific configuration from application code and align with Twelve-Factor App principles.

\---

\# Homework

Answer the following questions:

1\. Why is configuration different from business logic?

2\. Why should settings be loaded only once?

3\. What belongs in a Kubernetes ConfigMap?

4\. What belongs in a Kubernetes Secret?

5\. Why is `.env` intended only for local development?

6\. What risks arise if configuration validation is skipped?

\---

\# Summary

Configuration management is the foundation of every production-grade application.

A well-designed configuration system:

\- Separates environment-specific values from business logic.

\- Protects sensitive information.

\- Simplifies deployments.

\- Improves maintainability.

\- Supports multiple environments.

\- Enables secure, scalable, and reliable applications.

Understanding configuration management is a fundamental skill for AI Platform Engineers and AI Platform Architects.