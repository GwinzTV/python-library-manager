import mysql.connector

# Connect to MySQL database
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="pybookman"
    )

# Create a book table if it doesn't exist
def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255))")
    conn.close()

# Insert a new book into the database
def insert_book(title, author):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
    conn.commit()
    conn.close()

# Retrieve all books from the database
def get_all_books():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

# Update a book in the database
def update_book(id, title, author):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = %s, author = %s WHERE id = %s", (title, author, id))
    conn.commit()
    conn.close()

# Delete a book from the database
def delete_book(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (id,))
    conn.commit()
    conn.close()

# Main function to demonstrate usage
def main():
    create_table()
    insert_book("Python Programming", "John Smith")
    insert_book("Java Programming", "Alice Johnson")
    insert_book("C++ Programming", "Bob Brown")

    print("All Books:")
    books = get_all_books()
    for book in books:
        print(book)

    update_book(2, "Java Programming", "Alice Johnson-Smith")

    print("\nAll Books after updating:")
    books = get_all_books()
    for book in books:
        print(book)

    delete_book(3)

    print("\nAll Books after deleting:")
    books = get_all_books()
    for book in books:
        print(book)

if __name__ == "__main__":
    main()