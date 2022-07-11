import pandas as pd
import requests
import random
import sqlalchemy as db
from recipe_strings import get_loop_message


def print_recipe(meal):
    '''print meal and recipe details'''
    meal_name = meal['strMeal']
    instructions = meal['strInstructions']
    yt = meal['strYoutube']

    print("\nHere is your recipe: " + meal_name + "\n")
    print(instructions + "\n")

    print("Ingredients:")
    ingredient = meal['strIngredient1']
    measure = meal['strMeasure1']
    i = 2
    while ingredient is not None and ingredient != "" and i < 21:
        print(measure + " " + ingredient)
        ingredient = meal['strIngredient' + str(i)]
        measure = meal['strMeasure' + str(i)]
        i += 1
    if yt != "":
        print("\nHere is a YouTube tutorial for your recipe: " + yt)


def print_cuisines():
    '''print all cuisine types to user'''
    response = requests.get("https://www.themealdb.com" +
                            "/api/json/v1/1/list.php?a=list")
    data = response.json()["meals"]
    areas = []
    print("")
    for datum in data:
        print(datum["strArea"])


def has_restrictions(meal, restrictions):
    '''function to check that meal does not contain users restrictions'''
    ingredient = meal['strIngredient1']
    j = 2
    while ingredient is not None and ingredient != "" and j < 21:
        ingredient = ingredient.lower()
        for i in range(len(restrictions)):
            if restrictions[i] in ingredient:
                return True
        j += 1
        ingredient = meal['strIngredient' + str(j)]
    return False


def no_cuisine(meal, cuisine):
    '''function to check meal originates from the correct area'''
    area = meal['strArea']
    if area == cuisine:
        return False
    return True


def filter_meals(engine, c, restrictions, cuisine):
    '''Query database and update based on restrictions or cuisine
       returns list of possible meals'''
    query_results = engine.execute("SELECT idMeal FROM meals").fetchall()
    num_ids = engine.execute("SELECT COUNT(idMeal) FROM " +
                             "meals").fetchall()[0][0]
    meals = []
    for i in range(num_ids):
        id = pd.DataFrame(query_results)[0][i]
        result = requests.get("https://www.themealdb.com" +
                              "/api/json/v1/1/lookup.php?i=" + id)
        meal = result.json()["meals"][0]
        # filter out based on cuisine
        if c == "v" or c == "t":
            r = no_cuisine(meal, cuisine)
        else:  # filter out based on restrictions
            if restrictions[0] == "none":
                r = False
            else:
                r = has_restrictions(meal, restrictions)
        if r is True:
            engine.execute("DELETE FROM meals WHERE idMeal = " + id)
        else:
            meals.append(meal)
    return meals


def end_program_loop(data):
    '''prompt user to end the program once they've received a recipe'''
    while True:
        decision = input(get_loop_message())
        if decision == "y":
            if len(data) == 0:
                print("There are no other recipes " +
                      "with your preferences in the database.")
            else:
                chosen_meal = random.choice(data)
                print_recipe(chosen_meal)
                data.remove(chosen_meal)
        elif decision == "p":
            return "p"
        elif decision == "q":
            return "q"


def end_program_loop_2():
    '''prompt user to end program when they've received random recipe'''
    while True:
        decision = input(get_loop_message())
        if decision == "y":
            url = "https://www.themealdb.com/api/json/v1/1/random.php"
            response = requests.get(url)
            meal = response.json()['meals'][0]
            print_recipe(meal)
        elif decision == "p":
            return "p"
        elif decision == "q":
            return "q"


def create_database(category, response):
    '''create database storing all vegetarian meals, vegan meals, or
       based on cuisine'''
    try:
        response_data_nested = response.json()
        response_data_list = response_data_nested.get("meals")
        df = pd.DataFrame(response_data_list)
        engine = db.create_engine("sqlite:///" + category + ".db")
        df.to_sql('meals', con=engine, if_exists='replace', index=False)
        return engine
    except Exception as e:
        print("You entered invalid input")
        return "q"
