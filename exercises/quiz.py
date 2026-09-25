questions = ("Who was the first member to officially join the Straw Hat Pirates after Luffy? ",
           "What is the name of the island where the Straw Hats first encounter Dr. Kureha and Tony Tony Chopper? ", 
           "Which of these characters was formerly a member of the Seven Warlords of the Sea? ",
           "What was the name of the sword Zoro used that was originally owned by Kuina? ",
           "What is the name of the giant elephant that carries Zou on its back? ", )

options = (( "A. Zoro ", "B. Nami ", "C. Ussop ", "D. Sanji " ),
           ( "A. Alabasta ", "B. Drum Island ", "C. Jaya ", "D. Amazon Lily " ),
           ( "A. Kuzan ", "B. Shamrock ", "C. Rayleigh ", "D. Trafalgar D. Water Law " ),
           ( "A. Wado Ichimonji ", "B. Enma ", "C. Sandai Kitetsu ", "D. Shusui " ),
           ( "A. Laboon ", "B. Haathwi ", "C. Zouneisha ", "D. Davy Jones " ))


answers = ("A", "B", "D", "A", "C")
guesses = []
que_num = 0
score = 0

for question in questions:
    print("-----------------------------------")
    print()
    print(f"{que_num + 1}. {question}")
    for option in options[que_num]: #This lets only specific question number to be printed serially going from index zero to forever, rather than printing all the other options in the unrelated questions. 
        print(option)
    guess = str(input(f"Enter your guessed option to question {que_num + 1}: ").upper().strip())
    if guess == answers[que_num]:
        print(f"Option {guess} is CORRECT! ")
        score += 1
    else:
        print("INCORRECT!")
        print(f"Option {answers[que_num]} is the correct option.")
    que_num += 1

print(f"YOU HAVE SCORED {score} out of {que_num}! ")

    

