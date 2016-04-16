import json

from file_storage.auth import auth_needed as __required_access_level__
from file_storage.utils import Serializable as __Serializable__
from file_storage.utils import DEFAULT_SAVE_PATH as __asd__
from file_storage.users import User
from file_storage.users import Roles
from file_storage.auth import LoginManager
from file_storage.data import Data
from file_storage.file import File

all = [
    'Data',
    'DataStorage',
    'File',
    'LoginManager',
    'Roles',
]


class DataStorage(__Serializable__):

    __FILENAME__ = 'data.json'

    def __init__(self):
        absolute_path = '{}{}'.format(__asd__, self.__FILENAME__)
        try:
            with open(absolute_path, 'r') as config:
                data = json.loads(config.read)
            self.__data = list(map(lambda x: Data.deserialize(x), data))
        except OSError:
            self.__data = []

    def serialise(self):
        absolute_path = '{}{}'.format(__asd__, self.__FILENAME__)
        with open(absolute_path, "w") as config:
            config.write(json.dumps([
                data.serialise() for data in self.__data
            ]))

    @__required_access_level__(Roles.admin)
    def create(self, name):
        return Data(name)

    @__required_access_level__(Roles.user)
    def get(self, name=""):
        return filter(lambda x: x.name in name, self.__data)
