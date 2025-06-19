from flask import Flask, jsonify, request

app = Flask(__name__)


books = [
    {"id": 1, "title": "Python Basics", "author": "Ahmed"},
    {"id": 2, "title": "Data Science", "author": "Sara"}
]

@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route("/books", methods=["POST"])
def add_book():
    new_book = request.json
    books.append(new_book)
    return jsonify(new_book), 201


@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    for book in books:
        if book["id"] == book_id:
            book.update(request.json)
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})
    return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
