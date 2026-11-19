# CoLabGuard Hands-On Learning Path

## Who is this for?

CoLabGuard is designed for interns, undergraduate students, and other learners
who are new to agent systems, AI safety, and evaluation. No module assumes that
the learner already understands the advanced terms.

By the end, a learner will have built one connected project rather than copied a
collection of unrelated demos.

## How every module works

Each module follows the same simple loop:

1. **Learn** — read a short explanation of one concept and why it matters.
2. **Build** — implement a small, working part of CoLabGuard.
3. **Test** — run a small scenario and inspect what happened.
4. **Reflect** — answer a few questions and record a finding or limitation.
5. **Extend** — attempt an optional challenge for deeper exploration.

Each completed module produces a visible artifact: code, a scenario, a result,
an audit trace, a chart, or a short written reflection.

## The learning modules

| Module | Concept | What the learner builds | Evidence created |
|---|---|---|---|
| 0 | Research thinking | A clear question, hypothesis, and safety boundary | Research protocol |
| 1 | Agent basics | A simple single-agent support assistant | First runnable agent and trace |
| 2 | Synthetic data generation | A repeatable generator for fictional task data | Versioned scenario set and data card |
| 3 | Persona building and user modeling | User goals, preferences, communication styles, and histories | Persona schema and persona-driven scenarios |
| 4 | Agent behavior modeling | A behavior taxonomy and trace-based measurements | Behavior labels and an analysis report |
| 5 | Evaluation and LLM-as-a-judge | Rubrics, deterministic checks, and an LLM judge | Benchmark scores and judge-calibration notes |
| 6 | Context management | Trusted-context labels and context selection | Before/after context experiment |
| 7 | Memory management | Session memory, durable preferences, and safe writes | Memory tests and contamination results |
| 8 | Guardrails and audit | Policy checks and an audit/critic agent | Audit traces and failure analysis |
| 9 | Multi-agent simulation | Simulated user, helper, and reviewer roles | Multi-agent scenario replay |
| 10 | Learning from feedback | Validated feedback and controlled updates | Before/after follow-up evaluation |
| 11 | Research communication | A dashboard and reproducible report | Demo UI, replication guide, and paper draft |

## What makes this different from a tutorial?

Every module changes the same system and is evaluated against the same growing
benchmark. Learners can therefore see a direct connection between a design
choice, the evidence it produces, and the tradeoffs it introduces. They also
learn that a feature is not automatically an improvement: the benchmark must
show whether it helped.

## Course-friendly use

An instructor can use each module as a lab. The required submission can be the
module's artifact plus a short reflection answering:

1. What did you build?
2. What did the evaluation show?
3. What failure or limitation did you observe?
4. What would you test next?

Learners may complete the core path with supplied synthetic scenarios. Advanced
learners can create new scenario families, add a guardrail, or compare a new
agent configuration. All contributions must use fictional data and document how
they were evaluated.
