import json
import os
import uuid

from file_storage.utils import Deserializable
from file_storage.utils import Serializable
from file_storage.utils import build_absolute_path


class File(Serializable, Deserializable):
    """Implement file interactions."""

    def __init__(self, name="sample_file.txt", data="", file_name=""):
        self.name = name
        self.data = data
        self.file_name = file_name
        if file_name:
            with open(build_absolute_path(self.file_name), "r") as file_data:
                self.data = file_data.read()

    def serialize(self):
        _, file_ext = os.path.splitext(self.name)
        if not self.file_name:
            self.file_name = '{}{}'.format(uuid.uuid4().hex, file_ext)
        with open(build_absolute_path(self.filename), "w") as output_file:
            output_file.write(self.data)

    @staticmethod
    def deserialize(json_string):
        data = json.loads(json_string)
        if not (data or 'name' in data or 'file_name' in data):
            raise ValueError("Invalid json: {}".format(json_string))
        return File(**data)

    def __str__(self):
        return json.dumps({
            'name': self.name,
            'file_name': self.filename,
        })

    def __repr__(self):
        return "<File name={}>".format(self.name)
