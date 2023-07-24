from question_model import Question
from data import question_data

class QuizBrain:
    def __init__(self,question_list):
        self.q_number=0
        self.q_list=question_list
        self.score=0
    def still_has_question(self):
        if self.q_number<len(self.q_list):
            return True
        else:
            False
    def next_question(self):
        current_question=self.q_list[self.q_number]
        self.q_number=self.q_number+1
        user_answer=input(f"Q:{self.q_number} {current_question.question} 'True/false:' ")
        check_answer=self.check_answer(user_answer,current_question.answer)
        print(f'score {self.score}/{self.q_number}')

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            return True
        else:
            print('Incorrect ')
            return False