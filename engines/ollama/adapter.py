"""
Ollama engine adapter for MoralAgent.

This is a reference integration only.
It does not contain governance or ethical decision logic.
"""

from typing import Any, Dict

from engines.base_engine import BaseEngine


class OllamaAdapter(BaseEngine):
    """
    Reference adapter for an Ollama-based local AI engine.
    """

    engine_name = "ollama"

    def generate(
        self,
        request: str,
        context: Dict[str, Any] | None = None
    ) -> str:
        """
        Generate a proposed action.

        This reference implementation does not connect to Ollama.
        A production implementation would communicate with the local
        Ollama service and return its proposed action to MoralAgent.
        """

        return (
            f"[Ollama reference response] "
            f"Proposed action for request: {request}"
        )


if __name__ == "__main__":
    engine = OllamaAdapter()

    request = "Example request"

    proposed_action = engine.generate(request)

    action = engine.create_action(
        request=request,
        proposed_action=proposed_action
    )

    print(action)
