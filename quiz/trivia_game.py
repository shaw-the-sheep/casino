from questions import Questions
from quiz_interface import QuizInterface


class TriviaGame:
    def init__(self):
        self.ui = QuizInterface()
        self.q = Questions()

    def play_game(self):
        questions = self.ui.questions
        ratio = self.define_ratio()
        score = 0
        for idx, question in enumerate(questions, 1):
            print(f"\nQuestion {idx}: {question['question']}")
            options = self.q.shuffle_answers(question)
            for i, option in enumerate(options, 1):
                print(f"{i}) {option}")

            user_answer = input("Your answer (1/2/3/4): ").strip()
            correct_option = options.index(question['correct_answer']) + 1
            if user_answer == str(correct_option):
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question['correct_answer']}.")

        print(f"\nYour final score: {score}/{len(questions)}")

    def define_ratio(self):
        if self.ui.difficulty == "easy":
            return 10
        elif self.ui.difficulty == "medium":
            return 20
        elif self.ui.difficulty == "hard":
            return 30

TriviaGame()