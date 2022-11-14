from flask import Flask, request
from ably import AblyRest
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

PUBLISHER_KEY = 'Yomf6g.5FxiCA:9dIw0WsNOeB3MAlVvRErOlJVWEqvwvudPyEVu6c_vVA'
SUBSCRIBER_KEY = 'Yomf6g.ZD_bmg:pjzHmVjd-gaDboWTx440089linqJeJKLPAW4l8ZcVII'

@app.route('/get_token', methods=['POST'])
async def get_token():
    request_data = request.get_json()
    client_type = request_data['client_type']
    user_id = request_data['user_id']
    print("client_type: ", client_type)
    API_KEY = PUBLISHER_KEY if client_type == 'organizer' else SUBSCRIBER_KEY
    print("API_KEY: ", API_KEY)
    ably = AblyRest(key=API_KEY)
    token_request_data = {'clientId': user_id, 'ttl': 36000000}
    async with AblyRest(API_KEY) as ably:   
        token_request = await ably.auth.request_token(token_params=token_request_data)
        return {"token": token_request.token}
    



if __name__ == '__main__':
    app.run(debug=True)