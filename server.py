import json
import os

from ingredient_phrase_tagger.training import parse_ingredients

from flask import Flask, request

model_path = os.getenv("MODEL_PATH", "")

app = Flask(__name__)

@app.route("/ingredients", methods=["POST"])
def ingredients():
    if request.method == "POST":
        body = request.get_json()
        crf_output = parse_ingredients._exec_crf_test(body["data"], model_path)
        results = json.loads(parse_ingredients._convert_crf_output_to_json(crf_output.rstrip().split("\n")))
        return {"data": results}
