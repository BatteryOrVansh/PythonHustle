# Create a variable for your fav movie title(str), release year(int), rating(float) out of 10, and watched(bool) and recommend(bool). Print all the variables and their types.

title = input("Enter your favorite movie title: ")
year = int(input("Enter the release year of the movie: "))
rating = float(input("Enter the rating of the movie out of 10: "))
watched = input("Have you watched the movie? (yes/no): ").strip().lower() == "yes"
recommend = input("Would you recommend the movie? (yes/no): ").strip().lower() == "yes"

print("Movie: ", title)
print("Movie type: ", type(title))

print("Release Year: ", year)
print("Year type: ", type(year))

print("Rating: ", rating)
print("Rating type: ", type(rating))

print("Watched: ", watched)
print("Watched type: ", type(watched))

print("Recommend: ", recommend)
print("Recommend type: ", type(recommend))