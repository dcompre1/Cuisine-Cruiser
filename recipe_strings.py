class RecipeStrings:

    def __init__(self):
        pass

    def get_first_message(self):
        return "\nTo begin, please indicate whether you would like" + \
               " to input preferences like ingredients to exclude and" + \
               " cuisine type, or receive a recipe now:" + \
               " \n(y) yes, receive now\n(n) no, I have" + \
               " preferences to enter\n"

    def get_restrictions_prompt(self):
        return "\nDo you have any ingredients that you would like to exclude from" + \
                 " from potential recipes?" + \
                 " If you are vegan or vegetarian:\n" + \
                 "press (v) for Vegan\n" + \
                 "press (t) for Vegetarian\n" + \
                 "Otherwise enter ingredient(s) with comma in between:" + \
                 "or type \"none\":\n"

    def get_cuisine_prompt(self):
        return "\nFinally, please indicate a cuisine type,\n" + \
               "or press (c) to see a list of possible cuisine types\n"
