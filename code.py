import datetime

# ---------------- DATABASE (Dictionary-based for simplicity) ----------------
facilities = {
    "library": {"open": "08:00", "close": "22:00"},
    "gym": {"open": "06:00", "close": "21:00"},
}

events = [
    {"title": "Tech Fest", "date": "2025-09-25", "venue": "Auditorium"},
    {"title": "Hackathon", "date": "2025-09-20", "venue": "Innovation Lab"},
]

dining = [
    {"location": "South Canteen", "meal": "Lunch", "items": "Veg Biryani, Paneer, Dal, Salad"},
    {"location": "North Mess", "meal": "Dinner", "items": "Chapati, Chicken Curry, Rice, Kheer"},
]


# ---------------- CHATBOT LOGIC ----------------
def process_query(query: str) -> str:
    query = query.lower()

    # Facility hours
    for facility, times in facilities.items():
        if facility in query:
            return f"{facility.capitalize()} is open from {times['open']} to {times['close']}."

    # Events
    if "event" in query or "happening" in query:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        upcoming = [f"{e['title']} at {e['venue']} on {e['date']}" for e in events if e["date"] >= today]
        return "Upcoming events:\n" + "\n".join(upcoming) if upcoming else "No upcoming events."

    # Dining
    if "menu" in query or "lunch" in query or "dinner" in query:
        menus = [f"{d['meal']} at {d['location']}: {d['items']}" for d in dining]
        return "Dining options:\n" + "\n".join(menus)

    # Default response
    return "Sorry, I don’t know that yet. Please ask about library, gym, events, or dining."


# ---------------- MAIN PROGRAM ----------------
def chatbot():
    print("🤖 Campus Information Chatbot")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break
        response = process_query(user_input)
        print("Bot:", response)


if __name__ == "__main__":
    chatbot()