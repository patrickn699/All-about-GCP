import os
from re import S
from flask import render_template, request, redirect, url_for, Flask, send_from_directory
from werkzeug.utils import secure_filename
import requests
from img_limit import check_n_imgs



app = Flask(__name__)

TEMPLATE_DIRS = ['./templates']
STATIC_DIRS = ['./static']
app.config['UPLOAD_FOLDER'] = './cropped'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('in.html')


@app.route('/fil', methods=['POST'])
def fil():
    if request.method == 'POST':
        file = request.files["file"]
        height = request.form["height"]
        width = request.form["width"]
        percent = request.form["percent"]
        water = request.form["watermark"]
        file.save('./saved/' + secure_filename(file.filename))
        send_file('./saved/' + secure_filename(file.filename),height,width,percent,water)
        #return redirect(url_for('download'))
        return render_template('dwn.html')


def send_file(filename,height,width,percent,water):
    ur = os.environ['CONV_SERVICE_HOST']
    po = os.environ['CONV_SERVICE_PORT']
    #url = "http://localhost:9000/convert"
    url = "http://" + str(ur) + ":" + str(po) + "/convert"
    files = {'file': open(filename, 'rb')}
    try:
        r = requests.post(url, files=files,data={'height':height,'width':width,'percent':percent,'watermark':water})
        print("made a post request to conversion service:",r.text)
    except Exception as e:
        return render_template('error.html', error=e)


@app.route('/uploaded', methods=['POST'])
def uploaded():
    if request.method == 'POST':
        file = request.files["image"]
        file.save('./cropped/' + secure_filename(file.filename))
        #check_n_imgs()
        #return send_from_directory('./cropped/', file.filename)
        return redirect(url_for('download'))


@app.route('/download')
def download():
    return render_template('dwn.html')
    #return send_from_directory('./cropped/', 'cropped.jpg')



@app.route('/geti/<path:filename>')
def geti(filename):
    p = 'cropped'
    if os.listdir(p)!=[]:
        return send_from_directory(directory='./cropped',path=filename)
    return render_template('dwn.html', error="No file to download")
       






if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
    #app.run(debug=True,port=8005)