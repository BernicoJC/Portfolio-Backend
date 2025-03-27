from app import db, app, GameProject

def AddProject():
    title = "Terminal"
    subtitle = "TritonWare FA24 Group 9 Submission"
    description = "This is our submission for another game jam at UCSD. Terminal is a 2D top down minigame that has the player collect several items in order to open the gate of the level and escape to win the game. The level is dark and filled with monsters that spawn every few seconds. The only thing that the player has to defend themselves is their reaction time. There are four monster types and any wrong move to react to them is going to cause a game over: sometimes panic, sometimes don’t! The game has a decaying lighting system that can be refueled using items picked up throughout the level. I worked as one of the programmers and designer of the team. From this project, I learned a slightly advanced mechanic like lighting, refueling of lighting, how monsters react to the players’ controls, and working in a group. The game is not yet released, but the game is finished in a beta stage."
    image = "/images/other/terminal.png"
    link = "https://github.com/BernicoJC/TritonWare-FA24-Group-9"
    with app.app_context():
        new_project = GameProject(title=title, subtitle=subtitle, description=description, image=image, link=link)
        db.session.add(new_project)
        db.session.commit()
        print("Project added succesfully!")

if __name__ == "__main__":
    AddProject()