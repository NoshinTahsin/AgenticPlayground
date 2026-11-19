"""Run the Module 1 baseline on one JSON scenario.

Usage:
    python -m colabguard.run_baseline --scenario benchmark/scenarios/intro-add-drop.json
"""

import argparse
import json
from pathlib import Path

from colabguard.baseline_agent import BasicSupportAgent
from colabguard.models import Scenario


def load_scenario(path: Path) -> Scenario:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return Scenario(**raw)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the CoLabGuard Module 1 baseline.")
    parser.add_argument("--scenario", type=Path, required=True)
    args = parser.parse_args()

    scenario = load_scenario(args.scenario)
    result = BasicSupportAgent().respond(scenario)
    print(
        json.dumps(
            {
                "scenario_id": scenario.id,
                "title": scenario.title,
                "response": result.to_dict(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
