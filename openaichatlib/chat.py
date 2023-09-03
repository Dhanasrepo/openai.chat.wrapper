import openai
import uuid


class Chat:
    def __init__(self, api_key, default_system_prompt="You are a helpful assistant."):
        self.api_key = api_key
        self.default_system_prompt = default_system_prompt
        openai.api_key = self.api_key

    def start_new_session(self, system_prompt=None):
        """ Generate a new session ID and optionally set a system prompt """
        session_id = str(uuid.uuid4())
        system_message = system_prompt or self.default_system_prompt

        # Return the initial system message as part of the session's history
        return {
            'session_id': session_id,
            'history': [{'role': 'system', 'content': system_message}]
        }

    def ask(self, session_id, history, question):
        """ Ask the model a question with session history """
        messages = history + [{'role': 'user', 'content': question}]

        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        messages.append(response['choices'][0]['message'])

        return {
            'session_id': session_id,
            'history': messages,
            'response': response['choices'][0]['message']['content']
        }