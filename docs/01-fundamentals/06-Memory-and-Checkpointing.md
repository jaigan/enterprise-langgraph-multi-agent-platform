# [06-Memory-and-Checkpointing.md](http://06-Memory-and-Checkpointing.md)

# Understanding Memory and Checkpointing in LangGraph

## Introduction

One of the biggest challenges in AI applications is maintaining context across interactions and recovering from failures.

Imagine an AI assistant helping you over several days.

It should remember:

- Previous conversations

- User preferences

- Incomplete tasks

- Workflow progress

This is where **Memory** and **Checkpointing** become essential.

Although they are related, they solve different problems.

---

# State vs Memory

This is the most important distinction.

| State | Memory |
| --- | --- |
| Exists during one workflow execution | Exists across multiple workflow executions |
| Temporary | Persistent |
| Shared between nodes | Shared between sessions or conversations |
| Reset when the workflow finishes | Available when a new workflow starts |
| Stores current execution data | Stores historical information |

Think of it like this:

**State = RAM**

- Temporary

- Fast

- Lost when the process ends

**Memory = Hard Disk**

- Persistent

- Survives restarts

- Used in future sessions

---

# Example

User asks:

"Explain Kubernetes."

State stores:

```text
Question
Answer
Current execution status
```

After the workflow completes, the State is gone.

Later, the user asks:

"Continue from yesterday."

How does the AI know what happened yesterday?

Memory.

---

# Platform Engineering Analogy

Think about Kubernetes.

A Pod stores temporary files inside its container.

If the Pod restarts:

Everything disappears.

To preserve data, you use a Persistent Volume (PV).

LangGraph follows a similar model.

State = Container filesystem

Memory = Persistent Volume

---

# What is Memory?

Memory stores information that should survive beyond one execution.

Examples:

- User preferences

- Chat history

- Past conversations

- Frequently used tools

- Previous plans

- Long-running project details

Memory enables continuity across sessions.

---

# Types of Memory

## 1. Short-Term Memory

Used within a conversation or a limited context.

Example:

User:

"My name is Jaiganesh."

Later:

"What's my name?"

The AI answers correctly because it remembers the current conversation.

---

## 2. Long-Term Memory

Persists across multiple sessions.

Example:

Today:

"My preferred cloud provider is AWS."

Tomorrow:

"Generate Terraform."

The AI already knows to generate AWS resources.

Long-term memory requires persistent storage.

---

# What is Checkpointing?

Checkpointing is the ability to save workflow progress at specific stages.

If something fails, the workflow resumes from the latest checkpoint instead of starting over.

---

# Why Checkpointing Matters

Imagine a workflow:

Research

↓

Planning

↓

Coding

↓

Review

↓

Deploy

If deployment fails after 20 minutes, you don't want to repeat research, planning, and coding.

Instead:

Resume from the deployment step.

This saves time and cost.

---

# Checkpoint Flow

Workflow Starts

↓

Checkpoint #1

↓

Research

↓

Checkpoint #2

↓

Planning

↓

Checkpoint #3

↓

Coding

↓

Checkpoint #4

↓

Review

↓

Checkpoint #5

↓

Deploy

↓

Completed

If a failure occurs after Checkpoint #4:

Resume from Checkpoint #4.

---

# Benefits of Checkpointing

✔ Faster recovery

✔ Lower LLM costs

✔ Better user experience

✔ Supports long-running workflows

✔ Prevents repeated work

---

# Human-in-the-Loop

Sometimes AI should wait for human approval.

Example:

Research

↓

Generate Deployment

↓

WAIT

↓

Engineer Approves

↓

Continue Deployment

Checkpointing allows the workflow to pause safely and resume later.

---

# Where Can Memory Be Stored?

Production systems typically use external storage.

Examples:

- Redis (fast session storage)

- PostgreSQL (persistent metadata)

- MongoDB (document storage)

- Object Storage (large artifacts)

- Cloud databases

The choice depends on performance, durability, and access patterns.

---

# Production Example

AI Incident Response Platform

User reports an incident.

Workflow:

Collect Logs

↓

Analyze Metrics

↓

Identify Root Cause

↓

WAIT for SRE Approval

↓

Deploy Fix

↓

Notify Teams

If the system restarts after approval, checkpointing allows it to continue from the approval stage instead of starting over.

---

# Best Practices

✔ Keep State small.

✔ Store only workflow data in State.

✔ Store reusable knowledge in Memory.

✔ Use checkpointing for long-running workflows.

✔ Encrypt sensitive Memory data.

✔ Define expiration policies where appropriate.

✔ Avoid storing secrets in Memory.

---

# Common Mistakes

❌ Using Memory instead of State for temporary values.

❌ Storing large files in Memory.

❌ Forgetting to checkpoint long-running workflows.

❌ Assuming State survives application restarts.

❌ Mixing workflow execution data with user profile information.

---

# Interview Questions

## What is the difference between State and Memory?

State stores information required for the current workflow execution.

Memory stores information that persists across multiple workflow executions or user sessions.

---

## Why is checkpointing important?

Checkpointing allows workflows to resume from the last saved point instead of restarting from the beginning after a failure or interruption.

---

## Can State replace Memory?

No.

State is temporary and exists only for the current execution.

Memory is persistent and survives beyond the workflow.

---

## Can Memory replace State?

No.

State manages the live execution context.

Memory stores historical or reusable information.

Both have different responsibilities.

---

## When would you use checkpointing?

- Long-running AI workflows

- Human approval steps

- Expensive LLM calls

- Multi-agent systems

- Batch processing

- Incident response automation

---

# Summary

State

✔ Temporary

✔ Execution context

✔ Shared between nodes

✔ Reset after execution

Memory

✔ Persistent

✔ Shared across sessions

✔ Stores historical knowledge

Checkpointing

✔ Saves workflow progress

✔ Enables recovery

✔ Supports pause and resume

---

# Key Takeaways

✔ State manages the current execution.

✔ Memory preserves knowledge across executions.

✔ Checkpointing preserves workflow progress.

✔ Use State for workflow data.

✔ Use Memory for long-term context.

✔ Use Checkpointing to build resilient production AI systems.

Together, these three concepts make LangGraph suitable for enterprise-grade, long-running, fault-tolerant AI workflows.