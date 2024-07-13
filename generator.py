import imgkit
from jinja2 import Template
import os
from utils import calc_font_size

html_template = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>News</title>
        <style>
            body {
                font-family: "Arial", sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f5f5f5;
            }
            .container {
                position: relative;
                text-align: left;
                color: white;
                padding: 20px;
                width: 800px;
                height: 1000px;
                box-sizing: border-box;
                background-image: url("bg.png");
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
            }
            .news-image {
                height: 400px;
                width: auto;
                max-width: 100%;
                object-fit: contain;
                border-radius: 20px;
                display: block;
                margin: 0 auto;
            }
            .content {
                margin: 20px;
                margin-bottom: 100px;
            }
            .content p {
                font-size: {{ font_size }}px;
                text-align: center;
            }
            .svg-bg {
                position: absolute;
                bottom: 0;
                left: 0;
                width: 100%;
                height: auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="content">
                <img src="{{ image_url }}" alt="News Image" class="news-image">
                <p>
                    {{ main_text }}
                </p>
            </div>
        </div>
    </body>
</html>
"""

def generate_image(main_text, image_url, output_path):
    # Calculate the font size
    font_size = calc_font_size(main_text)

    # Render the HTML template
    template = Template(html_template)
    rendered_html = template.render(main_text=main_text, image_url=image_url, font_size=font_size)

    # Save the rendered HTML to a file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(rendered_html)

    # Configure imgkit options
    options = {
        'width': 800,
        'height': 1000,
        'quality': 100,
        'enable-local-file-access': None
    }

    # Convert HTML to image
    imgkit.from_file('index.html', output_path, options=options)

    # Clean up the temporary HTML file
    os.remove('index.html')
