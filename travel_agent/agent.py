from openai import OpenAI
from travel_agent.email_sender import send_email
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class AITravelAgent:
    def __init__(self):
        self.history = []

    def plan_trip(self, user_input):
        self.history.append(user_input)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a travel assistant."}] +
                     [{"role": "user", "content": user_input}]
        )
        plan = response.choices[0].message.content
        return plan

    def send_travel_email(self, recipient_email, plan):
        subject = "Your AI Travel Plan"
        send_email(recipient_email, subject, plan)
