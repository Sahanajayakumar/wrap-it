from flask import Flask, request, jsonify
from .imageprocessing import convert_frames, convert_grayscale_match, convert_grayscale_query
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["POST"])
def hello():
    url = request.json.get("url")
    refv1=url
    rpath='D:/code/S1r/frames'
    frames = convert_frames(refv1, rpath)
    images = convert_grayscale_match(frames)

    qvd1='D:/code/S1q/s1ep4query.mp4'
    qpath='D:/code/S1q/frames'
    opath='D:/code/S1m'
    framesq = convert_frames(qvd1, qpath)
    imageq = convert_grayscale_query(framesq,images, opath)
    # if imageq:
    #     imageq = imageq[0]
    return jsonify(imageq)

@app.route("/postData", methods=["POST"])
def post_data():
    return request.json


if __name__ == "__main__":
    app.run(debug=True)
