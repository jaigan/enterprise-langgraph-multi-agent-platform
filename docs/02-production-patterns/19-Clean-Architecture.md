\# Lesson 19 - Clean Architecture

&gt; Repository: `enterprise-langgraph-multi-agent-platform`

\---

\# Learning Objectives

By the end of this lesson, you should understand:

\## Beginner

\- What is Clean Architecture?

\- Why Clean Architecture exists

\- Separation of concerns

\- Layers and responsibilities

\## Intermediate

\- Dependency Rule

\- Domain Layer

\- Application Layer

\- Infrastructure Layer

\## Advanced

\- AI Platform Architecture

\- LangGraph Architecture

\- Hexagonal Architecture

\- Onion Architecture

\## Production

\- Enterprise AI systems

\- Maintainable software

\- Scalable architectures

\- Team collaboration

\---

\# Why Clean Architecture Exists

Imagine a project after five years.

100 Developers

↓

500 APIs

↓

200 Services

↓

1000 Features

↓

Millions of users

Can developers still understand the code?

If the answer is "No"

the architecture has failed.

\---

\# Business Problem

Without architecture:

\- Difficult onboarding

\- Difficult testing

\- Tight coupling

\- Slow feature development

\- Frequent production bugs

\---

\# Technical Problem

Developers begin mixing everything together.

\`\`\`

API

↓

Database

↓

OpenAI

↓

Business Logic

↓

Redis

↓

Logging

↓

Response

\`\`\`

Everything becomes dependent on everything else.

\---

\# What is Clean Architecture?

Clean Architecture separates responsibilities into independent layers.

Every layer has ONE responsibility.

\---

\# Core Principle

Business Logic should NOT depend on frameworks.

Instead,

Frameworks depend on Business Logic.

\---

\# Dependency Rule

The most important rule.

Dependencies ALWAYS point inward.

Never outward.

\`\`\`

Framework

↓

Infrastructure

↓

Application

↓

Domain

\`\`\`

Domain never depends on FastAPI.

Domain never depends on OpenAI.

Domain never depends on PostgreSQL.

\---

\# Four Layers

\`\`\`

+----------------------+

| Presentation         |

+----------------------+

↓

+----------------------+

| Application          |

+----------------------+

↓

+----------------------+

| Domain               |

+----------------------+

↓

+----------------------+

| Infrastructure       |

+----------------------+

\`\`\`

\---

\# 1 Presentation Layer

Responsible for

\- HTTP

\- REST API

\- FastAPI

\- Authentication

\- Validation

Contains

\`\`\`

api/

\`\`\`

Nothing else.

No business logic.

\---

\# 2 Application Layer

Responsible for

\- Use Cases

\- Workflow

\- Services

\- Graph execution

Contains

\`\`\`

graph/

services/

agents/

\`\`\`

\---

\# 3 Domain Layer

Responsible for

Business Rules.

Contains

\`\`\`

state/

models/

interfaces/

entities/

\`\`\`

This is the heart of the application.

\---

\# 4 Infrastructure Layer

Responsible for

External systems.

Contains

\`\`\`

clients/

database/

redis/

vectordb/

aws/

observability/

\`\`\`

\---

\# Our Repository

\`\`\`

src/

api/

↓

graph/

↓

nodes/

↓

services/

↓

clients/

↓

OpenAI

\`\`\`

Notice

The API never calls OpenAI directly.

\---

\# Bad Example

\`\`\`

FastAPI

↓

ChatOpenAI

↓

Return Response

\`\`\`

Impossible to maintain.

\---

\# Good Example

\`\`\`

FastAPI

↓

Graph

↓

Node

↓

Service

↓

Client

↓

OpenAI

\`\`\`

Each layer has one responsibility.

\---

\# Why Separate Layers?

Suppose tomorrow we replace

FastAPI

with

gRPC.

Only

\`\`\`

api/

\`\`\`

changes.

Everything else remains.

\---

Suppose we replace

OpenAI

with

Claude.

Only

\`\`\`

clients/

\`\`\`

changes.

Everything else remains.

\---

\# Domain Layer Example

Contains

\`\`\`

Conversation

Agent State

Message

Memory

Workflow Rules

\`\`\`

Never

\`\`\`

OpenAI

Redis

FastAPI

PostgreSQL

\`\`\`

\---

\# Infrastructure Layer Example

Contains

\`\`\`

OpenAI Client

Redis Client

VectorDB Client

S3 Client

Cloud Storage

\`\`\`

Business logic never belongs here.

\---

\# AI Platform Architecture

\`\`\`

API

↓

Graph

↓

Planner Node

↓

LLM Service

↓

LLM Client

↓

OpenAI

\`\`\`

Every responsibility is isolated.

\---

\# Why Services Exist

Services contain

Business Logic

Examples

\- Prompt generation

\- Retry logic

\- Memory selection

\- Agent orchestration

\---

\# Why Clients Exist

Clients only communicate with

External systems.

Examples

\- OpenAI SDK

\- Anthropic SDK

\- Redis SDK

Nothing else.

\---

\# Dependency Flow

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

SDK

\`\`\`

Never reverse this direction.

\---

\# Clean Architecture Benefits

\- Easy testing

\- Easy maintenance

\- Easy provider replacement

\- Easier onboarding

\- Better scalability

\- Better collaboration

\---

\# Testing

Presentation

↓

Mock Service

Application

↓

Mock Client

Infrastructure

↓

Integration Tests

Everything becomes easier to test.

\---

\# Clean Architecture vs Layered Architecture

Layered Architecture

Organizes code.

Clean Architecture

Organizes dependencies.

The Dependency Rule is what makes Clean Architecture different.

\---

\# Clean Architecture vs Hexagonal Architecture

Both aim to isolate business logic.

Hexagonal focuses on

Ports

Adapters

Clean Architecture focuses on

Dependency Direction.

\---

\# Clean Architecture vs Onion Architecture

Very similar.

Both place

Business Logic

at the center.

\---

\# Common Mistakes

❌ Business logic in FastAPI

❌ OpenAI SDK inside Nodes

❌ SQL inside API

❌ Logging everywhere

❌ Circular dependencies

❌ Massive utility modules

❌ Mixing infrastructure with business rules

\---

\# Production Best Practices

\- Keep layers independent.

\- Depend on abstractions.

\- Isolate business rules.

\- Keep infrastructure replaceable.

\- Write tests at every layer.

\- Avoid framework lock-in.

\- Follow the Dependency Rule.

\---

\# How FAANG Builds Software

The exact folder names differ.

But the principles are the same.

Every large engineering organization separates

Business Logic

from

Infrastructure.

Frameworks are treated as implementation details.

\---

\# Interview Questions

\## What is Clean Architecture?

A software architecture that separates responsibilities into independent layers while enforcing inward dependency flow.

\---

\## What is the Dependency Rule?

Dependencies should always point toward the core business logic.

The Domain layer should never depend on frameworks or infrastructure.

\---

\## Why shouldn't FastAPI call OpenAI directly?

It tightly couples the application to a specific framework and provider, making testing and future changes difficult.

\---

\## Why separate Clients and Services?

Clients communicate with external systems.

Services implement business logic.

This separation improves maintainability and testability.

\---

\## Why is business logic placed in the Domain/Application layer?

Business rules represent the core value of the application and should remain independent of infrastructure so they can evolve without being affected by framework or provider changes.

\---

\# Homework

Answer the following:

1\. What is the Dependency Rule?

2\. Why should the Domain layer never depend on FastAPI?

3\. Why separate Services from Clients?

4\. Why is OpenAI considered Infrastructure?

5\. How would you replace OpenAI with Anthropic using Clean Architecture?

\---

\# Summary

Clean Architecture is the foundation of production software.

It ensures:

\- Clear separation of responsibilities

\- Independent business logic

\- Replaceable infrastructure

\- Easier testing

\- Better scalability

\- Long-term maintainability

Our LangGraph platform will follow these principles throughout its implementation.

From this point forward, every component we build—configuration, logging, clients, services, graph, nodes, API, and deployment—will follow the architecture defined in this lesson.