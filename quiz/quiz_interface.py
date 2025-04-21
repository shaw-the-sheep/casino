from tkinter import *
from tkinter.font import Font
from questions import Questions
from random import randint

class QuizInterface(Questions):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.difficulty = ""
        self.category = 9
        self.amount = 10

        self.nb_question = -1

        self.Quiz_pararmeters()


    def __interface(self):
        self.parameter_win.destroy()

        self.quiz_win = Tk()

        self.quiz_win.title("Trivia Game")
        self.quiz_win.geometry("500x400")

        self.quiz_win.grid_rowconfigure(0, weight=1)
        self.quiz_win.grid_columnconfigure(0, weight=1)

        # titel of the quiz

        title_font = Font(family="Verdana", size=16, weight="bold")
        self.question_label = Label(self.quiz_win, text="Trivia Game", font=title_font, fg = "red")
        self.question_label.pack()

        # Body frames
        self.questions_frame = Frame(self.quiz_win)
        self.questions_frame.pack()

        self.options_frame = Frame(self.quiz_win)
        self.options_frame.pack()

        self.score_info_frame = Frame(self.quiz_win)
        self.score_info_frame.pack()

        # question labels

        question_font = Font(family="Verdana", size=12, weight="bold")
        self.question_label = Label(self.questions_frame, text="Question:", font=question_font)
        self.question_label.grid(row=0, column=0, padx=10, pady=10)

        self.question = Label(self.questions_frame, text="", font=("Arial", 12), anchor="center", wraplength=300)
        self.question.grid(row=0, column=1, pady=10)


        # option lables

        option_font = Font(family="Verdana", size=12)
        self.option1 = Button(self.options_frame, text="", font=option_font, bg="pink", anchor="center", width=40, command=lambda: self.check_answer(0))
        self.option1.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)

        self.option2 = Button(self.options_frame, text="", font=option_font, bg="lightblue", anchor="center", command=lambda: self.check_answer(1))
        self.option2.grid(row=1, column=0, padx=10, sticky=NSEW)

        self.option3 = Button(self.options_frame, text="", font=option_font, bg="yellow", anchor="center", command=lambda: self.check_answer(2))
        self.option3.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)

        self.option4 = Button(self.options_frame, text="", font=option_font, bg="orange", anchor="center", command=lambda: self.check_answer(3)) 
        self.option4.grid(row=3, column=0, padx=10, sticky=NSEW)

        # score info
        self.score_label = Label(self.score_info_frame, text="Score: 0", font=("Arial", 12))
        self.score_label.grid(row=0, column=0, padx=10, pady=10)

        self.difficulty_label = Label(self.score_info_frame, text=f"Difficulty: {self.difficulty}", font=("Arial", 12))
        self.difficulty_label.grid(row=0, column=1, padx=10, pady=10)

        self.category_label = Label(self.score_info_frame, text=f"Category: {self.category}", font=("Arial", 12))
        self.category_label.grid(row=0, column=2, padx=10, pady=10)

        self.combo_label = Label(self.score_info_frame, text="Combo: 0", font=("Arial", 12))
        self.combo_label.grid(row=1, column=0, padx=10, pady=10)

        self.start_button = Button(self.score_info_frame, text="Start", font=("Arial", 12), command=self.get_question)
        self.start_button.grid(row=1, column=1, padx=10, pady=10)

        self.quit_button = Button(self.score_info_frame, text="Quit", font=("Arial", 12), command = self.quiz_win.destroy)
        self.quit_button.grid(row=1, column=2, padx=10, pady=10)

        self.quiz_win.mainloop()

    
    def start_game(self, difficulty, category, num_questions):
        self.num_questions = int(num_questions)
        self.difficulty = difficulty
        self.category = category

        self.ratio = self.define_ratio()
        print(self.ratio)

        self.__interface()

    def get_question(self):
        self.nb_question += 1
        if self.nb_question >= len(self.questions):
            self.end_game()
            return
        self.question.config(text=f"Question {self.nb_question + 1}: {self.questions[self.nb_question]['question']}")
        self.options = self.shuffle_answers(self.questions, self.nb_question)

        print(self.options)
        self.option1.config(text=self.options[0])
        self.option2.config(text=self.options[1])
        self.option3.config(text=self.options[2])
        self.option4.config(text=self.options[3])

    def check_answer(self, user_answer):
        correct_option = self.options.index(self.questions[self.nb_question]['correct_answer'])
        if user_answer == correct_option:
            self.score += self.calculate_score()
            self.score_label.config(text=f"Score: {self.score}")
        self.get_question()
        

    def calculate_score(self):
        if self.difficulty == "easy":
            return 5 * self.ratio
        elif self.difficulty == "medium":
            return 10 * self.ratio
        elif self.difficulty == "hard":
            return 15 * self.ratio

    def define_ratio(self):
        if self.difficulty == "easy":
            return 10
        elif self.difficulty == "medium":
            return 20
        elif self.difficulty == "hard":
            return 30  

    def fetching_questions(self):
        try:
            x = int(self.num_questions_entry.get())
        except ValueError:
            self.error_label.config(text="Please enter a valid number of questions.")
            return
        if self.online:
            self.error_label.config(text="Fetching questions online...")
            self.questions = self.fetch_trivia_questions_online(amount=int(self.num_questions_entry.get()), category=self.selected_category, 
                                                                difficulty=self.selected_difficulty.get())
            self.questions = self.decode_html_entities(self.questions)
            self.save_questions_to_database(self.questions)  # Save new questions to the database for offline use
        else:
            self.error_label.config(text="No internet connection. Fetching questions from the database...")
            self.questions = self.fetch_questions_from_database(limit=self.num_questions, dif=self.difficulty)
        if not self.questions:
            self.error_label.config(text="No questions available.")
            self.parameter_win.after(3000, self.parameter_win.destroy)
        else:
            self.parameter_win.after(3000, lambda: self.start_game(self.selected_difficulty.get(), self.selected_category, self.num_questions_entry.get()))

    def end_game(self):
        self.quiz_win.destroy()

        endgame_win = Tk()
        endgame_win.title("Trivia Game")
        endgame_win.geometry("300x200")

        endgame_win.grid_rowconfigure(0, weight=1)
        endgame_win.grid_columnconfigure(0, weight=1)

        # Body frames
        f_score = Label(endgame_win, text=f"Your final score: {self.score}", font=("Arial", 12))
        f_score.pack()

        confirm_button = Button(endgame_win, text="Confirm", font=("Arial", 12), command=endgame_win.destroy)
        confirm_button.pack()

        endgame_win.mainloop() 

    def store_points(self, win):
        print(self.score)
        win.destroy()
            
    def Quiz_pararmeters(self):        
        self.parameter_win = Tk()

        self.parameter_win.title("Trivia Game")
        self.parameter_win.geometry("500x400")

        self.parameter_win.grid_rowconfigure(0, weight=1)
        self.parameter_win.grid_columnconfigure(0, weight=1)

        # Body frames
        self.title_frame = Frame(self.parameter_win)
        self.title_frame.pack()

        self.param_frame = Frame(self.parameter_win)
        self.param_frame.pack()

        self.button_frame = Frame(self.parameter_win)
        self.button_frame.pack()

        # titel of the quiz

        title_font = Font(family="Verdana", size=16, weight="bold")
        self.question_label = Label(self.title_frame, text="Trivia Game", font=title_font, fg = "red")
        self.question_label.pack()

        # parameter labels

        # Difficulty
        parameter_font = Font(family="Verdana", size=12, weight="bold")
        self.difficulty_label = Label(self.param_frame, text="Difficulty:", font=parameter_font)
        self.difficulty_label.grid(row=0, column=0, padx=10, pady=10)

        difficulties = ["easy", "medium", "hard"]

        # Variable to store selected value
        self.selected_difficulty = StringVar()
        self.selected_difficulty.set("easy")  # Placeholder text

        # Styled OptionMenu
        dropdown = OptionMenu(self.param_frame, self.selected_difficulty, *difficulties)
        dropdown.config(width=20, font=("Helvetica", 12))
        dropdown.grid(row=0, column=1, padx=10, pady=20)

        # Category
        self.category_label = Label(self.param_frame, text="Category:", font=parameter_font)
        self.category_label.grid(row=1, column=0, padx=10, pady=10)

        categories = ["Any Category", "General Knowledge", "Entertainment: Books", 
                      "Entertainment: Film", "Entertainment: Music", 
                      "Entertainment: Television", "Entertainment: Video Games", 
                      "Entertainment: Board Games", 
                      "Entertainment: Musical & Theatres", "Science & Nature", 
                      "Science: Computers", "Science: Mathematics",
                      "Mythology", "Sports", "Geography", "History", "Politics",
                      "Art", "Celebrities", "Animals", "Vehicles", "Entertainment: Comics", "Science: Gadgets",
                      "Entertainment: Japanese Anime & Manga", "Entertainment: Cartoon & Animations"]

        # Variable to store selected value
        self.selected_category = StringVar()
        self.selected_category.set("Any Category")  # Placeholder text

        # Styled OptionMenu
        dropdown = OptionMenu(self.param_frame, self.selected_category, *categories)
        dropdown.config(width=20, font=("Helvetica", 12))
        dropdown.grid(row=1, column=1, padx=10, pady=20)

        numbers_list =[randint(9, 32), "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32"]
        self.selected_category = int(numbers_list[categories.index(self.selected_category.get())])
        # Number of questions

        self.num_questions_label = Label(self.param_frame, text="Number of questions:", font=parameter_font)
        self.num_questions_label.grid(row=2, column=0, padx=10, pady=10)

        self.num_questions_entry = Entry(self.param_frame, font=("Helvetica", 12))
        self.num_questions_entry.grid(row=2, column=1, padx=10, pady=10)

        # Start button
        self.start_button = Button(self.button_frame, text="Start", font=parameter_font, command= self.fetching_questions)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)

        self.quit_button = Button(self.button_frame, text="Quit", font=parameter_font, command=self.parameter_win.destroy)
        self.quit_button.grid(row=0, column=1, padx=10, pady=10)

        self.error_label = Label(self.button_frame, text="", font=("Helvetica", 12), fg="red")
        self.error_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


        self.parameter_win.mainloop()

QuizInterface()
