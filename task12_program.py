RIGHT_ANSWER = 1


def correct_answer():
    choose_answer = int(input("Enter the answer: "))
    if choose_answer == RIGHT_ANSWER:
        print("Congrats! It is a correct answer. ")
    else:
        print("The right answer was ", RIGHT_ANSWER)


correct_answer()
