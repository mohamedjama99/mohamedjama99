class Question:
    def __init__(self, question_promt, answer_alternatives, correct_answer_nbr):
        self.question = question_promt
        self.answer = correct_answer_nbr
        self.alternatives = answer_alternatives

    def __str__(self):
        name = "Alternatives " + "\n"
        alt = 1
        for j in self.alternatives:
            name = name + str(alt) +": " + j + "\n"
            alt += 1
        return(self.question + "\n" + name + "\n")

    def answer_checker(self, alt):
        if alt == self.answer:
            return True
                            
 
score = 0
loop = 0

for question in questions:
    loop += 1
    print(question)
    try:
        answ = int(input("The answer is?: "))
        if question.answer_checker(answ) == True:
            score += 1
            print(f"That is correct! your score is {score}.  You have gotten {score}/{loop} correct."+"\n")
        else:
            print(f"HAH! you suck that is Incorrect!! the score is {score}. You have gotten {score}/{loop} correct."+"\n")
    except ValueError:
        print("You need to input a valid answer. You have just forfitted a point.")
        score-= 1
        print(f"your score is now {score}/{loop}" + "\n")
