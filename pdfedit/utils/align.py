""" Different align directions. Used by different elements and the interpretor
to align the element! """

from pdfedit.utils.types import Percentage


class Alignment:

    def __init__(self, relative_x: Percentage):
        self.relative_x = relative_x


class AlignToCenter(Alignment):

    def __init__(self,):
        super().__init__(0.5)


class AlignToRight(Alignment):

    def __init__(self,):
        super().__init__(1)


class AlignToLeft(Alignment):

    def __init__(self,):
        super().__init__(0)
