import typing

from pdfedit.utils import types
from pdfedit.utils.anchor import Anchor


class Element:
    """ A base-class for elements that can be included inside a section. """


class Section:
    """ The canvas can contain multiple sections. Each section can contain
    multiple elements, such as images, text, hyperlinks, etc. """

    def __init__(self,
                 *elements: Element,
                 anchor: Anchor,
                 position,
                 ):
        self.elements = elements
        self.anchor = anchor
        self.position = position

    def __generate_lines(self,) -> typing.List[typing.List[Element]]:
        pass

    @property
    def width(self,) -> types.PositiveNumber:

        return max(
            sum(element.width for element in line)
            for line in self.__generate_lines()
        )

    @property
    def height(self,) -> types.PositiveNumber:

        return sum(
            max(element.height for element in line)
            for line in self.__generate_lines()
        )
