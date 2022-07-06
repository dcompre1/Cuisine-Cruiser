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
