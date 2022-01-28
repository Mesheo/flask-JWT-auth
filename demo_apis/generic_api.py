from flask import Flask, request, jsonify

app = Flask(__name__)

# first argument of decorator helps to create the endpoint and
# second one says about the http methods the function can use
@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == "GET":
        return jsonify({"reponse": "GET request called"})
    elif request.method == 'POST':
        request_json = request.json
        name = request_json['name'] #getting the info on the 'name' key inside the json we send at postman
        return jsonify({"response": f"Hi {name}"})

if __name__ == '__main__':
    app.run(debug=True, port=9090)