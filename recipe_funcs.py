import pandas as pd

def print_recipe(meal):
    '''print meal and recipe details'''
    meal_name = meal['strMeal']
    instructions = meal['strInstructions']
    yt = meal['strYoutube']

    print("Here is your recipe: " + meal_name)
    # print(instructions)
    i = 1
    ingredient = meal['strIngredient' + str(i)]
    measure = meal['strMeasure' + str(i)]
    while ingredient is not None and ingredient != "":
        print(measure + " " + ingredient)
        ingredient = meal['strIngredient' + str(i)]
        measure = meal['strMeasure' + str(i)]
        i += 1
    if yt != "":
        print("Here is a youtube tutorial for this recipe: " + yt)


def has_restrictions(meal, restrictions):
    '''function to check that meal does not contain users restrictions'''
    i = 1
    while i < 21:
        ingredient = meal['strIngredient' + str(i)]
        ingredient = ingredient.lower()
        if ingredient in restrictions:
            return True
    return False

def filter_meals(engine, restrictions):
    query_results = engine.execute("SELECT idMeal FROM meals").fetchall()
    # print(pd.DataFrame(query_result))
    num_ids = engine.execute("SELECT COUNT(idMeal) FROM meals").fetchall()
    print(num_ids)
    # get ids
    # for each id, make an api call so we can get ingredients
    # if any ingredients overlap with those in restrictions, remove meal from database 
    