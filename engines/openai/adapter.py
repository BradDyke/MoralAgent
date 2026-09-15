"""
OpenAI engine adapter for MoralAgent.

This is a reference integration only.
It does not contain governance or ethical decision logic.
"""

from typing import Any, Dict

from engines.base_engine import BaseEngine


class OpenAIAdapter(BaseEngine):
    """
    Reference adapter for an OpenAI-based AI engine.
    """

    engine_name = "openai"

    def generate(
        self,
        request: str,
        context: Dict[str, Any] | None = None
    ) -> str:
        """
        Generate a proposed action.

        This reference implementation does not call an external API.
        A production implementation would invoke the selected AI service
        and return its proposed action to MoralAgent.
        """

        return (
            f"[OpenAI reference response] "
            f"Proposed action for request: {request}"
        )


if __name__ == "__main__":
    engine = OpenAIAdapter()

    request = "Example request"

    proposed_action = engine.generate(request)

    action = engine.create_action(
        request=request,
        proposed_action=proposed_action
    )

    print(action)
