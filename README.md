# Python MySQL CRUD Operations

This Python script demonstrates a basic implementation of a CRUD (Create, Read, Update, Delete) operations system for a MySQL database. Let's delve into what each part of the script does:

### Importing MySQL Connector
The script begins by importing the `mysql.connector` module, which provides the necessary tools to interact with a MySQL database.

### Connection Setup Functions
- `connect()`: Establishes a connection to the MySQL database using the provided host, username, password, and database name.
- `create_table()`: Creates a table named `books` in the database if it doesn't already exist. This table consists of columns for book `id`, `title`, and `author`.

### CRUD Operations
- `insert_book(title, author)`: Inserts a new book record into the `books` table with the provided title and author.
- `get_all_books()`: Retrieves all books from the `books` table and returns them as a list of tuples.
- `update_book(id, title, author)`: Updates the title and author of a book with the specified `id`.
- `delete_book(id)`: Deletes a book record from the `books` table based on the given `id`.

### Main Function
- `main()`: Demonstrates the usage of the CRUD operations.
  - Calls `create_table()` to ensure the table exists.
  - Inserts three sample books into the database.
  - Retrieves all books and prints them.
  - Updates the title and author of a book.
  - Prints all books after the update.
  - Deletes a book record.
  - Prints all books after the deletion.

### Execution Check
```python
if __name__ == "__main__":
    main()
```

### Requirements
