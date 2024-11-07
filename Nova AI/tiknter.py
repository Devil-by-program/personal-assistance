import random
import tkinter as tk
from tkinter import messagebox, ttk


# Recipe Data: 10 Recipes for each cuisine
recipes = [
    # Italian
    {"name": "Lasagna", "cuisine": "Italian", "ingredients": ["lasagna noodles", "ground beef", "tomato sauce", "ricotta", "mozzarella", "parmesan", "basil", "oregano", "onion", "garlic", "olive oil", "salt", "black pepper", "mushrooms", "spinach", "bell peppers", "eggplant", "zucchini"], "dietary": "non-vegetarian", "cook_time": 60},
    {"name": "Pasta Primavera", "cuisine": "Italian", "ingredients": ["penne", "olive oil", "garlic", "broccoli", "zucchini", "bell peppers", "cherry tomatoes", "parmesan", "basil", "salt", "black pepper", "peas", "spinach", "cherry tomatoes", "mushrooms", "lemon"], "dietary": "vegetarian", "cook_time": 30},
    {"name": "Fettuccine Alfredo", "cuisine": "Italian", "ingredients": ["fettuccine", "heavy cream", "butter", "parmesan", "black pepper", "parsley", "salt", "garlic", "lemon zest", "mushrooms", "spinach", "chicken"], "dietary": "vegetarian", "cook_time": 25},
    {"name": "Minestrone Soup", "cuisine": "Italian", "ingredients": ["vegetable broth", "tomatoes", "carrot", "celery", "zucchini", "beans", "pasta", "onion", "garlic", "basil", "thyme", "parmesan", "spinach", "potatoes", "peas", "bay leaves", "rosemary"], "dietary": "vegetarian", "cook_time": 40},
    {"name": "Chicken Parmesan", "cuisine": "Italian", "ingredients": ["chicken breast", "bread crumbs", "parmesan", "mozzarella", "tomato sauce", "basil", "olive oil", "salt", "black pepper", "garlic", "oregano", "spinach", "red pepper flakes", "mushrooms"], "dietary": "non-vegetarian", "cook_time": 45},
    {"name": "Risotto", "cuisine": "Italian", "ingredients": ["arborio rice", "chicken broth", "parmesan", "white wine", "butter", "onion", "garlic", "mushrooms", "black pepper", "parsley", "saffron", "peas", "lemon zest", "spinach", "shrimp"], "dietary": "vegetarian", "cook_time": 35},
    {"name": "Bruschetta", "cuisine": "Italian", "ingredients": ["baguette", "tomatoes", "basil", "garlic", "olive oil", "salt", "black pepper", "balsamic vinegar", "parmesan", "mozzarella"], "dietary": "vegetarian", "cook_time": 10},
    {"name": "Osso Buco", "cuisine": "Italian", "ingredients": ["veal shanks", "onion", "carrot", "celery", "tomato", "white wine", "garlic", "lemon zest", "thyme", "rosemary", "bay leaves", "parsley", "peas"], "dietary": "non-vegetarian", "cook_time": 120},
    {"name": "Caprese Salad", "cuisine": "Italian", "ingredients": ["tomatoes", "mozzarella", "basil", "olive oil", "balsamic vinegar", "salt", "black pepper", "avocado", "arugula", "olive tapenade"], "dietary": "vegetarian", "cook_time": 10},
    {"name": "Gnocchi", "cuisine": "Italian", "ingredients": ["potatoes", "flour", "egg", "parmesan", "butter", "sage", "salt", "mushrooms", "spinach", "garlic"], "dietary": "vegetarian", "cook_time": 30},

    # Chinese
    {"name": "Sweet and Sour Pork", "cuisine": "Chinese", "ingredients": ["pork", "bell pepper", "pineapple", "soy sauce", "vinegar", "sugar", "ginger", "garlic", "cornstarch", "onion", "green onion", "sesame oil", "black pepper", "red chili flakes", "carrot", "water chestnuts", "bamboo shoots"], "dietary": "non-vegetarian", "cook_time": 30},
    {"name": "Tofu Stir Fry", "cuisine": "Chinese", "ingredients": ["tofu", "soy sauce", "ginger", "garlic", "broccoli", "carrot", "bell pepper", "mushrooms", "green onion", "sesame oil", "hoisin sauce", "sesame seeds", "water chestnuts", "snow peas"], "dietary": "vegetarian", "cook_time": 20},
    {"name": "Kung Pao Chicken", "cuisine": "Chinese", "ingredients": ["chicken", "peanuts", "soy sauce", "ginger", "garlic", "bell pepper", "onion", "sesame oil", "sugar", "vinegar", "chili peppers", "scallions", "cornstarch", "rice wine", "black pepper", "water chestnuts"], "dietary": "non-vegetarian", "cook_time": 25},
    {"name": "Spring Rolls", "cuisine": "Chinese", "ingredients": ["spring roll wrappers", "cabbage", "carrot", "mushrooms", "rice noodles", "soy sauce", "ginger", "garlic", "green onions", "sesame oil", "salt", "pepper", "chili flakes", "hoisin sauce"], "dietary": "vegetarian", "cook_time": 15},
    {"name": "General Tso's Chicken", "cuisine": "Chinese", "ingredients": ["chicken", "soy sauce", "cornstarch", "ginger", "garlic", "green onion", "rice vinegar", "sugar", "chili paste", "sesame oil", "rice wine", "water chestnuts", "broccoli", "carrot", "sesame seeds"], "dietary": "non-vegetarian", "cook_time": 35},
    {"name": "Wonton Soup", "cuisine": "Chinese", "ingredients": ["wonton wrappers", "ground pork", "garlic", "ginger", "green onion", "soy sauce", "sesame oil", "chicken broth", "bok choy", "mushrooms", "water chestnuts", "carrot", "black pepper"], "dietary": "non-vegetarian", "cook_time": 25},
    {"name": "Beef and Broccoli", "cuisine": "Chinese", "ingredients": ["beef", "broccoli", "soy sauce", "garlic", "ginger", "rice wine", "sesame oil", "cornstarch", "scallions", "black pepper", "carrot", "bamboo shoots", "chili flakes"], "dietary": "non-vegetarian", "cook_time": 20},
    {"name": "Fried Rice", "cuisine": "Chinese", "ingredients": ["rice", "egg", "carrot", "peas", "soy sauce", "green onion", "garlic", "ginger", "sesame oil", "cornstarch", "water chestnuts", "mushrooms", "chicken", "shrimp"], "dietary": "vegetarian", "cook_time": 25},
    {"name": "Mapo Tofu", "cuisine": "Chinese", "ingredients": ["tofu", "ground pork", "soy sauce", "ginger", "garlic", "bean paste", "chili paste", "scallions", "rice wine", "sesame oil", "cornstarch", "water chestnuts", "black pepper"], "dietary": "non-vegetarian", "cook_time": 25},
    {"name": "Chow Mein", "cuisine": "Chinese", "ingredients": ["noodles", "chicken", "soy sauce", "ginger", "garlic", "bean sprouts", "carrot", "green onion", "sesame oil", "hoisin sauce", "mushrooms", "bamboo shoots"], "dietary": "non-vegetarian", "cook_time": 30},

    # Mexican
    {"name": "Tacos", "cuisine": "Mexican", "ingredients": ["taco shells", "ground beef", "cheese", "lettuce", "tomatoes", "onions", "sour cream", "jalapenos", "guacamole", "taco seasoning", "lime", "cilantro", "salsa"], "dietary": "non-vegetarian", "cook_time": 15},
    {"name": "Burritos", "cuisine": "Mexican", "ingredients": ["flour tortillas", "rice", "black beans", "cheese", "guacamole", "sour cream", "lettuce", "tomatoes", "ground beef", "onions", "salsa", "cilantro", "lime", "jalapenos"], "dietary": "non-vegetarian", "cook_time": 20},
    {"name": "Enchiladas", "cuisine": "Mexican", "ingredients": ["corn tortillas", "cheese", "chicken", "onions", "tomato sauce", "chili powder", "garlic", "lime", "sour cream", "guacamole", "cilantro"], "dietary": "non-vegetarian", "cook_time": 30},
    {"name": "Quesadillas", "cuisine": "Mexican", "ingredients": ["flour tortillas", "cheese", "chicken", "onions", "bell peppers", "sour cream", "guacamole", "lime", "salsa", "jalapenos"], "dietary": "non-vegetarian", "cook_time": 15},
    {"name": "Fajitas", "cuisine": "Mexican", "ingredients": ["flour tortillas", "chicken", "bell peppers", "onions", "garlic", "lime", "cilantro", "sour cream", "cheese", "guacamole", "salsa"], "dietary": "non-vegetarian", "cook_time": 30},
    {"name": "Chiles Rellenos", "cuisine": "Mexican", "ingredients": ["poblano peppers", "cheese", "ground beef", "tomatoes", "onions", "cilantro", "garlic", "sour cream", "lime", "corn tortillas"], "dietary": "vegetarian", "cook_time": 40},
    {"name": "Tamales", "cuisine": "Mexican", "ingredients": ["masa", "corn husks", "chicken", "pork", "cheese", "salsa", "onions", "garlic", "chili powder", "lime"], "dietary": "non-vegetarian", "cook_time": 60},
    {"name": "Guacamole", "cuisine": "Mexican", "ingredients": ["avocados", "onions", "tomatoes", "cilantro", "lime", "jalapenos", "garlic", "salt", "pepper"], "dietary": "vegetarian", "cook_time": 10},
    {"name": "Churros", "cuisine": "Mexican", "ingredients": ["flour", "sugar", "cinnamon", "butter", "eggs", "vanilla", "salt", "oil", "chocolate", "water"], "dietary": "vegetarian", "cook_time": 20},
    {"name": "Tostadas", "cuisine": "Mexican", "ingredients": ["tostada shells", "ground beef", "refried beans", "lettuce", "cheese", "tomatoes", "sour cream", "guacamole", "salsa", "cilantro"], "dietary": "non-vegetarian", "cook_time": 15},

    # Indian
    {"name": "Butter Chicken", "cuisine": "Indian", "ingredients": ["chicken", "butter", "tomatoes", "cream", "garlic", "ginger", "garam masala", "coriander", "cumin", "paprika", "cilantro", "onions"], "dietary": "non-vegetarian", "cook_time": 50},
    {"name": "Chicken Tikka Masala", "cuisine": "Indian", "ingredients": ["chicken", "yogurt", "tomatoes", "garam masala", "cumin", "paprika", "coriander", "garlic", "ginger", "onions", "cilantro", "cream"], "dietary": "non-vegetarian", "cook_time": 45},
    {"name": "Palak Paneer", "cuisine": "Indian", "ingredients": ["spinach", "paneer", "garlic", "onions", "tomatoes", "garam masala", "cumin", "coriander", "ginger", "cream", "cinnamon", "cardamom"], "dietary": "vegetarian", "cook_time": 35},
    {"name": "Biryani", "cuisine": "Indian", "ingredients": ["basmati rice", "chicken", "onions", "tomatoes", "garam masala", "cumin", "coriander", "saffron", "cilantro", "ginger", "garlic", "yogurt"], "dietary": "non-vegetarian", "cook_time": 60},
    {"name": "Aloo Gobi", "cuisine": "Indian", "ingredients": ["potatoes", "cauliflower", "garam masala", "coriander", "cumin", "ginger", "onions", "tomatoes", "cilantro", "garlic"], "dietary": "vegetarian", "cook_time": 35},
    {"name": "Rogan Josh", "cuisine": "Indian", "ingredients": ["lamb", "yogurt", "garam masala", "ginger", "garlic", "onions", "tomatoes", "cumin", "cardamom", "coriander", "cilantro"], "dietary": "non-vegetarian", "cook_time": 80},
    {"name": "Chana Masala", "cuisine": "Indian", "ingredients": ["chickpeas", "tomatoes", "garam masala", "cumin", "coriander", "ginger", "garlic", "onions", "cilantro", "lemon"], "dietary": "vegetarian", "cook_time": 40},
    {"name": "Samosas", "cuisine": "Indian", "ingredients": ["potatoes", "peas", "onions", "cumin", "garam masala", "coriander", "ginger", "garlic", "coriander", "flour"], "dietary": "vegetarian", "cook_time": 25},
    {"name": "Tandoori Chicken", "cuisine": "Indian", "ingredients": ["chicken", "yogurt", "garam masala", "coriander", "cumin", "ginger", "garlic", "paprika", "lemon", "cilantro"], "dietary": "non-vegetarian", "cook_time": 60},
    {"name": "Naan", "cuisine": "Indian", "ingredients": ["flour", "yeast", "yogurt", "butter", "baking powder", "salt", "garlic", "cilantro"], "dietary": "vegetarian", "cook_time": 15},

    # Japanese
    {"name": "Sushi", "cuisine": "Japanese", "ingredients": ["sushi rice", "nori", "fish", "avocado", "cucumber", "soy sauce", "wasabi", "pickled ginger", "rice vinegar", "sugar"], "dietary": "non-vegetarian", "cook_time": 30},
    {"name": "Ramen", "cuisine": "Japanese", "ingredients": ["ramen noodles", "chicken broth", "soy sauce", "ginger", "garlic", "scallions", "egg", "bamboo shoots", "seaweed", "sesame oil"], "dietary": "non-vegetarian", "cook_time": 40},
    {"name": "Tempura", "cuisine": "Japanese", "ingredients": ["shrimp", "vegetables", "flour", "rice flour", "water", "egg", "soy sauce", "ginger", "garlic", "sesame oil"], "dietary": "non-vegetarian", "cook_time": 30},
    {"name": "Teriyaki Chicken", "cuisine": "Japanese", "ingredients": ["chicken", "soy sauce", "ginger", "garlic", "brown sugar", "rice vinegar", "sesame oil", "sesame seeds", "green onions"], "dietary": "non-vegetarian", "cook_time": 30},
    {"name": "Miso Soup", "cuisine": "Japanese", "ingredients": ["miso paste", "tofu", "seaweed", "green onions", "ginger", "soy sauce", "fish stock", "tofu"], "dietary": "vegetarian", "cook_time": 15},
    {"name": "Okonomiyaki", "cuisine": "Japanese", "ingredients": ["flour", "egg", "cabbage", "pork", "soy sauce", "green onions", "mayonnaise", "sugar", "pickled ginger", "sesame oil"], "dietary": "non-vegetarian", "cook_time": 40},
    {"name": "Sashimi", "cuisine": "Japanese", "ingredients": ["raw fish", "soy sauce", "wasabi", "pickled ginger", "rice", "sesame oil", "cucumber", "avocado", "nori"], "dietary": "non-vegetarian", "cook_time": 20},
    {"name": "Yakitori", "cuisine": "Japanese", "ingredients": ["chicken", "soy sauce", "ginger", "garlic", "green onions", "sake", "sugar", "sesame oil"], "dietary": "non-vegetarian", "cook_time": 25},
    {"name": "Donburi", "cuisine": "Japanese", "ingredients": ["rice", "chicken", "egg", "soy sauce", "ginger", "onions", "sesame oil", "seaweed", "sesame seeds"], "dietary": "non-vegetarian", "cook_time": 30},
    {"name": "Tonkatsu", "cuisine": "Japanese", "ingredients": ["pork", "breadcrumbs", "flour", "egg", "cabbage", "tonkatsu sauce", "rice", "green onions", "ginger"], "dietary": "non-vegetarian", "cook_time": 35}
]

def get_ingredients_by_cuisine_and_diet(cuisine, dietary):
    ingredients = set()
    for recipe in recipes:
        if recipe["cuisine"].lower() == cuisine.lower() and recipe["dietary"] == dietary:
            ingredients.update(recipe["ingredients"])
    return list(ingredients)

def recommend_recipes(cuisine, dietary, available_ingredients):
    matching_recipes = [
        recipe for recipe in recipes
        if recipe["cuisine"].lower() == cuisine.lower() and recipe["dietary"] == dietary
        and any(ingredient in available_ingredients for ingredient in recipe["ingredients"])
    ]
    if matching_recipes:
        recommended_recipe = random.choice(matching_recipes)
        recipe_details = (
            f"Recommended Recipe: {recommended_recipe['name']}\n"
            f"Cuisine: {recommended_recipe['cuisine']}\n"
            f"Ingredients: {', '.join(recommended_recipe['ingredients'])}\n"
            f"Cook Time: {recommended_recipe['cook_time']} minutes"
        )
        messagebox.showinfo("Recipe Recommendation", recipe_details)
    else:
        messagebox.showwarning("No Match", "No matching recipes found based on your preferences and available ingredients.")

def main():
    root = tk.Tk()
    root.title("Recipe Recommender")
    root.geometry("400x600")

    tk.Label(root, text="Select Cuisine:").pack()
    cuisine_var = tk.StringVar()
    cuisine_dropdown = ttk.Combobox(root, textvariable=cuisine_var)
    cuisine_dropdown['values'] = ["Italian", "Chinese", "Mexican", "Mediterranean", "Indian"]
    cuisine_dropdown.pack()

    tk.Label(root, text="Select Dietary Preference:").pack()
    dietary_var = tk.StringVar(value="vegetarian")
    tk.Radiobutton(root, text="Vegetarian", variable=dietary_var, value="vegetarian").pack()
    tk.Radiobutton(root, text="Non-Vegetarian", variable=dietary_var, value="non-vegetarian").pack()

    # Frame for ingredients with scrollbar
    ingredients_frame = tk.Frame(root)
    ingredients_frame.pack(pady=10)

        # Create a canvas for the ingredients
    canvas = tk.Canvas(ingredients_frame)
    scrollbar = tk.Scrollbar(ingredients_frame, orient="vertical", command=canvas.yview)
    ingredients_list_frame = tk.Frame(canvas)

    # Configure the scrollbar
    ingredients_list_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a window in the canvas
    canvas.create_window((0, 0), window=ingredients_list_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    veg_ingredient_vars = {}
    nonveg_ingredient_vars = {}

    def update_ingredient_options(*args):
        # Clear previous checkbuttons
        for widget in ingredients_list_frame.winfo_children():
            widget.destroy()

        selected_cuisine = cuisine_var.get()
        selected_dietary = dietary_var.get()

        veg_ingredients = get_ingredients_by_cuisine_and_diet(selected_cuisine, "vegetarian")
        nonveg_ingredients = get_ingredients_by_cuisine_and_diet(selected_cuisine, "non-vegetarian")

        if selected_dietary == "vegetarian":
            for ingredient in veg_ingredients:
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(ingredients_list_frame, text=ingredient, variable=var)
                checkbox.pack(anchor='w')
                veg_ingredient_vars[ingredient] = var
        else:
            for ingredient in nonveg_ingredients:
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(ingredients_list_frame, text=ingredient, variable=var)
                checkbox.pack(anchor='w')
                nonveg_ingredient_vars[ingredient] = var

    # Trace changes in the cuisine and dietary preferences
    cuisine_var.trace("w", update_ingredient_options)
    dietary_var.trace("w", update_ingredient_options)

    def on_recommend():
        cuisine = cuisine_var.get()
        dietary = dietary_var.get()

        if dietary == "vegetarian":
            selected_ingredients = [ingredient for ingredient, var in veg_ingredient_vars.items() if var.get()]
        else:
            selected_ingredients = [ingredient for ingredient, var in nonveg_ingredient_vars.items() if var.get()]

        if not cuisine:
            messagebox.showwarning("Input Error", "Please select a cuisine.")
            return
        if not selected_ingredients:
            messagebox.showwarning("Input Error", "Please select available ingredients.")
            return

        recommend_recipes(cuisine, dietary, selected_ingredients)

    recommend_button = tk.Button(root, text="Recommend Recipe", command=on_recommend)
    recommend_button.pack(pady=10)

    root.mainloop()

# Run the program
main()