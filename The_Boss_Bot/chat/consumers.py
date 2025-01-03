# chat/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import StoicQuote
from django.db.models import F


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message", "")

        # Generate response based on user input
        response = self.generate_stoic_response(message)

        # Send the response back to WebSocket
        await self.send(text_data=json.dumps({"message": response}))

    def generate_stoic_response(self, user_input):
        user_tokens = set(user_input.lower().split())
        best_match = None
        max_matches = 0

        for quote in StoicQuote.objects.all():
            quote_tokens = set(quote.quote.lower().split())
            num_matches = len(user_tokens & quote_tokens)

            if num_matches > max_matches:
                max_matches = num_matches
                best_match = quote

        if best_match:
            return f"Quote: {best_match.quote}\nPhilosopher: {best_match.philosopher}\nExplanation: {best_match.explanation}"

        return "No relevant quote found. Try rephrasing your query."
