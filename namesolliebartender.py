import random
import sys

questions = {
    "bitter": "Do you like bitters?",
    "salty": "Drinks with a salty tang?",
    "strong": "Do you like your drinks strong?",
    "sweet": "Would you like a bit of sweetness?",
    "fruity": "Would you like a bit of fruitiness?"
}

ingredients = {
    "bitter": ["bitters", "splash of tonic", "twist of lemon"],
    "salty": ["three olives", "salt poured rim"],
    "strong": ["two thumbs of rum", "slug of whiskey", "splash of vodka"],
    "sweet": ["sugar rim", "spoonful of honey", "chocolate stirrring stick"],
    "fruity": ["slice of orange", "pomegranate seeds", "cherry on top"]
}

drinknames = {
    "bitter": ["Chicago Towers"],
    "salty": ["Ocean Sea Breeze"],
    "strong": ["Straight Up"],
    "sweet": ["Sugar Mist"],
    "fruity": ["Shirley Temple"]
}

def find_preferences():
    preferences = {}
    for type, question in questions.iteritems():
        print question
        preferences[type] = raw_input().lower() in ["y", "yes"]
        print ""
    return preferences

def make_drink(preferences):
    drink = []
    for ingredient_type, liked in preferences.iteritems():
        if not liked:
            continue

        drink.append(random.choice(ingredients[ingredient_type]))
    return drink

def drink_name(preferences):
    drinkname = []
    for ingredient_type, liked in preferences.iteritems():
        if not liked:
            continue
        drinkname.append(random.choice(drinknames[ingredient_type]))
    return random.choice(drinkname)


def main():
    preferences = find_preferences()
    drink = make_drink(preferences)
    drinkname = drink_name(preferences)
    print drinkname
    print "It's full of good stuff.  The recipe is:"
    for ingredient in drink:
        print "A {}".format(ingredient)


if __name__ == "__main__":
    main()
