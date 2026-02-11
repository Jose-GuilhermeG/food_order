FoodPhotoSerializerExample = {
    "photo_url" : "/static/example-1.png"
}

FoodSerializerExamples = [
    {
        "id" : 1,
        "name" : "Soverte de morango",
        "slug" : "soverte-de-morango",
        "description" : "Soverte de morango com leite ninho e cobertura de chocolate",
        "price" : 5.50,
        "photos" : [
            FoodPhotoSerializerExample
        ]
    },
]

FoodListSerializerExamples = {
        "id" : 1,
        "name" : "Soverte de morango",
        "slug" : "soverte-de-morango",
        "description" : "Soverte de morango com leite ninho e cobertura de chocolate",
        "price" : 5.50,
        "photo_url" : FoodPhotoSerializerExample["photo_url"]
    }


CategoryListSerializerExamples ={
        "name" : "Açai",
        "slug" : "acai",
        "image" : "/static/acai-image-1.png"
    }

CategoryDetailSerializerExamples = [
    {
        **CategoryListSerializerExamples,
        "foods" : [
            FoodListSerializerExamples
        ]
    }
]

OrderDetailSerializerExamples = {
    "food_id" : 5,
    "quantity" : 2,
    "status" : "Pendente"
}

OrderIdentifyCodeSerializerExamples = {
    "code" : 3
}

OrderIdentifySerializerExamples = [{
    **OrderIdentifyCodeSerializerExamples,
    "client_name" : "João",
    "orders" : [
        OrderDetailSerializerExamples,
    ]
}]