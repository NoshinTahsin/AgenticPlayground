# CoLabGuard

**CoLabGuard** is a research prototype, benchmark, and hands-on learning lab
for evaluating guardrails in persona-aware, collaborative AI agents. It helps
new interns and undergraduate learners build the core ideas themselves while
studying whether trusted-context handling, memory-write controls, and
audit-oriented agent roles improve reliability on multi-turn support tasks.

The project will produce:

- a versioned synthetic benchmark (`colabbench`);
- reproducible agent configurations and evaluation runs;
- audit traces and guardrail analyses;
- an interactive research showcase UI; and
- a technical/tool paper with a replication package.

The initial protocol is in [docs/research-protocol.md](docs/research-protocol.md).
The learner journey is in [docs/learning-path.md](docs/learning-path.md).

## Project status

Module 0 — research protocol: in progress.

## Intended repository layout

```text
colabguard/
  benchmark/       Scenario schema, generators, and versioned datasets
  agents/          Baseline and guarded agent configurations
  evaluation/      Metrics, judges, and experiment runners
  dashboard/       Research showcase UI
  docs/            Protocol, data card, model card, and paper sources
  results/          Versioned experiment summaries (no secrets or private data)
```

## Safety and data boundaries

All benchmark users, organizations, records, policies, and attack-like inputs
are fictional. CoLabGuard evaluates defensive handling and auditing; it does not
operate against live systems or use real personal data.
