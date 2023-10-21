from flask import Flask, jsonify
from db_utils import db_shelter_overview, db_adopt_dog

app = Flask(__name__)


@app.route('/adopt/<location>/<age>/<size>/<sex>', methods=['GET'])
def adopt_a_dog(location=None, age=None, size=None, sex=None ):
    try:
        result = db_adopt_dog(location, age, size, sex)
        return jsonify(result)
    except Exception as exc:
        return jsonify({'error': str(exc)}), 500


@app.route('/PawsitiveAdoptions/rescue', methods=['POST'])
def add_new_dog():
    try:
        db_rescue_dog()
    except Exception as exc:
        raise exc


@app.route('/shelter', methods=['GET'])
def summary_of_shelter():
    try:
        shelter_info = db_shelter_overview()
        return jsonify(shelter_info)
    except Exception as exc:
        print(f" {exc} Failed to retrieve shelter information")


if __name__ == '__main__':
    app.run(debug=True)
