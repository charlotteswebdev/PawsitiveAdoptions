from flask import Flask, jsonify
from db import get_shelter_info, get_adoption_info, insert_new_dog_info

app = Flask(__name__)

@app.route('/PawsitiveAdoptions/adopt', methods=['GET'])
def adopt_a_dog():
    try:
        res = get_adoption_info()
        return jsonify(res)
    except Exception as exc:
        raise exc

@app.route('/PawsitiveAdoptions/rescue', methods=['POST'])
def add_new_dog():
    try:
        res = insert_new_dog_info()
        return jsonify(res)
    except Exception as exc:
        raise exc

@app.route('/PawsitiveAdoptions/shelter', methods=['GET'])
def summary_of_shelter():
    try:
        res = get_shelter_info()
        return jsonify(res)
    except Exception as exc:
        raise exc


if __name__ == '__main__':
    app.run(debug=True)