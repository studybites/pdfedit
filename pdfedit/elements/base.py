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

    @property
    def width(self,) -> types.PositiveNumber:
        pass

    @property
    def height(self,) -> types.PositiveNumber:
        pass
