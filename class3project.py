#name the file as main.py , uncomment the imports and basic functions, complete  the code by writing remainig functions 

import re, random
from colorama import Fore, init
from datetime import datetime
import pytz

# # Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# # Destination & joke data
destinations = {
      "beaches": ["Bali", "Maldives", "Phuket"],
      "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
      "cities": ["Tokyo", "Paris", "New York"]
  }
jokes = [
     "Why don't programmers like nature? Too many bugs!",
     "Why did the computer go to the doctor? Because it had a virus!",
     "Why do travelers always feel warm? Because of all their hot spots!"
 ]
weather=[
    "Sunny",
    "Rainy",
    "Windy",
    "Cloudy"
]
news= [
    "thousands protest against government in Mexico over violent crime",
    "a US football coach featured on Netflix dies after on-campus shooting"
]
cities_timezones = {
    'New York': 'America/New_York',
    'London': 'Europe/London',
    'Tokyo': 'Asia/Tokyo',
    'Sydney': 'Australia/Sydney',
    'Dubai': 'Asia/Dubai'
}

# # Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, r cities")
    preference=input(Fore.YELLOW + "You: ")
    preference=normalize_input(preference)

    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(Fore.GREEN + f"travelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer=input(Fore.YELLOW + "You: ").lower()

        if answer=="yes":
            print(Fore.GREEN + f"travelot: Awesome! Enjy {suggestion}!")
        elif answer=="no":
            print(Fore.RED + "TrevelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: Sorry,I don't have tht type of destination")

        show_help()
# Offer packing tips based on user’s destination and duration
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location=normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days=input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forcast.")

# Tell a random joke
def tell_joke():
    print(Fore.YELLOW + f"TraveBot: {random.choice(jokes)}")

# Tell the weather
def current_weather():
    current_weather=random.choice(weather)
    print(Fore.GREEN + f"The current weather is {current_weather}")
# Tell the time of different cities
def time():
    print(Fore.GREEN + "Current local times in different cities:")
    for city, timezone_name in cities_timezones.items():
        try:
            # Create a timezone object
            tz = pytz.timezone(timezone_name)
            
            # Get the current time in that timezone
            city_time = datetime.now(tz)
            
            # Format the time for a clean output
            formatted_time = city_time.strftime("%A, %B, %d, %Y %I:%M:%S %p")
            
            print(Fore.CYAN + f"  {city}: {formatted_time}")
        except pytz.UnknownTimeZoneError:
            print(Fore.RED + f"  Error: Unknown time zone for {city}: {timezone_name}")

#Tell the news
def news_now():
    crnews=random.choice(news)
    print(Fore.GREEN + f"A resent news is that {crnews}")
    print(Fore.CYAN + "There are many more news on the web you can find them on websites like BBC")

# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Tell the current weather (say 'weather')")
    print(Fore.GREEN + "- Tell the news (say 'news')")
    print(Fore.GREEN + "- Tell the current time of different cities (say 'time')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! i'm TravelBot.")
    name=input(Fore.YELLOW + "Your name?")
    print(Fore.GREEN + f"Nice to meet you, {name}")


    show_help()

    while True:
        user_input= input(Fore.YELLOW + f"{name}: ")
        user_input= normalize_input(user_input)

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "weather" in user_input:
            current_weather()
        elif "news" in user_input:
            news_now()
        elif "time" in user_input:
            time()
        elif "exit" in user_input or "ybye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")
# Run the chatbot
if __name__ == "__main__":
    chat()