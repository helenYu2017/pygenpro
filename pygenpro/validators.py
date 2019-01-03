
from . import errors


def not_none_validator(v):
    if v is None:
        raise errors.NoneIsNotAllowedError()
    return v