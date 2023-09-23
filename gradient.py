"""
Simpler Python wrapping around this blog post:

https://bsouthga.dev/posts/color-gradients-with-python

Only includes the Linear Gradient.
"""
from __future__ import annotations
import functools
from dataclasses import dataclass


@dataclass
class Colour:
    hex: str
    rgb: tuple[int, int, int]


class TextGradient:
    def __init__(self, text: str, c1: str, c2: str):
        self.text = text
        self.c1 = c1
        self.c2 = c2

        self.wrap(text, c1, c2)

    def __str__(self):
        return self.gradient_text(self.text, self.c1, self.c2)

    def __repr__(self):
        return f"<TextGradient text={self.text} c1={self.c1} c2={self.c2}>"

    def wrap(
        self,
        text: str,
        c1: str = None,
        c2: str = None,
        open_tag: str = "[{hex}]",
        close_tag: str = "[/{hex}]",
    ):
        """Wraps each individual letter in the opener and closer."""
        c1 = c1 or self.c1
        c2 = c2 or self.c2
        grad = self.linear_gradient(c1, c2, len(text))
        build_str = ""
        for i, char in enumerate(text):
            hex = grad["hex"][i]
            opener = open_tag.format(hex=hex)
            closer = close_tag.format(hex=hex)
            build_str += f"{opener}{char}{closer}"
        return build_str


    def hex_to_RGB(self, hex):
        """ "#FFFFFF" -> [255,255,255]"""
        # Pass 16 to the integer function for change of base
        return [int(hex[i : i + 2], 16) for i in range(1, 6, 2)]


    def RGB_to_hex(self, RGB):
        """[255,255,255] -> "#FFFFFF" """
        # Components need to be integers for hex to make sense
        RGB = [int(x) for x in RGB]
        return "#" + "".join(
            ["0{0:x}".format(v) if v < 16 else "{0:x}".format(v) for v in RGB]
        )


    def color_dict(self, gradient):
        """Takes in a list of RGB sub-lists and returns dictionary of
        colors in RGB and hex form for use in a graphing function
        defined later on"""
        return {
            "hex": [self.RGB_to_hex(RGB) for RGB in gradient],
            "r": [RGB[0] for RGB in gradient],
            "g": [RGB[1] for RGB in gradient],
            "b": [RGB[2] for RGB in gradient],
        }


    def linear_gradient(self, start_hex, finish_hex="#FFFFFF", n=10):
        """returns a gradient list of (n) colors between
        two hex colors. start_hex and finish_hex
        should be the full six-digit color string,
        inlcuding the number sign ("#FFFFFF")"""
        # Starting and ending colors in RGB form
        s = self.hex_to_RGB(start_hex)
        f = self.hex_to_RGB(finish_hex)
        # Initilize a list of the output colors with the starting color
        RGB_list = [s]
        # Calcuate a color at each evenly spaced value of t from 1 to n
        for t in range(1, n):
            # Interpolate RGB vector for color at the current value of t
            curr_vector = [
                int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j])) for j in range(3)
            ]
            # Add it to our list of output colors
            RGB_list.append(curr_vector)

        return self.color_dict(RGB_list)


    def gradient_text(self, text: str, c1: str, c2: str) -> str:
        """Convert a string to bbcode-styled coloured text."""
        grad = self.linear_gradient(c1, c2, len(text))
        build_str = ""
        for i, char in enumerate(text):
            hex = grad["hex"][i]
            build_str += f"[{hex}]{char}[/{hex}]"
        return build_str


my_title = functools.partial(TextGradient, c1="#000000", c2="#ffffff")

if __name__ == "__main__":
    print(my_title("hello world"))
