""" Contains the abstract `Position` object, and the `RelativePosition` and
`AbsolutePosition` objects that represent positions on a canvas. """

import typing
from abc import ABC, abstractmethod

from pdfedit.utils.types import PositiveNumber
from pdfedit import Canvas


class Position(ABC):
    """ An abstract object. Represents a position on the drawing pdf canvas. """

    def __init__(self,
                 x: PositiveNumber,
                 y: PositiveNumber):
        self.x, self.y = x, y

    @abstractmethod
    def to_real_position(self, canvas: Canvas
                         ) -> typing.Tuple[PositiveNumber, PositiveNumber]:
        """ Converts the position instance into a tuple that represents the
        real position of the object on the canvas. """


class RelativePosition(Position):
    """ Represent a relative position on the canvas. The X and Y values can
    be values between 0 and 1, and the real position is multiplied by the canvas
    size. For example, the relative position (0.5, 0.5) will represent exactly
    the center of the canvas. """

    def to_real_position(self, canvas: Canvas):
        return (
            self.x * canvas.width,
            self.y * canvas.height,
        )


class AbsolutePosition(Position):
    """ Represents an absolute position on the canvas, when the top left corner
    of the canvas is the (0, 0) point. """

    def to_real_position(self, _):
        return (self.x, self.y)
