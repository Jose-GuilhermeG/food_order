from api.domain.enums import OrderStatus
from api.domain.validations import (
    EnumValidate,
    IdFieldValidation,
    PositiveNumberValidate,
    RequiredFieldValidation,
    TypeFieldValidation,
)


class Category:
    __id: int
    __name: str
    __slug: str

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = IdFieldValidation.validate(value)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = RequiredFieldValidation.validate(value, "name")

    @property
    def slug(self) -> str:
        return self.__slug

    @slug.setter
    def slug(self, value: str) -> None:
        validate_value = RequiredFieldValidation.validate(value, "slug")
        self.__slug = validate_value.lower().replace(" ", "-")

    def __str__(self) -> str:
        return self.__name


class Food:
    __id: int
    __name: str
    __slug: str
    __description: str
    __price: float
    __photos : list['FoodPhoto']

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = IdFieldValidation.validate(value)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = RequiredFieldValidation.validate(value, "name")

    @property
    def slug(self) -> str:
        return self.__slug

    @slug.setter
    def slug(self, value: str) -> None:
        validate_value = RequiredFieldValidation.validate(value, "slug")
        self.__slug = validate_value.lower().replace(" ", "-")

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        self.__description = TypeFieldValidation.validate(value , str , "description")

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        self.__price = PositiveNumberValidate.validate(value , 'price')

    @property
    def photos(self)->list['FoodPhoto']:
        return self.__photos

    @photos.setter
    def photos(self , value : list['FoodPhoto'])->None:
        self.__photos = TypeFieldValidation.validate(value , list , 'photos')

    def add_photo(self , value : 'FoodPhoto') -> None:
        self.__photos.append(value)

    def __str__(self) -> str:
        return f"{self.__name} - R${self.__price:.2f}"

    def __repr__(self):
        return self.__str__()

class FoodPhoto:
    __id: int
    __food_id: int
    __photo_url: str

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = IdFieldValidation.validate(value)

    @property
    def food_id(self) -> int:
        return self.__food_id

    @food_id.setter
    def food_id(self, value: int) -> None:
        self.__food_id = IdFieldValidation.validate(value)

    @property
    def photo_url(self) -> str:
        return self.__photo_url

    @photo_url.setter
    def photo_url(self, value: str) -> None:
        validated = RequiredFieldValidation.validate(value, "photo_url")
        self.__photo_url = TypeFieldValidation.validate(validated, str, "photo_url")

    def __str__(self) -> str:
        return f"FoodPhoto {self.__id} -> Food {self.__food_id}: {self.__photo_url}"



class Order:
    __order_identify: int
    __food_id: int
    __quantity: int
    __status: OrderStatus

    @property
    def order_identify(self) -> int:
        return self.__order_identify

    @order_identify.setter
    def order_identify(self, value: int) -> None:
        self.__order_identify = IdFieldValidation.validate(value , "order_identify")

    @property
    def food_id(self) -> int:
        return self.__food_id

    @food_id.setter
    def food_id(self, value: int) -> None:
        self.__food_id = IdFieldValidation.validate(value)

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        self.__quantity = int(PositiveNumberValidate.validate(value , 'quantity'))

    @property
    def status(self) -> OrderStatus:
        return self.__status

    @status.setter
    def status(self, value: str) -> None:
        self.__status = EnumValidate.validate(value , OrderStatus) #type: ignore

    def __str__(self) -> str:
        return f"Order {self.__order_identify} - Food {self.__food_id} x {self.__quantity} [{self.__status}]"


class OrderIdentify:
    __code: int
    __client_name: str

    @property
    def code(self) -> int:
        return self.__code

    @code.setter
    def code(self, value: int) -> None:
        self.__code = IdFieldValidation.validate(value)

    @property
    def client_name(self) -> str:
        return self.__client_name

    @client_name.setter
    def client_name(self, value: str) -> None:
        self.__client_name = RequiredFieldValidation.validate(value, "client_name")

    def __str__(self) -> str:
        return f"Order Code: {self.__code} - Client: {self.__client_name}"
