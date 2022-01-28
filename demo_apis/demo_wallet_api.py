from flask import Flask, jsonify, request

app = Flask(__name__)

wallets = [
    {
        'name': 'carteira1',
        'assets': [
            {
                'name': 'btc',
                'quantity': 100
            },
            {
                'name': 'eth',
                'quantity': 200
            }
        ]
    },
    {
        'name': 'carteira2',
        'assets': [
            {
                'name': 'sol',
                'quantity': 100
            },
            {
                'name': 'ltc',
                'quantity': 50
            }
        ]
    }
]

users = [
    {
        'email': 'usuario@1',
        'senha': 'senha@1'
    },
    {
        'email': 'usuario@2',
        'senha': 'senha@2'
    }
]

# home ✅
@app.route('/')
def home():
    return "Welcome to the Wallet Api"

# Get all wallets info ✅
@app.route('/wallets')
def get_all_wallets():
        return jsonify({
            "wallets" : wallets
        })

# Get a specific wallet info ✅
@app.route('/wallets/<string:name>', methods=['GET'])
def get_wallet_name(name):
    for wallet in wallets:
        if(wallet["name"] == name):
            return jsonify(wallet)
    return jsonify({'message': 'wallet does not exist'})

# Get a specific wallet asset info ✅
@app.route('/wallets/<string:name>/assets', methods=['GET'])
def get_wallet_asset(name):
    for wallet in wallets:
        if(wallet["name"] == name):
            return jsonify(wallet['assets'])
    return jsonify({'message': 'wallet does not exist'})

# Post a new wallet ✅
@app.route('/wallet', methods=['POST'])
def create_wallet():
    request_data = request.get_json()
    new_wallet = {
        'name': request_data['name'],
        'assets': []
    }
    wallets.append(new_wallet)
    return jsonify(new_wallet)

# Post a new wallet asset ✅
@app.route('/wallets/<string:name>/assets', methods=['POST'])
def create_wallet_asset(name):
    request_data = request.get_json()
    for wallet in wallets:
        if(wallet['name'] == name):
            new_asset = {
                'name': request_data['name'],
                'quantity': request_data['quantity']
            }
            wallet['assets'].append(new_asset)
            return jsonify(new_asset)
    return jsonify({'message':'wallet does not exist'})


app.run(port=5000)

##### EXEMPLE OF ENDPOINTS #####
# GET METHOD http://127.0.0.1:5000/wallets/
# GET METHOD http://127.0.0.1:5000/wallets/{name_of_wallet}
# GET METHOD http://127.0.0.1:5000/wallets/{name_of_wallet}/assets
# POST METHOD http://127.0.0.1:5000/wallet + a json like above
'''
{
    'name': name_of_wallet,
    'assets': [
        {
            'name': name_of_the_asset,
            'quantity': quantity_of_the_wallet
        }
    ]
}
'''
# POST METHOD http://127.0.0.1:5000/wallets/{name_of_wallet}/assets + likely json above
'''
{
        "name": name_of_the_asset,
        "quantity": quantity_of_the_asset
}
'''
