# 1. Erstelle ein Programm mit Rezepten:
# a. Schreibe Variablen mit Zutatenlisten, bspw spiegelei = [“Ei”, “Salz”,
# “Paprika”, “Pfeffer”]
# b. Schreibe eine Funktion, die beim ausführen der Datei gestartet wird, die
# i. Den User fragt, welches Rezept ausgegeben werden soll
# ii. Die Zutaten für das Rezept auf der Konsole ausgibt

# Creating recipes

scramble_eggs = ['olive oil', 'eggs', 'ham', 'spinach']
pancakes = ['milk', 'flour', 'egg']

# Adding them to a dictionary

recipes = {'scramble_eggs': scramble_eggs, 'pancakes': pancakes}


def available_recipes():
    print(f'Available recipes:')
    for i in recipes:
        print (i)


available_recipes()

def recipe():
    if user_input in recipes:
        print(f'The ingredients for {user_input} are:')
        for ingredients in recipes[user_input]:
            print(f'- {ingredients}')
    else:
        print(f'There is no such recipe in the library.')


user_input = input(f'Please write a name of a desired recipe: ')

recipe()

    


# user_input = input(f'Please write a name of the desired recipe: ')

# #print(f'Ingriedients needet for {user_input} are ')



