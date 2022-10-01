import canvas_markup
import asyncio

markup = canvas_markup.Markup()

# Rendering the file index.ejs and saving it as a png.
markup.renderFile('./index.html', { 'title': 'Markup', 'description': 'Made with Canvas-Markup©' })
# Setting the viewport of the display to 1920x1080.
markup.setViewport(1920, 1080)
asyncio.run(markup.save('./image.png'))