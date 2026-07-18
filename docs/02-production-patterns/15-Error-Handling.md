\# Lesson 15 - Error Handling & Exception Management

&gt; Repository: `enterprise-langgraph-multi-agent-platform`

\---

\# Learning Objectives

By the end of this lesson, you should understand:

\## Beginner

\- What is an exception?

\- Why applications fail

\- Basic error handling concepts

\## Intermediate

\- Exception propagation

\- Custom exceptions

\- Retry mechanisms

\- Error categorization

\## Advanced

\- Circuit Breaker Pattern

\- Fallback strategies

\- Fail Fast principle

\- Graceful degradation

\## Production

\- AI application error handling

\- Distributed system failures

\- Incident response

\- Observability integration

\- Recovery strategies

\---

\# Why Error Handling Exists

Every production application will fail at some point.

The question is **not whether failures happen**.

The question is:

&gt; How does your application respond when failures happen?

Good software anticipates failures and handles them gracefully.

\---

\# Business Problem

Without proper error handling:

\- Users receive generic "Internal Server Error"

\- AI responses fail unexpectedly

\- Incidents take longer to resolve

\- Customers lose trust

\- Downtime increases

\---

\# Technical Problem

Applications interact with:

\- APIs

\- Databases

\- LLM Providers

\- Vector Databases

\- Redis

\- Kubernetes

\- Networks

Every dependency can fail.

\---

\# Common Failure Types

\## Application Errors

\- Invalid input

\- Null values

\- Invalid state

\- Missing configuration

\---

\## Infrastructure Errors

\- Network timeout

\- DNS failure

\- Database unavailable

\- Kubernetes node failure

\---

\## AI Platform Errors

\- LLM timeout

\- Rate limiting

\- Token limit exceeded

\- Invalid prompt

\- Provider unavailable

\- Invalid API key

\---

\# Error Flow

\`\`\`

User Request

      ↓

FastAPI

      ↓

Graph

      ↓

Node

      ↓

LLM

      ↓

Exception

      ↓

Error Handler

      ↓

Log Error

      ↓

Return Safe Response

\`\`\`

Never expose raw exceptions to users.

\---

\# Exception Categories

\## Validation Errors

User submitted invalid data.

Example:

\- Missing prompt

\- Invalid request format

Return:

HTTP 400

\---

\## Authentication Errors

Examples:

\- Invalid API Key

\- Expired Token

Return:

HTTP 401

\---

\## Authorization Errors

Examples:

\- Access denied

\- Missing permissions

Return:

HTTP 403

\---

\## Resource Errors

Examples:

\- Document not found

\- Session not found

Return:

HTTP 404

\---

\## External Service Errors

Examples:

\- OpenAI unavailable

\- PostgreSQL down

\- Redis unavailable

Return:

HTTP 503

\---

\## Internal Errors

Unexpected failures.

Return:

HTTP 500

\---

\# Exception Hierarchy

\`\`\`

ApplicationException

        │

        ├── ValidationException

        ├── AuthenticationException

        ├── AuthorizationException

        ├── LLMException

        ├── DatabaseException

        ├── VectorDBException

        └── ConfigurationException

\`\`\`

Using custom exceptions makes error handling more organized.

\---

\# Fail Fast Principle

Detect problems as early as possible.

Example:

Application Startup

↓

Missing API Key

↓

Stop Startup

Better to fail immediately than fail during production traffic.

\---

\# Retry Pattern

Some failures are temporary.

Examples:

\- Network timeout

\- LLM timeout

\- Rate limit

\- Temporary service outage

Retry can solve these issues.

\---

\# When NOT to Retry

Never retry:

\- Invalid API Key

\- Authentication failure

\- Validation errors

\- Bad Request

Retries waste resources.

\---

\# Exponential Backoff

Instead of:

\`\`\`

Retry

Retry

Retry

\`\`\`

Use:

\`\`\`

1 second

↓

2 seconds

↓

4 seconds

↓

8 seconds

\`\`\`

This reduces pressure on external services.

\---

\# Circuit Breaker Pattern

Suppose OpenAI is unavailable.

Without Circuit Breaker:

\`\`\`

Every request

↓

OpenAI

↓

Fails

↓

Retry

↓

Fails

↓

Retry

↓

Fails

\`\`\`

Application becomes slower.

With Circuit Breaker:

\`\`\`

Failure threshold reached

↓

Circuit Opens

↓

Stop calling OpenAI

↓

Return fallback

↓

Recover later

\`\`\`

This protects your system.

\---

\# Fallback Strategy

If primary LLM fails:

\`\`\`

GPT-4

↓

Unavailable

↓

Fallback

↓

Claude

↓

Fallback

↓

Gemini

↓

Fallback

↓

Cached Response

\`\`\`

Graceful degradation improves availability.

\---

\# Error Logging

Every exception should include:

\- Timestamp

\- Request ID

\- User ID (if available)

\- Graph Name

\- Node Name

\- Exception Type

\- Stack Trace

\- LLM Provider

\- Model Name

Never log sensitive data.

\---

\# User-Friendly Errors

Bad:

\`\`\`

KeyError: 'prompt'

\`\`\`

Good:

\`\`\`

The request is missing the required 'prompt' field.

\`\`\`

Users should receive understandable messages.

\---

\# AI Platform Example

LLM returns:

\`\`\`

429 Too Many Requests

\`\`\`

Recommended flow:

\`\`\`

Retry

↓

Exponential Backoff

↓

Still failing

↓

Fallback Provider

↓

Still failing

↓

Return Friendly Error

↓

Log Incident

\`\`\`

\---

\# Error Handling Architecture

\`\`\`

FastAPI

      ↓

Exception Middleware

      ↓

Application Exceptions

      ↓

Structured Logger

      ↓

Monitoring

      ↓

Alerting

\`\`\`

\---

\# Observability Integration

Errors should generate:

\- Logs

\- Metrics

\- Traces

\- Alerts

Example:

\`\`\`

LLM Failure

↓

Error Log

↓

Prometheus Metric

↓

OpenTelemetry Trace

↓

PagerDuty Alert

\`\`\`

\---

\# Common Mistakes

❌ Using bare `except`

❌ Swallowing exceptions silently

❌ Returning raw stack traces

❌ Logging secrets

❌ Retrying every error

❌ No custom exception hierarchy

❌ No monitoring

\---

\# Production Best Practices

\- Create custom exceptions.

\- Fail fast during startup.

\- Retry only transient failures.

\- Use exponential backoff.

\- Implement circuit breakers.

\- Log every unexpected exception.

\- Return meaningful error messages.

\- Integrate with monitoring systems.

\- Alert on critical failures.

\---

\# Interview Questions

\## Why shouldn't we catch every exception?

Catching every exception hides problems, makes debugging difficult, and may mask critical failures.

\---

\## What is the Fail Fast principle?

Detect configuration or application issues as early as possible and stop execution before serving requests.

\---

\## What is a Circuit Breaker?

A resilience pattern that temporarily stops calling an unhealthy external service after repeated failures.

\---

\## Why use custom exceptions?

They improve readability, consistency, and allow different error types to be handled appropriately.

\---

\## When should retries be used?

Only for transient failures such as timeouts, temporary network issues, or rate limiting.

\---

\# Homework

Answer the following:

1\. Why is retrying an authentication error a bad idea?

2\. What is the difference between retry and fallback?

3\. Why are custom exceptions useful?

4\. What information should every production error log contain?

5\. How does a Circuit Breaker improve system reliability?

\---

\# Summary

Error handling is a core part of production engineering.

A robust error handling strategy should:

\- Detect failures early

\- Categorize exceptions

\- Retry only when appropriate

\- Protect downstream services

\- Provide meaningful error messages

\- Generate logs, metrics, and traces

\- Improve reliability and user experience

Reliable AI systems are not those that never fail—they are systems that fail predictably, recover gracefully, and provide operators with enough information to diagnose and resolve issues quickly.