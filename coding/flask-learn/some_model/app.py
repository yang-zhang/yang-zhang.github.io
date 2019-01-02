from flask import Flask, jsonify, request

app = Flask(__name__)


# POST /mymodel/predict_url
# {
#     "url": "https://www.akc.org/wp-content/themes/akc/component-library/assets/img/welcome.jpg"
# }
# http://127.0.0.1:5000/mymodel/predict_url
@app.route('/mymodel/predict_url', methods=['POST'])
def predict_url():
    request_data = request.get_json()
    print(request_data['url'])
    return jsonify({'predictions': ['dog', 'puppy']})


# POST /mymodel/predict_label
# {
#     "url": 'dog'
# }
# http://127.0.0.1:5000/mymodel/predict_label
@app.route('/mymodel/predict_label', methods=['POST'])
def predict_label():
    request_data = request.get_json()
    print(request_data['url'])
    return jsonify({'predictions':
                   ['/data/imgs/1.jpg',
                    '/data/imgs/5.jpg']})


app.run(port=5000)
