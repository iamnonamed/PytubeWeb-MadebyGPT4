from flask import Flask, request, send_file, render_template
from pytube import YouTube
import os
import certifi
from pytube.helpers import safe_filename


os.environ["SSL_CERT_FILE"] = certifi.where()



app = Flask(__name__)
output_path = 'downloads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form['video_url']
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    video.download(output_path)
    filename = safe_filename(yt.title) + ".mp4"  # Use safe_filename to create a sanitized filename
    return send_file(os.path.join(output_path, filename), as_attachment=True)


if __name__ == '__main__':
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    app.run(debug=True)
