import json
from flask import Flask, request, jsonify
import jwt


'''
DO NOT STORAGE YOUR API KEY INSEDE THE CODE, SEARCH FOR ENVIRONMENT VARIABLES. THIS A DEMO CODE FOR TEACHING PURPOSES
'''

KEY = "my_secret"

users = {
    'usuario1' : {'email': 'usuario1@',
                  'password': 'usuario1senha'},
    'usuario2' : {'email': 'usuario2@',
                  'password': 'usuario2senha'}
}

app = Flask(__name__)

@app.route('/api')
def api_hello_world():
    return "<h1> Voce quer logar? go to /login </h1>"

@app.route('/api/login', methods=['POST'])
def api_login():
    code = 500
    token = ''
    try:
        # collect user info from the HTTP request
        email = request.json['email']
        password = request.json['password']
    
        # Check if this user info exist inside our "database" and validate it
        for user in users:
            if users[user]['email'] == email:
                if users[user]['password'] == password:
                    code = 200
                    
                    # create the data we will put on the payload part of the JWT token
                    payload_data = {
                        'user': user,
                        'email': users[user]['email'],
                        'senha': users[user]['password']
                    }
                    
                    # Even tho the JWT token is made it from 3 parts we only pass two args because PyJWT by default sets header properties (the missing . here) as JWT and HASH256
                    token = jwt.encode(
                        payload=payload_data,
                        key=KEY #this must be a hidden thing on the code 
                    )
                    break 
                else:  
                    return jsonify({'erro': "suas credenciais estao erradas"})
            else:
                return jsonify({'erro': 'usuario nao encontrado'})

    except Exception as erro:
        message = f'{erro}'
        code = 500 
    
    return jsonify({'code': code, 'token': token})

@app.route("/api/secret", methods=["GET"])
def api_secret_route():
    #gettin token from bearer header
    raw_token = request.headers.get("Authorization")

    if not raw_token:
        return jsonify({
            'error': "Nao autorizado"
        }, 403)

    token = raw_token.split()[1]
    token_info = jwt.decode(token, key=KEY, algorithms="HS256")
    print(token_info)

    return  jsonify({
        'message': 'Mensagem Secreta'
    }, 200)

app.run(port=5000, debug=True)
