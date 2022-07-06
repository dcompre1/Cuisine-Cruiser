import requests
import pandas as pd
import random
from recipe_funcs import print_recipe, has_restrictions


print("Welcome to the Random Recipe Generator!")

# go = True
while(True):

    # prompt user: input preferences or receive recipe?
    skip = input("\nTo begin, please indicate whether you would like" +
                 " to input preferences like ingredients, " +
                 "cuisine type, etc. or receive a recipe now:" +
                 " \n(y) yes, receive now\n(n) no, I have" +
                 " preferences to enter\n")
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
    diet = input("\nIndicate if you are vegan or vegetarian:\n" +
                 "press (v) for Vegan\n" +
                 "press (t) for Vegetarian\n" +
                 "press any other key to continue: ")
    # if not vegan or vegetarian, prompt for main ingredient
    if diet != "v" and diet != "t":
        main_in = input("\nAre you craving a main ingredient" +
                        " that you would like" +
                        " to include in your dish? If yes, please" +
                        " enter the name, if not press (n):")
        main_in = main_in.replace(" ", "_")
        main_in = main_in.lower()
        # prompt for any restrictions
        ''' restricts = input("\nDo you have any ingredients" +
                          "that you would like to exclude" +
                          " from potential meals?\n" +
                          "Please enter each ingredient with space" +
                          " inbetween, or type \"none\"" +
                          " if you have no restrictions: ")
        restricts = restricts.lower()
        restrictions = restricts.split() '''
        # prompt for cuisine type
        '''yes = True
        while (yes):
            cuisine = input("\nFinally, please indicate a cuisine type,\n" +
                            "to see a list of possible cuisine types" +
                            "press (y),\n to skip this step and" +
                            " receive a recipe result press (n):")
            cuisine = cuisine.lower()
            if cuisine == "y":
                response = requests.get("https://www.themealdb.com" +
                                        "/api/json/v1/1/list.php?a=list")
                data = response.json()["meals"]
                areas = []
                for datum in data:
                    areas.append(datum["strArea"])
                print(areas)
            else:
                yes = False '''

        # API get recipes based on MI, if not, get based on vegan or vegetarian
    if diet == "v":
        response = requests.get("https://www.themealdb.com" +
                                "/api/json/v1/1/filter.php?c=Vegan")
    elif diet == "t":
        response = requests.get("https://www.themealdb.com" +
                                "/api/json/v1/1/filter.php?c=Vegetarian")
    elif main_in != "n":
        response = requests.get("https://www.themealdb.com" +
                                "/api/json/v1/1/filter.php?i=" + main_in)
    else:
        response = requests.get("https://www.themealdb.com" +
                                "/api/json/v1/1/random.php")

    meal_data = response.json()["meals"]
    new_data = []
    for i in range(len(meal_data)):
        meal = meal_data[i]
        resp = requests.get("https://www.themealdb.com" +
                            "/api/json/v1/1/lookup.php?i=" + meal["idMeal"])
        meal = resp.json()["meals"][0]
        # get list of meals that meet the specifications
        '''if has_restrictions(meal, restrictions) is False:
                if cuisine != "n" and meal["strArea"].lower() == cuisine:
                    new_data.append(meal)
                if cuisine == "n":
                    new_data.append(meal)'''
        new_data.append(meal)

        # randomize meal choice
    chosen_meal = random.choice(new_data)
    print_recipe(chosen_meal)
    while True:
        decision = input("\nIf you would like to view a different" +
                         " recipe press (y)," +
                         "\nif you would like to begin the search" +
                         " over again press (p),\n" +
                         "otherwise press (q) to quit\n")
        if decision == "y":
            chosen_meal = random.choice(new_data)
            print_recipe(chosen_meal)
            # this will cause big loop to start over
        if decision == "p":
            break
            # this will cause big loop to end program
        if decision == "q":
            exit()
            # go = False

''' idea for database use: keep a database of meal ids inorder to keep
    record of user's previously viewed recipes '''
'''another database idea: every time a recipe is chosen it is
   added to the database and so we keep a record of the most popular
   dishes in certain areas, categories '''
'''another idea: use database to make meal plan'''
