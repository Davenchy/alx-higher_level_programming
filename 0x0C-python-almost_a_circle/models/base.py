#!/usr/bin/python3
"""Module of the base class"""

import json
import csv


class Base:
    """The Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the base class with an id
        if ''id'' was set then its value is applied as ''id'' attr otherwise
        a auto increment id value will be set

        Args:
            id (int|None): the id of the current instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with attributes defined in **dictionary"""
        dummy = cls(*[1, 1])
        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        """Assigns *args or **kwargs as attributes values"""
        if len(args) >= 1:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']

    def to_dictionary(self):
        """converts instance into a dictionary of its attributes"""
        return self.__dict__

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a json string

        Args:
            list_dictionaries (list): the list of dictionaries to convert

        Returns:
            str: the json string"""
        if list_dictionaries is None:
            return "[]"
        if (not isinstance(list_dictionaries, list)
                or not all(isinstance(i, dict) for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dicts")
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string) -> list[dict]:
        """loads dictionaries from json string

        Args:
            json_string (str): the json string

        Returns:
            list[dict]"""
        if json_string is None:
            return []
        if type(json_string) is not str:
            raise TypeError("json_string must be a string")
        if not len(json_string):
            return []

        try:
            data = json.loads(json_string)
            if not isinstance(data, list):
                return []
            if not all(isinstance(i, dict) for i in data):
                return []
            return data
        except Exception:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a list of objects that inherits from the Base class to a file
        of the same name of the class name"""
        objs = list_objs[:]
        for i in range(len(objs)):
            item = objs[i]
            if isinstance(item, Base):
                objs[i] = item.to_dictionary()
            else:
                raise TypeError(r"""list_objs items must be instances of
                    classes inherits from Base""")
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(objs))

    @classmethod
    def load_from_file(cls):
        """Loads a list of objects that inherits from the Base class from a
        file of the same name of the class name"""
        try:
            with open(cls.__name__ + ".json", "r") as file:
                json_string = file.read()
            objs_list = Base.from_json_string(json_string)
            return map(lambda d: cls.create(**d), objs_list)
        except FileNotFoundError:
            return []
        except Exception as err:
            raise err

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves the objects in ''list_objs'' of type cls into a csv file
        of the same name of the class

        Args:
            list_objs (list): list of objects that inheit from Base"""
        objs = list_objs[:]
        header = None
        for i in range(len(objs)):
            item = objs[i]
            if isinstance(item, Base):
                d = item.to_dictionary()
                objs[i] = d.values()
                if header is None:
                    header = d.keys()
            else:
                raise TypeError(r"""list_objs items must be instances of
                    classes inherits from Base""")
        with open(cls.__name__ + ".csv", "w") as file:
            writer = csv.writer(file)
            if header is not None:
                writer.writerow(header)
            writer.writerows(objs)

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of objects that inherits from the Base class from a
        csv file of the same name of the class name"""
        try:
            objs_list = list()
            with open(cls.__name__ + ".csv", "r") as file:
                reader = csv.reader(file)
                header = None
                for row in reader:
                    if header is None:
                        header = row
                        continue
                    d = dict(zip(header, map(lambda v: int(v), row)))
                    obj = cls(*[1, 1])
                    obj.update(**d)
                    objs_list.append(obj)
            return objs_list
        except FileNotFoundError:
            return []
        except Exception as err:
            raise err
