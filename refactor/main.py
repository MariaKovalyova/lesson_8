from random import choice

from utils import make_class_questions_list, show_statistics

if __name__ == '__main__':
    questions_list = make_class_questions_list()

    input("Это игра в вопросы. Нажимет Enter, чтобы начать.\n")

    question_index = list(range(len(questions_list)))
    while len(question_index) != 0:  # Цикл для случайного порядка вопросов
        index = choice(question_index)
        questions_list[index].build_question()
        questions_list[index].user_answer = input("Ответ: ")
        questions_list[index].get_feedback()
        question_index.remove(index)

    show_statistics(questions_list)


