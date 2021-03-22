class PdfEditError(Exception):
    """ An error raised by the pdfedit module. """


class InvalidPdfElement(TypeError, PdfEditError):
    """ Raised when trying to create an element with other elements,
    but the given elements are not compatible with the new one. """


class InvalidElementAlignment(PdfEditError):
    """ Raised when the given alignment string doesn't match any known
    alignment option, or if the given object is not a string at all. """

class InvalidAnchor(ValueError, PdfEditError):
    """ Raised when the given anchor setting is invalid. """


class InvalidBackground(ValueError, PdfEditError):
    """ Raised when the given background is invalid. Background can be a
    file-like object that represents an image, a path to an image, or
    a string that represents a color. """
