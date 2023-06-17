Authentication
============
This API uses DRF default token authentication method. An access token is required to inorder to perform operations on some endpoints.

SIGN UP (register new user)
-----------

endpoint: http://127.0.0.1:8000/user/signup/
Requires a valid username, email, password, and a matching password2. This endpiont register user and creates auth token.

<h3>Request http method=POST</h3>

- sample request
```
curl --location 'http://127.0.0.1:8000/user/signup/' \
--data-raw '{
    "username": "sessionlord",
    "email": "sessionlord@yahoo.com",
    "password": "lord023sess",
    "password2": "lord023sess",
}'
```

- sample response
```
{
    "response": "Sucessfully created an account",
    "username": "demoladele",
    "token": "4d3be3188d488563604dbe85c554b0bf45178994"
}
```


LOGIN (login registered user)
-------------
endpoint: http://127.0.0.1:8000/user/login/
Requires a valid username, password.

<h3>Request http method=POST</h3>

- sample request
```
curl --location 'http://127.0.0.1:8000/user/login/' \
--data-raw '{
    "username": "sessionlord",
    "password": "lord023sess",
}'
```

- sample response
```
{
    "token": "9b6610887d1d213f1e27071f49948e01cd77073f"
}
```
