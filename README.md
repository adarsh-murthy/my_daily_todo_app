# Daily Todo App

A simple no-frill to-do application that helps you plan your day and lets you
see how you do at the end of the day.

## Features

- Create new items everyday.
- Complete items during the course of the day.
- Cannot change items of the past but can view them.
- View analytics on how your planning is going on some timely cadence.

## MVP

This is my first attempt at building a functioning application in my spare
time. The first version will contain:

- Build backend using falcon framework.
- Use peewee as backend ORM.
- Design API endpoints for any client to use.

## Model Design

### Item

| Attribute | Type | Description |
| --------- |:----:|------------:|
| id | Integer | Primary key of the object |
| user_id | Integer | Foreign key to the user model |
| create_date | Integer | Create date in epoch format |
| description | text | Description of the to-do item |
| is_complete | boolean | Indicates if the item is complete or not |

## API design

### Authentication

The server will support the following authentication methods:

#### Basic Authentication

### Endpoints

#### Items

Get or create items for a given user.


##### URL: `/items`

##### method `GET`

##### Authentication required: `YES`

| Data | Type | Description |
| ---- |:----:|------------:|
| id | integer | Id of the item |
| description | text | Describes the item |
| is_complete | boolean | Indicate if the item is complete |
| create_date | integer | Epoch time idicating creation date of the item |

##### Success Response

###### Code `200`

###### Body:
```
[
    {
        "id": <value>,
        "description": <value>,
        "is_complete": <value>,
        "create_date": <value>,
    },...
]
```

##### Error Response

###### Code `401`

###### Body:
```
{
    "message": "Not Authorized",
}
```

###### Code `400`

###### Body:
```
{
    "message": <error_message>,
}
```

###### Code `404`

###### Body:
```
{
    "message": "Could not find item for given id"
}
```

###### Code `500`

###### Body:
```
{
    "message": "Oops! Something went wrong. We will look into it and get back to you"
}
```

##### method `POST`

##### Authentication required: `YES`

| Data | Type | Description |
| ---- |:-----|------------:|
| description | text | Describes an item |

The POST data will be expected in the body as:

```
{
    "description": <value>,
}
```

##### Success Response

###### Code: `201`

###### Body:
```
{
    "id": "1",
}
```

##### Error Response

###### Code `401`

###### Body
```
{
    "message": "Not Authorized",
}
```

###### Code `400`

###### Body
```
{
    "message": <error_message>,
}
```

###### Code `500`

###### Body:
```
{
    "message": "Oops! Something went wrong. We will look into it and get back to you"
}
```

##### method `PUT`

##### Authentication required: `YES`

| Data | Type | Description |
| ---- |:-----|------------:|
| id | integer | ID of the item to be updated |
| description | text | Describes an item |
| is_complete | boolean | Indicate if the item is complete |

Here, the description and is_complete are both optional.
The PUT data will be expected in the body as:

```
{
    "id": <value>,
    "description": <value>,
    "is_complete": "True",
}
```

##### Success Response

###### Code: `200`

###### Body:
```
{
    "id": "1",
}
```

##### Error Response

###### Code `401`

###### Body
```
{
    "message": "Not Authorized",
}
```

###### Code `400`

###### Body
```
{
    "message": <error_message>,
}
```

###### Code `400`

###### Body:
```
{
    "message": <error_message>,
}
```

###### Code `404`

###### Body:
```
{
    "message": "Could not find item for given id"
}
```

###### Code `500`

###### Body:
```
{
    "message": "Oops! Something went wrong. We will look into it and get back to you"
}
```

### Throttle limit

The API throttle limit is 200,000 requests a minute.

## Future development

- Build frontend on web using a suitable framework.
- Build mobile interface for the same.
