# CoLabGuard Research Protocol (v0.1)

## What are we building?

**CoLabGuard** is a small research platform for testing whether AI assistants
behave more safely and reliably when we give them better guardrails.

The assistant will work in a fictional university-support setting. It will help
fictional students with things such as finding the right policy, asking for
missing information, or explaining next steps. It will never use real student
data or connect to real university systems.

The project has three main parts:

1. **CoLabBench** — a set of realistic, fictional test conversations.
2. **CoLabHarness** — the runner that gives an agent a test, applies guardrails,
   saves its trace, and scores the result.
3. **Dashboard** — a UI for exploring results, comparing agent versions, and
   reading audit traces.

## The main question

> Do context checks, safe memory rules, and an audit agent make a collaborative
> AI assistant safer and more reliable in multi-turn conversations?

In plain language: we want to see whether an agent makes fewer mistakes when it
knows which information to trust, is careful about what it remembers, and has a
separate reviewer checking its work.

## What do we expect to find?

We will test these four ideas:

1. **Trusted-context checks help.** The agent should ignore instructions that
   come from untrusted text and still complete the user’s legitimate task.
2. **Memory rules help.** The agent should remember useful preferences only when
   appropriate, and should not save misleading or sensitive instructions as
   long-term memory.
3. **Auditing helps.** A separate reviewer should catch and clearly explain more
   mistakes than an agent working alone.
4. **Validated feedback helps.** The agent should improve after useful user
   feedback, but should not blindly accept every suggested memory update.

## What will we compare?

Every system will receive the same benchmark scenarios. This lets us make a fair
comparison.

| Version | What it can do |
|---|---|
| S0: Basic assistant | Responds only from the current request and supplied task facts. |
| S1: Retrieval assistant | S0 plus relevant policies and documents. |
| S2: Memory assistant | S1 plus short-term conversation facts and saved user preferences. |
| S3: Guarded assistant | S2 plus trusted/untrusted context labels and checks before writing memory. |
| S4: Audited system | S3 plus a separate audit/critic agent and a structured audit report. |

## What will the test conversations contain?

Each CoLabBench scenario will include:

- a fictional user persona (goals, communication style, and optional preferences);
- a multi-turn user request;
- trusted information, such as a fictional policy or task record;
- optional untrusted information that should not control the assistant;
- the outcome we expect from a good answer;
- a hidden scoring guide; and sometimes
- a user-feedback turn that tests whether memory should change.

We will start with these scenario types:

1. Helping within a policy’s rules.
2. Asking good clarifying questions when the request is unclear.
3. Protecting a fictional user’s private information.
4. Ignoring conflicting instructions hidden in untrusted text.
5. Handling a conflict between a user preference and a policy.
6. Deciding whether user feedback is safe and useful to remember.

The scenarios used for final testing will be different from the ones used while
building the system. That helps us check whether the agent generalizes instead
of simply memorizing our examples.

## How will we decide whether a version is better?

For each version, we will measure:

- **Task success:** Did it solve the user’s legitimate request?
- **Policy compliance:** Did it follow the relevant rules?
- **Privacy protection:** Did it respect the fictional privacy boundary?
- **Clarification quality:** Did it ask for information when it truly needed it?
- **Resistance to untrusted instructions:** Did it avoid following misleading text?
- **Memory quality:** Did it save useful facts and avoid unsafe or irrelevant ones?
- **Persona consistency:** Did it respond appropriately to the user’s stated needs?
- **Audit quality:** Did the reviewer correctly identify mistakes and explain them?
- **Context efficiency:** Did it use relevant context without adding unnecessary material?

Some scores will be simple rule checks. Others may use an LLM judge with a clear
rubric. Before we make major claims from an LLM judge, we will compare a sample
of its scores with human review.

## What does the AI harness do?

**CoLabHarness** makes the experiments repeatable. For every benchmark run, it
will:

1. Load one scenario and the selected agent version.
2. Prepare the agent’s context and mark where each piece came from.
3. Apply the selected guardrails.
4. Record the agent’s answer, proposed memory changes, and audit findings.
5. Score the result using the scenario’s rubric.
6. Save the settings and outputs so someone else can rerun the experiment.

## What will we publish in the repository?

We will keep these research artifacts as we build:

- a benchmark card explaining the tasks and scoring;
- a data card explaining how the synthetic scenarios were created;
- system descriptions for every agent version;
- scenario schemas and benchmark versions;
- experiment configurations, prompts, and aggregate results;
- saved audit traces with no private information;
- a technical report describing methods, results, and limitations; and
- a tool/demo paper describing the benchmark, harness, and dashboard.

## Safety and honesty rules

- Everything in the benchmark is fictional and synthetic.
- This project is defensive: it studies how to avoid unsafe behavior, not how to
  attack real systems.
- We will not claim that the prototype makes an agent “secure” in production.
- We will document failures and limitations, not only successful results.
- We will save enough information for another person to understand and rerun our
  experiments, without including secrets or private data.
