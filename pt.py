score = 0
print('Это викторина на знание кухни разных народов. Ответь на вопросы и узнай, насколько хорошо ты разбираешься в еде!')

question1 = "Кто придумал эчпочмак?"
question2 = "Луковый суп — это блюдо какой кухни?"
question3 = "Где родина начос?"
question4 = "Как называются китайские пельмени?"
question5 = "В национальную кухню какой страны входят драники?"

true_answer1 = "татары"
true_answer2 = "Франция"
true_answer3 = "Мексика"
true_answer4 = "гёдза"
true_answer5 = "Беларусь"

answer1 = input(question1)
if answer1  == true_answer1 :
    score   = score + 1
answer2 = input(question2)
if answer2  == true_answer2 :
    score   = score + 1
answer3 = input(question3)
if answer3  == true_answer3 :
    score   = score + 1
answer4 = input(question4)
if answer4  == true_answer4 :
    score   = score + 1
answer5 = input(question5)
if answer5  == true_answer5 :
    score   = score + 1

if score >= 3:
    print("Вы набрали много баллов! Вас можно считать экспертом")
else:
    print("Вы набрали не очень много баллов. Расширяйте свой кругозор, вам есть, куда стремиться")

