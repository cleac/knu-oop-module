import os

DEFAULT_SAVE_PATH = '/var/data/'


def build_absolute_path(filename):
    """Build absolute path to load or save file

    Arguments:
        filename {str} -- name of file
    """
    destination = DEFAULT_SAVE_PATH
    _, file_ext = os.path.splitext(filename)
    return os.path.join(destination, filename)


class Serializable:
    """Abstract interface for serializable classes."""

    def serialize():
        raise NotImplementedError("Serialization not implemented")


class Deserializable:
    """Abstract interface for deserializable classes."""

    @staticmethod
    def deserialize(json_string):
        raise NotImplementedError("Serialization not implemented")
