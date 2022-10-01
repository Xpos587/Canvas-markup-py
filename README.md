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
#  main.py:

import canvas_markup
import asyncio

markup = canvas_markup.Markup()

# Rendering the file index.ejs and saving it as a png.
markup.renderFile('./index.html', { 'title': 'Markup', 'description': 'Made with Canvas-Markup©' })
# Setting the viewport of the display to 1920x1080.
markup.setViewport(1920, 1080)
asyncio.run(markup.save('./image.png'))
```

<a href="https://github.com/Xpos587/Canvas-markup-py/blob/master/index.html">See index.html</a>

<style>
    * {
        font-family: arial;
    }
</style>