# import os
# from __init__ import create_app, db
# from models import User, Event, Reservation

# app = create_app()

# with app.app_context():
#     db.drop_all()
#     db.create_all()

#     user1 = User(email="test1@example.com", password="password")
#     user2 = User(email="test2@example.com", password="password")
    
#     db.session.add(user1)
#     db.session.add(user2)
#     db.session.commit()

#     event1 = Event(title="Event 1", description="Description for event 1", date="2023-08-07", user_id=user1.id)
#     event2 = Event(title="Event 2", description="Description for event 2", date="2023-08-08", user_id=user2.id)
    
#     db.session.add(event1)
#     db.session.add(event2)
#     db.session.commit()

#     reservation1 = Reservation(event_id=event1.id, user_id=user2.id)
#     reservation2 = Reservation(event_id=event2.id, user_id=user1.id)
    
#     db.session.add(reservation1)
#     db.session.add(reservation2)
#     db.session.commit()

#     print("Database seeded successfully")

#!/usr/bin/env python3

from app import app, db
from models import User, Event, Reservation

with app.app_context():
    db.create_all()

    user1 = User(email='user1@example.com', password='password')
    db.session.add(user1)
    db.session.commit()

    event1 = Event(title='Sample Event', description='This is a sample event', date='2024-08-01', user_id=user1.id)
    db.session.add(event1)
    db.session.commit()

    reservation1 = Reservation(user_id=user1.id, event_id=event1.id)
    db.session.add(reservation1)
    db.session.commit()