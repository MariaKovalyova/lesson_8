from random import choice  # Функция для случайного выбора вопроса

questions_list = [{  #Словарь с заготовкой для вопросов
    "q": "How many days do we have in a week?",
    "d": "1",
    "a": "7"
}, {
    "q": "How many letters are there in the English alphabet?",
    "d": "3",
    "a": "26"
}, {
    "q": "How many sides are there in a triangle?",
    "d": "2",
    "a": "3"
}, {
    "q": "How many years are there in one Millennium?",
    "d": "2",
    "a": "1000"
}, {
    "q": "How many sides does hexagon have?",
    "d": "4",
    "a": "6"
}]


class Question:
    def __init__(self, question, difficult, answer):
        self.question = question
        self.diffiult = difficult
        self.answer = answer

        self.is_asked = False
        self.user_answer = None
        self.score = int(difficult) * 10

    def get_points(self):
        return self.score

    def build_question(self):
        print(f"Вопрос: {self.question}  \nСложность: {self.diffiult}/5")

    def is_correct(self):
        if self.answer == self.user_answer:
            return True
        return False

    def feedback(self):
        if self.is_correct():
            print(f"Ответ верный, получено {self.score} баллов\n")
        else:
            print(f"Ответ неверный, верный ответ - {self.answer}\n")


def make_class_questions_list(questions_list):  # Создания экземпляров класса с вопросами
    questions = []
    for question in questions_list:
        q = question.get("q")
        d = question.get("d")
        a = question.get("a")
        questions.append(Question(q, d, a))
    return questions


def static(questions):  # Функция вывода статистики
    score = 0  # Счётчик очков
    right = 0  # Счётчик правильных ответов

    for question in questions:
        if question.is_correct():
            right += 1
            score += question.get_points()

    print("\nВот и всё!")
    print(f"Отвечено {right} вопроса из {len(questions)}")
    print(f"Набрано баллов: {score}")


def main():
    questions = make_class_questions_list(questions_list)  # Функция для создания списка экзепляров класса с вопросами

    input("Это игра в вопросы. Нажимет Enter, чтобы начать.\n")

    question_index = list(range(len(questions)))
    while len(question_index) != 0:  # Цикл для случайного порядка вопросов
        index = choice(question_index)
        questions[index].build_question()
        questions[index].user_answer = input("Ответ: ")
        questions[index].feedback()
        question_index.remove(index)

    static(questions)


main()