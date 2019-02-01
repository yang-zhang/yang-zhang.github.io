from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'name': 'book1',
        'price': 7.1,
        'isbn': 9023490234
    },
    {
        'name': 'book2',
        'price': 2.1,
        'isbn': 284927459
    }

]


# GET /store
@app.route('/books')
def get_books():
    return jsonify({'books': books})


# POST /books
# {
#     "name": "book3",
#     "price": 3.1,
#     "isbn": 9240029834
# }

def validBookObject(bookObject):
    if ("name" in bookObject and "price" in bookObject and "isbn" in bookObject): return True
    return False


@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    if validBookObject(request_data):
        books.insert(0, request_data)
        return "True"
    else:
        return "False"


# GET /books/284927459
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book['isbn'] == isbn:
            return_value = {
                'name': book['name'],
                'price': book['price']
            }
    return jsonify(return_value)


app.run(port=5000)
