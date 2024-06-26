def reponse_questionnaire(reponse_question):
    reponse_user = input("Votre reponse:")
    if reponse_question == reponse_user:
        print("Bonne reponse")
    else:
        print("Mauvaise reponse")

def questionnaire(question, rep_possibe,nb_rep_possible, index_rep_possible=0):
    print(question)
    for i in range(nb_rep_possible):
        print(index_rep_possible[i] ,"->", rep_possibe[i])

    # print(f"({index_rep_possible[1]}) -> {rep_possibe[1]}")
    # print(f"({index_rep_possible[2]}) -> {rep_possibe[2]}")
    # print(f"({index_rep_possible[3]}) -> {rep_possibe[3]}")

index_rep_possible = ["a","b", "c", "d"]

question_1 = "Quelle est la capitale de la France ?"
reponse_possible_1 = ["Mareille", "Nice", "Paris", "Nante"]

question_2 = "Quelle est la capitale de l'Italie ?"
reponse_possible_2 = ("Rome", "Juventus", "Venis", "Milan")

question_3 = "Quelle le nom de votre chien ?"
reponse_possible_3 = ("Rocky", "Milou", "Mars", "Champion")

questionnaire(question_1, reponse_possible_1, 4,index_rep_possible)
reponse_questionnaire("c")


questionnaire(question_2, reponse_possible_2, 4, index_rep_possible)
reponse_questionnaire("a")

questionnaire(question_3, reponse_possible_3, 4, index_rep_possible)
reponse_questionnaire("d")
