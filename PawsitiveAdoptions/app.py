from flask import Flask

app = Flask(__name__)

@app.route('/PawsitiveAdoptions/adopt', methods=['GET'])
def adopt_a_dog():
    try:
        db_adopt_dog()
    except Exception as exc:
        raise exc

@app.route('/PawsitiveAdoptions/rescue', methods=['POST'])
def add_new_dog():
    try:
        db_rescue_dog()
    except Exception as exc:
        raise exc

@app.route('/PawsitiveAdoptions/shelter', methods=['GET'])
def summary_of_shelter():
    try:
        db_shelter_overview()
    except Exception as exc:
        raise exc


if __name__ == '__main__':
    app.run(debug=True)
