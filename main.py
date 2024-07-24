from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABSE_URI"] = (
    "sqlite:///api.db"  # sqlite:///api.db is a relative path .It creates the database in our working directory
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class video(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    dislikes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return (
            f"Video(name= {name}, views= {views}, likes= {likes}, dislikes= {dislikes})"
        )


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video ", required=True)
video_put_args.add_argument(
    "views", type=int, help="Views of the video ", required=True
)
video_put_args.add_argument(
    "likes", type=int, help="Likes on the video ", required=True
)
video_put_args.add_argument(
    "dislikes", type=int, help="Dislikes on the video ", required=True
)
videos = {}


def abort_no_video_id(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video...")


def abort_yes_video_id(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID ...")


class video(Resource):
    def get(self, video_id):
        abort_no_video_id(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_yes_video_id(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_no_video_id(video_id)
        del videos[video_id]
        return "", 204


api.add_resource(video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
