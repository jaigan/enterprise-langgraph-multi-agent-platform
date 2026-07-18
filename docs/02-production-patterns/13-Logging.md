\# Lesson 13 - Logging

&gt; Repository: `enterprise-langgraph-multi-agent-platform`

\---

\# Learning Objectives

By the end of this lesson, you should understand:

\## Beginner

\- What is logging?

\- Why logging is important

\- Difference between logging and print()

\## Intermediate

\- Log levels

\- Structured logging

\- Log formatting

\- Logging best practices

\## Advanced

\- Correlation IDs

\- Request IDs

\- Distributed logging

\- Centralized logging

\- Log aggregation

\## Production

\- OpenTelemetry

\- JSON logging

\- Cloud logging

\- Log retention

\- Security logging

\- Audit logging

\- AI application logging

\---

\# Why Logging Exists

Imagine your AI application receives thousands of requests every minute.

A user reports:

&gt; "The AI returned an incorrect answer."

How do you investigate?

Without logs...

You don't know:

\- Which user made the request

\- Which model was used

\- Which prompt was sent

\- How long the request took

\- Whether the LLM timed out

\- Which node failed

Logging provides visibility into your application's behavior.

\---

\# Business Problem

Without logging:

\- Difficult troubleshooting

\- Slow incident response

\- Poor customer support

\- No audit trail

\- Difficult production monitoring

\---

\# Technical Problem

Without logs:

\- No visibility

\- No debugging information

\- No performance analysis

\- No root cause analysis

\- No operational insights

\---

\# Logging vs print()

\## print()

\`\`\`python

print("Calling OpenAI")

\`\`\`

Problems:

\- No timestamp

\- No log level

\- No request tracking

\- No filtering

\- No central collection

\- Not suitable for production

\---

\## Logging

\`\`\`text

2026-07-18 10:00:12 INFO

LLM request started

RequestID=abc123

\`\`\`

Provides:

\- Timestamp

\- Severity

\- Context

\- Traceability

\- Structured output

\---

\# Log Levels

\## DEBUG

Detailed developer information.

Example:

\- Prompt generated

\- State transitions

\- Token counts

Production:

Usually disabled.

\---

\## INFO

Normal application events.

Examples:

\- Request started

\- Graph executed

\- Response returned

Production:

Always enabled.

\---

\## WARNING

Unexpected situations.

Examples:

\- Retry occurred

\- Slow response

\- Missing optional configuration

\---

\## ERROR

Operation failed.

Examples:

\- LLM timeout

\- Database unavailable

\- Invalid request

Application continues running.

\---

\## CRITICAL

Application cannot continue.

Examples:

\- Configuration missing

\- Startup failure

\- Database unavailable during startup

Application may terminate.

\---

\# Logging Flow

\`\`\`

User Request

      ↓

API

      ↓

Request Logger

      ↓

Graph

      ↓

Node

      ↓

LLM

      ↓

Response Logger

      ↓

User

\`\`\`

Every major step should produce meaningful logs.

\---

\# What Should Be Logged?

\## Application Startup

\- Version

\- Environment

\- Model

\- Configuration summary

\---

\## Request

\- Request ID

\- User ID (if available)

\- Endpoint

\- Start time

\---

\## LLM

\- Model

\- Provider

\- Tokens

\- Latency

\- Success/Failure

\---

\## Graph

\- Graph started

\- Node execution

\- Routing decision

\- Completion

\---

\## Errors

\- Error type

\- Stack trace

\- Request ID

\- Node

\- Timestamp

\---

\# What Should NOT Be Logged?

Never log:

\- API Keys

\- Passwords

\- JWT Tokens

\- Secrets

\- Private customer data

\- Sensitive prompts containing confidential information

Logs often end up in centralized systems.

Treat them as sensitive.

\---

\# Structured Logging

Bad

\`\`\`

Calling OpenAI...

\`\`\`

Good

\`\`\`json

{

  "timestamp":"2026-07-18T10:00:00Z",

  "level":"INFO",

  "request_id":"abc123",

  "graph":"customer-support",

  "node":"planner",

  "duration_ms":150

}

\`\`\`

Structured logs are machine-readable.

\---

\# Request ID

Every request should have:

\`\`\`

RequestID

↓

API

↓

Graph

↓

Node

↓

LLM

↓

Database

↓

Response

\`\`\`

One ID follows the request through the entire system.

\---

\# Correlation ID

Request ID

Tracks one request.

Correlation ID

Tracks multiple related requests across multiple services.

Useful for microservices.

\---

\# AI Application Logging

For every LLM request log:

\- Provider

\- Model

\- Tokens

\- Latency

\- Cost

\- Retry count

\- Cache hit

\- Success

Avoid logging raw prompts if they contain sensitive information.

\---

\# Centralized Logging

Production applications send logs to systems such as:

\- ELK Stack

\- Grafana Loki

\- Splunk

\- Datadog

\- AWS CloudWatch

\- Azure Monitor

\- Google Cloud Logging

Developers should never SSH into servers to read log files.

\---

\# OpenTelemetry

Modern AI platforms use OpenTelemetry.

It collects:

\- Logs

\- Metrics

\- Traces

This provides end-to-end observability.

\---

\# Log Retention

Typical production policies:

Development

\- 7 Days

Staging

\- 14 Days

Production

\- 30–365 Days

Depending on compliance requirements.

\---

\# Security Logging

Important security events include:

\- Login attempts

\- Authentication failures

\- Authorization failures

\- Secret access

\- Configuration changes

\- Administrative actions

\---

\# Audit Logging

Audit logs answer:

Who?

Did what?

When?

From where?

These are essential for compliance and investigations.

\---

\# Logging Architecture

\`\`\`

Application

      ↓

Python Logger

      ↓

Structured JSON

      ↓

OpenTelemetry

      ↓

Log Collector

      ↓

Grafana / Kibana / Splunk

\`\`\`

\---

\# Common Mistakes

❌ Using print()

❌ Logging secrets

❌ No request IDs

❌ No timestamps

❌ Logging everything at ERROR

❌ Huge log files

❌ Inconsistent formats

❌ No structured logging

\---

\# Production Best Practices

\- Use structured logging.

\- Generate a Request ID for every request.

\- Use correlation IDs across services.

\- Log meaningful events.

\- Never log secrets.

\- Centralize logs.

\- Define retention policies.

\- Monitor logs continuously.

\---

\# Interview Questions

\## Why is logging important?

Logging provides operational visibility, simplifies debugging, supports monitoring, and helps investigate incidents.

\---

\## Why shouldn't we use print()?

print() lacks severity levels, timestamps, structured output, filtering, and integration with centralized logging systems.

\---

\## What is structured logging?

Structured logging records logs in a machine-readable format (typically JSON) to support searching, filtering, and analytics.

\---

\## What is a Request ID?

A unique identifier that tracks a single request through the application.

\---

\## What is a Correlation ID?

An identifier used to link related requests across multiple services in a distributed system.

\---

\## Why shouldn't secrets be logged?

Logs are often stored centrally and accessed by multiple systems. Logging secrets increases the risk of credential exposure.

\---

\# Homework

Answer the following:

1\. Why is structured logging better than plain text?

2\. What is the difference between Request ID and Correlation ID?

3\. What information should every LLM request log contain?

4\. What should never be logged?

5\. Why do production systems use centralized logging?

\---

\# Summary

Logging is one of the most important aspects of production software.

A strong logging strategy enables:

\- Faster debugging

\- Better monitoring

\- Incident investigation

\- Performance analysis

\- Security auditing

\- AI observability

For AI Platform Engineers, logging is not optional—it is a core operational capability.