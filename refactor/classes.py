class Question:
    def __init__(self, question, difficult, answer):
        self.question = question
        self.diffiult = difficult
        self.answer = answer

        self.is_question_asked = False
        self.user_answer = None
        self.score = int(difficult) * 10

    def get_score(self):
        return self.score

    def build_question(self):
        print(f"Вопрос: {self.question}  \nСложность: {self.diffiult}/5")

    def is_answer_correct(self):
        if self.answer == self.user_answer:
            return True
        return False

    def get_feedback(self):
        if self.is_answer_correct():
            print(f"Ответ верный, получено {self.score} баллов\n")
        else:
            print(f"Ответ неверный, верный ответ - {self.answer}\n")