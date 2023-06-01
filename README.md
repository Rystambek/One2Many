# One2One

## Database design

### Company

| Field | Type | Description |
| --- | --- | --- |
| id | int | Primary key |
| name | varchar(255) | Company name |
| website | varchar(255) | Company website |

### Product

| Field | Type | Description |
| --- | --- | --- |
| id | int | Primary key |
| company_id | int | Foreign key to company.id |
| name | varchar(255) | Product name |
| price | int | Product price |

## API

### Endpoints

#### Company

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /companies | Get all companies |
| GET | /companies/:id | Get company by id |
| POST | /companies | Create company |
| PUT | /companies/:id | Update company |
| DELETE | /companies/:id | Delete company |

#### Product

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /companies/:company_id/products | Get all products by company id |
| GET | /companies/:company_id/products/:id | Get product by id |
| POST | /companies/:company_id/products | Create product |
| PUT | /companies/:company_id/products/:id | Update product |
| DELETE | /companies/:company_id/products/:id | Delete product |

### Request & Response

#### Comapny

##### GET /companies

Request

```
curl -X GET http://localhost:3000/companies
```

Response

```
[
  {
    "id": 1,
    "name": "Apple",
    "website": "https://www.apple.com"
  },
  {
    "id": 2,
    "name": "Google",
    "website": "https://www.google.com"
  }
]
```

##### GET /companies/:id

Request

```
curl -X GET http://localhost:3000/companies/1
```

Response

```
{
  "id": 1,
  "name": "Apple",
  "website": "https://www.apple.com"
}
```

##### POST /companies

Request

```
curl -X POST -H "Content-Type: application/json" -d '{"name":"Microsoft","website":"https://www.microsoft.com"}' http://localhost:3000/companies
```

Response

```
{
  "id": 3,
  "name": "Microsoft",
  "website": "https://www.microsoft.com"
}
```

##### PUT /companies/:id

Request

```
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Microsoft","website":"https://www.microsoft.com"}' http://localhost:3000/companies/3
```

Response

```
{
  "id": 3,
  "name": "Microsoft",
  "website": "https://www.microsoft.com"
}
```

##### DELETE /companies/:id

Request

```
curl -X DELETE http://localhost:3000/companies/3
```

Response

```
{
  "id": 3,
  "name": "Microsoft",
  "website": "https://www.microsoft.com"
}
```

#### Product

##### GET /companies/:company_id/products

Request

```
curl -X GET http://localhost:3000/companies/1/products
```

Response

```
[
  {
    "id": 1,
    "company_id": 1,
    "name": "iPhone",
    "price": 1000
  },
  {
    "id": 2,
    "company_id": 1,
    "name": "iPad",
    "price": 500
  }
]
```

##### GET /companies/:company_id/products/:id

Request

```
curl -X GET http://localhost:3000/companies/1/products/1
```

Response

```
{
  "id": 1,
  "company_id": 1,
  "name": "iPhone",
  "price": 1000
}
```

##### POST /companies/:company_id/products

Request

```
curl -X POST -H "Content-Type: application/json" -d '{"name":"MacBook","price":2000}' http://localhost:3000/companies/1/products
```

Response

```
{
  "id": 3,
  "company_id": 1,
  "name": "MacBook",
  "price": 2000
}
```

##### PUT /companies/:company_id/products/:id

Request

```
curl -X PUT -H "Content-Type: application/json" -d '{"name":"MacBook","price":2000}' http://localhost:3000/companies/1/products/3
```

Response

```
{
  "id": 3,
  "company_id": 1,
  "name": "MacBook",
  "price": 2000
}
```

##### DELETE /companies/:company_id/products/:id

Request

```
curl -X DELETE http://localhost:3000/companies/1/products/3
```

Response

```
{
  "id": 3,
  "company_id": 1,
  "name": "MacBook",
  "price": 2000
}
```
