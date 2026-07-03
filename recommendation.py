recommendations = {
    "movies": ["Inception", "Avengers", "Interstellar"],
    "music": ["Arijit Singh", "Taylor Swift", "Imagine Dragons"],
    "books": ["Atomic Habits", "The Alchemist", "Rich Dad Poor Dad"],
    "sports": ["Cricket", "Football", "Badminton"]
}

print("Categories:")
for category in recommendations:
    print("-", category)

choice = input("\nEnter your favorite category: ").lower()

if choice in recommendations:
    print("\nRecommended for you:")
    for item in recommendations[choice]:
        print("-", item)
else:
    print("Sorry! Category not found.")