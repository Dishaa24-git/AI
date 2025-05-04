import tkinter as tk
from tkinter import scrolledtext
import random

# Define chatbot responses
responses = {
    "greeting": ["Hello! How can I assist you with the college admission process?",
                 "Hi there! Welcome to the college admission chatbot. How can I help you?"],
    "admission_process": ["The admission process involves filling out an online application form, followed by an entrance exam. "
                          "You can check the college website for more details.",
                          "You need to fill out the online admission form, appear for an entrance exam, and provide your academic documents."],
    "eligibility": ["To be eligible, you need to have completed your 12th grade with Physics, Chemistry, and Mathematics as subjects. "
                    "A minimum percentage cutoff is required for eligibility. Please check our website for the exact cutoff.",
                    "Eligibility criteria include completing 12th grade with Physics, Chemistry, and Mathematics, with the required percentage. "
                    "Please refer to our website for detailed criteria."],
    "courses": ["The engineering courses we offer include Computer Science, Mechanical, Civil, Electrical, Electronics, and Information Technology.",
                "We offer various engineering courses such as Computer Science, Civil, Mechanical, Electrical, and Electronics. Let me know if you want to know more about any specific course."],
    "fees": ["The fee structure varies by course and category. You can find the detailed fee structure on our official website.",
             "The tuition fees depend on the course and category. Please refer to our website for the exact fees."],
    "contact": ["You can contact our admission office at admission@college.edu for further inquiries.",
                "For any further questions, feel free to contact us at admission@college.edu or visit our admissions office."]
}

# Function to get chatbot response
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
        return "I'm sorry, I didn't quite understand that. Can you please rephrase?"

# Function to handle sending messages
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    chat_area.config(state='normal')
    chat_area.insert(tk.END, "You: " + user_input + "\n")
    response = get_response(user_input)
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    chat_area.config(state='disabled')
    entry.delete(0, tk.END)
    chat_area.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("College Admission Chatbot")
root.geometry("600x500")
root.configure(bg="#e6f2ff")

title = tk.Label(root, text=" College Admission Chatbot", font=("Helvetica", 16, "bold"), bg="#e6f2ff", fg="#003366")
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), state='disabled', bg="white", fg="black")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

frame = tk.Frame(root, bg="#e6f2ff")
frame.pack(pady=5)

entry = tk.Entry(frame, font=("Arial", 12), width=50)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(frame, text="Send", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=send_message)
send_button.pack(side=tk.LEFT)

# Run the main event loop
root.mainloop()
