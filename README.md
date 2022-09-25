[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<img style="border-radius: 5%" src="https://github.com/Xpos587/Canvas-markup-py/blob/master/logo.png?raw=true" alt></img>
<br>
<br>
<br>

Canvas-markup
=============
Canvas-markup - It lib is used to render html to image

#### **Example**
```python
# main.py:

from canvas_markup import Markup
import asyncio

markup = Markup()

# Rendering the file index.ejs and saving it as a png.
markup.renderFile('./index.jinja2', { 'title': 'Markup', 'description': 'Made with Canvas-Markup©' })
# Setting the viewport of the display to 1920x1080.
markup.setViewport(1920, 1080)
asyncio.run(markup.save('./image.png'))
```

<a href="https://github.com/Xpos587/Canvas-markup-py/blob/master/index.jinja2">See index.jinja2</a>

<style>
    * {
        font-family: arial;
    }
</style>