import requests
import pandas as pd
import random
from recipe_funcs import print_recipe, has_restrictions


print("Welcome to the Random Recipe Generator!")

# loop:
go = True
while(go):

    # prompt user: vegan or vegetarian?
    skip = input("To begin, please indicate whether you would like to input preferences" +
                 " like ingredients, cuisine type, etc. or receive a recipe now:" + 
                 " \n(y) yes, receive now\n(n) no, I have preferences to enter\n")
    if skip == "y":
        # no restrictions 
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
        response = requests.get(url)
        meal = response.json()['meals'][0]
        print_recipe(meal)
        go = False
    if skip == "n":
        diet = input("\nIndicate if you are vegan or vegetarian:\n" +
                     "press (v) for Vegan\n" +
                     "press (t) for Vegetarian\n" +
                     "press any other key to continue: ")
        #if diet = "v":
            #vegan
        #elif diet = "t":
            #vegetarian
        if diet != "v" and diet != "t":
            main_in = input("\nAre you craving a main ingredient that you would like" +
                            " to include in your dish? If yes, please enter the name, if no press (n):")
        # format main ingredient to have _ where spaces would be
        restricts = input("\nDo you have any ingredients that you would like to exclude" +
                          "from potential meals?\n" +
                          "Please enter each ingredient with space inbetween, or " +
                          "type \"none\" if you have no restrictions: ")
        #to lower restricts so every word is lowercase
        restrictions = restricts.split()
        cuisine = input("\nFinally, please indicate a cuisine type,\n" +
                        "to see a list of possible cuisine types press (y),\n" +
                        " to skip this step and receive a recipe result press (n):")
        #if cuisine == "y":
        # print cuisine types url: https://www.themealdb.com/api/json/v1/1/list.php?a=list

        # API get recipes based on MI, if not, get based on vegan or vegetarian
        if diet == "v":
            response = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=Vegan")
        elif diet == "t":
            response = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=Vegetarian")
        elif main_in != "":
            response = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?i=" + main_in)
        else:
            response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")

        meal_data = response.json()["meals"]
        # i = len(meal_data)
        new_data = []
        for i in range(len(meal_data)):
            meal = meal_data[i]
            resp = requests.get("https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + meal["idMeal"])
            meal = resp.json()["meals"][0]
            if meal["strArea"] == cuisine:
                new_data.append(meal)
            if restrictions != "none":
                if has_restrictions(meal, restrictions) is False:
                    new_data.append(meal)

        chosen_meal = random.choice(new_data)
        print_recipe(chosen_meal)
        while True:
            decision = input("\nIf you would like to view a different recipe press (y)," +
                             "if you would like to begin the search over again press (p),\n" +
                             "otherwise press (q) to quit")
            if decision == "y":
                chosen_meal = random.choice(new_data)
                print_recipe(chosen_meal)
            elif decision == "p":
                break
            if decision == "q":
                go = False


# url to search full meal info by id: https://www.themealdb.com/api/json/v1/1/lookup.php?i=52942

# idea for database use: keep a database of meal ids inorder to keep record of user's previously viewed recipes

# filter out any that have the RI

# filter out any outside of cuisine type, if possible

# if there are multiple recipes, rand() select one to display

# loop(true)
# prompt user: we've selected recipe_name for you: would you like to view it?
# prompt user: press l if you'd like to view a new one or q if you'd like to quit(system exit)
# if no other recipes: There are no other recipes that meet your criteria, continue

# output:
# recipe
# ingredients
# if exists, youtube video

