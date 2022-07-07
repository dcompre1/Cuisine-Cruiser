import pandas as pd
import requests

def print_recipe(meal):
    '''print meal and recipe details'''
    meal_name = meal['strMeal']
    instructions = meal['strInstructions']
    yt = meal['strYoutube']

    print("Here is your recipe: " + meal_name)
    # print(instructions)

    ingredient = meal['strIngredient1']
    measure = meal['strMeasure1']
    i = 2
    while ingredient is not None and ingredient != "":
        print(measure + " " + ingredient)
        ingredient = meal['strIngredient' + str(i)]
        measure = meal['strMeasure' + str(i)]
        i += 1
    if yt != "":
        print("Here is a youtube tutorial for this recipe: " + yt)


def has_restrictions(meal, restrictions):
    '''function to check that meal does not contain users restrictions'''
    ingredient = meal['strIngredient1']
    j = 2
    while ingredient is not None and ingredient != "":
        ingredient = ingredient.lower()
        for i in range(len(restrictions)):
            if restrictions[i] in ingredient:
                return True
        j += 1
        ingredient = meal['strIngredient' + str(j)]
    return False

def filter_meals(engine, restrictions):
    query_results = engine.execute("SELECT idMeal FROM meals").fetchall()
    num_ids = engine.execute("SELECT COUNT(idMeal) FROM meals").fetchall()[0][0]
    meals = []
    for i in range(num_ids):
        id = pd.DataFrame(query_results)[0][i]
        result = requests.get("https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + id)
        meal = result.json()["meals"][0]
        r = has_restrictions(meal, restrictions)
        # has restrictions, so needs to be removed from database
        if r == True:
            engine.execute("DELETE FROM meals WHERE idMeal = " + id)
        else:
            meals.append(meal)
    query_results = engine.execute("SELECT idMeal FROM meals").fetchall()
    return meals
    # if any ingredients overlap with those in restrictions, remove meal from database
    # save meal info of meals that don't have restrictions

