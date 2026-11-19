# Module 1: Persona Building for Learners

## What you will learn

You will learn how to describe a learner in a way that helps an AI tutor choose
the right next exercise—without pretending to know private things about them.

## The central idea

A **learner persona** is a small, editable description of information that is
relevant to learning. It is not a prediction about intelligence, potential, or
whether someone deserves an internship.

For this project, a persona may include:

- learning goal;
- self-reported prior experience;
- concepts already covered;
- preferred explanation format; and
- available study time.

It must not include protected characteristics, inferred personality traits,
health information, or a hiring score.

## Persona versus user model

A **persona** is a starting profile. A **user model** is the information the
system uses during learning, including updates the learner explicitly approves.

```text
Persona: “I know basic Python and want to learn agent evaluation.”
        ↓
Learning interaction: learner completes a scenario-design exercise.
        ↓
User model update: “Module 1 completed” (saved only with permission).
```

## A minimal example

```json
{
  "id": "learner_ava",
  "goal": "Build a small agent-evaluation research project",
  "experience": ["basic Python", "introductory machine learning"],
  "concepts_completed": [],
  "learning_preferences": {
    "explanation_style": "step-by-step",
    "practice_style": "small coding exercises"
  },
  "memory_consent": {
    "save_learning_preferences": true,
    "save_progress": true,
    "save_sensitive_information": false
  }
}
```

The system can use this information to begin with plain-language explanations,
small Python tasks, and agent-evaluation examples. It may not infer that Ava is
or is not a strong candidate for any role.

## Hands-on exercise

1. Open `data/example-learner-personas.json`.
2. Pick one fictional learner.
3. Write the first learning activity you would offer them.
4. Identify one field that is useful only during the current session and should
   not be saved permanently.
5. Explain why saving an unstated personal fact would be inappropriate.

## Success criteria

Your persona is ready when it is:

- **Relevant:** every field helps choose a learning activity;
- **Minimal:** it does not collect unnecessary information;
- **Transparent:** the learner can read and edit it;
- **Consented:** stored fields have clear permission; and
- **Non-evaluative:** it does not label or rank the learner.

## Next module

We will turn the persona into a user model with short-term session context,
durable progress, learner-controlled updates, and safe forgetting.
