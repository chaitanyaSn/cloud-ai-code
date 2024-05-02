problem_dict = {
    "communication skills": "Rate the employee's communication skills on a scale of 1 to 5.",
    "problem-solving ability": "Rate the employee's problem-solving ability on a scale of 1 to 5.",
    "time management": "Rate the employee's time management skills on a scale of 1 to 5.",
    "teamwork": "Rate the employee's ability to work effectively in a team on a scale of 1 to 5.",
    "creativity": "Rate the employee's creativity and innovation on a scale of 1 to 5.",
    "adaptability": "Rate the employee's ability to adapt to changes on a scale of 1 to 5.",
    "leadership": "Rate the employee's leadership skills on a scale of 1 to 5.",
    "attention to detail": "Rate the employee's attention to detail on a scale of 1 to 5.",
    "customer service": "Rate the employee's customer service skills on a scale of 1 to 5.",
}

def handle_request(user_input):
   
    user_input = user_input.strip().lower()  # Convert to lowercase and remove leading/trailing whitespace
    if user_input == "exit":
        return "Goodbye!"
    elif user_input in problem_dict:
        return problem_dict[user_input]
    else:
        return "I'm sorry, I don't know how to help with that problem."

# Main loop to prompt user for input
while True:
    user_input = input("What's the problem? Type 'exit' to quit. ")
    response = handle_request(user_input)
    print(response)
 

