\# Lesson 18 - Design Patterns

&gt; Repository: `enterprise-langgraph-multi-agent-platform`

\---

\# Learning Objectives

By the end of this lesson, you should understand:

\## Beginner

\- What is a Design Pattern?

\- Why Design Patterns exist

\- When to use them

\- When NOT to use them

\## Intermediate

\- Creational Patterns

\- Structural Patterns

\- Behavioral Patterns

\## Advanced

\- Applying Design Patterns in AI Platforms

\- Combining multiple patterns

\- Pattern trade-offs

\## Production

\- Enterprise software architecture

\- AI Platform architecture

\- LangGraph architecture

\- Cloud-native design

\---

\# What is a Design Pattern?

A Design Pattern is a **proven reusable solution** to a commonly occurring software design problem.

It is **not code**.

It is a way of thinking.

Think of it as an architectural blueprint.

\---

\# Why Design Patterns Exist

Imagine every developer solved the same problem differently.

The result would be:

\- Inconsistent code

\- Difficult maintenance

\- Poor scalability

Design Patterns provide standardized solutions that engineers can recognize and understand.

\---

\# Categories of Design Patterns

\`\`\`

Design Patterns

├── Creational

│

├── Structural

│

└── Behavioral

\`\`\`

\---

\# 1. Creational Patterns

Responsible for creating objects.

Examples:

\- Singleton

\- Factory

\- Builder

\---

\# Singleton Pattern

\## Purpose

Ensure only one instance of an object exists.

\---

\## Examples in Our Repository

\`\`\`

Settings

Logger

Configuration

OpenTelemetry Provider

\`\`\`

Only one instance should exist.

\---

\## Why?

Having multiple configuration objects can lead to inconsistent application behavior.

\---

\## When to Use

\- Configuration

\- Logger

\- Database Connection Pool

\- Metrics Provider

\---

\## When NOT to Use

Objects that store request-specific data.

\---

\# Factory Pattern

\## Purpose

Create objects without exposing creation logic.

\---

Instead of

\`\`\`

ChatOpenAI()

\`\`\`

everywhere,

use

\`\`\`

LLMFactory

↓

OpenAI

Claude

Gemini

vLLM

\`\`\`

\---

\## Why?

Changing providers should not require changing business logic.

\---

\# Builder Pattern

\## Purpose

Construct complex objects step by step.

\---

Example

Building a LangGraph.

\`\`\`

Create Graph

↓

Add State

↓

Add Nodes

↓

Add Edges

↓

Compile

\`\`\`

This is exactly what `StateGraph` does.

\---

\# 2. Structural Patterns

Responsible for organizing objects.

Examples:

\- Adapter

\- Facade

\- Proxy

\- Decorator

\---

\# Adapter Pattern

\## Purpose

Make incompatible interfaces work together.

\---

Example

\`\`\`

OpenAI SDK

↓

Adapter

↓

Common Interface

\`\`\`

\`\`\`

Anthropic SDK

↓

Adapter

↓

Common Interface

\`\`\`

Your application interacts with one interface regardless of the provider.

\---

\# Facade Pattern

\## Purpose

Hide complexity behind a simpler interface.

\---

Example

\`\`\`

LLMService

↓

Prompt Builder

↓

Client

↓

Retry Logic

↓

Logging

↓

Metrics

↓

Return Response

\`\`\`

The caller only interacts with `LLMService`.

\---

\# Proxy Pattern

\## Purpose

Control access to another object.

\---

Examples

\- Authentication

\- Rate Limiting

\- Caching

\- Logging

\---

\# Decorator Pattern

\## Purpose

Add functionality without modifying the original object.

\---

Example

\`\`\`

LLM Call

↓

Logging

↓

Retry

↓

Metrics

↓

Tracing

\`\`\`

Each concern wraps the original behavior.

\---

\# 3. Behavioral Patterns

Responsible for communication between objects.

Examples:

\- Strategy

\- Observer

\- Command

\- Chain of Responsibility

\---

\# Strategy Pattern

\## Purpose

Choose behavior at runtime.

\---

Example

\`\`\`

Provider

↓

OpenAI

Claude

Gemini

vLLM

\`\`\`

The application selects a strategy without changing business logic.

\---

\# Observer Pattern

\## Purpose

Notify multiple components when an event occurs.

\---

Example

\`\`\`

LLM Completed

↓

Metrics

↓

Logging

↓

Tracing

↓

Audit

\`\`\`

One event triggers multiple actions.

\---

\# Command Pattern

\## Purpose

Represent an action as an object.

\---

LangGraph uses this idea when nodes execute operations and routing decisions.

Each node represents a command in the workflow.

\---

\# Chain of Responsibility

\## Purpose

Pass a request through multiple handlers.

\---

Example

\`\`\`

Authentication

↓

Authorization

↓

Validation

↓

Logging

↓

LLM

↓

Response

\`\`\`

Each handler performs one responsibility before passing control to the next.

\---

\# Repository Pattern

\## Purpose

Separate business logic from data access.

\---

Example

\`\`\`

Application

↓

Memory Repository

↓

Redis

↓

PostgreSQL

↓

Vector Database

\`\`\`

The application does not know where the data is stored.

\---

\# Dependency Injection Pattern

Already covered in Lesson 14.

Works together with Factory and Strategy patterns.

\---

\# Which Patterns Will Our Repository Use?

| Pattern | Usage |

|----------|-------|

| Singleton | Settings, Logger |

| Factory | LLM Factory |

| Builder | Graph Builder |

| Adapter | LLM Providers |

| Facade | LLM Service |

| Strategy | Provider Selection |

| Repository | Memory Storage |

| Command | Graph Nodes |

| Chain of Responsibility | Request Processing |

| Observer | Metrics & Logging |

\---

\# Design Pattern Relationships

\`\`\`

API

↓

Factory

↓

LLM Service

↓

Strategy

↓

Adapter

↓

Provider

↓

Repository

↓

Storage

\`\`\`

Patterns work together rather than in isolation.

\---

\# Pattern Selection Guidelines

Not every problem requires a Design Pattern.

Ask:

\- Does this reduce coupling?

\- Does this improve maintainability?

\- Does this simplify testing?

\- Will this scale as the application grows?

Avoid adding patterns without a clear benefit.

\---

\# Common Mistakes

❌ Using patterns everywhere

❌ Applying patterns without understanding the problem

❌ Overengineering

❌ Creating unnecessary abstraction layers

❌ Ignoring simplicity

\---

\# Production Best Practices

\- Choose the simplest pattern that solves the problem.

\- Combine patterns when appropriate.

\- Keep responsibilities clear.

\- Avoid deep inheritance.

\- Prefer composition over inheritance.

\- Document architectural decisions.

\---

\# Interview Questions

\## What is a Design Pattern?

A reusable solution to a recurring software design problem.

\---

\## Why use the Factory Pattern?

To centralize object creation and reduce coupling between object creation and business logic.

\---

\## Why use the Singleton Pattern?

To ensure only one shared instance exists for resources such as configuration or logging.

\---

\## Why use the Strategy Pattern?

To allow algorithms or behaviors to be selected at runtime without modifying existing code.

\---

\## Why use the Adapter Pattern?

To provide a common interface for different implementations or third-party libraries.

\---

\## Why avoid overusing Design Patterns?

Unnecessary patterns increase complexity, reduce readability, and make maintenance more difficult.

\---

\# Homework

Answer the following:

1\. Why is a Design Pattern not the same as code?

2\. Which pattern would you use to support multiple LLM providers?

3\. Why is Singleton suitable for configuration?

4\. How does the Adapter Pattern simplify provider integration?

5\. When would you use the Builder Pattern in a LangGraph application?

\---

\# Summary

Design Patterns are reusable architectural solutions that improve maintainability, scalability, and collaboration.

Our LangGraph platform will rely on several key patterns:

\- Singleton for shared configuration

\- Factory for object creation

\- Builder for graph construction

\- Adapter for provider abstraction

\- Facade for simplified APIs

\- Strategy for runtime provider selection

\- Repository for data access

\- Command for graph execution

\- Chain of Responsibility for request processing

\- Observer for logging and monitoring

Choosing the right pattern at the right time leads to cleaner, more flexible, and production-ready software.