from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)