def rgb_color(color: str) -> tuple:
    """Convert an RGB color string to an RGB tuple.

    >>> rgb_color('#fff')
    (15, 15, 15)
    >>> rgb_color('#500100')
    (80, 1, 0)
    """
    color = color.lstrip('#')
    if len(color) == 3:
        return (int(color[0], 16),
                int(color[1], 16),
                int(color[2], 16))
    elif len(color) == 6:
        return (int(color[0:2], 16),
                int(color[2:4], 16),
                int(color[4:6], 16))
    else:
        raise ValueError(f'RGB color strings must have 3 or 6 digits')

class Formatter():
    ESCAPE = '\033'
    BG = '48;2;{r};{g};{b}'
    FG = '38;2;{r};{g};{b}'

    def __rgb(func):
        """ Formatter's inhouse decorator.
        Converting string rgb color to touple
        """
        def convert_color(self, color):
            if isinstance(color, str):
                color = rgb_color(color)
            return func(self, color)
        return convert_color

    def __call__(self, text: str):
        self.__raw_text = text
        self.__baking_string = f'{self.ESCAPE}['
        return self

    @__rgb
    def fg(self, color):
        """ set foreground color
        """
        # if isinstance(color, str):
        #     color = rgb_color(color)
        result = self.FG.format(r=color[0], g=color[1], b=color[2])
        self.__baking_string += f';{result}'
        return self

    @__rgb
    def bg(self, color):
        """ set background color
        """
        # if isinstance(color, str):
        #     color = rgb_color(color)
        result = self.BG.format(r=color[0], g=color[1], b=color[2])
        self.__baking_string += f';{result}'
        return self

    def bold(self):
        """ set style to bold
        """
        self.__baking_string += ';1'
        return self

    def dim(self):
        """ set style to dim
        """
        self.__baking_string += ';2'
        return self

    def flush(self):
        self.__baking_string = f'{self.ESCAPE}['
        # self.__raw_text = ''

    def bake(self) -> str:
        result = f'{self.__baking_string}m{self.__raw_text}'
        self.flush()
        return result
