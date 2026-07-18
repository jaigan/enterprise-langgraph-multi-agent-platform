\# Lesson 31 – Planner–Executor Pattern

&gt; Learn how AI systems separate planning, execution, and validation to build reliable, scalable, and production-ready workflows.

\---

\# Learning Objectives

After completing this lesson, you will be able to:

\- Understand the Planner–Executor Pattern.

\- Explain why planning and execution should be separated.

\- Design production AI workflows.

\- Build iterative execution pipelines.

\- Apply validation and review.

\- Understand how modern AI coding assistants work.

\---

\# Table of Contents

1\. Introduction

2\. Why the Pattern Exists

3\. Business Problem

4\. Technical Problem

5\. Architecture

6\. Components

7\. Execution Lifecycle

8\. Production Examples

9\. Mermaid Diagrams

10\. Advantages & Trade-offs

11\. Performance Considerations

12\. Common Mistakes

13\. Best Practices

14\. Kubernetes Perspective

15\. Interview Questions

16\. Summary

17\. References

\---

\# Introduction

Imagine asking:

&gt; "Build a production-ready FastAPI application with authentication."

Should one AI agent immediately start generating code?

No.

A better approach is:

1\. Understand the requirements.

2\. Create a plan.

3\. Execute the plan.

4\. Review the output.

5\. Fix any issues.

This is the Planner–Executor Pattern.

\---

\# Why the Pattern Exists

Human software teams rarely jump straight into implementation.

A typical project looks like this:

\`\`\`

Requirements

↓

Architecture

↓

Implementation

↓

Testing

↓

Review

↓

Deployment

\`\`\`

AI systems follow the same disciplined process.

\---

\# Business Problem

Suppose a user requests:

&gt; "Migrate our Kubernetes cluster from EKS 1.32 to 1.34."

A production AI system shouldn't immediately generate commands.

Instead it should:

\- Analyze the environment.

\- Identify dependencies.

\- Create a migration plan.

\- Execute each step.

\- Validate the outcome.

\---

\# Technical Problem

Single-agent workflow:

\`\`\`

Request

↓

LLM

↓

Answer

\`\`\`

Problems:

\- No planning

\- Higher error rate

\- Difficult debugging

\- No validation

\- Poor repeatability

\---

\# Architecture

\`\`\`

                 User

                   │

                   ▼

             Planner Agent

                   │

          Create Execution Plan

                   │

                   ▼

            Executor Agent

                   │

            Perform Each Task

                   │

                   ▼

            Reviewer Agent

                   │

         Validate the Result

                   │

          ┌────────┴────────┐

          │                 │

      Success            Needs Fix

          │                 │

          ▼                 ▼

      Final Output     Back to Executor

\`\`\`

\---

\# Components

\## Planner

Responsibilities:

\- Understand intent.

\- Break work into tasks.

\- Prioritize execution.

\- Identify dependencies.

Output example:

\`\`\`

Step 1:

Collect requirements.

Step 2:

Design API.

Step 3:

Generate code.

Step 4:

Create tests.

Step 5:

Deploy.

\`\`\`

\---

\## Executor

Responsibilities:

\- Perform the assigned task.

\- Call tools.

\- Generate code.

\- Query databases.

\- Execute APIs.

The Executor focuses on doing, not deciding.

\---

\## Reviewer

Responsibilities:

\- Validate correctness.

\- Check security.

\- Verify quality.

\- Detect missing requirements.

\- Request fixes if needed.

The Reviewer acts as a quality gate.

\---

\# Execution Lifecycle

\`\`\`mermaid

flowchart TD

A\[User Request\]

A --&gt; B\[Planner\]

B --&gt; C\[Execution Plan\]

C --&gt; D\[Executor\]

D --&gt; E\[Reviewer\]

E --&gt; F{Approved?}

F --&gt;|Yes| G\[Return Response\]

F --&gt;|No| D

\`\`\`

The workflow iterates until the result satisfies the review criteria.

\---

\# Production Example 1 — AI Coding Assistant

User:

&gt; "Create a REST API."

Planner:

\- Design endpoints.

\- Select framework.

\- Plan tests.

Executor:

\- Generate FastAPI code.

\- Create Dockerfile.

\- Write CI pipeline.

Reviewer:

\- Validate code quality.

\- Check security.

\- Ensure tests exist.

\---

\# Production Example 2 — Platform Engineering

Request:

&gt; "Upgrade Kubernetes cluster."

Planner:

\- Verify versions.

\- Check PDBs.

\- Validate node groups.

\- Plan rollout.

Executor:

\- Upgrade control plane.

\- Upgrade node groups.

\- Restart workloads.

Reviewer:

\- Verify cluster health.

\- Check application availability.

\- Confirm version.

\---

\# Production Example 3 — Enterprise Research

Planner:

\- Identify information sources.

Executor:

\- Search documents.

\- Query databases.

\- Read APIs.

Reviewer:

\- Verify accuracy.

\- Detect contradictions.

\- Produce summary.

\---

\# Mermaid Sequence Diagram

\`\`\`mermaid

sequenceDiagram

User-&gt;&gt;Planner: Request

Planner-&gt;&gt;Executor: Execution Plan

Executor-&gt;&gt;Tools: Execute Tasks

Tools--&gt;&gt;Executor: Results

Executor-&gt;&gt;Reviewer: Output

Reviewer--&gt;&gt;Executor: Fix Issues (if needed)

Reviewer--&gt;&gt;User: Final Response

\`\`\`

\---

\# Advantages

\- Better accuracy.

\- Higher quality.

\- Easier debugging.

\- Modular design.

\- Supports iterative improvement.

\- Clear separation of concerns.

\---

\# Trade-offs

\- Additional execution time.

\- More LLM calls.

\- Higher token usage.

\- More orchestration complexity.

These costs are often justified for production-critical workflows.

\---

\# Performance Considerations

\- Cache reusable plans.

\- Execute independent tasks in parallel.

\- Minimize unnecessary review loops.

\- Apply timeouts and retries.

\---

\# Common Mistakes

❌ Planner generates implementation details.

❌ Executor changes the overall plan.

❌ Reviewer rewrites everything instead of validating.

❌ No stopping condition for review loops.

❌ Mixing responsibilities across agents.

\---

\# Best Practices

\- Planner creates the strategy.

\- Executor performs the work.

\- Reviewer validates the result.

\- Keep prompts specialized.

\- Log each stage for observability.

\- Version plans and outputs for traceability.

\---

\# Kubernetes Perspective

Think about Kubernetes reconciliation.

\`\`\`

Desired State

↓

Controller Creates Plan

↓

Scheduler Places Pods

↓

Kubelet Runs Pods

↓

Controller Verifies State

\`\`\`

Different components own different responsibilities.

Similarly:

\`\`\`

Planner

↓

Executor

↓

Reviewer

\`\`\`

Each agent has one clear role.

\---

\# Interview Questions

\### What is the Planner–Executor Pattern?

A multi-agent architecture where one agent creates an execution plan, another performs the work, and a reviewer validates the output before completion.

\---

\### Why separate planning and execution?

It improves reliability, maintainability, explainability, and allows different agents to specialize in different responsibilities.

\---

\### What is the role of the Reviewer?

The Reviewer verifies correctness, completeness, security, and quality. If issues are found, the work is sent back to the Executor for correction.

\---

\### Where is this pattern commonly used?

\- AI coding assistants

\- Enterprise automation

\- Research systems

\- Platform engineering

\- Infrastructure management

\- Software generation

\---

\# Summary

The Planner–Executor Pattern:

\- Separates thinking from doing.

\- Improves quality through validation.

\- Supports iterative refinement.

\- Mirrors how engineering teams operate.

\- Is one of the most common production AI architectures.

Mastering this pattern is essential for designing enterprise-grade AI systems.

\---

\# References

\- LangGraph Multi-Agent Documentation

\- Anthropic Agent Design Patterns

\- OpenAI Agent Workflows

\- Software Architecture Patterns