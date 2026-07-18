\# Lesson 14 - Dependency Injection (DI)

&gt; Repository: `enterprise-langgraph-multi-agent-platform`

\---

\# Learning Objectives

By the end of this lesson, you should understand:

\## Beginner

\- What Dependency Injection (DI) is

\- Why applications use DI

\- Difference between creating and injecting objects

\## Intermediate

\- Tight coupling vs Loose coupling

\- Constructor Injection

\- Factory Pattern

\- Service Layer

\## Advanced

\- Dependency Injection Containers

\- Dependency Graph

\- Object Lifecycle

\- Interface-based Design

\## Production

\- Testability

\- Mocking

\- Swappable implementations

\- Cloud portability

\- AI Provider abstraction

\---

\# Why Dependency Injection Exists

Imagine you write a LangGraph node:

\`\`\`python

llm = ChatOpenAI(...)

\`\`\`

inside every node.

It works.

But what happens if tomorrow you need to switch from:

\- OpenAI

\- Anthropic

\- Azure OpenAI

\- Bedrock

\- Gemini

\- Local vLLM

Would you edit every node?

No.

Dependency Injection solves this problem.

\---

\# Business Problem

Without Dependency Injection:

\- Every module creates its own dependencies.

\- Difficult to change providers.

\- Difficult to test.

\- High maintenance cost.

\- Code duplication.

\---

\# Technical Problem

When one class creates another class directly, they become tightly coupled.

Example:

\`\`\`

LLM Node

↓

Creates ChatOpenAI()

↓

Uses ChatOpenAI()

\`\`\`

Now the node only works with OpenAI.

\---

\# Tight Coupling

\`\`\`

LLM Node

      │

      ▼

ChatOpenAI

\`\`\`

Changing the LLM provider requires modifying the node.

\---

\# Loose Coupling

\`\`\`

LLM Node

      │

      ▼

LLM Service

      │

      ▼

LLM Client

      │

      ▼

OpenAI / Anthropic / Gemini

\`\`\`

The node doesn't know which provider is being used.

\---

\# What is Dependency Injection?

Instead of creating an object...

\`\`\`

Create It Yourself

\`\`\`

someone else creates it and gives it to you.

Think of it like electricity.

Your laptop doesn't generate electricity.

It simply receives it.

Your application should receive dependencies instead of creating them.

\---

\# Real World Example

Restaurant

Chef

↓

Needs ingredients

The chef doesn't grow vegetables.

Someone supplies them.

Dependency Injection follows the same principle.

\---

\# LangGraph Example

Bad

\`\`\`

LLM Node

↓

ChatOpenAI()

\`\`\`

Good

\`\`\`

LLM Node

↓

LLM Service

↓

LLM Client

↓

Provider

\`\`\`

\---

\# Constructor Injection

The most common DI pattern.

\`\`\`

class LLMService:

↓

Receives

↓

LLM Client

\`\`\`

Instead of creating it internally.

\---

\# Service Layer

Our architecture will use:

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

Provider

\`\`\`

Each layer has one responsibility.

\---

\# Why Service Layer?

Service layer handles:

\- Business logic

\- Validation

\- Retry logic

\- Provider selection

\- Metrics

\- Logging

Nodes remain simple.

\---

\# Why Client Layer?

Client layer handles:

\- SDK interaction

\- Authentication

\- API calls

\- Timeouts

\- Retries

Nothing else.

\---

\# Future Flexibility

Today

\`\`\`

OpenAI

\`\`\`

Tomorrow

\`\`\`

Anthropic

\`\`\`

Next Month

\`\`\`

Azure OpenAI

\`\`\`

Next Year

\`\`\`

Self-hosted vLLM

\`\`\`

No node changes required.

\---

\# Testing Benefits

Without DI

\`\`\`

Real OpenAI API

↓

Unit Test

\`\`\`

Bad.

Slow.

Costs money.

\---

With DI

\`\`\`

Mock Client

↓

Unit Test

\`\`\`

Fast.

Free.

Reliable.

\---

\# Object Lifecycle

Some objects should exist once.

Examples

\- Configuration

\- Logger

\- Database Connection

Singleton

\---

Some should be created every request.

Examples

\- Request Context

\- Graph State

Transient

\---

\# Dependency Graph

\`\`\`

Settings

      │

      ▼

Logger

      │

      ▼

LLM Client

      │

      ▼

LLM Service

      │

      ▼

Node

      │

      ▼

Graph

\`\`\`

Every dependency is created once and shared where appropriate.

\---

\# SOLID Principle

Dependency Inversion Principle

High-level modules should not depend on low-level modules.

Both should depend on abstractions.

Example

Node

↓

LLM Service

↓

LLM Interface

↓

OpenAI Client

Instead of directly depending on ChatOpenAI.

\---

\# Design Patterns

Dependency Injection commonly works with:

\- Factory Pattern

\- Singleton Pattern

\- Strategy Pattern

\- Adapter Pattern

These patterns help swap implementations without changing business logic.

\---

\# AI Platform Example

Suppose your company wants:

OpenAI

↓

Anthropic

↓

Gemini

↓

Bedrock

↓

vLLM

With DI only the client changes.

Everything else continues working.

\---

\# Common Mistakes

❌ Creating ChatOpenAI inside every node

❌ Business logic inside the client

❌ Multiple configuration objects

❌ Global mutable objects

❌ Mixing responsibilities

❌ Direct SDK calls throughout the application

\---

\# Production Best Practices

\- Inject dependencies instead of creating them.

\- Separate Client and Service layers.

\- Keep nodes lightweight.

\- Depend on abstractions, not implementations.

\- Create reusable services.

\- Use interfaces where appropriate.

\- Keep object lifecycles well defined.

\---

\# Interview Questions

\## What problem does Dependency Injection solve?

It reduces coupling, improves maintainability, enables testing, and allows implementations to be replaced without changing business logic.

\---

\## What is Tight Coupling?

When one component directly depends on another concrete implementation, making changes difficult.

\---

\## What is Loose Coupling?

Components interact through abstractions, allowing implementations to change independently.

\---

\## Why separate Client and Service?

The Client communicates with external systems.

The Service contains business logic.

This separation improves maintainability and testability.

\---

\## Why is Dependency Injection useful in AI applications?

It allows switching between LLM providers, simplifies testing with mock clients, and keeps business logic independent of provider-specific SDKs.

\---

\# Homework

Answer the following:

1\. Why shouldn't a LangGraph node create `ChatOpenAI()` directly?

2\. What is the difference between a Client and a Service?

3\. What is the Dependency Inversion Principle?

4\. How does Dependency Injection improve testing?

5\. Which objects should be Singletons?

\---

\# Summary

Dependency Injection is a foundational principle of enterprise software.

It enables:

\- Loose coupling

\- Better testing

\- Easier maintenance

\- Swappable implementations

\- Cleaner architecture

\- Production-ready AI systems

Nearly every modern framework—including FastAPI, Spring Boot, [ASP.NET](http://ASP.NET) Core, and NestJS—relies on Dependency Injection because it scales well as applications grow.