from groq import generate_response
def reinforcement_learning_activity():
    print("\nWelcome to the Reinforcement Learning Activity!")
    prompt=input("Please enter a prompt for the AI model").strip()
    if not prompt:
        print("Please enter a prompt to run the activity")
        return

    initial_response=generate_response(prompt,temperature=0.3, max_tokens=1024)
    print("\nInitial Response from the AI model:")
    print(initial_response)
    try:
        rating=int(input("Rate the response from 1 (bad) to 5 (excellent): "))
        if rating < 1 or rating > 5:
            print("Invalid rating. Using 3.")
            rating = 3
    except ValueError:
        print("Invalid input. Using 3.")
        rating = 3
    feedback=input("Provide feedback for improvement:").strip()
    improved_response=f"{initial_response}(improved with feedback: {feedback})"
    print(f"\nImproved Response from the AI model based on your feedback:")
    print(improved_response)
    print("\nRelflection")
    print("1. How did the model's response improve with feedback?")
    print("2. How does reinforcement learning help AI to improve its performance over time?")

def role_based_prompt_activity():
    print("\nWelcome to the Role-Based Prompt Activity!")
    category=input("Enter a category(e.g., 'Science', 'History', 'Technology'): ").strip()
    item=input("Enter an item within that category: ").strip()
    if not category or not item:
        print("Please enter both category and item to run the activity")
        return
    teacher_prompt=f"You are a teacher. Explain {item} in simple terms."
    expert_prompt=f"You are an expert in {category}. Provide a detailed explanation of {item}."
    techer_response=generate_response(teacher_prompt,temperature=0.3, max_tokens=1024)
    expert_response=generate_response(expert_prompt,temperature=0.3, max_tokens=1024)
    print("\nResponse from the Teacher Role:")
    print(techer_response)
    print("\nResponse from the Expert Role:")
    print(expert_response)
    print("\nReflection")
    print("1. How did the responses differ based on the role of the AI model?")
    print("2. How can role-based prompting be used to get more accurate or relevant responses from AI models?")

def run_activity():
    print("Welcome to the AI Activities!")
    print("1. Reinforcement Learning Activity")
    print("2. Role-Based Prompt Activity")
    choice=input("Please select an activity (1 or 2): ").strip()
    if choice=="1":
        reinforcement_learning_activity()
    elif choice=="2":
        role_based_prompt_activity()
    else:
        print("Invalid choice. Please select either 1 or 2.")
if __name__=="__main__":
    run_activity()