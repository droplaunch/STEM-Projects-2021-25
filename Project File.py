# Project Library Management System based on NCERT Class 11 concepts
# Concepts used:-
'''
1. Data Structures like list,tuple and dictionary
2. Python modules
3. Iterative statements, Strings, Error Handling and Expressions
4. Menu Driven
'''
library = {}

def add_book(book_id, title, author, copies):
    if book_id in library:
        print("Book ID already exists.")
    else:
        library[book_id] = {'Title': title, 'Author': author, 'Copies': copies}
        print("Book '" + title + "' added successfully.")

def delete_book(book_id):
    if book_id in library:
        removed_book = library.pop(book_id)
        print("Book '" + removed_book['Title'] + "' deleted successfully.")
    else:
        print("Book ID not found.")

def search_book(book_id):
    if book_id in library:
        book = library[book_id]
        print("Book Found: ID: " + book_id + ", Title: " + book['Title'] + ", Author: " + book['Author'] + ", Copies: " + str(book['Copies']))
    else:
        print("Book not found.")

def display_books():
    if library:
        print("\nAvailable Books:")
        for book_id, details in library.items():
            print("ID:", book_id, ", Title:", details['Title'], ", Author:", details['Author'], ", Copies:", details['Copies'])
    else:
        print("No books available.")

def issue_book(book_id):
    if book_id in library:
        if library[book_id]['Copies'] > 0:
            library[book_id]['Copies'] -= 1
            print("Book", library[book_id]['Title'], " issued successfully.")
        else:
            print("No copies available.")
    else:
        print("Book ID not found.")

def return_book(book_id):
    if book_id in library:
        library[book_id]['Copies'] += 1
        print("Book", library[book_id]['Title'], "returned successfully.")
        print("Book", library[book_id]['Title'], " issued successfully.")
    else:
        print("Book ID not found.")

def main_menu():
    while True: 
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            copies = int(input("Enter Number of Copies: "))
            add_book(book_id, title, author, copies)
        elif choice == '2':
            book_id = input("Enter Book ID to delete: ")
            delete_book(book_id)
        elif choice == '3':
            book_id = input("Enter Book ID to search: ")
            search_book(book_id)
        elif choice == '4':
            display_books()
        elif choice == '5':
            book_id = input("Enter Book ID to issue: ")
            issue_book(book_id)
        elif choice == '6':
            book_id = input("Enter Book ID to return: ")
            return_book(book_id)
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 7.")

# Start the application
main_menu()
