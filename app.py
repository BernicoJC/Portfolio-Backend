from flask import Flask, request, jsonify, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Flask constructor
app = Flask(__name__)

# Use CORS for every routes
CORS(app)


# Configure app to use sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create Alchemy instance
db = SQLAlchemy(app)

# Database classes
class SoftwareProject(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), unique = False, nullable = False)
    subtitle = db.Column(db.String(200), unique = False, nullable = False)
    description = db.Column(db.String(500), unique = False, nullable = False)
    background = db.Column(db.String(500), unique = False, nullable = False)
    image = db.Column(db.String(50), unique = False, nullable = False)
    link = db.Column(db.String(200), unique = False, nullable = False)

    # return a string when we make an element
    def __repr__(self):
        return f"Software Project Created with id: {self.id}, title: {self.title}"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "description": self.description,
            "background": self.background,
            "image": self.image,
            "link": self.link
        }

class GameProject(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), unique = False, nullable = False)
    subtitle = db.Column(db.String(200), unique = False, nullable = False)
    description = db.Column(db.String(500), unique = False, nullable = False)
    image = db.Column(db.String(50), unique = False, nullable = False)
    link = db.Column(db.String(200), unique = False, nullable = False)

    # return a string when we make an element
    def __repr__(self):
        return f"Game Project Created with id: {self.id}, title: {self.title}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "subtitle": self.subtitle,
            "description": self.description,
            "image": self.image,
            "link": self.link
        }

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = False, nullable = False)
    email = db.Column(db.String(50), unique = False, nullable = False)
    feedback = db.Column(db.String(500), unique = False, nullable = False)
    
    # return a string when we make an element
    def __repr__(self):
        return f"Form received with id: {self.id}, title: {self.title}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "feedback": self.feedback
        }


# Database API

# Get software projects
@app.route('/projects/software/get', methods=["GET"])
def GetSoftware():
    projects = SoftwareProject.query.all()
    return jsonify([project.to_dict() for project in projects])

# Get game projects
@app.route('/projects/game/get', methods=["GET"])
def GetGame():
    projects = GameProject.query.all()
    return jsonify([project.to_dict() for project in projects])

# Get feedbacks
@app.route('/feedback/get', methods=["GET"])
def GetFeedback():
    feedback = Feedback.query.all()
    return jsonify([project.to_dict() for project in feedback])

# For posting feedback to the database
@app.route('/feedback/add', methods=["POST"])
def addFeedback():
    data = request.get_json()
    
    fname = data.get("name")
    femail = data.get("email")
    ffeedback = data.get("feedback")
    new_feedback = Feedback(name=fname, email=femail, feedback=ffeedback)
    db.session.add(new_feedback)
    db.session.commit()

    # if you don't return a json, the frontend will complain, despite the posting being succesful
    return jsonify({"message": "Feedback added successfully!"})

# Run
if __name__ == '__main__':
    app.run(debug=True)
    # from os import environ
    # app.run(host='0.0.0.0', port=int(environ.get('PORT', 5000)))