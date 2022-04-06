#!/usr/bin/env python3


"""Color-Fi is a tool to color and format strings in python to enhance user experience and to highlight important
information so it does not go unnoticed.
"""


__author__ = 'John J Kenny'
__version__ = '1.0.1'


class ColorFi():
    """Color and formatting tool for string output."""
    def __init__(self):
        # Available Colors
        self.colors = {
            'foreground': {
                'black': '30m',
                'red': '31m',
                'green': '32m',
                'yellow': '33m',
                'blue': '34m',
                'magenta': '35m',
                'cyan': '36m',
                'white': '37m',
                'bright-black': '90m',
                'bright-red': '91m',
                'bright-green': '92m',
                'bright-yellow': '93m',
                'bright-blue': '94m',
                'bright-magenta': '95m',
                'bright-cyan': '96m',
                'bright-white': '97m'
            },
            'background': {
                'black': '40m',
                'red': '41m',
                'green': '42m',
                'yellow': '43m',
                'blue': '44m',
                'magenta': '45m',
                'cyan': '46m',
                'white': '47m',
                'bright-black': '100m',
                'bright-red': '101m',
                'bright-green': '102m',
                'bright-yellow': '103m',
                'bright-blue': '104m',
                'bright-magenta': '105m',
                'bright-cyan': '106m',
                'bright-white': '107m'
            }
        }
        # Available Formatting
        self.formatting = {
            'reset': '00m',
            'default': '10m',
            'bold': '01m',
            'dim': '02m',
            'italic': '03m',
            'underline': '04m',
            'double-underline': '21m',
            'slow-blink': '05m',
            'rapid-blink': '06m',
            'invert': '07m',
            'hide': '08m',
            'strike': '09m'
        }
        self.esc = '\033['
        self.reset = f'{self.esc}{self.formatting["reset"]}'

    def print_message(self, msg: str, color: str, ground: str = 'foreground', _format: str = 'default',
                      show_keys: bool = False):
        """Prints a formatted message to the console.

        Args:
            msg (str): Message to be displayed.
            color (str): Color to be used.
            ground (str, optional): Foreground or background option. Defaults to 'foreground'.
            _format (str, optional): Formatting to be used (bold, italic, invert, etc..). Defaults to 'default'.
            show_keys (bool, optional): Display which keys were used in the formatting for debugging. Defaults to False.
        """
        if show_keys:
            print(f'{self.format_message(msg, color, ground, _format)}: {ground} {color} {_format}')
        else:
            print(self.format_message(msg, color, ground, _format))

    def format_message(self, msg: str, color: str, ground: str = 'foreground', _format: str = 'default'):
        """Formats a message using the given color and formatting.

        Args:
            msg (str): Message to be displayed.
            color (str): Color to be used.
            ground (str, optional):  Foreground or background option. Defaults to 'foreground'.
            _format (str, optional): Formatting to be used (bold, italic, invert, etc..). Defaults to 'default'.

        Returns:
            str: Formatted message.
        """
        return f'{self.build_color(color, ground)}{self.build_format(_format)}{msg}{self.reset}'

    def build_color(self, color: str, ground: str = 'foreground'):
        """Builds the color string.

        Args:
            color (str): Color to be used.
            ground (str, optional): Foreground or background option. Defaults to 'foreground'.

        Returns:
            str: Formatted color string.
        """
        try:
            return f'{self.esc}{self.colors[ground][color]}'
        except KeyError:
            print('Failed to get color format using keys: %s, %s ', ground, color)

    def build_format(self, _format: str = 'default'):
        """Builds the formatting string.

        Args:
            _format (str, optional): Formatting to be used (bold, italic, invert, etc..). Defaults to 'default'.

        Returns:
            str: Formatted string.
        """
        try:
            return f'{self.esc}{self.formatting[_format]}'
        except KeyError:
            print('Failed to get formatting using key: %s', _format)

    def display_all_formatting_options(self, msg: str = 'Sample Text', show_keys: bool = True):
        """Displays all available formatting options to console.

        Args:
            msg (str, optional): Sample string to use for console display. Defaults to 'Sample Text'.
            show_keys (bool, optional): Show which keys are used to display the given format. Defaults to True.
        """
        for ground in self.colors:
            for color in self.colors[ground]:
                for _format in self.formatting:
                    if _format == 'reset':
                        continue
                    self.print_message(msg, color, ground, _format, show_keys)

    def display_key_options(self):
        """Display all available formatting keys to console."""
        for _function in [self.display_ground_options, self.display_color_options, self.display_formatting_options]:
            _function()

    def display_ground_options(self):
        """Display all available ground options to console."""
        ground_list = list()
        for ground in self.colors:
            if ground not in ground_list:
                ground_list.append(ground)
        self.print_message(f'Ground Options: {(", ").join(ground_list)}', 'green')

    def display_color_options(self):
        """Display all available color options to console."""
        color_list = list()
        for ground in self.colors:
            for color in self.colors[ground]:
                if color not in color_list:
                    color_list.append(color)
        self.print_message(f'Color Options: {(", ").join(color_list)}', 'cyan')

    def display_formatting_options(self):
        """Display all available formatting options to console."""
        format_list = list()
        for _format in self.formatting:
            if _format not in format_list:
                format_list.append(_format)
        self.print_message(f'Formatting Options: {(", ").join(format_list)}', 'yellow')
