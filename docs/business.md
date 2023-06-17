Business
===========

BUSINESS
-----------
endpoint: http://127.0.0.1:8000/api/business/
Allowed Methods: GET, POST

<h3>Request http method=POST</h3>

<ul>
Requires:
        <li>'name'=name of the business</li>
        <li>'image'=image of the business</li>
        <li>'description'=description of business</li>
        <li>'category'=category of business</li>
        <li>'phone'= business phone number</li>
        <li>'city'=city business is in</li>
        <li>'address'=business address</li>
</ul>

- sample request

```bash
curl --location 'http://127.0.0.1:8000/api/business/'\
--data-raw '{
        "name": "sola photos 1",
        "image": path_to_image_location,
        "description": "best photography you can afford,
        "category": "photo",
        "phone": "=2349034213456,
        "city": "Ado Ekiti",
        "address": "L58, idoile road",
}'
```

- sample response

```bash
{
        "name": "sola photos 1",
        "image": path_to_image_location,
        "description": "best photography you can afford,
        "category": "photo",
        "phone": "=2349034213456,
        "city": "Ado Ekiti",
        "address": "L58, idoile road",
        "id": "1",
        "active": "True",
        "code": "we21k"
},
```

When request is sent, a business with admin as logged-in user is created alongside a code for each business and active status is changed to True.
Users can only book session with active business. Code is a 5 character unique value assigned to each business.

<h3>Request http method=GET</h3>

- sample request
When request is sent, all registered business is returned.

- sample request

```bash
curl --location 'http://127.0.0.1:8000/api/business/'
```

- sample response

```bash
{
        {
                "name": "sola photos 1",
                "image": path_to_image_location,
                "description": "best photography you can afford,
                "category": "photo",
                "phone": "=2349034213456,
                "city": "Ado Ekiti",
                "address": "L58, idoile road",
                "id": "1",
                "active": "True",
                "code": "we21k"
        },
        {
                "name": "sola photos 2",
                "image": path_to_image_location,
                "description": "best photography you can afford,
                "category": "photography",
                "phone": "=2349034213456,
                "city": "Ido Ekiti",
                "address": "L68, idoile road",
                "id": "2",
                "active": "True",
                "code": "we22k"
        },
        {
                "name": "sola photos 3",
                "image": path_to_image_location,
                "description": "best photography you can afford,
                "category": "photo",
                "phone": "=2349034213456,
                "city": "Oye Ekiti",
                "address": "L78, idoile road",
                "id": "3",
                "active": "True",
                "code": "we23k"
        },
        {
                "name": "sola photos 4",
                "image": path_to_image_location,
                "description": "best photography you can afford,
                "category": "photography",
                "phone": "=2349034213456,
                "city": "Are Ekiti",
                "address": "L88, idoile road",
                "id": "4",
                "active": "True",
                "code": "we24k"
        }
}
```



FETCH CATEGORY BUSINESS
-------
endpoint: http://127.0.0.1:8000/api/business/category/cat/
Allowed Methods: GET
Returns all registered businesses with category==cat

<h3>Request http method=GET</h3>
- sample request

```bash
curl --location 'http://127.0.0.1:8000/api/business/category/photo/'
```

- sample response

```bash
{
        {
                "name": "sola photos 1",
                "image": path_to_image_location,
                "description": "best photography you can afford,
                "category": "photo",
                "phone": "=2349034213456,
                "city": "Ado Ekiti",
                "address": "L58, idoile road",
                "id": "1",
                "active": "True",
                "code": "we21k"
        },
        {
                "name": "sola photos 3",
                "image": path_to_image_location,
                "description": "best photography you can afford,
                "category": "photo",
                "phone": "=2349034213456,
                "city": "Oye Ekiti",
                "address": "L78, idoile road",
                "id": "3",
                "active": "True",
                "code": "we23k"
        }
}
```


FETCH SINGLE BUSINESSES
---------

endpoint: http://127.0.0.1:8000/api/business/id/pk/
Allowed Methods: GET
Returns registered businesses with id=pk

<h3>Request http method=GET</h3>
- sample request

```bash
curl --location 'http://127.0.0.1:8000/api/business/id/1/'
```

- sample response

```bash
{
        "name": "sola photos 1",
        "image": path_to_image_location,
        "description": "best photography you can afford,
        "category": "photo",
        "phone": "=2349034213456,
        "city": "Ado Ekiti",
        "address": "L58, idoile road",
        "id": "1",
        "active": "True",
        "code": "we21k"
}
```
