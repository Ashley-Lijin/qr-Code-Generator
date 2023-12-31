from flask import Flask, render_template, request
from io import BytesIO
import qrcode
from base64 import b64encode

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO()
    link = request.form.get('link')
    qr = qrcode.make(link)
    qr.save(memory)
    memory.seek(0)

    base64_img = "data:image/png;base64," + \
        b64encode(memory.getvalue()).decode('ascii')

    return render_template('index.html', qrcode=base64_img, link=link)


if __name__ == "__main__":
    app.run(debug=True)
