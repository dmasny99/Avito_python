import json


class JsonParser:
    """Parses json objects and creates attributes of python object"""
    def __init__(self, json_object: dict):
        for key, value in json_object.items():
            if isinstance(value, dict):
                value = JsonParser(value)
            setattr(self, key, value)


class ColorizeMixin:
    """Colorizes given text"""
    def __repr__(self) -> str:
        text = super().__repr__()
        return f'\033[1;{self.repr_color_code};40m {text}'


class BaseAdvert(JsonParser):  # created because of mixin properties
    """Creates advert object"""
    def __init__(self, json_object: dict):
        super().__init__(json_object)
        
    def __getattribute__(self, name):
        if name == 'class_':
            return object.__getattribute__(self, 'class')
        else:
            return object.__getattribute__(self, name)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price_value: float):
        if price_value < 0:
            raise Exception('ValueError: must be >= 0')
        elif price_value >= 0:
            self._price = price_value

    @price.deleter
    def price(self):
        self._price = None

    def __repr__(self) -> str:
        return f'{self.title} | {self.price} ₽'


class Advert(ColorizeMixin, BaseAdvert):
    """Creates advert object"""
    repr_color_code = 33  # yellow


if __name__ == '__main__':
    lesson_str = """{"title": "python",
                     "price": 1,
                     "location": {"address": "город Москва, Лесная, 7", "metro_stations": ["Белорусская"]}}"""
    pet_str = """{"title": "Вельш-корги",
                  "price": 1000,
                  "class": "dogs",
                  "location": {"address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"}}"""
    ad = Advert(json.loads(lesson_str))
    pet = Advert(json.loads(pet_str))
    print(ad.location.metro_stations)
    print(pet.class_)
    print(pet)
    ad.price = -1
