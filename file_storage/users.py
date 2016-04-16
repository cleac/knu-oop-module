import json

from enum import IntEnum

from file_storage.utils import Deserializable
from file_storage.utils import Serializable

Roles = IntEnum("Roles", {
    'user': 1,
    'moderator': 2,
    'admin': 3,
    'superadmin': 4
})


class User(Serializable, Deserializable):

    def __init__(
            self, login, name='Anonymous', role=Roles.user,
            password='password'):
        self.name = name
        self.login = login
        self.role = role
        self.password = password

    def serialize(self):
        return json.dumps({
            'name': self.name,
            'login': self.login,
            'role': self.role.value,
            'password': self.password,
        })

    @staticmethod
    def deserialize(json_string):
        data = json.loads(json_string)
        for field in ['name', 'login', 'role', 'password']:
            if field not in data:
                raise ValueError("Invalid json {}".format(json_string))
        data.role = Roles(data.role)
        return User(**data)

    def __repr__(self):
        return '<User name={} access={}'.format(
            self.name, self.role)
