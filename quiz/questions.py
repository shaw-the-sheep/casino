from sqlite3 import connect
from requests import get
from html import unescape
from random import shuffle as shuf
from socket import setdefaulttimeout, create_connection
from socket import error as err

class Questions:
    def __init__(self):
        self.online = self.is_online()
        
    DB_FILE = "trivia_questions.db"
    def save_questions_to_database(self, questions):
        """Save fetched questions to the SQLite database."""
        conn = connect(self.DB_FILE)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                correct_answer TEXT,
                incorrect_answers TEXT
            )
        """)  # Ensure the table exists

        for question in questions:
            cursor.execute("""
                INSERT INTO questions (question, correct_answer, incorrect_answers)
                VALUES (?, ?, ?)
            """, (
                question['question'],
                question['correct_answer'],
                ";".join(question['incorrect_answers'])  # Store incorrect answers as a semicolon-separated string
            ))

        conn.commit()
        conn.close()

    def fetch_questions_from_database(self, dif, limit=10):
        """Fetch questions from the SQLite database."""
        conn = connect(self.DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT question, correct_answer, incorrect_answers FROM questions ORDER BY RANDOM() LIMIT ? where difficulty = ?", (limit, dif))
        rows = cursor.fetchall()
        conn.close()

        questions = []
        for row in rows:
            questions.append({
                'question': row[0],
                'correct_answer': row[1],
                'incorrect_answers': row[2].split(";")  # Convert the semicolon-separated string back to a list
            })

        return questions

    def fetch_trivia_questions_online(self, amount=10, category=9, difficulty='easy'):
        """Fetch trivia questions from the Open Trivia Database API."""
        url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple"
        response = get(url)
        data = response.json()

        if data['response_code'] == 0:
            return data['results']
        else:
            print("Error fetching trivia questions.")
            return []

    def decode_html_entities(self, data):
        """Decode HTML entities in questions and options."""
        for question in data:
            question['question'] = unescape(question['question'])
            question['correct_answer'] = unescape(question['correct_answer'])
            question['incorrect_answers'] = [
                unescape(answer) for answer in question['incorrect_answers']
            ]
        return data

    def shuffle_answers(self, question, nb_question):
        """Shuffle the answers and ensure the correct answer is included."""
        options = question[nb_question]['incorrect_answers'] + [question[nb_question]['correct_answer']]
        shuf(options)
        return options

    def is_online(self, host="8.8.8.8", port=53, timeout=3):
        """
        Check if the computer is online by attempting to connect to a known server.
        Default is Google's public DNS server.
        """
        try:
            setdefaulttimeout(timeout)
            create_connection((host, port))
            return True
        except err:
            return False


if __name__ == "__main__":
    game = Questions()
    print(game.fetch_trivia_questions_online(category=9, amount=10, difficulty="easy"))
