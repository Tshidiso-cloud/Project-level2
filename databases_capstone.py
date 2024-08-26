import sqlite3

# Connect to the database.
db = sqlite3.connect('ebookstore.db')
cursor= db.cursor()

# Create the book table.
cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                qty INTEGER)
''')

# Populate the table with initial values.
books = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, 'Harry Potter and the Philosophosopher\'s Stone', 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
]
cursor.executemany('INSERT INTO book VALUES (?, ?, ?, ?)', books)

# Define the menu and functions.
def add_book():
    '''
    Add a new book to the database.
    
    Prompts the user to enter the book's ID, title, author, and quantity.
    '''
    id = int(input('Enter book ID: '))
    title = input('Enter book title: ')
    author = input('Enter book author: ')
    qty = int(input('Enter book quantity: '))
    cursor.execute('INSERT INTO book VALUES (?, ?, ?, ?)', (id, title, author, qty))
    db.commit()

def update_book():
    '''
    Update an existing book in the database.
    
    Prompts the user to enter the book's ID and new title, author, and/or quantity.
    '''
    id = int(input('Enter book ID to update: '))
    title = input('Enter new title (or press Enter to skip): ')
    author = input('Enter new author (or press Enter to skip): ')
    qty = input('Enter new quantity (or press Enter to skip): ')
    if title: cursor.execute('UPDATE book SET title = ? WHERE id = ?', (title, id))
    if author: cursor.execute('UPDATE book SET author = ? WHERE id = ?', (author, id))
    if qty: cursor.execute('UPDATE book SET qty = ? WHERE id = ?', (int(qty), id))
    db.commit()

def delete_book():
    '''
    Delete a book from the database.
    
    Prompts the user to enter the book's ID.
    '''
    id = int(input('Enter book ID to delete: '))
    cursor.execute('DELETE FROM book WHERE id = ?', (id,))
    db.commit()

def search_books():
    '''
    Search for books in the database.
    
    Prompts the user to enter a title (or press Enter to show all books).
    '''
    title = input('Enter book title to search (or press Enter to show all): ')
    if title:
        cursor.execute('SELECT * FROM book WHERE title LIKE ?', ('%' + title + '%',))
    else:
        cursor.execute('SELECT * FROM book')
    books = cursor.fetchall()
    for book in books:
        print(book)

def exit_program():
    '''
    Exit the program and close the database connection.
    '''
    db.close()
    print('Goodbye!')

# Main program loop.
def main():
    while True:
        print("\nBookstore Management System:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")

        choice = input("Enter choice:")

        if choice == '1': 
            add_book()
        elif choice == '2': 
            update_book()
        elif choice == '3': 
            delete_book()
        elif choice == '4': 
            search_books()
        elif choice == '0': 
            exit_program(); 
            break
        else: print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()
    