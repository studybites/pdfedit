class PdfEditError:
    """ An error raised by the pdfedit module. """


class InvalidPdfElement(TypeError, PdfEditError):
    """ Raised when trying to create an element with other elements,
    but the given elements are not compatible with the new one. """
