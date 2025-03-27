from app import db, app, Feedback

def ClearFeedback():
    with app.app_context():
        feedbacks = Feedback.query.all()
        for feedback in feedbacks:
            db.session.delete(feedback)
            db.session.commit()
        print("Feedbacks cleared succesfully!")

if __name__ == "__main__":
    
    ClearFeedback()