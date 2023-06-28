class Question:

    def __init__(self, q_category, q_type, q_difficulty, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
        self.category = q_category
        self.type = q_type
        self.difficulty = q_difficulty

