books = ["Grandmother's Bag of Stories", "The Peculiar Pumpkin Thief", "Haunting Adeline", "Harry Potter", "Breaking Dawn"]
print("Books list:", books)


print("Total books:", len(books))
print("First book:", books[0])
print("Last book:", books[-1])
print("First three", books[:3])


books.append("Percy Jackson")
print("\nAfter adding Percy Jackson:", books)
books.remove("Breaking Dawn")
print("After removing Breaking Dawn:", books)
books.sort()
print("Sorted alphabetically:", books)
books.reverse()
print("Reversed:", books)


librarian = {"name": "Mrs.Gupta", "experience": 10}
print("\nLibrarian profile:", librarian)


print("Experience:", librarian.get("experience", "Not found"))
librarian["experience"] = 6
librarian["email"] = "gupta@school.com"
librarian.pop('experience')
print("Updates librarian profile:", librarian)

book_numbers = [1, 2, 3, 4, 5]
names = ["Grandmother's Bag of Stories", "The Peculiar Pumpkin Thief", "Haunting Adeline", "Harry Potter", "Percy Jackson"]
library_directory = dict(zip(book_numbers, names))
print("\nLibrary Directory:", library_directory)
print("Book at Book 3:", library_directory[3])