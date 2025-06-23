from app import db, app, SoftwareProject

def AddProject():
    title = "TritonTube"
    subtitle = "YouTube Clone with Rich Backend Infrastructure, CSE 124 Homework"
    description = "This one month long programming homework for UCSD's Systems Networking class, CSE 124, is an attempt to recreate video content sharing HTTP website that utilizes several backend technologies for effective horizontal scaling and fault tolerance. The website's core is built with Golang HTTP server infrastructure that allows the user to upload videos to the storage, and both view the videos and retrieve contents from it; on top of the content, the website also stores simple metadata of the video: time of when it was uploaded and its video ID. It converts and stores videos using MPEG-DASH to support scaling and network connection adaptability. When a video is uploaded, the files generated from MPEG-DASH are distributed through protobuf messages to the appropriate storage gRPC servers using consistent hashing, allowing a single video to be stored in multiple storage servers, whilst ensuring not a single server is overloaded thanks to hashing. This system also allows storage servers' removal and addition causing only localized file transports (so a failure of a single server, and increasing capacity are easy to deal with). Consistent hashing is also used to allow quick retrieval of contents from the appropriate servers. I also implemented the API for such removal / addition of servers. Furthermore, I also learned about AWS and about how the metadata can be stored using RAFT / Leader Election mechanism, but the implementation of it ended up got cancelled due to time constraints, and thus the metadata is simply stored on a single storage using SQLite."
    background = "Through this homework, I learned about HTTP and gRPC servers, MPEG-DASH, horizontal scaling, AWS, and RAFT. I have passed this class, but due to school policy, I am unable to post my code publicly. Please email me at bernicojc113@gmail.com for an invitation to view the repository linked below."
    image = "/images/software/tritontube.png"
    link = "https://github.com/BernicoJC/tritontube-cse124"
    
    with app.app_context():
        new_project = SoftwareProject(title=title, subtitle=subtitle, description=description, background=background, image=image, link=link)
        db.session.add(new_project)
        db.session.commit()
        print("Project added succesfully!")

if __name__ == "__main__":
    AddProject()