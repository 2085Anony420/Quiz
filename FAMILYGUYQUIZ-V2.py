import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Family Guy Quiz")

        self.questions = [
            ("What is Peter's youngest son's name? ", "STEWIE", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyNV7ASFpNVLXGSjX_LLGqls4QgAcaItej80EeBtNFzQ&s"),
            ("Who has a secret relationship with Mayor West? ", "MEG", "https://www.slashfilm.com/img/gallery/new-family-guy-tribute-to-adam-west/intro-import.jpg"),
            ("What street do the Griffin's live on? ", "SPOONER", "https://static1.srcdn.com/wordpress/wp-content/uploads/2017/04/Family-Guy-the-Griffin-House.jpg"),
            ("What kind of pet does Quagmire have? ", "CAT", "https://static1.srcdn.com/wordpress/wp-content/uploads/2019/09/Quagmire-in-Family-Guy.jpg"),
            ("Which one of Peter's friends lives across the street? ", "CLEVELAND", "https://static.wikia.nocookie.net/familyguyfanon/images/1/10/The_Brown_House_%28Family_Guy%29.png/revision/latest?cb=20180405024241")
        ]
        self.current_question_index = 0

        self.question_frame = tk.Frame(self.master)
        self.question_frame.pack()

        self.display_question()

    def display_question(self):
        question, _, image_url = self.questions[self.current_question_index]

        response = requests.get(image_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))

        photo = ImageTk.PhotoImage(image)

        if hasattr(self, "image_label"):
            self.image_label.destroy()
        self.image_label = tk.Label(self.question_frame, image=photo)
        self.image_label.image = photo 
        self.image_label.pack()

        if hasattr(self, "question_label"):
            self.question_label.destroy()
        self.question_label = tk.Label(self.question_frame, text=question)
        self.question_label.pack()

        if hasattr(self, "answer_entry"):
            self.answer_entry.destroy()
        self.answer_entry = tk.Entry(self.question_frame)
        self.answer_entry.pack()

        if hasattr(self, "submit_button"):
            self.submit_button.destroy()
        self.submit_button = tk.Button(self.question_frame, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().upper()
        _, correct_answer, _ = self.questions[self.current_question_index]

        if user_answer == correct_answer:
            messagebox.showinfo("RIGHT", "A true fan may be among us")
        else:
            messagebox.showerror("FAIL!", f"Wrong answer {correct_answer.capitalize()}.")

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.display_question()
        else:
            messagebox.showinfo("Completed", "You have finished the quiz!")
            self.master.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()