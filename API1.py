import requests

def get_reamdom_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response=requests.get(url)

    if response.status_code==200:
        #One line to print the JSON response:
        #print(f"Full JSON Response: {response.json()}")

        joke_data=response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    else:
        return "Failed to fetch a joke. Please try again later." \
        

def main():
    print("Welcome to the Random Joke Generator!")

    while True:
        user_input = input("Press Enter to get a random joke or type 'q/exit' to quit: ")
        if user_input.lower() in ['exit', 'q']:
            print("Goodbye!")
            break

        joke=get_reamdom_joke()
        print(joke)

if __name__ == "__main__":
        main()
