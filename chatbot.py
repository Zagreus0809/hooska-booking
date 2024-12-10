import lyroai

def hooska_chatbot1(user_input):
    user_input = user_input.lower()

    if user_input == "What is Hooska Travel & Tours all about":
        return "Hooska Travel and Tours is a premier travel agency dedicated to making your travel dreams a reality. We specialize in curated travel experiences, from adventure-packed getaways to relaxing retreats. Our mission is to provide seamless, personalized, and unforgettable journeys tailored to your needs."
    elif user_input == "Do you offer any discounts or promotions?":
        return "Yes, we do! 🎉 At Hooska Travel and Tours, we’re excited to offer an exclusive discount and package promotion for our valued customers: 🌟 ₱1,000 OFF Discount Enjoy ₱1,000 OFF on your first booking with us! This offer is valid for all travel packages, whether you're planning a solo adventure, family vacation, or group getaway. 🏖️ Special Package Promotion Book one of our top-selling packages and unlock amazing deals like: Up to 50% OFF on sightseeing tours. A FREE E-Visa for select destinations. Complimentary upgrades and surprise perks on select bookings. 📅 Limited Time Offer: These promotions are available for bookings made before [insert deadline, e.g., December 31, 2024].  ✨ Don’t miss this opportunity to save while enjoying unforgettable experiences! Contact us now to learn more or secure your spot. 🌍✈️"
    elif user_input == "Epic discount on boracay":
        return "🌟 EPIC Discounts Await You! 🌟Looking for your next getaway? Hooska Travel and Tours is offering exclusive deals for our most popular destinations:🏖️ BoracayUp to 50% OFF on beachfront accommodations.FREE sunset cruise with select packages.Enjoy complimentary breakfast for bookings of 3 nights or more!"
    elif user_input == "what can you do":
        return ("I can have a simple conversation with you. You can ask me about the weather, "
                "the time, or just say 'bye' to end our chat. 💬")
    elif user_input == "what's the time":
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')} ⏰"
    elif user_input == "what's the date":
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%Y-%m-%d')} 📅"
    elif user_input == "tell me a joke":
        return ("Why don't scientists trust atoms? 🤔\n"
                "Because they make up everything! ⚛️")
    elif user_input.startswith("what is the weather like"):
        return "I can't check the weather right now, but I hope it's sunny where you are! ☀️"
    elif user_input.startswith("what is your favorite"):
        if "color" in user_input:
            return "My favorite color is blue! 💙"
        elif "food" in user_input:
            return "I don't eat, but I imagine pizza would be great! 🍕"
        else:
            return "I don't have preferences, but I can help with many topics! 🤓"
    elif user_input == "bye":
        return "Goodbye! Have a fantastic day! 👋"
    else:
        return "I'm sorry, I don't understand that. 😕"

def hooska_chatbot2(user_input):
    # Training-style prompt for travel and tours
    system_message = """
    You are a helpful chatbot for Hooska Travels and Tours, specializing in:
    - Guiding users through the booking process.
    - Providing details about travel destinations.
    - Explaining cancellation and refund policies.
    - Suggesting travel plans based on user preferences.
    
    Respond specifically to these questions:
    1. "What destinations do you offer?"
    2. "How can I book a trip?"
    3. "What are your cancellation policies?"
    4. "Do you offer group discounts?"
    5. "Can I reschedule my trip?"
    6. "What payment methods do you accept?"
    7. "What travel packages are currently available?"
    
    """

    response = lyroai.ChatCompletion.create(
        model="claude-3.5",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input},
        ],
    )
    return response['choices'][0]['message']['content']
