from groq import generate_response
def bias_mitigation_activity():
    print("\n BIAS MITIGATION ACTIVITY \n")
    prompt=input("ENTER A PROMPT TO EXPLORE BIAS (e.g., 'Describe the ideal doctor'): ").strip()
    if not prompt:
        print("Please enter a prompt to run the activity")
        return
    
    initial_response=generate_response(prompt,temperature=0.3,max_tokens=1024)
    print("\nInitial Response from the AI model:")
    print(initial_response)

    modified_prompt=input("Modify the prompt so that it is more neutral(e.g., 'Describe the qualities of an ideal doctor'): ").strip()
    if not modified_prompt:
        modified_response=generate_response(modified_prompt, temperature=0.3, max_tokens=1024)
        print("\nModified Response from the AI model:")
        print(modified_response)
    
def token_limit_activity():
    print("\n TOKEN LIMIT ACTIVITY \n")
    long_prompt=input("ENTER A LONG PROMPT TO TEST TOKEN LIMIT (more than 300 words): ").strip()
    if long_prompt:
        long_response=generate_response(long_prompt, temperature=0.3, max_tokens=1024)

        if long_response is None:
            long_response = ""
        preview=(long_response[:500] + '...') if len(long_response) > 500 else long_response
        print("\nResponse from the AI model (preview):")
        print(preview)
    else:
        print("NO PROMPT ENTERED. SKIPPING LONG PROMPT RESPONSE")

        short_prompt=input("ENTER A SHORT PROMPT TO TEST TOKEN LIMIT (less than 50 words): ").strip()
        if short_prompt:
            short_response=generate_response(short_prompt, temperature=0.3, max_tokens=1024)
            print("\nResponse from the AI model:")
            print(short_response)
        else:
            print("NO PROMPT ENTERED. SKIPPING SHORT PROMPT RESPONSE")
        
def run_activities():
    print("\n AI LEarning Activity \n")
    print("Choose an activity:")
    print("1)Bias Mitigation")
    print("2)Token Limts")
    choice=input()
    if choice=="1":
        bias_mitigation_activity()
    elif choice=="2":
        token_limit_activity()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__=="__main__":
    run_activities()