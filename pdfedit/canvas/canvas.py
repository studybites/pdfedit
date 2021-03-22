
import typing

from PIL import Image
from reportlab.pdfgen.canvas import Canvas as genCanvas

from pdfedit.utils import types
from pdfedit.exceptions import InvalidBackground


class Canvas:
    """ Design from zero a single page in a pdf file. """

    def __init__(self,
                 width: types.PositiveNumber,
                 height: types.PositiveNumber,
                 background: typing.Union[
                     types.ColorString,
                     Image.Image] = None,
                 ):
        self.width = width
        self.height = height
        self.background = background

    def _generate(self, file) -> None:
        """ Generates the canvas art and saves it in pdf foramt to the given
        file object. """

        # Creates an empty canvas generator with the given dimensions.
        canvas = genCanvas(
            file,
            pagesize=(self.width, self.height),
            bottomup=False,
        )

        # If a background is given,
        # adds the background to the canvas.
        if self.background is not None:
            self.__add_background(canvas)

        # "Update" the page and write into the given file.
        canvas.showPage()
        canvas.save()

    # - - - B A C K G R O U N D - - - #

    def __add_background(self, canvas: genCanvas) -> None:
        """ Adds the background that is saved in the `self.background` property
        to the given canvas. """

        if isinstance(self.background, Image.Image):
            # If the given background is an image,
            # adds an image as the background.

            self.__add_background_image(canvas, self.background)
            return

        # Otherwise, assumes that the given background is a path to an image,
        # and tries to open it!

        try:
            self.__add_background_image(
                canvas, self.background
            )

        except FileNotFoundError:
            # If the background is not actually a path to an image.
            # assumes that the background is a color, and tries to
            # create a rectangle to fill the background with the given color

            try:
                self.__add_background_color(canvas, self.background)

            except ValueError as _:
                # If the background is not even a color, raises an error.
                raise InvalidBackground(
                    f"{self.background} is not a valid background color or image."
                )

    def __add_background_image(self, canvas: genCanvas, image: Image.Image) -> None:
        """ Recives an empty canvas and an image, and pastes the image 
        onto the canvas. """

        canvas.drawImage(
            image,
            x=0, y=0,
            width=self.width, height=self.height
        )

    def __add_background_color(self, canvas: genCanvas, color) -> None:
        """ Recives an empty canvas and a color, fills the canvas with
        the given color. """

        canvas.setFillColor(color)
        canvas.rect(
            x=0, y=0,
            width=self.width, height=self.height,
            stroke=False, fill=True,
        )
