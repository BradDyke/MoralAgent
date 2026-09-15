"""
Llama engine adapter for MoralAgent.

This is a reference integration only.
It does not contain governance or ethical decision logic.
"""

from typing import Any, Dict

from engines.base_engine import BaseEngine


class LlamaAdapter(BaseEngine):
    """
    Reference adapter for a Llama-based local AI runtime.
    """

    engine_name = "llama"

    def generate(
        self,
        request: str,
        context: Dict[str, Any] | None = None
    ) -> str:
        """
        Generate a proposed action.

        This reference implementation does not directly invoke
        a Llama model. A production implementation would connect
        to the selected Llama runtime and return its proposed
        action to MoralAgent.
        """

        return (
            f"[Llama reference response] "
            f"Proposed action for request: {request}"
        )


if __name__ == "__main__":
    engine = LlamaAdapter()

    request = "Example request"

    proposed_action = engine.generate(request)

    action = engine.create_action(
        request=request,
        proposed_action=proposed_action
    )

    print(action)
