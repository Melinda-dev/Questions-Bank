#TODO: asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we are the end of the quiz


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number <= len(self.questions_list):
            return True
        else:
            return False

    def next_question(self):
        '''
        Retrieve the item at the current question_number from the question_list.
        use the input() function to show the user the question text and ask for the user's answer.
        :return:
        '''
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}(True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
            print(f"Te current answer was:{correct_answer}")
            print(f"Your current score is: {self.score/self.question_number}")
        else:
            print("That is wrong. ")




