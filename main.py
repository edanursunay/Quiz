import Classes
import quız_soruları

quiz_list = quız_soruları.question_list

quiz = Classes.Quiz(quiz_list)
quiz.showQuestion()