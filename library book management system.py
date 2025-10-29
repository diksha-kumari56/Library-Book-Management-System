class Book:
    def __init__(self, book_id, title, author, status="Available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None

class BookList:
    def __init__(self):
        self.head = None

    def insert_book(self, book_id, title, author, status="Available"):
        new_book = Book(book_id, title, author, status)
        if self.head is None:
            self.head = new_book
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_book
        print("Book inserted successfully.")

    def delete_book(self, book_id):
        if self.head is None:
            print("No books to delete.")
            return

        if self.head.book_id == book_id:
            self.head = self.head.next
            print("Book deleted successfully.")
            return

        temp = self.head
        while temp.next and temp.next.book_id != book_id:
            temp = temp.next

        if temp.next is None:
            print("Book not found.")
        else:
            temp.next = temp.next.next
            print("Book deleted successfully.")

    def search_book(self, book_id):
        temp = self.head
        while temp:
            if temp.book_id == book_id:
                return temp
            temp = temp.next
        return None

    def display_books(self):
        if self.head is None:
            print("No books available.")
            return

        print("\nCurrent Books in Library:")
        print("---------------------------------------------")
        temp = self.head
        while temp:
            print(f"ID: {temp.book_id} | Title: {temp.title} | Author: {temp.author} | Status: {temp.status}")
            temp = temp.next
        print("---------------------------------------------")

class TransactionStack:
    def __init__(self):
        self.stack = []

    def push(self, transaction):
        self.stack.append(transaction)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def view_transactions(self):
        if not self.stack:
            print("No recent transactions.")
            return

        print("\nRecent Transactions:")
        print("---------------------------------------------")
        for t in reversed(self.stack):
            print(f"Book ID: {t['book_id']} | Action: {t['action']}")
        print("---------------------------------------------")

class LibrarySystem:
    def __init__(self):
        self.book_list = BookList()
        self.transactions = TransactionStack()

    def insert_book(self, book_id, title, author):
        self.book_list.insert_book(book_id, title, author)

    def delete_book(self, book_id):
        self.book_list.delete_book(book_id)

    def search_book(self, book_id):
        book = self.book_list.search_book(book_id)
        if book:
            print(f"Book Found - ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Status: {book.status}")
        else:
            print("Book not found.")

    def issue_book(self, book_id):
        book = self.book_list.search_book(book_id)
        if not book:
            print("Book not found.")
            return
        if book.status == "Issued":
            print("Book already issued.")
            return
        book.status = "Issued"
        self.transactions.push({"book_id": book_id, "action": "Issue"})
        print("Book issued successfully.")

    def return_book(self, book_id):
        book = self.book_list.search_book(book_id)
        if not book:
            print("Book not found.")
            return
        if book.status == "Available":
            print("Book already available.")
            return
        book.status = "Available"
        self.transactions.push({"book_id": book_id, "action": "Return"})
        print("Book returned successfully.")

    def undo_transaction(self):
        if self.transactions.is_empty():
            print("No transactions to undo.")
            return

        last = self.transactions.pop()
        book = self.book_list.search_book(last["book_id"])

        if not book:
            print("Book not found for undo.")
            return

        if last["action"] == "Issue":
            book.status = "Available"
            print("Undo successful: Book returned to Available.")
        elif last["action"] == "Return":
            book.status = "Issued"
            print("Undo successful: Book re-issued.")

    def display_books(self):
        self.book_list.display_books()

    def view_transactions(self):
        self.transactions.view_transactions()

def main():
    library = LibrarySystem()

    while True:
        print("\n========= Library Book Management System =========")
        print("1. Insert Book")
        print("2. Delete Book")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Undo Last Transaction")
        print("7. Display All Books")
        print("8. View Transactions")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            library.insert_book(book_id, title, author)

        elif choice == "2":
            book_id = int(input("Enter Book ID to delete: "))
            library.delete_book(book_id)

        elif choice == "3":
            book_id = int(input("Enter Book ID to search: "))
            library.search_book(book_id)

        elif choice == "4":
            book_id = int(input("Enter Book ID to issue: "))
            library.issue_book(book_id)

        elif choice == "5":
            book_id = int(input("Enter Book ID to return: "))
            library.return_book(book_id)

        elif choice == "6":
            library.undo_transaction()

        elif choice == "7":
            library.display_books()

        elif choice == "8":
            library.view_transactions()

        elif choice == "9":
            print("Exiting... Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
