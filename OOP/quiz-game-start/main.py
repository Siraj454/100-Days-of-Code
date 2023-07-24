from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
questions=question_data
#create question object 

    
# create a list of question and answer , with question object
q_object_data=[]
for q in questions:
    q_obj=Question(q['text'],q['answer'])
    q_object_data.append(q_obj)
quiz=QuizBrain(q_object_data)
while quiz.still_has_question()==True:
    quiz.next_question()