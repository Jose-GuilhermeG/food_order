from abc import ABC, abstractmethod


class ICache(ABC):

    @abstractmethod
    def set_cache(self , key : str , value)->None:
        pass

    @abstractmethod
    def get_cache(self , key : str):
        pass
