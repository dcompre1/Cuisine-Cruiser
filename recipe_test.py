import unittest
from recipe_funcs import has_restrictions, no_cuisine, create_database

restrictions = ["cheese", "peanut butter", "eggs"]

meal1 = {"strIngredient1": "Cheese", "strIngredient2": "Bread",
         "strIngredient3": "Butter", "strIngredient4":"Eggs",
         "strIngredient5": "Mayonnaise", "strArea": "American",
         "strIngredient6": "Cheese", "strIngredient7": "Bread",
         "strIngredient8": "Butter", "strIngredient9":"Eggs",
         "strIngredient10": "Mayonnaise", "strIngredient11": "Cheese", "strIngredient12": "Bread",
         "strIngredient13": "Butter", "strIngredient14":"Eggs",
         "strIngredient15": "Mayonnaise",
         "strIngredient16": "Cheese", "strIngredient17": "Bread",
         "strIngredient18": "Butter", "strIngredient19":"Eggs",
         "strIngredient20": "Mayonnaise","strIngredient21": "Lint"}

meal2 = {"strIngredient1": "chocolate", "strIngredient2": "strawberries",
         "strIngredient3": "banana", "strIngredient4":"milk",
         "strIngredient5": "sugar", "strArea": "Vietnamese", "strIngredient6": None, "strIngredient7": "Bread",
         "strIngredient8": "Butter", "strIngredient9":None,
         "strIngredient10": "Mayonnaise", "strIngredient11": "Cheese", "strIngredient12": "Bread",
         "strIngredient13": "Butter", "strIngredient14":None,
         "strIngredient15": "Mayonnaise",
         "strIngredient16": None, "strIngredient17": "Bread",
         "strIngredient18": "Butter", "strIngredient19":"Eggs",
         "strIngredient20": "Mayonnaise","strIngredient21": "Lint"}
meal_data = [meal1, meal2]
cuisine = "American"

response1 = "https://www.themealdb.com" + \
            "/api/json/v1/1/filter.php?c=843540"
response2 = "https://www.themealdb.com" + \
            "/api/json/v1/1/filter.php?c=324983"

response3 = "https://www.themealdb.com/api/json/v1/1/filter.php?a=31398"

class RecipeTest(unittest.TestCase):
    def test_has_restrictions(self):
        result = has_restrictions(meal1, restrictions)
        self.assertEqual(result, True)
        result = has_restrictions(meal2, restrictions)
        self.assertEqual(result, False)

    def test_no_cuisine(self):
        result = no_cuisine(meal1, cuisine)
        self.assertEqual(result, False)
        result = no_cuisine(meal2, cuisine)
        self.assertEqual(result, True)

    def test_create_database(self):
        c = create_database("Vegan", response1)
        self.assertEqual(c, "q")
        c = create_database("Vegetarian", response2)
        self.assertEqual(c, "q")
        c = create_database("Cuisine", response3)
        self.assertEqual(c, "q")

if __name__ == '__main__':
    unittest.main()
