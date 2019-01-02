from flask import Flask, jsonify, request

app = Flask(__name__)

# POST /get_url
# {
#     "url": "https://www.akc.org/wp-content/themes/akc/component-library/assets/img/welcome.jpg"
# }


@app.route('/get_url', methods=['POST'])
def get_url():
    request_data = request.get_json()
    print(request_data['url'])
    return jsonify({'predictions': ['dog', 'puppy']})


app.run(port=5000)
