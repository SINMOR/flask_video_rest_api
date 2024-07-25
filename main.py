from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy, Model

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

    # with app.app_context():
    #     try:
    #         db.create_all()
    #         print("Tables created successfully.")
    #     except Exception as e:
    #         print("An error occurred while creating tables:", e)


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
# serializing objects
resource_fields = {
    "id": fields.String,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer,
    "dislikes": fields.Integer,
}


class video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = video.Model.query.filter_by(id=video_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = video.Model(
            id=video_id,
            name=args["name"],
            views=args["views"],
            likes=args["likes"],
            dislikes=args["dislikes"],
        )
        return video, 201

    # def delete(self, video_id):
    #     abort_no_video_id(video_id)
    #     del videos[video_id]
    #     return "", 204


api.add_resource(video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)
