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

- user_id
    - Foreign key to the user object.

- description
    - Describe the item.

- is_complete
    - boolean to represent if the item is complete or not.

- create_date
    - Date the item was created.

## API design

### Authentication

The server will support the following authentication methods:

#### Basic Authentication

### Routes

#### Get all items for a user

method: GET
route: */items*

| Data | Type | Description |
| ---- |:----:|------------:|
| id | integer | Id of the item |
| description | text | Describes the item |
| is_complete | boolean | Indicate if the item is complete |
| create_date | integer | Epoch time idicating creation date of the item |

The data will be served in JSON format as:

```
[
    {
        'id': <value>,
        'description': <value>,
        'is_complete': <value>,
        'create_date': <value>,
    },...
]
```

#### Create a new item for a user

method: POST
route: */items*

| Data | Type | Description |
| ---- |:-----|------------:|
| description | Text | Describes an item |

The POST data will be expected in the body as:

```
{
    'description': <value>,
}
```

### Throttle limit

The API throttle limit is 200,000 requests a minute.

## Future development

- Build frontend on web using a suitable framework.
- Build mobile interface for the same.
