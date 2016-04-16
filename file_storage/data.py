import json

from file_storage.file import File
from file_storage.auth import auth_needed
from file_storage.users import Roles
from file_storage.utils import Deserializable
from file_storage.utils import Serializable


class Data(Serializable, Deserializable):
    """Implement the storage for files."""

    def __init__(self, name="SampleData", files=None):
        self.name = name
        self._files = files if files is None else []

    @auth_needed(Roles.moderator)
    def add_file(self, file):
        if not isinstance(file, File):
            raise TypeError("Only File's are accepted")
        if file not in self.files:
            self.files.append(file)
        else:
            raise ValueError("File already is in storage")

    @auth_needed(Roles.user)
    def get_file(self, id):
        if id >= len(self._files):
            raise ValueError("File not found")
        return self._files[id]

    @auth_needed(Roles.moderator)
    def update_file(self, id, data):
        file = self.get_file(id)
        file[id].data = data
        file[id].serialize()

    @auth_needed(Roles.moderator)
    def remove_file(self, id):
        file = self.get_file(id)
        file.delete()
        del self._files[id]

    @auth_needed(Roles.user)
    def has_file(self, id):
        return bool(self.get_file(id))

    def serialize(self):
        return json.dumps({
            'name': self.name,
            'files': [
                file.serialize()
                for file in self._files
            ]
        })

    @staticmethod
    def deserialize(json_string):
        data = json.loads(json_string)
        data.files = list(map(lambda x: File.deserialize(x), data.files))
        if not (data or 'name' in data):
            raise ValueError("Invalid json: {}".format(json_string))
        return Data(**data)
