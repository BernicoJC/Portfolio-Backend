from app import db, app, GameProject
import sys

def DeleteProject(id):
    with app.app_context():
        project = GameProject.query.get(id)
        db.session.delete(project)
        db.session.commit()
        print("Project deleted succesfully!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please input the id you want to delete!")
    else:
        id = sys.argv[1]
        DeleteProject(id)