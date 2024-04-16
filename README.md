# Python Book Library Manager

This Python script demonstrates an implementation of a CRUD (Create, Read, Update, Delete) operations system for a MySQL database. Let's delve into what each part of the script does:

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
- We will be using VSCode
- Open your terminal and install the mysql-connector:
 ```bash
 pip install mysql-connector-python
 ```
- Now, to connect to the server, type the following command:
  - Here -u means that you’ve to provide the username that is ‘root’ and -p means you have give the password.
```bash
mysql -u root -p
```

- Create a new user:
```sql
CREATE USER 'sqluser'@'%' IDENTIFIED WITH mysql_native_password BY 'password' ;
```

- A new user is created by the name ‘sqluser’ with password ‘password’. Provide this user with all the privileges :
```sql
GRANT ALL PRIVILEGES ON *.* TO 'sqluser'@'%' ;
```

- We need to validate these privileges :
```sql
FLUSH PRIVILEGES;
```