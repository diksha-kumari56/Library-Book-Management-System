📚 Library Book Management System (DSA Assignment 2)

Course: Data Structures (ENCS205)
Semester: 3rd
Session: 2025–26
Assignment Number: 02

📖 Objective

To design and implement a Library Book Management System using
👉 a Single Linked List to manage dynamic book records
👉 a Stack to implement an undo functionality for recent transactions (issue or return).

🧩 Data Structures Used
Structure	Purpose
Single Linked List	To store and manage book records dynamically
Stack (list)	To record and undo recent issue/return transactions
⚙️ Functionalities Implemented
📗 Book Management (Linked List)

insert_book(book_id, title, author) → Add a new book

delete_book(book_id) → Delete a book by its ID

search_book(book_id) → Search for a book and display details

display_books() → Display all books in the library

🔄 Transaction Management (Stack)

issue_book(book_id) → Mark a book as Issued and record the transaction

return_book(book_id) → Mark a book as Available and record the transaction

undo_transaction() → Undo the last issue/return operation using stack pop

view_transactions() → Display all recent transactions

🧠 Learning Outcomes

Implemented real-world dynamic data handling using linked lists.

Applied stack operations for undo mechanisms.

Demonstrated algorithmic thinking and integration of two linear data structures.

Enhanced understanding of data abstraction and modular programming.

🧾 Sample Output

========= Library Book Management System =========
1. Insert Book
2. Delete Book
3. Search Book
4. Issue Book
5. Return Book
6. Undo Last Transaction
7. Display All Books
8. View Transactions
9. Exit
Enter your choice: 1
Enter Book ID: 101
Enter Title: Python Basics
Enter Author: Guido van Rossum
Book inserted successfully.

Enter your choice: 4
Enter Book ID: 101
Book issued successfully.

Enter your choice: 6
Undo successful: Book returned to Available.
