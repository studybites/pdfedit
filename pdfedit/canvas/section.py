import typing

from reportlab.pdfgen.canvas import Canvas as genCanvas

from pdfedit.utils import types
from pdfedit.utils.anchor import Anchor, AnchorTopLeft
from pdfedit.utils.align import Alignment, AlignToLeft
from pdfedit.utils.position import Position

from pdfedit.elements.base import Element


class Section:
    """ The canvas can contain multiple sections. Each section can contain
    multiple elements, such as images, text, hyperlinks, etc. """

    def __init__(self,
                 *elements: Element,
                 width: types.PositiveNumber,
                 position: Position,
                 anchor: Anchor = AnchorTopLeft(),
                 align: Alignment = AlignToLeft(),
                 ):
        self.elements = elements
        self.width = width
        self.position = position
        self.anchor = anchor
        self.align = align

    def __generate_lines(self,) -> typing.List[typing.List[Element]]:
        pass

    def __get_line_width(self,
                         line: typing.List[Element]
                         ) -> types.PositiveNumber:
        """ Recives a line (row) of elements, and returns the sum of the widths
        of those elements. """
        return sum(element.width for element in line)

    def onto_canvas(self, canvas: genCanvas) -> None:

        start_y = self.position.y - (self.anchor.relative_y * self.height)
        start_x = self.position.x - (self.anchor.relative_x * self.width)

        cur_y = start_y
        for line in self.__generate_lines():
            line_height = 0

            cur_x_pad = self.align.relative_x * \
                (self.width - self.__get_line_width(line))
            cur_x = start_x + cur_x_pad

            for element in line:
                element.onto_canvas(canvas, cur_x, cur_y)
                cur_x += element.width

                line_height = max((line_height, element.height))
            cur_y += line_height

    @property
    def height(self,) -> types.PositiveNumber:

        # TODO: Can be improved and not generate the lines
        # each time this function is called

        return sum(
            max(element.height for element in line)
            for line in self.__generate_lines()
        )
