from travel_agent.agent import AITravelAgent

def main():
    agent = AITravelAgent()
    print("Welcome to AI Travel Agent!")
    user_input = input("Describe your travel plan: ")
    plan = agent.plan_trip(user_input)
    print("\nGenerated Travel Plan:\n", plan)

    send_email = input("\nDo you want to send this plan via email? (yes/no): ").strip().lower()
    if send_email == 'yes':
        recipient = input("Enter recipient email: ")
        agent.send_travel_email(recipient, plan)
        print("Email sent successfully!")

if __name__ == "__main__":
    main()
