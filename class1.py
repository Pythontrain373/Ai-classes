"""Hello AI
Outline:
Create a basic Python program that simulates an AI chatbot, 
interacting with users through text and responding intelligently based on their input."""
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
print(f"It was nice chatting with you {name}.Goodbye!")