import json

from file_storage.users import User
from file_storage.users import Roles
from file_storage.utils import Serializable
from file_storage.utils import DEFAULT_SAVE_PATH


def auth_needed(access_level):
    def outer_wrapper(func):
        def wrapper(*args, **kargs):
            cur_access_level = LoginManager().logged_in_user_access_level()
            if cur_access_level.value >= access_level:
                return func(*args, **kargs)
            raise ValueError("Access denied")
        return wrapper
    return outer_wrapper


class LoginManager(Serializable):
    """Login manager class.

    Class that implements all the logging in interactions: creating users
    and using their credentials to log in.
    Implemented as Singleton.
    """

    __FILENAME__ = 'auth.json'

    __instance = None
    __users = None
    __authorised_user = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super(LoginManager, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__users = []
        self.deserialize()

    @auth_needed(Roles.superadmin)
    def register_user(self, user):
        if user.login in map(lambda x: x.name, self.__users):
            raise ValueError('User with login "{}" exists'.format(user.login))
        self.__users.append(user)

    @auth_needed(Roles.superadmin)
    def delete_user(self, id):
        if not self.__users[id]:
            raise ValueError("User with id {} not found".format(id))
        del self.__users[id]

    def __validate_login_password(self, user, login, password):
        return user.login == login and user.password == password

    def sign_in(self, login, password):
        user = next(filter(
            lambda x: self.__validate_login_password(x, login, password),
            self.__users,
        ))
        if not user:
            raise ValueError("Login or password incorrect")
        self.__authorised_user = user

    def sign_out(self):
        if self.__authorised_user:
            self.__authorised_user = None
        else:
            raise Exception("You are not signed in!")

    def logged_in_user_access_level(self):
        if not self.__authorised_user:
            raise ValueError("You need to log in to proceed")
        return self.__authorised_user.role

    def serialize(self):
        absolute_path = '{}{}'.format(DEFAULT_SAVE_PATH, self.__FILENAME__)
        with open(absolute_path, "w") as config:
            config.write(json.dumps([
                user.serialise() for user in self.__users
            ]))

    def deserialize(self):
        absolute_path = '{}{}'.format(DEFAULT_SAVE_PATH, self.__FILENAME__)
        try:
            with open(absolute_path, 'r') as config:
                data = json.loads(config.read)
            self.__users = list(map(lambda x: User.deserialize(x), data))
        except OSError:
            self.__users = [
                User('admin', password='admin', role=Roles.superadmin)
            ]
