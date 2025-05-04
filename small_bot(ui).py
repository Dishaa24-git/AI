import tkinter as tk
from tkinter import scrolledtext
import random

responses = {
    "greeting": ["hi", "hello"],
    "admission_process": ["Fill form, take test.", "Apply online, then exam."],
    "eligibility": ["Need PCM in 12th.", "Diploma required"],
    "courses": ["CS", "MECH", "ENTC", "A&R"],
    "fees": ["Check website for fees", "Fees vary by course"],
    "contact": ["email:abc@gmail.com", "Contact us online"],
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


root = tk.Tk()
root.title("College Admission")
root.geometry("600x500")
root.configure(bg="#e6f2ff")

title = tk.Label(root, text="College Admission", font=("Helvetica", 16, "bold"), bg="#e6f2ff", fg="#003366")
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), state='disabled', bg="white", fg="black")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

frame = tk.Frame(root, bg="#e6f2ff")
frame.pack(pady=5)

entry = tk.Entry(frame, font=("Arial", 12), width=50)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(frame, text="Send", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=send_message)
send_button.pack(side=tk.LEFT)

root.mainloop()
