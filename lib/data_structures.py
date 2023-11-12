spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

    pass

def get_spiciest_foods(spicy_foods):
    # if food[heat_level] > 5 return list of dictionaries 
    # pass
    spiciest_list = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_list.append(food)
    return spiciest_list

def print_spicy_foods(spicy_foods):
    # take slist and outputes each spicy food in format with correcto number of emojis 

    for food in spicy_foods:
        heat_level_emoj = "🌶" * food["heat_level"] 
        # print(food["name"]+ "(" + food["cuisine"] + ") | Heat Level: " + 🌶 * food["heat_level"] )
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoj}")
    # pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
         if(food["cuisine"]).lower() == cuisine.lower():
             return food
    return None

def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        heat_level_emoj = "🌶" * food["heat_level"] 
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emoj}")

def get_average_heat_level(spicy_foods):
    # get spice levels, then average and return 
    avg = []
    for food in spicy_foods:
        avg.append(food["heat_level"])

    total_sum = sum(avg)
    average = total_sum/len(avg)
    return average



def create_spicy_food(spicy_foods, spicy_food):
    pass
