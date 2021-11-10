import json


class CustomError(Exception):
    pass


class JsonParser:
    """Parses json objects and creates attributes of python object"""
    def __init__(self, json_object: dict):
        for key, value in json_object.items():
            if key == 'location':
                value = JsonParser(value)
            setattr(self, key, value)


class ColorizeMixin:
    """Colorizes given text"""
    def __repr__(self):
        return f'\033[1;{self.repr_color_code};40m {self.title} | {self.price} ₽'


class ParentAdvert:  # created because of mixin properties
    """Creates advert object"""
    def __init__(self, json_object: dict):
        self.__dict__ = JsonParser(json_object).__dict__
        if 'price' in JsonParser(json_object).__dict__:
            if JsonParser(json_object).__dict__['price'] < 0:
                raise CustomError('ValueError: must be >= 0')
        else:
            self.price = 0

    def __repr__(self):
        return f'{self.title} | {self.price}'


class Advert(ColorizeMixin, ParentAdvert):
    """Creates advert object"""
    repr_color_code = 33 # yellow

    def __init__(self, json_object: dict):
        super().__init__(json_object)


if __name__ == '__main__':
    lesson_str = """{"title": "python",
                     "price": 0,
                     "location": {"address": "город Москва, Лесная, 7", "metro_stations": ["Белорусская"]}}"""
    pet_str = """{"title": "Вельш-корги",
                  "price": 1000,
                  "class": "dogs",
                  "location": {"address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"}}"""
    ad = Advert(json.loads(lesson_str))
    pet = Advert(json.loads(pet_str))
    print(ad.location.address)
    print(ad.price)
    print(ad)
    print(pet)
