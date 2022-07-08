class RecipeStrings:

    def __init__(self):
        pass

    def get_first_message(self):
        return "\nTo begin, please indicate whether you would like" + \
               " to input preferences like ingredients to exclude and" + \
               " cuisine type, or receive a random recipe now:" + \
               " \n(y) yes, receive now\n(n) no, I have" + \
               " preferences to indicate:\n"

    def get_restrictions_prompt(self):
        return "\nDo you have any ingredients that you " + \
                 "would like to exclude from potential recipes?\n" + \
                 "If you are Vegan or Vegetarian:\n" + \
                 "press (v) for Vegan\n" + \
                 "press (t) for Vegetarian\n" + \
                 "Otherwise, enter ingredient(s) with commas " + \
                 "in between each, or type \"none\":\n"

    def get_cuisine_prompt(self):
        return "\nLastly, enter a cuisine type, or\n" + \
               "press (c) to see a list of all cuisine types:\n"
