from enum import Enum

from api.domain.exceptions import IdValidationException , EmptyValidationException , ValidationException

class IdFieldValidation:
    @staticmethod
    def validate(value : int, key : str = "id" ) -> int:
        if not isinstance(value , int):
           raise IdValidationException("The id field must be a integer",key)
       
        if value < 0 :
            raise IdValidationException("The id field can't be negative",key)

        return value
    
class RequiredFieldValidation:
    @staticmethod
    def validate(value : str , key : str):
        if value is None:
                raise ValidationException(f"'{key}' can't be null")

        if not len(value):
            raise EmptyValidationException(f"'{key}' this field can't be empty")

        return value
    
class TypeFieldValidation:
    @staticmethod
    def validate(value : any , type_field : type , key : str):
        if not isinstance(value , type_field):
            raise ValidationException(f"'{key}' field must be of type {type_field.__name__}")

        return value
    
class PositiveNumberValidate:
    @staticmethod
    def validate(value : int | float , key : str) -> int:
        if value <= 0:
            raise ValidationException(f"{key} must be greater than zero" , key)
        return value
    
class EnumValidate:
    @staticmethod
    def validate(value : str , enum : Enum) -> str:
        normalized = value.strip().capitalize() 
        valid_values = [status.value for status in enum]
        if normalized not in valid_values: 
            raise ValidationException(f"Invalid status '{value}'. Must be one of {valid_values}") 
        
        return normalized