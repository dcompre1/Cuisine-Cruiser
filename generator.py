import requests
import pandas as pd
import sqlalchemy as db
import random
from recipe_funcs import print_recipe, has_restrictions, filter_meals


print("Welcome to the Random Recipe Generator!")

while(True):

    # prompt user: input preferences or receive recipe?
    skip = input("\nTo begin, please indicate whether you would like" +
                 " to input preferences like ingredients to exclude and " +
                 " cuisine type, or receive a recipe now:" +
                 " \n(y) yes, receive now\n(n) no, I have" +
                 " preferences to enter\n")
    if skip != "y" and skip != "n":
        print("You must enter 'y' or 'n'.")
        exit()
    if skip == "y":
        # no restrictions
        # make into a loop for input to prompt if they want a different recipe
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
        response = requests.get(url)
        meal = response.json()['meals'][0]
        print_recipe(meal)
        exit()

    # yes restrictions
    # prompt user: vegan or vegetarian?
    restricts = input("\nDo you have any ingredients that you would like to exclude" +
                 " from potential recipes?"
                 " If you are vegan or vegetarian:\n" +
                 "press (v) for Vegan\n" +
                 "press (t) for Vegetarian\n" +
                 "Otherwise enter ingredient(s) with comma in between: \n"
                 + "or type \"none\"")

    if restricts == "":
        print("You have to input something") # TODO: fix
        exit()
    r = restricts.lower()
    restrictions = r.split(",")

    # prompt for cuisine type
    yes = True
    while (yes):
        cuisine = input("\nFinally, please indicate a cuisine type,\n" +
                            "to see a list of possible cuisine types " +
                            "press (c), or to receive a recipe result press any key:")
        cuisine = cuisine.lower().capitalize()
        if cuisine == "c":
            response = requests.get("https://www.themealdb.com" +
                                        "/api/json/v1/1/list.php?a=list")
            data = response.json()["meals"]
            areas = []
            for datum in data:
                areas.append(datum["strArea"])
                print(areas)
        else:
            yes = False

        # API get recipes based on MI, if not, get based on vegan or vegetarian
    if restricts == "v":
        response = requests.get("https://www.themealdb.com" +
                                "/api/json/v1/1/filter.php?c=Vegan")
        response_data_nested = response.json()
        response_data_list = response_data_nested.get("meals")
        df = pd.DataFrame(response_data_list)
        engine = db.create_engine('sqlite:///Vegan.db')
        df.to_sql('meals', con=engine, if_exists='replace', index=False)
        meal_data = filter_meals(engine, "v",restrictions, cuisine)
    elif restricts == "t":
        response = requests.get("https://www.themealdb.com" +
                                "/api/json/v1/1/filter.php?c=Vegetarian")
        response_data_nested = response.json()
        response_data_list = response_data_nested.get("meals")
        df = pd.DataFrame(response_data_list)
        engine = db.create_engine('sqlite:///Vegetarian.db')
        df.to_sql('meals', con=engine, if_exists='replace', index=False)
        meal_data = filter_meals(engine, "t", restrictions, cuisine)
    elif cuisine != "":
        response = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?a=" + cuisine)
        response_data_nested = response.json()
        response_data_list = response_data_nested.get("meals")
        df = pd.DataFrame(response_data_list)
        engine = db.create_engine('sqlite:///Ingredient.db')
        df.to_sql('meals', con=engine, if_exists='replace', index=False)
        meal_data = filter_meals(engine, "n", restrictions, cuisine)
    else:
        print("You must enter a cuisine type.")
        exit() # TODO change into loop later

   # meal_data = response.json()["meals"]
    try:
        meal_data_len = len(meal_data)
    except TypeError:
        print("There are no recipes with your preferences in the database.")
        exit()

    # randomize meal choice
    chosen_meal = random.choice(meal_data)
    print_recipe(chosen_meal)
    meal_data.remove(chosen_meal)

    while True:
        decision = input("\nIf you would like to view a different" +
                         " recipe press (y)," +
                         "\nif you would like to begin the search" +
                         " over again press (p),\n" +
                         "otherwise press (q) to quit\n")
        if decision == "y":
            if len(meal_data) == 0:
                print("There are no other recipes with your preferences in the database")
            else:
                chosen_meal = random.choice(meal_data)
                print_recipe(chosen_meal)
                meal_data.remove(chosen_meal)
            # this will cause big loop to start over
        if decision == "p":
            break
            # this will cause big loop to end program
        if decision == "q":
            exit()

