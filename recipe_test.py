import unittest
from recipe_funcs import has_restrictions

restrictions = ["chEese", "Peanut Butter", "EGGS"]
meal1 = {"strIngredient1": "Cheese", "strIngredient2": "Bread"
         "strIngredient3": "Butter", "strIngredient4":"Eggs",
         "strIngredient5": "Mayonnaise"}
meal2 = {"strIngredient1": "chocolate", "strIngredient2": "strawberries"
         "strIngredient3": "banana", "strIngredient4":"milk",
         "strIngredient5": "sugar"}
meal_data = [meal1, meal2]
cuisine = "American"

class RecipeTest(unittest.TestCase):
    def test_has_restrictions(self):
        result = has_restrictions(meal1, restrictions)
        self.assertEqual(result, True)
        result = has_restrictions(meal2, restrictions)
        self.assertEqual(result, False)

    def test_get_recipes(self):
        response = get_recipes("v", "")
        meal_data1 = response.json["meals"]
        self.assertTrue(isinstance(meal_data1, list))
        self.assertEqual(len(meal_data1), 3)

        response = get_recipes("t", "")
        meal_data2 = response.json["meals"]
        self.assertTrue(isinstance(meal_data2, list))
        self.assertNotEqual(len(meal_data2), 0)


        response = get_recipes("n", "chicken")
        meal_data3 = response.json["meals"]
        self.assertTrue(isinstance(meal_data3, list))
        self.assertNotEqual(len(meal_data2), 0)

    def test_filter_meals(self):
        result = filter_meals(meal_data, len(meal_data))
        self.assertTrue(isinstance(result), list)

if __name__ == '__main__':
    unittest.main()
