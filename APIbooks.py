from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ==========================================
# 1. DEFINE THE BOOK MODEL
# ==========================================
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"{self.book_name} by {self.author}"

# ==========================================
# 2. CRUD ROUTES (API ENDPOINTS)
# ==========================================

@app.route('/')
def index():
    return "Welcome to the Book API!"

# CREATE: Add a new book (POST)
@app.route('/books', methods=['POST'])
def add_book():
    book_data = request.json
    new_book = Book(
        book_name=book_data['book_name'], 
        author=book_data['author'], 
        publisher=book_data['publisher']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": f"Book '{new_book.book_name}' added successfully!"}), 201

# READ: Get all books (GET)
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'book_name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
        }
        output.append(book_data)
    return jsonify({"books": output})

# READ: Get a specific book by ID (GET)
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'book_name': book.book_name,
        'author': book.author,
        'publisher': book.publisher
    })

# UPDATE: Update an existing book (PUT)
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    update_data = request.json
    
    book.book_name = update_data.get('book_name', book.book_name)
    book.author = update_data.get('author', book.author)
    book.publisher = update_data.get('publisher', book.publisher)
    
    db.session.commit()
    return jsonify({"message": "Book updated successfully!"})

# DELETE: Delete a book (DELETE)
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": f"Book '{book.book_name}' deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
