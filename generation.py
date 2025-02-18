birth_year = int(input("Please enter your birth year (e,g., 1990, 2000, etc): "))

if birth_year < 1946:
   Generation = "Silent Generation"
elif birth_year < 1965:
   Generation = "Baby Boomer"
elif birth_year < 1981:
   Generation = "Generation X"
elif birth_year < 1997 :
   Generation = "Millenials"
elif birth_year < 2013 :
   Generation = "Generation Z"
else: Generation = "Generation Alpha"

print (f"You belong to: {Generation}")
