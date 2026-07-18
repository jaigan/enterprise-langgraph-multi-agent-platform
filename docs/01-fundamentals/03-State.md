# Understanding State in LangGraph

## Introduction

State is the heart of every LangGraph application.

Without State, each node would execute independently without knowing what happened before.

State acts as the shared source of truth for the entire workflow.

Think of it as a central object that every node can read and update.

---

# Why Do We Need State?

Imagine a software development team.

Developer writes code.

↓

Tester tests the code.

↓

DevOps deploys the code.

How does the Tester know which code to test?

How does DevOps know which version to deploy?

Because information is shared between them.

LangGraph solves the same problem using State.

Instead of passing variables manually between nodes, every node reads and updates the same State object.

---

# Platform Engineering Analogy

Think about Terraform.

Terraform stores infrastructure information in a state file.

Example

terraform.tfstate

It remembers:

- EC2 IDs

- VPC IDs

- Security Groups

- Route Tables

Without the state file, Terraform wouldn't know what infrastructure already exists.

LangGraph works similarly.

Instead of infrastructure resources, it stores workflow data.

Example:

- User question

- LLM response

- Search results

- Generated code

- Review comments

---

# State Flow

User

↓

State Created

↓

Research Agent

↓

State Updated

↓

Planning Agent

↓

State Updated

↓

Coding Agent

↓

State Updated

↓

Reviewer

↓

Final State Returned

Notice that every node modifies the same State object.

---

# Example State

```python
state = {
    "question": "Create a FastAPI application",
    "research": "",
    "plan": "",
    "code": "",
    "review": "",
    "status": "STARTED"
}
```

Initially, only the question is available.

As each node executes, the State grows.

---

# State After Research Agent

```python
state = {
    "question": "Create a FastAPI application",
    "research": "FastAPI is a modern Python framework...",
    "plan": "",
    "code": "",
    "review": "",
    "status": "RESEARCH_COMPLETED"
}
```

---

# State After Planner

```python
state = {
    "question": "Create a FastAPI application",
    "research": "...",
    "plan": "1. Create API\n2. Add Docker\n3. Deploy",
    "code": "",
    "review": "",
    "status": "PLAN_COMPLETED"
}
```

---

# State After Coding Agent

```python
state = {
    "question": "...",
    "research": "...",
    "plan": "...",
    "code": "from fastapi import FastAPI...",
    "review": "",
    "status": "CODE_COMPLETED"
}
```

---

# State After Reviewer

```python
state = {
    "question": "...",
    "research": "...",
    "plan": "...",
    "code": "...",
    "review": "Looks good.",
    "status": "COMPLETED"
}
```

The graph returns the final State.

---

# State Lifecycle

Every workflow follows the same lifecycle.

Create State

↓

Read State

↓

Modify State

↓

Pass State

↓

Repeat

↓

Return Final State

Every node follows this process.

---

# Why State Is Better Than Passing Variables

Imagine writing Python without State.

```python
research = research_agent(question)

plan = planner(question, research)

code = coder(question, research, plan)

review = reviewer(question, research, plan, code)
```

As the application grows, function arguments become difficult to manage.

State simplifies this.

Every function receives the same object.

---

# State Schema

Production applications define a schema for State.

Example:

```python
class AgentState(TypedDict):
    question: str
    research: str
    plan: str
    code: str
    review: str
    status: str
```

Advantages:

- Type safety

- Validation

- Better IDE support

- Easier maintenance

---

# Mutable vs Immutable State

Bad Practice:

Node modifies random values without validation.

Good Practice:

Each node updates only the fields it owns.

Example:

Research Agent

Updates:

✔ research

✔ status

Does NOT modify:

✘ code

✘ review

This makes workflows predictable and easier to debug.

---

# Production Best Practices

✔ Keep State small.

✔ Store only required information.

✔ Avoid storing large files directly in State.

✔ Store references (URLs, IDs) instead of large documents.

✔ Define a strict schema.

✔ Update only owned fields.

✔ Validate State after each node.

✔ Log State changes.

---

# Common Mistakes

❌ Store everything in State.

❌ Store binary files.

❌ Allow every node to modify every field.

❌ Use inconsistent field names.

❌ Forget validation.

❌ Keep sensitive secrets inside State.

---

# Real Production Example

Incident Management AI

State

```text
alert_id

cluster_name

namespace

pod_name

logs

metrics

root_cause

recommendation

ticket_id

status
```

Flow

Dynatrace Alert

↓

Research Agent

↓

Kubernetes Agent

↓

AWS Agent

↓

Root Cause Agent

↓

ServiceNow Agent

↓

Completed

Every agent reads and updates the same State object.

---

# Interview Questions

### What is State?

State is the shared data object that flows through every node in a LangGraph workflow.

---

### Why is State required?

It enables nodes to share context without manually passing variables between functions.

---

### Why not use global variables?

Global variables are difficult to manage, unsafe for concurrent execution, and make workflows harder to maintain. State provides a structured and explicit approach.

---

### What should you store in State?

Store only workflow-related information, metadata, identifiers, intermediate results, and references.

Avoid storing secrets, large binary data, or unnecessary information.

---

# Key Takeaways

✔ State is the central source of truth.

✔ Every node reads from State.

✔ Every node updates State.

✔ State evolves as the workflow progresses.

✔ Define a schema for State.

✔ Keep State small and structured.

✔ Validate updates.

✔ Think of State like Terraform's state file—but for AI workflows instead of infrastructure.