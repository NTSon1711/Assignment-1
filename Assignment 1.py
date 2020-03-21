questions = {"strong": "Do ye like yer drinks strong?",
             "salty": "Do ye like it with a salty tang?",
             "bitter": "Are ye a lubber who likes it bitter?",
             "sweet": "Would ye like a bit of sweetness with yer poison?",
             "fruity": "Are ye one for a fruity finish?"}

ingredients = {"strong": ["glug of rum", "slug of whisky", "splash of gin"],
               "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
               "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
               "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
               "fruity": ["slice of orange", "dash of cassis", "cherry on top"]}

# Given two above dictionaries, construct the Python program (using functions) to ask users entering their tastes and then match randomly with the ingredients (print out outputs for user).

import random

def answer_question():
    answers = {}
    for type, question in questions.items():
        print(question, 'y/n')
        answers[type] = input()
        while answers[type] not in ['y', 'n']:
            print('Enter the wrong syntax. Please try again')
            answers[type] = input()

    return answers

def make_drink(answers):
    drink = []
    for type, answer in answers.items():
        if answer == 'y':
            drink.append(random.choice(ingredients[type]))

    return drink


def order():
    answers = answer_question()
    drink = make_drink(answers)
    print('\n' + 'Ingredients of drinking included are:' + '\n' + '-'*30)
    for ingredient in drink:
        print("A {}".format(ingredient))
    print('-'*30 + '\n' + 'Ẹnjoy your drinking. Thank you!')

order()