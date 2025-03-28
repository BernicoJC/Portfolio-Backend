from app import db, app, SoftwareProject

def AddProject():
    title = "Portfolio Website"
    subtitle = "This website!"
    description = "This project is a full stack development of a portfolio website utilizing ReactJS frontend and Python Flask backend. This is where I store my projects and to introduce myself to the world about my skills and what I do. I display my software projects and other development projects. Furthermore, I also display my resume here, and it uses SQLAlchemy for its database on the feedback forms and its projects. From this project, I learned about full stack development of a website from the groundup using ReactJS and Flask (and their API like CORS and how to access between frontend and backend), and polished my SQL skills with a real case scenario using Python SQLite, and my general CSS / JS skills."
    background = "I decided to make this website to show myself to the world, and what my skills are, so that people can know who I am more easily. Furthermore, I also did this project to hone my website development skills in general. The Github repo for the backend code is below. You can also find the link to the front end repo there."
    image = "/images/bernico.jpg"
    link = "https://github.com/BernicoJC/Portfolio-Backend"
    with app.app_context():
        new_project = SoftwareProject(title=title, subtitle=subtitle, description=description, background=background, image=image, link=link)
        db.session.add(new_project)
        db.session.commit()
        print("Project added succesfully!")

if __name__ == "__main__":
    AddProject()