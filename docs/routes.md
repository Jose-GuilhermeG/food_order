# Routes
This file has the docs about frontend and backend routes

- [BackEnd](#api--backend)

## APi / Backend

By default the fastApi gives two routes of docs :
- /docs 
- /redoc

all both do have the same function : show the api routes and how it works , but if you don't want to run the application and read the completed doc here had the basic routes docs:

### food:

#### List food:
- **GET**: `/food/`
- **Description** : show all foods register in the database
- **Response/Body**: 
```json
    [
        {
            "name" : "Salad",
            "slug" : "salad",
            "description" : "a simple salad made with apple , lettuce and carrot ",
            "price" : 5.0,
            "photos" : [
                "/static/food_photos/salad_1.png"
            ]
        }
    ]
```

#### Food details:
- **GET**: `/food/<slug>/`
- **Description** : get a food by its slug and show all details
- **Params** : 
    - **slug** : slug of the food what you wanna
- **Response/Body**:
```json
{
  "name": "Hambúrguer Artesanal",
  "slug": "hambúrguer-artesanal",
  "description": "Blend premium com queijo cheddar, bacon e molho especial",
  "price": 28.9,
  "photos": [
    {
      "photo_url": "/static/food_photos/hamburguer_1.png"
    }
  ]
}
```

#### List category:
- **GET**: `/category/` 
- **Description**: show all categories register in the database 
- **REsponse/Body**:
```json
    [
        {
            "name": "Todos",
            "slug": "todos",
            "image": "/static/categories/todos-icon.png"
        },
    ]
```


#### Category details:
- **GET**: `/category/<slug>/`
- **Description** : get a category by its slug and show all details
- **Params** : 
    - **slug** : slug of the category what you wanna
- **Response/Body**:
```json
{
  "name": "Todos",
  "slug": "todos",
  "image": "",
  "foods": [
    {
      "name": "Hambúrguer Artesanal",
      "slug": "hambúrguer-artesanal",
      "description": "Blend premium com queijo cheddar, bacon e molho especial",
      "price": 28.9,
      "id": 27,
      "photo_url": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400&h=300&fit=crop"
    },
    {
      "name": "Pizza Margherita",
      "slug": "pizza-margherita",
      "description": "Molho de tomate, mussarela de búfala e manjericão fresco",
      "price": 42,
      "id": 28,
      "photo_url": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400&h=300&fit=crop"
    },
  ]
}
```