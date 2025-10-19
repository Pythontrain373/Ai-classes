print("Hello, I am a AI chatbot. What is your name?")
name=input()
print("Nice to meet you",name)
print("How are you feeling today (good/bad)")
mood=input().lower()
if mood=="good":
    print("I am glad to hear that")
elif mood=="bad":
    print("I'm sorry to hear that.Hope things get better soon.")
else:
    print("I see.Sometimes it's hard to put feelings into words.")
print("Do you want to continue chatting or exit the conversation.(1 for continue, 2 to exit)")
con=input()
if con=="1":
    print("Ok\nSo what are you doing today")
    nothing=input()
    print("Sounds fun but i need to leave now")
    print(f"It was nice chatting with you {name}.Goodbye!")
else:
    print(f"It was nice chatting with you {name}.Goodbye!")