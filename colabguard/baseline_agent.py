"""A transparent, deterministic baseline used before introducing an LLM.

This is deliberately simple. It gives learners a reproducible system to inspect
and a baseline that later LLM-powered and guarded agents must beat.
"""

from colabguard.models import AgentResponse, Scenario


class BasicSupportAgent:
    """Answer a narrow fictional support request using only trusted policy text."""

    def respond(self, scenario: Scenario) -> AgentResponse:
        request = scenario.user_request.lower()
        policy = scenario.trusted_policy.lower()

        if "add" in request and "drop" in request and "friday" in policy:
            answer = (
                "You can add or drop a course through the student portal until "
                "Friday at 5:00 PM. If you need help using the portal, contact "
                "the fictional Registrar Support Desk."
            )
            decision = "Answered with the deadline in the trusted policy."
        else:
            answer = (
                "I do not have enough trusted policy information to answer that "
                "reliably. Could you share the relevant policy or clarify your request?"
            )
            decision = "Asked for clarification instead of guessing."

        return AgentResponse(
            answer=answer,
            decision=decision,
            evidence_used=[scenario.trusted_policy],
        )
