from app import db, app, SoftwareProject
import sys

def EditProject(id):
    title = ""
    subtitle = ""
    description = ""
    background = ""
    image = ""
    link = "https://github.com/BernicoJC/Portfolio-Backend"
    
    with app.app_context():
        project = SoftwareProject.query.get(id)
        if not project:
            print(f"No project found with ID {id}")
            return
        
        # Update the fields
        if title:
            project.title = title
        if subtitle:
            project.subtitle = subtitle
        if description:
            project.description = description
        if background:
            project.background = background
        if image:
            project.image = image
        if link:
            project.link = link

        db.session.commit()
        print(f"Project with ID {id} updated successfully!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please input the id you want to delete!")
    else:
        id = sys.argv[1]
        EditProject(id)