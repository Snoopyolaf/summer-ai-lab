# Hunter's allergen list
my_allergens = ["peanuts", "tree nuts", "cashews", "almonds", "walnuts"]

# Pretend these came from a photo of a label
ingredients = ["sugar", "flour", "cashew butter", "salt", "vanilla extract"]

print("Scanning ingredients...\n")

found = []

for ingredient in ingredients:
    for allergen in my_allergens:
        if allergen in ingredient.lower():
            found.append(ingredient)

if found:
    print("⚠️  WARNING - Contains allergens:")
    for item in found:
        print(f"   - {item}")
else:
    print("✅ Looks clear - no allergens found")