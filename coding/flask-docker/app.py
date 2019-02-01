from flask import request
import flask
from waitress import serve
import model


if __name__ == "__main__":
    app = flask.Flask(__name__)


    @app.route("/", methods=["GET"])
    def index():
        return flask.jsonify(True)

    @app.route('/pred_url', methods=['POST'])
    def pred_url():
        try:
            req = request.get_json()
            print(req['url'])
        except:
            res = flask.jsonify([])
            res.status_code = 404
            return res
        return flask.jsonify({'predictions': ['dog', 'puppy']})

    serve(app, host="0.0.0.0", port=9900, ipv6=False, ipv4=True)
