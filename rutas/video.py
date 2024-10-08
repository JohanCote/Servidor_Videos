from sys import path
from flask import Blueprint, request, send_from_directory
from os import getcwd
from responses import respons

routes_video = Blueprint("route_video", __name__)

PATH_VIDEO = getcwd() + "/video/"

VIDEO_MINE_TYPE = {'mp4', 'mpg', 'mov', 'webm', 'avi', 'wmv', '3gpp', 'flv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in VIDEO_MINE_TYPE

@routes_video.post("/upload")
def upload_file():
    try:
        video = request.files['video']
        if video and allowed_file(video.filename):
            video.save(PATH_VIDEO + video.filename)
            return respons.response_json("success")
        else:
            return respons.response_json("invalid_video_type"), 400
    except FileNotFoundError:
        return respons.response_json("video_not_found"), 404
    
@routes_video.get("/video/<string:name_file>")
def get_file(name_file):
    return send_from_directory(PATH_VIDEO, path = name_file, as_attachment = False)

@routes_video.get("/download/<string:name_file>")
def download_file(name_file):
    return send_from_directory(PATH_VIDEO, path = name_file, as_attachment = True)