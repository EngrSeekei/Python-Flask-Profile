def grade_question(answer_key, student_answers, question_number):
    correct_answer = answer_key[question_number]
    student_answer = student_answers[question_number]
    return correct_answer == student_answer

def calculate_score(answer_key, student_answers):
    total_score = sum(grade_question(answer_key, student_answers, i) for i in range(len(answer_key)))
    return total_score