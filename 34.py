# ----------------------------------------------------------------
def new_game() :
    guesses = []
    correct_guesses =0
    question_no = 1
    for key in questions :
        print("----------------------------------------------------------------")
        print(key)
        for i in options [question_no -1] :
            print(i)
            guesses=input("enter (A,B,C,D) :")
            guesses=guesses.upper()

            check_answer(questions.get(key),guesses)
        question_no += 1

# ----------------------------------------------------------------
def check_answer(answers,guesses):
    if answers == guesses :
        print("correct")
    pass
# ----------------------------------------------------------------
def display_score ():
    pass
# ----------------------------------------------------------------
def play_again():
    pass
# ----------------------------------------------------------------

questions ={
    "Who created Python :":" A",
    "What year was python created :":" B",
    "Is the Earth Round : ":" A"
}
options=[["A.Guido van Rossum", "B.Nikola Tesla ","C.Ratan Tata","D.Danis ritchie "],
         ["A.1989","B.1991","C.2000","D.2016"],
         ["A.True","B.False","Sometimes'true ","D.None of above"]]
new_game()