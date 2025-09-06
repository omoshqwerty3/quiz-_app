import tkinter as tk
from tkinter import simpledialog, messagebox


questions = ("Who was the first human on earth?: ",
             "Who was the first president of Kenya?: ",
             "What is 2 +2 ?: ",
             "Who is the king of United Kingdom?: ", "What is the capital city of Kenya?: ",
             "Which planet is known as the Red Planet?: ",
             "Who wrote the play 'Romeo and Juliet'?: ",
             "Which ocean is the largest in the world?: ",
             "What is the chemical symbol for water?: ",
             "Which country is known as the Land of the Rising Sun?: ",
             "In which year did World War II end?: ",
             "Who painted the Mona Lisa?: ",
             "What is the smallest prime number?: ",
             "Which language has the most native speakers?: ",
             "Which continent is the Sahara Desert located on?: ")

options = (("A. Adam","B. Noah","C. Jacob","D. Isaac"),
           ("A. Jomo","B. Ruto","C. Uhuru","D. Mwai"),
           ("A. 2","B. 4","C. 3","D. 5"),
           ("A. Chales III","B. James II","C. Henry V","D. William III"),
           ("A. Mombasa", "B. Nairobi", "C. Kisumu", "D. Eldoret"),
           ("A. Mars", "B. Jupiter", "C. Venus", "D. Saturn"),
           ("A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. George Orwell"),
           ("A. Atlantic Ocean", "B. Pacific Ocean", "C. Indian Ocean", "D. Arctic Ocean"),
           ("A. O2", "B. CO2", "C. H2O", "D. NaCl"),
           ("A. China", "B. Japan", "C. Korea", "D. Thailand"),
           ("A. 1940", "B. 1945", "C. 1950", "D. 1939"),
           ("A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"),
           ("A. 0", "B. 1", "C. 2", "D. 3"),
           ("A. English", "B. Mandarin Chinese", "C. Spanish", "D. Hindi"),
           ("A. Africa", "B. Asia", "C. Australia", "D. South America"))

answers = ("A","A","B","A","B","A","A","B", "C","B","B","C","C","B","A")
guesses = []
score = 0
question_num = 0


root = tk.Tk()
root.withdraw()

# Quiz Loop
for question in questions:
    messagebox.showinfo("Question", question + "\n\n" + "\n".join(options[question_num]))

    guess = simpledialog.askstring("Your Answer", "Enter your Guess (A,B,C,D): ")
    if guess:
        guess = guess.upper()
        guesses.append(guess)

        if guess == answers[question_num]:
            score += 1
            messagebox.showinfo("Result", "CORRECT!")
        else:
            messagebox.showwarning("Result", f"WRONG!\nCorrect answer: {answers[question_num]}")

    question_num += 1


results_text = "Answers: " + " ".join(answers) + "\n" + \
               "Guesses: " + " ".join(guesses) + "\n" + \
               f"Your score is {int(score/len(questions)*100)}%"

messagebox.showinfo("Quiz Finished", results_text)
