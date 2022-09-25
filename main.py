from canvas_markup import Markup
import asyncio

markup = Markup()

# Rendering the file index.ejs and saving it as a png.
markup.renderFile('./index.jinja2', { 'title': 'Markup', 'description': 'Made with Canvas-Markup©' })
# Setting the viewport of the display to 1920x1080.
markup.setViewport(1920, 1080)
asyncio.run(markup.save('./image.png'))