# Dictionary
# Creating a dictionary for book with keys: title, author, year
book = {"name":"Vijayaniki 5 metlu","author":"Yandamuri Veerendranath","year":"1988"}
print(book,"\n")

# Adding a new key: genre
book["genre"] = "Non-Fiction"
print(book,"\n")

# Looping through the dictionary and printing all key:value pairs
for key, value in book.items():
    print(key,":",value)

# Set
# Creating a Set of 3 Colors
primary_colors = {"Red", "Green", "Blue"}
print(primary_colors,"\n")

# Adding new Color to Set: primary_colors
primary_colors.add("Cyan")
print(primary_colors,"\n")

# Creating a Second Set of Colors
secondary_colors = {"Red","Yellow","Blue"}

# Finding the Intersection of two Sets
print(primary_colors&secondary_colors)