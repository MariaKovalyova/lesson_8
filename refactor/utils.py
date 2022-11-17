import json

from classes import Question

def make_class_questions_list():
    questions_list = []
    with open('questions.json', 'r', encoding='utf-8') as file:
        questions_json = json.load(file)
    for question in questions_json:
        q = question.get("q")
        d = question.get("d")
        a = question.get("a")
        questions_list.append(Question(q, d, a))
    return questions_list


def show_statistics(questions_list):
    score = 0
    right_answers = 0

    for question in questions_list:
        if question.is_answer_correct():
            right_answers += 1
            score += question.get_score()

    print("\nВот и всё!")
    print(f"Отвечено {right_answers} вопроса из {len(questions_list)}")
    print(f"Набрано баллов: {score}")