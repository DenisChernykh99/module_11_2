import inspect


def introspection_info(obj):
    type_obj = type(obj).__name__ # Тип объекта
    dir_obj = dir(obj) # Список атрибутов объекта

    # Сортировка атрибутов и методов
    metods = []
    attrs = {}
    for attr in dir_obj:
        try:
            value = getattr(obj, attr)
            if callable(value):
                metods.append(attr)
            else:
                attrs[attr] = value
        except AttributeError:
            pass  # Некоторые специальные методы могут вызывать ошибку при попытке получить их значение
    #module_obj = sys.modules(obj)

    # Узнаем модуль объекта
    module_obj = inspect.getmodule(obj)

    return {'Тип объекта': type_obj,
            'Атрибуты': attrs,
            'Методы': metods,
            'Модуль': module_obj}

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


number_info = introspection_info(42)
string_info = introspection_info('Привет')
class_info = introspection_info(Table)
print(number_info)
print(string_info)
print(class_info)