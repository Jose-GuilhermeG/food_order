from fastapi import Request
from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    @classmethod
    def to_schema(cls , entity : object):
        entity_atrrs = [atrr for atrr in dir(entity) if not atrr.startswith("__") and not atrr.endswith("__")]
        cls_atrrs = [atrr for atrr in cls.model_fields.keys() if atrr in entity_atrrs]
        instance = cls
        for atrr in cls_atrrs:
            setattr(instance,atrr,getattr(entity,atrr))

        return instance

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

class FoodListSerializer(BaseSchema):
    name : str
    slug : str
    description : str
    price : float

class CategoryListSerializer(BaseSchemaLink):
    name : str
    slug : str
    image : str
