def print_recipe(meal):
    meal_name = meal['strMeal']
    instructions = meal['strInstructions']
    yt = meal['strYoutube']

    # this can be a function called print_recipe(name, data):
    print("Here is your recipe: " + meal_name)
    # print(instructions)
    i = 1
    while i < 21:
        ingredient = meal['strIngredient' + str(i)]
        measure = meal['strMeasure' + str(i)]
        if ingredient != "":
            print(measure + " " + ingredient)
        i += 1
    if yt != "":
        print("Here is a youtube tutorial for this recipe: " + yt)

def has_restrictions(meal, restrictions):
    i = 1
    while i < 21:
        ingredient = meal['strIngredient' + str(i)]
        if ingredient in restrictions:
            return True
    return False
#to lower each ingredient to compare to restrictions list
