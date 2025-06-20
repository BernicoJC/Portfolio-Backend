from app import db, app, SoftwareProject

def AddProject():
    title = "Go Display It, Canvas!"
    subtitle = "UCSD Canvas .go File Displayer Web Extension"
    description = "This personal project is a simple web extension project that's also full of applications of the knowledge I got from my CSE 124: Systems Networking coursework. The extension will detect if the current URL is the UCSD Canvas URL: `*://*.canvas.ucsd.edu/courses/*/files/*` or `*://ucsd.instructure.com/courses/*/files/*`. If the URL matches, and the file displayed is a .go code, it'll find the HTML element that stores a link to the download page. The extension will then fetch the link (sending a HTTP request), following all of the redirections until the file is acquired. It will then get the file's content and make a new div element that will apply PrismJS syntax highlighter. From this project I learned about the usage of CURL and HTTP requests in practice, CDN links, Service Worker and Background Script for Manifest V3, and other general Web Extension skills, especially giving access to the extension."
    background = "I decided to make this extension when I was studying for my CSE 110 midterm and got annoyed that Canvas couldn't recognize .go file types, unable to display it, and thus I had to keep downloading .go files just to view them. I was only expecting to hone my general frontend skills before making this, and as such it really pleasantly surprised me that I ended up applying the skills I learned from the class I target this extension for."
    image = "/images/software/godisplayitcanvas_icon_128.png"
    link = "https://github.com/BernicoJC/GoDisplayItCanvas"
    with app.app_context():
        new_project = SoftwareProject(title=title, subtitle=subtitle, description=description, background=background, image=image, link=link)
        db.session.add(new_project)
        db.session.commit()
        print("Project added succesfully!")

if __name__ == "__main__":
    AddProject()