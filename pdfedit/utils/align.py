""" Different align directions. Used by different elements and the interpretor
to align the element! """

import typing
from pdfedit.exceptions import InvalidElementAlignment


class Alignment:
    pass


class AlignToCenter(Alignment):
    pass


class AlignToRight(Alignment):
    pass


class AlignToLeft(Alignment):
    pass


ALIGNMENT_TABLE = {
    "center": AlignToCenter,
    "right": AlignToRight,
    "left": AlignToLeft,
}


def to_alignment_instance(param: typing.Union[str, Alignment]) -> Alignment:
    """ Converts the given param into an alignment instance, if possible.
    The given param could be a string, or an alignment instance. If there
    is a problem converting the param into an alignment instance, an
    `InvalidelementAlignment` exception will be raised. """

    if isinstance(param, Alignment):
        # If the given param is already an alignment instance,
        # returns the param!
        return param

    if isinstance(param, str):

        # Checks if the alignment string is a valid one
        if param.lower() in ALIGNMENT_TABLE:
            # If the string is valid
            return ALIGNMENT_TABLE[param.lower()]

    # If the string is not valid or it is not a string at all,
    # raises an error.
    raise InvalidElementAlignment(f"{param} is not a valid alignment")
