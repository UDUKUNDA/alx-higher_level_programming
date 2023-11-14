#!/usr/bin/python3
"""Now this represents a bbase class"""
class Base:
    __nb_objects = 0
    def __init__(self, id = None):
        """This is a constructor.
        Args:
        id: This is the parameter of the contructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """This will be Converting a list of dictionaries to a JSON string"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):

        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(json_string)
    @staticmethod
    def from_json_string(json_string):
        """This will Parse a JSON string and return a list of dictionaries"""

        if json_string is None or json_string == "":
            return []

        return json.loads(json_string)
     @classmethod
    def create(cls, **dictionary):
        """Create an instance with attributes based on the dictionary"""

        if cls.__name__ == "Rectangle":
            d_i = cls(1, 1)  
        elif cls.__name__ == "Square":
            d_i = cls(1)

        d_i.update(**dictionary)
        return d_i
    @classmethod
    def load_from_file(cls):
        """This method will Load instances from a JSON file and return a list of instances"""

        filename = cls.__name__ + ".json"
        instances = []

        try:
            with open(filename, 'r') as f:
                json_data = f.read()
                data_list = cls.from_json_string(json_data)
                for data_dict in data_list:
                    instance = cls.create(**data_dict)
                    instances.append(instance)

        except FileNotFoundError:
            pass

        return instances
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize instances to CSV format and write to a file"""

        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            for objects in list_objs:
                if cls.__name__ == "Rectangle":
                    line = "{},{},{},{},{}\n".format(objects.id, objects.width, objects.height, objects.x, objects.y)
                elif cls.__name__ == "Square":
                    line = "{},{},{},{}\n".format(objects.id, objects.size, objects.x, objects.y)
                f.write(line)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from CSV format and return a list of instances"""

        filename = cls.__name__ + ".csv"
        instances = []

        try:
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(data[1]), int(data[2]), int(data[3]), int(data[0]))
                    instances.append(instance)

        except FileNotFoundError:
            pass

        return instances

