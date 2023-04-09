from flask import Flask, request, render_template
from flask_cors import CORS
from actions.db_operations import validate_user


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def post():
    value = request.get_json()
    result = validate_user(
        uname=value["username"],
        password=value["password"]
    )

    result = {
        "result": result,
    }

    result = {str(key): value for key, value in result.items()}
    return result


@app.route("/payment", methods=['POST'])
def post_payment():
    value = request.get_json()
    card_details = {
                "card_number": "123456789012",
                "expiry_date": "12/23",
                "cvv": "333"
            }

    if all([
        value["card_number"] == card_details["card_number"],
        value["expiry_date"] == card_details["expiry_date"],
        value["cvv"] == card_details["cvv"]
    ]):
        result = 1
    else:
        result = 0
    result = {
        "result": result,
    }
    result = {str(key): value for key, value in result.items()}
    # return jsonify(result=result)
    return result


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
