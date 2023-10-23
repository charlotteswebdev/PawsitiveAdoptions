import requests
from flask import Flask, jsonify, request
from db_utils import db_shelter_overview, db_adopt_dog, db_insert_new_member

app = Flask(__name__)


@app.route('/adopt/<location>/<age>/<size>/<sex>', methods=['GET'])
def adopt_a_dog(location=None, age=None, size=None, sex=None ):
    try:
        result = db_adopt_dog(location, age, size, sex)
        return jsonify(result)
    except Exception as exc:
        return jsonify({'error': str(exc)}), 500


@app.route('/new', methods=['POST'])
def add_new_member():
    try:
        data = request.get_json()
        full_name = data['full_name']
        email_address = data['email_address']
        new_member = {
            'full_name': full_name,
            'email_address': email_address
        }
        db_insert_new_member(new_member)
        return 'Membership updated',200
    except Exception as exc:
        error_message = {'error': str(exc)}
        return jsonify(error_message),500


@app.route('/shelter', methods=['GET'])
def summary_of_shelter():
    try:
        shelter_info = db_shelter_overview()
        return jsonify(shelter_info)
    except Exception as exc:
        print(f" {exc} Failed to retrieve shelter information")


if __name__ == '__main__':
    app.run(debug=True)
