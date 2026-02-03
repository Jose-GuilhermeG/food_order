import pytest

from api.adapters.schemas.models import FoodModel, FoodPhotoModel
from api.domain.entities import Food, FoodPhoto


class FoodMappingTest:
    def test_to_model(self,food_mapping, food_factory):
        food = food_factory.create(
            id=1,
            name="Pizza",
            slug="pizza",
            description="Deliciosa pizza",
            price=30.0,
            photos=[]
        )



        model = food_mapping.to_model(food)
        assert isinstance(model, FoodModel)
        assert model.id == 1
        assert model.name == "Pizza"
        assert model.slug == "pizza"
        assert model.description == "Deliciosa pizza"
        assert model.price == 30.0


    def test_to_entitie(self,food_mapping):
        model = FoodModel(
            id=2,
            name="Suco",
            slug="suco",
            description="Suco natural",
            price=5.5,
            photos=[
                FoodPhotoModel(
                    food_id=2,
                    photo_url="http://test.example.com"
                ),
            ]
        )

        entity = food_mapping.to_entitie(model)
        assert isinstance(entity, Food)
        assert entity.id == 2
        assert entity.name == "Suco"
        assert entity.slug == "suco"
        assert entity.description == "Suco natural"
        assert entity.price == 5.5
        assert len(entity.photos) == 1
        assert isinstance(entity.photos[0],FoodPhoto)


    def test_to_model_many(self,food_mapping, food_factory):
        foods = [
            food_factory.create(id=1, name="Pizza", slug="pizza", description="Pizza", price=30.0, photos=[]),
            food_factory.create(id=2, name="Suco", slug="suco", description="Suco", price=5.5, photos=[]),
        ]

        models = food_mapping.to_model_many(foods)
        assert all(isinstance(m, FoodModel) for m in models)
        assert [m.id for m in models] == [1, 2]


    def test_to_entitie_many(self,food_mapping):
        models = [
            FoodModel(id=1, name="Pizza", slug="pizza", description="Pizza", price=30.0),
            FoodModel(id=2, name="Suco", slug="suco", description="Suco", price=5.5),
        ]

        entities = food_mapping.to_entitie_many(models)
        assert all(isinstance(e, Food) for e in entities)
        assert [e.id for e in entities] == [1, 2]
