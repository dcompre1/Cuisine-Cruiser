import requests
import random
from recipe_funcs import print_recipe, has_restrictions, filter_meals, \
                         end_program_loop, end_program_loop_2, \
                         create_database, print_cuisines
from recipe_strings import get_first_message, get_restrictions_prompt, \
                           get_cuisine_prompt

print("Welcome to the Cuisine Cruiser!")

while True:
    # prompt user: input preferences or receive recipe?
    skip = input(get_first_message())
    while skip != "y" and skip != "n":
        skip = input("You must enter 'y' or 'n'.\n")
    if skip == "y":
        # recieve random recipe
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
        response = requests.get(url)
        meal = response.json()['meals'][0]
        print_recipe(meal)
        result = end_program_loop_2()
        if result == "q":
            exit()
        elif result == "p":
            continue

    # input restrictions
    # prompt user: vegan or vegetarian?
    restricts = input(get_restrictions_prompt())
    while restricts == "":
        restricts = input("Please enter a list of ingredients" +
                          " or type \"none\":\n")
    r = restricts.lower()
    restrictions = r.split(", ")

    # prompt for cuisine type
    cuisine = input(get_cuisine_prompt())
    while True:
        cuisine = cuisine.lower().capitalize()
        if cuisine == "C":
            print_cuisines()
            cuisine = input(get_cuisine_prompt())
        elif cuisine == "":
            while cuisine == "":
                cuisine = input("Please enter a cuisine type:\n")
        else:
            break

    # API get recipes based on cuisine, if not, get based on vegan/vegetarian
    # create databases
    if restricts == "v":
        response = requests.get("https://www.themealdb.com" +
                                "/api/json/v1/1/filter.php?c=Vegan")
        engine = create_database("Vegan", response)
        if engine == "q":
            exit()
        meal_data = filter_meals(engine, "v", restrictions, cuisine)
    elif restricts == "t":
        response = requests.get("https://www.themealdb.com" +
                                "/api/json/v1/1/filter.php?c=Vegetarian")
        engine = create_database("Vegetarian", response)
        if engine == "q":
            exit()
        meal_data = filter_meals(engine, "t", restrictions, cuisine)
    elif cuisine != "":
        response = requests.get("https://www.themealdb.com" +
                                "/api/json/v1/1/filter.php?a=" + cuisine)
        engine = create_database("Cuisine", response)
        if engine == "q":
            exit()
        meal_data = filter_meals(engine, "n", restrictions, cuisine)

    # randomize meal choice, catch error if meal_data is empty
    try:
        chosen_meal = random.choice(meal_data)
    except IndexError:
        print("There are no recipes with your preferences in the database.")
        exit()
    print_recipe(chosen_meal)
    meal_data.remove(chosen_meal)

    # call loop to end program
    result = end_program_loop(meal_data)
    if result == "p":
        continue
    if result == "q":
        exit()
