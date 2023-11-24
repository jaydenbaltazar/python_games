import random

words = []
definitions = []
times = int(input('How many terms do you need to study: '))
for cards in range(times):
    word = input('Enter your term: ').lower()
    words.append(word)
    definition = input(f'What is the definition of {word}: ').lower()
    definitions.append(definition)
answers = []
for i in range(len(words)):
    word = words[i] + ': ' + definitions[i]
    answers.append(word.capitalize())
print('Here are all your flashcards.')
for card in answers:
    print(card.capitalize())

program = True
while program:
    quiz = input('Do you want to be quizzed on the terms or study on your own?(Quiz/Own): ').lower()
    if quiz == 'o' or quiz == 'own':
        while program:
            term = input('What term would you like to get: ').lower()
            for word in words:
                if term == word:
                    indices = [i for i, term in enumerate(words) if term == word]
                    for index in indices:
                        print(answers[index])
            finish = input('Do you want to get another term? ').lower()
            if finish == 'y' or finish == 'yes':
                continue
            else:
                break
    elif quiz == 'q' or quiz == 'quiz':
        correct = 0
        incorrect = 0
        while program:
            for times in range(len(definitions)):
                question = random.choice(definitions)
                term = input(f'What is the term for {question}? ')
                indices = [i for i, word in enumerate(words) if term == word]
                for i in indices:
                    term = definitions[i]
                    if term == question:
                        print(f'That is the correct term.')
                        correct += 1
                    elif term != question:
                        print(f"That isn't the correct term.")
                        incorrect += 1
            finish = input('Do you want to continue the quizzing? ')
            if finish == 'y' or finish == 'yes':
                continue
            else:
                print(f'Thanks for doing the quiz. You got {correct} correct and {incorrect} incorrect.')
                break
    again = input('Do you want to continue studying? ').lower()
    if again == 'y' or again == 'yes':
        continue
    else:
        print('Good job studying today!')
        program = False


