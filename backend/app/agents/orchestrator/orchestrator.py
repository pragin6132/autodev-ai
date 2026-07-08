import json

from backend.app.core.gemini import generate
from backend.app.prompts.orchestrator_prompt import ORCHESTRATOR_PROMPT


class Orchestrator:

    def process_request(self, request: str):

        prompt = f"""
{ORCHESTRATOR_PROMPT}

User Request:
{request}
"""

        response = generate(prompt)

        # Remove markdown code fences
        cleaned = (
            response.replace("```json", "")
                    .replace("```", "")
                    .strip()
        )

        try:
            return json.loads(cleaned)
        except Exception:
            return {
                "raw_response": response,
                "cleaned_response": cleaned
            }