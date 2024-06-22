from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No image uploaded' , 401
        file = request.files['file']
        if file.filename == "":
            return 'No file selected', 400
        if file:
            inputImage = Image.open(file.stream)
            outputImage = remove(inputImage, post_process_mask=True)
            imgIo = BytesIO()
            outputImage.save(imgIo, 'PNG')
            imgIo.seek(0)
            return send_file(imgIo, mimetype="image/png", as_attachment=True, download_name=f"bgone_{file.filename}.png")
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)