\# Lesson 35 – Multi-Agent Communication

&gt; Learn how AI agents exchange information, coordinate tasks, share state, and communicate reliably in production-grade multi-agent systems.

\---

\# Learning Objectives

After completing this lesson, you will be able to:

\- Understand agent communication models.

\- Design message contracts.

\- Choose between shared state and message passing.

\- Prevent tight coupling.

\- Build scalable communication architectures.

\- Apply communication best practices in enterprise AI systems.

\---

\# Table of Contents

1\. Introduction

2\. Why Communication Matters

3\. Business Problem

4\. Technical Problem

5\. Communication Models

6\. Shared State vs Message Passing

7\. Message Contracts

8\. Internal Architecture

9\. Production Examples

10\. Mermaid Diagrams

11\. Advantages & Trade-offs

12\. Performance Considerations

13\. Common Mistakes

14\. Best Practices

15\. Kubernetes Perspective

16\. Interview Questions

17\. Summary

18\. References

\---

\# Introduction

In a multi-agent system, no agent works in isolation.

A Planner may send work to an Executor.

The Executor may request additional data from a Research Agent.

The Research Agent may return evidence to a Reviewer.

Without a well-defined communication model, the workflow becomes difficult to maintain and debug.

\---

\# Why Communication Matters

Poor communication leads to:

\- Duplicate work.

\- Lost context.

\- Inconsistent decisions.

\- Infinite loops.

\- Tight coupling.

\- Difficult debugging.

Good communication enables modularity and scalability.

\---

\# Business Problem

Imagine an AI Platform Assistant.

User asks:

&gt; Upgrade our Kubernetes cluster.

Planner sends:

\`\`\`

Upgrade cluster.

\`\`\`

Executor asks:

\`\`\`

Which cluster?

\`\`\`

Planner responds:

\`\`\`

Production.

\`\`\`

Executor asks:

\`\`\`

Which version?

\`\`\`

Planner responds:

\`\`\`

1.34.

\`\`\`

This repeated back-and-forth wastes time.

Instead, the Planner should send a complete task definition.

\---

\# Technical Problem

Bad communication:

\`\`\`

Planner

↓

Executor

↓

Planner

↓

Executor

↓

Planner

\`\`\`

Many unnecessary exchanges increase latency and token usage.

\---

\# Communication Models

\## Model 1 — Shared State

Agents communicate by reading and updating a shared workflow state.

\`\`\`

Planner

↓

Workflow State

↓

Executor

↓

Workflow State

↓

Reviewer

\`\`\`

Advantages:

\- Simple.

\- Centralized.

\- Easy to inspect.

Challenges:

\- State conflicts.

\- Version management.

\- Large state objects.

\---

\## Model 2 — Message Passing

Agents exchange explicit messages.

\`\`\`

Planner

↓

Task Message

↓

Executor

↓

Result Message

↓

Reviewer

\`\`\`

Advantages:

\- Clear ownership.

\- Loose coupling.

\- Easier distribution.

Challenges:

\- More message definitions.

\- Serialization overhead.

\---

\## Model 3 — Hybrid

Most production systems combine both.

\`\`\`

Shared State

+

Message Passing

\`\`\`

Shared state stores workflow context.

Messages communicate task-specific information.

\---

\# Shared State vs Message Passing

| Shared State | Message Passing |

|--------------|-----------------|

| Global workflow context | Explicit communication |

| Easier debugging | Better modularity |

| Simpler implementation | Better scalability |

| Risk of conflicting updates | More protocol design |

\---

\# Message Contracts

Every message should have a defined structure.

Example:

\`\`\`json

{

  "task_id": "123",

  "agent": "planner",

  "target": "executor",

  "action": "upgrade_cluster",

  "priority": "high",

  "payload": {

    "cluster": "production",

    "version": "1.34"

  }

}

\`\`\`

A consistent contract reduces ambiguity and makes logging and tracing easier.

\---

\# Internal Architecture

\`\`\`

               Planner

                  │

          Task Message

                  ▼

             Executor

                  │

         Result Message

                  ▼

             Reviewer

                  │

        Approval Message

                  ▼

              Response

\`\`\`

Each communication has a defined purpose and schema.

\---

\# Production Example 1 — Platform Automation

Planner sends:

\- Cluster name

\- Target version

\- Maintenance window

\- Rollback strategy

Executor performs the upgrade.

Reviewer validates:

\- Version

\- Health

\- Availability

\---

\# Production Example 2 — Enterprise Research

Research Planner sends:

\- Search query

\- Sources

\- Time range

\- Priority

Retriever returns:

\- Documents

\- Metadata

\- Confidence score

Summarizer generates the report.

\---

\# Production Example 3 — AI Coding Assistant

Planner:

\- Generate FastAPI project.

Executor:

\- Code

\- Tests

\- Dockerfile

Reviewer:

\- Security review

\- Quality review

\- Best practices

\---

\# Mermaid Workflow

\`\`\`mermaid

flowchart TD

A\[Planner\]

A --&gt; B\[Task Message\]

B --&gt; C\[Executor\]

C --&gt; D\[Result Message\]

D --&gt; E\[Reviewer\]

E --&gt; F\[Final Response\]

\`\`\`

\---

\# Mermaid Sequence Diagram

\`\`\`mermaid

sequenceDiagram

Planner-&gt;&gt;Executor: Task

Executor--&gt;&gt;Planner: Status

Executor-&gt;&gt;Reviewer: Result

Reviewer--&gt;&gt;Executor: Fix Needed

Executor--&gt;&gt;Reviewer: Updated Result

Reviewer--&gt;&gt;User: Final Answer

\`\`\`

\---

\# Advantages

\- Loose coupling.

\- Better observability.

\- Easier debugging.

\- Clear responsibilities.

\- Scalable architecture.

\---

\# Trade-offs

\- More design effort.

\- Message versioning.

\- Serialization overhead.

\- Contract management.

\---

\# Performance Considerations

\- Send complete task descriptions.

\- Avoid unnecessary round trips.

\- Compress large payloads when appropriate.

\- Keep messages focused on a single responsibility.

\- Use correlation IDs for tracing.

\---

\# Common Mistakes

❌ Sending incomplete messages.

❌ Allowing agents to modify unrelated state.

❌ Tight coupling between agent implementations.

❌ No message versioning.

❌ Using one message format for every use case.

\---

\# Best Practices

\- Define message schemas.

\- Include task identifiers.

\- Include timestamps.

\- Record sender and receiver.

\- Validate incoming messages.

\- Version message contracts when introducing breaking changes.

\---

\# Kubernetes Perspective

Think about Kubernetes components.

\`\`\`

Scheduler

↓

API Server

↓

Kubelet

↓

Container Runtime

\`\`\`

Each component communicates using well-defined APIs and object schemas.

They don't exchange arbitrary data.

Multi-agent systems should follow the same discipline.

\---

\# Interview Questions

\### Why are communication protocols important in multi-agent systems?

They reduce ambiguity, improve maintainability, enable interoperability, and simplify debugging and observability.

\---

\### What is the difference between shared state and message passing?

Shared state allows agents to coordinate through a common data model.

Message passing uses explicit requests and responses between agents.

Most enterprise systems use both.

\---

\### What should every message contain?

\- Task identifier

\- Sender

\- Receiver

\- Action

\- Payload

\- Metadata

\- Timestamp

\- Correlation ID (recommended)

\---

\### Why version message contracts?

To evolve agent implementations without breaking compatibility across independently deployed components.

\---

\# Summary

Effective communication is the foundation of scalable multi-agent systems.

A production-ready communication model:

\- Uses clear message contracts.

\- Separates workflow state from task messages.

\- Supports observability and tracing.

\- Enables independent evolution of agents.

\- Avoids unnecessary communication overhead.

\---

\# References

\- LangGraph Documentation

\- Enterprise Integration Patterns

\- Distributed Systems Design

\- Message-Oriented Middleware Concepts