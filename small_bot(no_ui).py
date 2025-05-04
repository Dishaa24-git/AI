import random

responses = {
    "greeting": ["Hi!", "Hello!"],
    "admission_process": ["Fill the form and take the test.", "Apply online, then exam."],
    "eligibility": ["12th with PCM required.", "Need PCM with cutoff marks."],
    "courses": ["CSE, Mech, Civil, etc.", "We offer CSE, IT, ECE."],
    "fees": ["Check website for fees.", "Fees depend on course."],
    "contact": ["Email: admission@college.edu", "Visit our admission office."]
}

def get_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["greeting"])
    elif "admission" in user_input or "process" in user_input:
        return random.choice(responses["admission_process"])
    elif "eligibility" in user_input or "criteria" in user_input:
        return random.choice(responses["eligibility"])
    elif "course" in user_input or "program" in user_input:
        return random.choice(responses["courses"])
    elif "fee" in user_input or "fees" in user_input:
        return random.choice(responses["fees"])
    elif "contact" in user_input or "email" in user_input:
        return random.choice(responses["contact"])
    else:
        return "Sorry, I didn't get that."

def chatbot():
    print("Welcome to the College Admission Chatbot!")
    print("Ask me about admission, eligibility, courses, fees, etc. (Type 'exit' to quit)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        print("Bot:", get_response(user_input))


chatbot()
