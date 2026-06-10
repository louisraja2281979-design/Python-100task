from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def gallery():
    image_folder = os.path.join("static", "images")
    images = os.listdir(image_folder)

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Image Gallery</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                text-align:center;
                background:#f4f4f4;
            }
            .gallery{
                display:grid;
                grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
                gap:15px;
                padding:20px;
            }
            img{
                width:100%;
                height:250px;
                object-fit:cover;
                border-radius:10px;
                box-shadow:0 2px 5px rgba(0,0,0,0.2);
            }
        </style>
    </head>
    <body>
        <h1>Image Gallery</h1>

        <div class="gallery">
            {% for image in images %}
                <img src="{{ url_for('static', filename='images/' + image) }}">
            {% endfor %}
        </div>
    </body>
    </html>
    """

    return render_template_string(html, images=images)

if __name__ == "__main__":
    app.run(debug=True)