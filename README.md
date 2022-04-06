# Color-Fi

Color-Fi is a tool to color and format strings in python to enhance user experience and to highlight important information so it does not go unnoticed.

## Installation

Color-Fi is a python package which can be found on [Python Package Index (PyPi)](https://pypi.org/project/Color-Fi/). Run the following command to install:<br>
``` bash
pip install Color-Fi
```


## Import Color-Fi into your projects
``` python
from ColorFi.color_fi import ColorFi
```

## Usage
### Display key options:
``` python
color_fi = ColorFi()

# Display key options:
color_fi.display_key_options()
```
Output: 
``` bash
Ground Options: foreground, background
Color Options: black, red, green, yellow, blue, magenta, cyan, white, bright-black, bright-red, bright-green, bright-yellow, bright-blue, bright-magenta, bright-cyan, bright-white
Formatting Options: reset, default, bold, dim, italic, underline, double-underline, slow-blink, rapid-blink, invert, hide, strike
```

### Display all formatting options to help you choose what you want to use in your project:
``` python
# Display samples:
color_fi.display_all_formatting_options()
```
Output as a gif:<br>
![Formatting Samples](/assets/view_options/ColorFi.gif)

### View selected formatting options on console
``` python
# print message to console with formatting options:
color_fi.print_message('Test Message', 'red', 'foreground', 'invert')
```
Output as png:<br>
![message Sample](/assets/sample_message/sample_message.png)

### Format message without printing directly to console
``` python
msg = color_fi.format_message('Test Message', 'red', 'foreground', 'invert')
print(msg)
```
Output as png:<br>
![message Sample](/assets/sample_message/sample_message.png)
