class QuizBrain:

    def __init__(self, list_of_questions):
        self.question_number = 0
        self.list_of_questions = list_of_questions

    def next_question(self):
        current_question = self.list_of_questions[self.question_number]
        self.question_number += 1
        input(f"Q{self.question_number} {current_question.question} (True/False): ")
