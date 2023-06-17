Sessions
=======

Book Session
-------
endpoint: http://127.0.0.1:8000/api/sessions/book/pk/
Allowed Methods: POST
A request is made with the id(pk) of a business to book a session with.

<h3>Request http method=POST</h3>

When request is sent, all BookedSession are queried to for an active session with logged-in user and session with id=pk.

- sample request

```bash
curl --location 'http://127.0.0.1:8000/api/sessions/book/pk/'\
```

If there is an active session, return message saying user has an active session with business

- sample response

```bash
{
    'message': 'you have an open session with {business.name}'
}
```

If user has no active session with business, A session is created with ref_code and opened

- sample response

```bash
{
    'message': 'you have opened a session with {business.name}',
    'session code': session.ref_code
}
```

Accept Session
------
endpoint: http://127.0.0.1:8000/api/sessions/accept/pk/
Allowed Methods: POST
A request is made with the id(pk) of an opened BookedSession for user that is the admin of bookedsession business to accept a session request.

<h3>Request http method=POST</h3>

When request is sent, if logged-in user is admin of booked business in BookedSession, activate session.

- sample request

```bash
curl --location 'http://127.0.0.1:8000/api/sessions/accept/pk/'
```

- sample response

```bash
{
    'message': f'Session is active. Remember to close section after you complete the session.',
    'session code': bookedsession.ref_code
}
```

If logged-in user is not admin of booked business
- sample response

```bash
{
    'message': f'You are not the admin of {bookedsession.business.name}',
}
```



Decline Session
--------------
endpoint: http://127.0.0.1:8000/api/sessions/decline/pk/
Allowed Methods: POST
A request is made with the id(pk) of an opened BookedSession for user that is the admin of bookedsession business to decline a session request.


<h3>Request http method=POST</h3>

When request is sent, if logged-in user is admin of booked business in BookedSession, activate and then close session.

- sample request

```bash
curl --location 'http://127.0.0.1:8000/api/sessions/decline/pk/'
```

- sample response

```bash
{
    'message': f'Session is has been closed',
    'session code': bookedsession.ref_code
}
```

If logged-in user is not admin of booked business
- sample response

```bash
{
    'message': f'You are not the admin of {bookedsession.business.name}',
}
```


User close Session
------
endpoint: http://127.0.0.1:8000/api/sessions/user-close/pk/
Allowed Methods: POST
A request is made with the id(pk) of an active BookedSession for user that is the user of bookedsession  to close a session.

<h3>Request http method=POST</h3>

When request is sent, if logged-in user is user of BookedSession, then close session.

- sample request

```bash
curl --location 'http://127.0.0.1:8000/api/sessions/user-close/pk/'
```

If BookedSession is active, close session

- sample response
- 
```bash
{
    'message': f'session closed sucessfully',
    'session code': session.ref_code
}
```

If user has no active session with BookedSession business, return message that says user has no active session

- sample response
```bash
{
    'message': "You don't have an open session with {session.business.name}",
}
```


Admin close Session
---------
endpoint: http://127.0.0.1:8000/api/sessions/admin-close/pk/
Allowed Methods: POST
A request is made with the id(pk) of an active BookedSession for user that is the admin of bookedsession business to close a session.

<h3>Request http method=POST</h3>

When request is sent, if logged-in user is admin of BookedSession business, then close session.

- sample request
```bash
curl --location 'http://127.0.0.1:8000/api/sessions/admin-close/pk/'
```

If BookedSession is active, close session
- sample response

```bash
{
    'message': f'session closed sucessfully',
    'session code': session.ref_code
}
```

If user has no active session with id = pk, return message that says user has no active session
- sample response

```bash
{
    'message': "You don't have an open session with {session.user.username}",
}
```

User's Booked Session
--------
endpoint: http://127.0.0.1:8000/api/sessions/user-booked/
Allowed Methods: GET
A request is made to filter all active BookedSession with logged-in user as user of the session.

<h3>Request http method=GET</h3>

- sample request
```bash
curl --location 'http://127.0.0.1:8000/api/sessions/user-booked/'
```
If BookedSession is active,
- sample response

```bash
{
        {
                "user": "logged_in user's username",
                "admin": "business admin's username",
                "business": "business name",
                "opened" "True",
                "user_closed": "False",
                "admin_closed": "False",
                "id": "1",
                "active": "True",
                "ref_code": "session ref_code",
                "opened_date": "date session was opened(user booked session)",
                "close": "False",
                "closed_date": "empty(session is still active",
        },
}
```


User's Closed Session
-------
endpoint: http://127.0.0.1:8000/api/sessions/user-closed/
Allowed Methods: GET
A request is made to filter all closed BookedSession with logged-in user as user of the session.

<h3>Request http method=GET</h3>

- sample request

```bash
curl --location 'http://127.0.0.1:8000/api/sessions/user-closed/'
```

If BookedSession is closed,
- sample response

```bash
{
        {
                "user": "logged_in user's username",
                "admin": "business admin's username",
                "business": "business name",
                "opened" "False",
                "user_closed": "True",
                "admin_closed": "True",
                "id": "1",
                "active": "False",
                "ref_code": "session ref_code",
                "opened_date": "date session was opened(user booked session)",
                "close": "True",
                "closed_date": "date session was closed",
        },
}
```

Admin's Open Session
------
endpoint: http://127.0.0.1:8000/api/sessions/admin-opened/
Allowed Methods: GET
A request is made to filter all active BookedSession with logged-in user as admin of the session business.

<h3>Request http method=GET</h3>

- sample request

```bash
curl --location 'http://127.0.0.1:8000/api/sessions/admin-opened/'
```

- sample response

```bash
{
        {
                "user": "session user's username",
                "admin": "logged-in user's username",
                "business": "business name",
                "opened" "True",
                "user_closed": "False",
                "admin_closed": "False",
                "id": "1",
                "active": "True",
                "ref_code": "session ref_code",
                "opened_date": "date session was opened(user booked session)",
                "close": "False",
                "closed_date": "empty(session is still active",
        },
}
```

Admin's Closed Session
---------
endpoint: http://127.0.0.1:8000/api/sessions/admin-closed/
Allowed Methods: GET
A request is made to filter all closed BookedSession with logged-in user as admin of the booked session.

<h3>Request http method=GET</h3>

- sample request
```bash
curl --location 'http://127.0.0.1:8000/api/sessions/admin-closed/'\
```

- sample response
```bash
{
        {
                "user": "bookedsession user's username",
                "admin": "logged-in user's username",
                "business": "business name",
                "opened" "False",
                "user_closed": "True",
                "admin_closed": "True",
                "id": "1",
                "active": "False",
                "ref_code": "session ref_code",
                "opened_date": "date session was opened(user booked session)",
                "close": "True",
                "closed_date": "date session was closed",
        },
}
```
