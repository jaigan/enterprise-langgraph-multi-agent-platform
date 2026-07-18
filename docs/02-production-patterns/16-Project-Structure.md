\# Lesson 16 - Project Structure

&gt; Repository: `enterprise-langgraph-multi-agent-platform`

\---

\# Learning Objectives

By the end of this lesson, you should understand:

\## Beginner

\- Why project structure matters

\- Organizing source code

\- Separation of concerns

\## Intermediate

\- Layered architecture

\- Feature-based organization

\- Modular design

\## Advanced

\- Clean Architecture

\- Dependency flow

\- Package organization

\- Enterprise repository standards

\## Production

\- Scalable repository design

\- Team collaboration

\- Monorepo vs Polyrepo

\- AI Platform repository organization

\---

\# Why Project Structure Exists

A project structure is not just about organizing files.

It defines:

\- Maintainability

\- Scalability

\- Readability

\- Team collaboration

\- Deployment strategy

Good software can become difficult to maintain if the project structure is poor.

\---

\# Business Problem

Imagine joining a company where the repository contains:

\`\`\`

[main.py](http://main.py)

[utils.py](http://utils.py)

[helper.py](http://helper.py)

[test.py](http://test.py)

[new.py](http://new.py)

[old.py](http://old.py)

[backup.py](http://backup.py)

[main2.py](http://main2.py)

main\_[final.py](http://final.py)

\`\`\`

Questions arise immediately:

\- Where is the API?

\- Where is the graph?

\- Where are the agents?

\- Where are the prompts?

\- Where is the configuration?

A poor structure slows down development and onboarding.

\---

\# Technical Problem

As projects grow:

\- More developers contribute.

\- More services are added.

\- More integrations appear.

\- More environments are introduced.

Without structure:

\- Code duplication increases.

\- Dependencies become tangled.

\- Testing becomes harder.

\- Refactoring becomes risky.

\---

\# Goals of a Good Project Structure

A good project structure should:

\- Separate responsibilities

\- Be easy to navigate

\- Be scalable

\- Support testing

\- Support deployment

\- Encourage modularity

\---

\# Repository Structure

\`\`\`

enterprise-langgraph-multi-agent-platform/

├── .github/

├── docs/

├── architecture/

├── assets/

├── scripts/

│

├── src/

│

├── tests/

│

├── docker/

├── kubernetes/

├── helm/

├── terraform/

│

├── pyproject.toml

├── [README.md](http://README.md)

├── LICENSE

└── .env.example

\`\`\`

\---

\# Why Each Top-Level Folder Exists

\## .github/

Contains:

\- GitHub Actions

\- Issue templates

\- Pull request templates

\- Dependabot configuration

\---

\## docs/

Contains:

\- Architecture

\- Tutorials

\- SOPs

\- ADRs

\- Lessons

\- Runbooks

\---

\## architecture/

Contains:

\- [Draw.io](http://Draw.io)

\- Mermaid

\- PNG diagrams

\- Sequence diagrams

\- Infrastructure diagrams

\---

\## assets/

Contains:

\- Images

\- Screenshots

\- Logos

\---

\## scripts/

Contains:

\- Local setup

\- Database initialization

\- Utility scripts

\- Deployment helpers

\---

\# Source Directory

\`\`\`

src/

├── api/

├── graph/

├── state/

├── nodes/

├── agents/

├── services/

├── clients/

├── tools/

├── prompts/

├── memory/

├── checkpoint/

├── config/

├── observability/

├── auth/

├── models/

├── schemas/

└── utils/

\`\`\`

\---

\# Folder Responsibilities

\## api/

Contains:

\- FastAPI routes

\- API versioning

\- Request handling

No business logic.

\---

\## graph/

Contains:

\- StateGraph

\- Graph Builder

\- Graph compilation

\- Routing

\---

\## state/

Contains:

\- AgentState

\- State definitions

\- Typed state models

\---

\## nodes/

Contains:

\- LangGraph nodes

\- Node execution logic

One file per node.

\---

\## agents/

Contains:

\- Planner Agent

\- Research Agent

\- Reviewer Agent

\- Supervisor Agent

\---

\## services/

Contains:

Business logic.

Examples:

\- LLM Service

\- Search Service

\- Memory Service

\---

\## clients/

Contains:

External SDK wrappers.

Examples:

\- OpenAI Client

\- Anthropic Client

\- Pinecone Client

\- Redis Client

\---

\## tools/

Contains:

LangGraph tools.

Examples:

\- Calculator

\- Search Tool

\- SQL Tool

\---

\## prompts/

Contains:

System prompts.

Prompt templates.

No business logic.

\---

\## memory/

Contains:

Memory implementation.

Conversation history.

Summarization.

\---

\## checkpoint/

Contains:

Checkpoint storage.

Recovery.

Persistence.

\---

\## config/

Contains:

Configuration.

Logging.

Constants.

Settings.

\---

\## observability/

Contains:

Logging.

Metrics.

Tracing.

OpenTelemetry.

\---

\## auth/

Contains:

Authentication.

Authorization.

RBAC.

JWT.

\---

\## models/

Contains:

Internal domain models.

Business entities.

\---

\## schemas/

Contains:

Pydantic request and response models.

\---

\## utils/

Contains:

Reusable helper functions.

Avoid placing business logic here.

\---

\# Test Structure

\`\`\`

tests/

├── unit/

├── integration/

├── e2e/

├── performance/

├── security/

└── fixtures/

\`\`\`

\---

\# Why Separate Tests?

Unit tests:

Fast.

No external services.

\---

Integration tests:

Multiple components together.

\---

End-to-End tests:

Complete workflow.

\---

Performance tests:

Latency.

Throughput.

Load.

\---

Security tests:

Authentication.

Authorization.

Vulnerability checks.

\---

\# Infrastructure Folders

\## docker/

Dockerfile

docker-compose.yml

Development containers

\---

\## kubernetes/

Deployment

Service

Ingress

ConfigMap

Secret

HPA

RBAC

\---

\## helm/

Reusable Helm chart.

Values.

Templates.

\---

\## terraform/

Infrastructure as Code.

Cloud resources.

Networking.

IAM.

\---

\# Layered Architecture

\`\`\`

API

↓

Graph

↓

Node

↓

Service

↓

Client

↓

External Service

\`\`\`

Each layer has one responsibility.

\---

\# Dependency Direction

Dependencies should always move downward.

\`\`\`

API

↓

Graph

↓

Node

↓

Service

↓

Client

\`\`\`

Never reverse the dependency flow.

\---

\# Naming Conventions

Good

\`\`\`

llm\_[service.py](http://service.py)

planner\_[agent.py](http://agent.py)

memory\_[service.py](http://service.py)

\`\`\`

Bad

\`\`\`

[helper.py](http://helper.py)

[utils2.py](http://utils2.py)

[temp.py](http://temp.py)

[new.py](http://new.py)

[old.py](http://old.py)

\`\`\`

File names should describe their responsibility.

\---

\# Common Mistakes

❌ Everything inside utils/

❌ Huge [main.py](http://main.py)

❌ Business logic in API routes

❌ SDK calls inside nodes

❌ Mixed responsibilities

❌ Circular imports

❌ No separation between clients and services

\---

\# Production Best Practices

\- One responsibility per module.

\- Keep files focused.

\- Organize by domain.

\- Avoid circular dependencies.

\- Keep infrastructure separate from application code.

\- Version APIs.

\- Separate configuration from logic.

\---

\# Interview Questions

\## Why separate Services and Clients?

Clients communicate with external systems.

Services implement business logic.

Keeping them separate improves maintainability and testing.

\---

\## Why avoid business logic in API routes?

API routes should only handle HTTP concerns.

Business logic belongs in the service layer.

\---

\## Why separate Nodes from Services?

Nodes orchestrate workflow execution.

Services perform business operations.

This keeps the graph simple and reusable.

\---

\## Why have dedicated infrastructure folders?

Infrastructure evolves independently from application code and should remain organized and version-controlled.

\---

\# Homework

Answer the following:

1\. Why shouldn't business logic exist in API routes?

2\. Why separate Clients and Services?

3\. Why are Nodes different from Agents?

4\. Why avoid putting everything inside utils/?

5\. Why should dependencies flow in one direction?

\---

\# Summary

A well-designed project structure is the foundation of maintainable software.

A production-ready AI Platform should:

\- Separate concerns clearly

\- Follow layered architecture

\- Organize code by responsibility

\- Support testing and deployment

\- Scale with teams and features

\- Enable long-term maintainability

A good project structure allows engineers to understand the system quickly, collaborate efficiently, and extend the platform without introducing unnecessary complexity.