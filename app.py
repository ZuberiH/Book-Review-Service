from flask import Flask, jsonify, request
import models
import service

app = Flask(__name__)

# Initialize the database
models.init_db()

# Route to list all books
@app.route("/books", methods=["GET"])
def list_books():
    books = service.get_all_books()
    return jsonify([dict(book) for book in books])

# Route to get details of a specific book
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = service.get_book_by_id(book_id)
    if book:
        reviews = service.get_reviews(book_id)
        return jsonify({"book": dict(book), "reviews": [dict(review) for review in reviews]})
    return jsonify({"error": "Book not found"}), 404

# Route to add a new book
@app.route("/books", methods=["POST"])
def add_book():
    new_book = request.json
    service.add_new_book(new_book["title"], new_book["author"])
    return jsonify({"message": "Book added successfully"}), 201

# Route to update a book's information
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    updated_data = request.json
    book = service.get_book_by_id(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    service.update_book(book_id, updated_data.get("title"), updated_data.get("author"))
    return jsonify({"message": "Book updated successfully"})

# Route to delete a book
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = service.get_book_by_id(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    service.delete_book(book_id)
    return jsonify({"message": "Book deleted successfully"})

# Route to add a review to a book
@app.route("/books/<int:book_id>/review", methods=["POST"])
def add_review(book_id):
    review = request.json.get("review")
    book = service.get_book_by_id(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    service.add_review(book_id, review)
    return jsonify({"message": "Review added successfully"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
