from fastapi import Request
from pydantic import BaseModel, Field, computed_field

from api.adapters.docs.response_examples import (
    CategoryDetailSerializerExamples,
    CategoryListSerializerExamples,
    FoodListSerializerExamples,
    FoodSerializerExamples,
    OrderIdentifySerializerExamples,
)
from api.domain.enums import OrderStatus


class BaseSchema(BaseModel):
    @classmethod
    def to_schema(cls , entity: object):
        entity_atrrs = [
            atrr for atrr in dir(entity)
            if not atrr.startswith("__") and not atrr.endswith("__")
        ]
        cls_atrrs = [atrr for atrr in cls.model_fields.keys() if atrr in entity_atrrs]
        data = {}

        for atrr in cls_atrrs:
            value = getattr(entity, atrr)

            field_type = cls.model_fields[atrr].annotation
            if getattr(field_type, "__origin__", None) is list:
                inner_type = field_type.__args__[0] #type: ignore
                if issubclass(inner_type, BaseSchema):
                    value = [inner_type.to_schema(v) for v in value]

            elif isinstance(value, object) and issubclass(field_type, BaseSchema): #type: ignore
                value = field_type.to_schema(value) #type: ignore

            data[atrr] = value

        return cls(**data)


class BaseSchemaLink(BaseSchema):
    url : str | None = None
    view_name : str | None = Field(exclude=True , default=None)
    lookup_field : str | None = Field(exclude=True , default=None)

    @classmethod
    def to_schema(cls , entity : object , request : Request | None = None):
        instance = super().to_schema(entity)
        if request and cls.view_name and cls.lookup_field:
            lookup_value = getattr(entity , cls.lookup_field)
            instance.url = request.url_for(cls.view_name , **{cls.lookup_field : lookup_value})
        return instance


class FoodPhotoSerializer(BaseSchema):
    photo_url : str = Field(examples=["/static/example_1.com"])

class FoodSerializer(BaseSchema):
    id : int
    name : str
    slug : str
    description : str
    price : float
    photos : list[FoodPhotoSerializer]

    model_config = {
        "json_schema_extra" : {
            "examples" : FoodSerializerExamples #type: ignore
        }
    }

class FoodListSerializer(FoodSerializer):
    photos : list[FoodPhotoSerializer] = Field(exclude=True)

    @computed_field #type: ignore
    @property
    def photo_url(self) -> str:
        return self.photos[0].photo_url

    model_config = {
        "json_schema_extra" : {
            "example" : FoodListSerializerExamples #type: ignore
        }
    }

class CategoryListSerializer(BaseSchemaLink):
    name : str
    slug : str
    image : str

    model_config = {
        "json_schema_extra":{
            "example" : CategoryListSerializerExamples #type: ignore
        }
    }

class CategoryDetailSerializer(CategoryListSerializer):
    foods : list[FoodListSerializer]

    model_config = {
        "json_schema_extra":{
            "example" : CategoryDetailSerializerExamples #type: ignore
        }
    }

class OrderDetailSerializer(BaseSchema):
    food_id : int
    quantity : int
    status : OrderStatus

class OrderWithFoodSerializer(BaseSchema):
    food : FoodListSerializer
    quantity : int
    status : OrderStatus

class OrderIdentifyCodeSerializer(BaseSchema):
    code : int

class OrderIdentifySerializer(BaseSchema):
    client_name : str
    orders : list[OrderDetailSerializer]

    model_config = {
        "json_schema_extra" : {
            "examples" : OrderIdentifySerializerExamples #type: ignore
        }
    }

class OrderIdentifyDetailSerializer(OrderIdentifySerializer , OrderIdentifyCodeSerializer):
    pass

class RegisterOrderIdentifySerializer(OrderIdentifySerializer):
    pass

class OrderIdentifyFoodSerializer(OrderIdentifyCodeSerializer , OrderIdentifySerializer):
    orders : list[OrderWithFoodSerializer] #type: ignore
