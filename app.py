from flask import Flask, render_template, request, redirect, url_for
import os
from analyze import analyze_video  # Import the analyze_video function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'static/output'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['OUTPUT_FOLDER']):
    os.makedirs(app.config['OUTPUT_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'videoFile' not in request.files:
        return redirect(request.url)
    file = request.files['videoFile']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        output_filename = 'output_' + file.filename
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        analyze_video(file_path, output_path)  # Call the analyze_video function
        return redirect(url_for('result', filename=output_filename))

@app.route('/result')
def result():
    filename = request.args.get('filename')
    return render_template('result.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
