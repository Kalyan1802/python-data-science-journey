# ===================================
# Topic: Loops in Python
# Author: Kalyan
# Description: Covers for, while, enumerate, break, continue, pass
# ===================================

# ==============================
# 1. BASIC FOR LOOP
# ==============================

for i in range(10):
    print("Looping...", i)

# ==============================
# 2. LOOP THROUGH COLLECTION
# ==============================

favorite_foods = ('idli', 'dosa', 'vada')

for food in favorite_foods:
    print(f"I like {food} very much!")

# ==============================
# 3. ENUMERATE (INDEX + VALUE)
# ==============================

cities = ('New York', 'Los Angeles', 'Chicago')

for idx, city in enumerate(cities):
    print(f"{idx + 1}. {city}")

# ==============================
# 4. WHILE LOOP
# ==============================

games = ['chess', 'soccer', 'basketball']
count = 0

while count < len(games):
    print(f"I like to play {games[count]}")
    count += 1

# ==============================
# 5. CONDITIONAL INSIDE LOOP
# ==============================

shows = ['Game of Thrones', 'Breaking Bad', 'Stranger Things']

for show in shows:
    if show == "Game of Thrones":
        print(f"I love how well character development is handled in {show}")

# ==============================
# 6. IF-ELSE IN LOOP
# ==============================

party_guests = ['Alice', 'Bob', 'Charlie', 'David']

for guest in party_guests:
    if guest == 'Undertaker':
        print("He is the chief guest of the party!")
    else:
        print(f"{guest} is a great guest too!")

# ==============================
# 7. BREAK STATEMENT
# ==============================

indian_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata']

for city in indian_cities:
    if city == 'Vizag':
        print("Vizag has beautiful beaches!")
        break
    else:
        print("City not found in the list")

# ==============================
# 8. FOR-ELSE (IMPORTANT)
# ==============================

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print(f"Yes, one of my favorite desserts is {dessert}")
        break
else:
    print("No favorite dessert found")

# ==============================
# 9. CONTINUE STATEMENT
# ==============================

diseases = ['Diabetes', 'Hypertension', 'Asthma', 'Cancer']

for disease in diseases:
    if disease == 'Asthma':
        continue
    print(f"I am concerned about {disease}")

# ==============================
# 10. PASS STATEMENT
# ==============================

indian_cricketers = ['Sachin Tendulkar', 'Virat Kohli', 'MS Dhoni', 'Kapil Dev']

for player in indian_cricketers:
    if player == 'Virat Kohli':
        pass  # placeholder
    else:
        print(f"I admire {player}")

# ==============================
# 11. PASS EXAMPLE 2
# ==============================

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print(f"Other desserts I like are {dessert}")