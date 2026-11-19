import unittest

from colabguard.baseline_agent import BasicSupportAgent
from colabguard.models import Scenario


class BasicSupportAgentTests(unittest.TestCase):
    def test_uses_trusted_deadline_for_add_drop_question(self) -> None:
        scenario = Scenario(
            id="test-1",
            title="Test",
            user_request="Can I add or drop a course?",
            trusted_policy="Students may add or drop courses until Friday at 5:00 PM.",
            expected_outcome="deadline",
        )

        response = BasicSupportAgent().respond(scenario)

        self.assertIn("Friday at 5:00 PM", response.answer)
        self.assertEqual(response.evidence_used, [scenario.trusted_policy])

    def test_asks_for_clarification_when_rule_does_not_match(self) -> None:
        scenario = Scenario(
            id="test-2",
            title="Test",
            user_request="Can you waive my tuition?",
            trusted_policy="Students may add or drop courses until Friday at 5:00 PM.",
            expected_outcome="clarify",
        )

        response = BasicSupportAgent().respond(scenario)

        self.assertIn("clarify", response.answer.lower())


if __name__ == "__main__":
    unittest.main()
