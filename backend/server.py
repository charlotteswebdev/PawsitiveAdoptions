from flask import Flask, jsonify, request
from database_connection import select_category, get_all_categories

app = Flask(__name__)


@app.route('/api/events', methods=['GET'])
def get_events():
    category = request.args.get('category', '')
    return jsonify(select_category(category))


@app.route('/api/categories', methods=['GET'])
def get_categories():
    data = get_all_categories()
    return jsonify(data)


@app.route('/')
def index():
    return 'Hello, this is the WonderMap backend!'


if __name__ == '__main__':
    app.run(debug=True)
