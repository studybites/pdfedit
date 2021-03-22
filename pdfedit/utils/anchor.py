""" Contains the `Anchor` class that lets you to change the default anchor
location. Also, contains 9 different pre-defined anchor objects, like
`AnchorLeftTop` and `AnchorCenterMiddle`. """


class Anchor:

    def __init__(self,
                 relative_pos_x: float,
                 relative_pos_y: float):
        self.relative_pos = (relative_pos_x, relative_pos_y)


# pylint: disable=too-few-public-methods

class AnchorTopLeft(Anchor):
    """ Set the anchor of a section or an element to the top left corner. """

    def __init__(self,):
        super().__init__(0, 0)


class AnchorCenterLeft(Anchor):
    """ Set the anchor of a section or an element to the center left corner. """

    def __init__(self,):
        super().__init__(0, 0.5)


class AnchorBottomLeft(Anchor):
    """ Set the anchor of a section or an element to the bottom left corner. """

    def __init__(self,):
        super().__init__(0, 1)


class AnchorTopMiddle(Anchor):
    """ Set the anchor of a section or an element to the top middle corner. """

    def __init__(self,):
        super().__init__(0.5, 0)


class AnchorCenterMiddle(Anchor):
    """ Set the anchor of a section or an element to the center of the element
    or section. """

    def __init__(self):
        super().__init__(0.5, 0.5)


class AnchorBottomMiddle(Anchor):
    """ Set the anchor of a section or an element to the bottom middle corner. """

    def __init__(self,):
        super().__init__(0.5, 1)


class AnchorTopRight(Anchor):
    """ Set the anchor of a section or an element to the top right corner. """

    def __init__(self,):
        super().__init__(1, 0)


class AnchorCenterRight(Anchor):
    """ Set the anchor of a section or an element to the center right corner. """

    def __init__(self):
        super().__init__(1, 0.5)


class AnchorBottomRight(Anchor):
    """ Set the anchor of a section or an element to the bottom right corner. """

    def __init__(self,):
        super().__init__(1, 1)
