from app import db, app, SoftwareProject
import sys

def DeleteProject(id):
    with app.app_context():
        project = SoftwareProject.query.get(id)
        db.session.delete(project)
        db.session.commit()
        print(f"Project with ID {id} deleted successfully!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please input the id you want to delete!")
    else:
        id = sys.argv[1]
        DeleteProject(id)