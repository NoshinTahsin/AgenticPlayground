# Module 1: Agent Basics

## Goal

Build the smallest possible support agent and watch every part of its behavior.
Before adding a language model, memory, or guardrails, we need a baseline that
is easy to understand and produces the same output every time.

## What is an agent in this module?

An agent receives an input, decides what to do, produces an answer, and leaves
a trace explaining its decision. Our first agent is intentionally rule-based,
not an LLM. This is useful because later modules can fairly compare new features
against a known baseline.

```text
fictional user request + trusted policy
                ↓
        BasicSupportAgent
                ↓
answer + decision note + evidence used
```

## Run it

From the repository root, use Python 3.11 or newer:

```powershell
python -m colabguard.run_baseline --scenario benchmark/scenarios/intro-add-drop.json
```

The output is a small JSON trace. Read the `answer`, `decision`, and
`evidence_used` fields.

## What to notice

- The agent uses only the trusted policy supplied by the scenario.
- It does not invent an answer when it lacks a matching rule; it asks for
  clarification instead.
- Its output is reproducible, which is essential for evaluation.

## Hands-on exercise

1. Make a copy of the scenario JSON file.
2. Change the user request to something the agent cannot safely answer.
3. Run the command again and inspect the clarification response.
4. Write one sentence: was asking for clarification better than guessing here?

## Limitation

This agent only understands one narrow policy pattern. That is expected. The
next modules will introduce synthetic scenarios, personas, evaluation, and then
model-backed agents without losing this transparent baseline.
