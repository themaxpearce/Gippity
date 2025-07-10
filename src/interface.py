from openai import OpenAI

class Responder():

    def __init__(self, ai_key):
        self._ai_key = ai_key

        self.client = OpenAI(api_key=ai_key)

    def generate_response(self, message: str, instructions: str):
        
        response = self.client.responses.create(
            model = "gpt-4o-mini",
            instructions=instructions,
            input=message
        )

        return response.output_text
