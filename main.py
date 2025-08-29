from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# User details
USER_ID = "john_doe_17091999"
EMAIL = os.getenv("EMAIL", "john@xyz.com")
ROLL_NUMBER = "ABCD123"

def alternating_caps(s):
    result = ""
    upper = True
    for char in s:
        if char.isalpha():
            result += char.upper() if upper else char.lower()
            upper = not upper
        else:
            result += char
    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        data = request.json.get("data", [])
        if not isinstance(data, list):
            return jsonify({"is_success": False, "message": "Invalid input"}), 400

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        sum_numbers = 0
        concat_letters = ""

        for item in data:
            item_str = str(item)
            if item_str.isdigit():
                if int(item_str) % 2 == 0:
                    even_numbers.append(item_str)
                else:
                    odd_numbers.append(item_str)
                sum_numbers += int(item_str)
            elif item_str.isalpha():
                alphabets.append(item_str.upper())
                concat_letters += item_str
            else:
                special_characters.append(item_str)

        concat_letters = alternating_caps(concat_letters[::-1])

        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "even_numbers": even_numbers,
            "odd_numbers": odd_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(sum_numbers),
            "concat_string": concat_letters
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

