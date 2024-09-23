import tkinter as tk
from tkinter import messagebox

class PersonalityQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Personality Quiz")

        self.questions = [
            {
                "question": "What do you enjoy doing in your free time?",
                "choices": ["Reading", "Sports", "Socializing", "Gaming"]
            },
            {
                "question": "How do you handle stress?",
                "choices": ["Meditate", "Exercise", "Talk to friends", "Watch TV"]
            },
            {
                "question": "What's your ideal weekend?",
                "choices": ["Relaxing at home", "Going on an adventure", "Spending time with friends", "Catching up on games"]
            },
            {
                "question": "How do you prefer to spend your vacation?",
                "choices": ["Quiet retreat", "Exploring new places", "Partying with friends", "Staying home"]
            },
            {
                "question": "How do you feel in large social gatherings?",
                "choices": ["Overwhelmed", "Tolerant", "Energized", "Excited"]
            },
            {
                "question": "What motivates you?",
                "choices": ["Personal growth", "Achievements", "Social interactions", "Fun"]
            },
            {
                "question": "How do you recharge?",
                "choices": ["Alone time", "Light activities", "Being around others", "Creative hobbies"]
            },
            {
                "question": "How do you make decisions?",
                "choices": ["Think it through", "Consult others", "Go with the flow", "Trust your instincts"]
            },
            {
                "question": "What's your communication style?",
                "choices": ["Written", "In-person", "Group discussions", "Digital messages"]
            },
            {
                "question": "How do you feel about new experiences?",
                "choices": ["Prefer familiar things", "Willing to try", "Love exploring", "Always seeking thrills"]
            }
        ]

        self.current_question = 0
        self.total_score = 0

        self.question_label = tk.Label(self.master, text="")
        self.question_label.pack(pady=20)

        self.var = tk.IntVar()
        self.choices = []

        self.next_button = tk.Button(self.master, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question]["question"])
            self.var.set(0)

            for widget in self.choices:
                widget.destroy()
            self.choices.clear()

            for index, choice in enumerate(self.questions[self.current_question]["choices"]):
                radio_button = tk.Radiobutton(self.master, text=choice, variable=self.var, value=index + 1)
                radio_button.pack(anchor='w')
                self.choices.append(radio_button)

        else:
            self.show_result()

    def next_question(self):
        if self.var.get() == 0:
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        self.total_score += self.var.get()
        self.current_question += 1
        self.load_question()

    def show_result(self):
        personality_type = self.get_personality_type(self.total_score)
        messagebox.showinfo("Your Personality Type", f"Your personality type is: {personality_type}")
        self.master.quit()

    def get_personality_type(self, score):
        if score <= 10:
            return "Introvert"
        elif score <= 20:
            return "Ambivert"
        elif score <= 30:
            return "Extrovert"
        else:
            return "Social Butterfly"

if __name__ == "__main__":
    root = tk.Tk()
    quiz = PersonalityQuiz(root)
    root.mainloop()
