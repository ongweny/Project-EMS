#!/usr/bin/env python3

from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from __init__ import create_app, db, bcrypt  
from models import User, Event, Reservation

app = create_app()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Joel & Joys Event Management System"})

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    password_confirmation = data.get('password_confirmation')

    if not email or not password or not password_confirmation:
        return jsonify({"errors": ["Missing email or password"]}), 400

    if password != password_confirmation:
        return jsonify({"errors": ["Passwords do not match"]}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"errors": ["Email already in use"]}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(email=email, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error creating user: {str(e)}")
        return jsonify({"errors": ["Internal server error"]}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email=email).first()
    
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity={'email': user.email})
        return jsonify({"access_token": access_token, "user": user.to_dict()}), 200
    return jsonify({"errors": ["Invalid credentials"]}), 401

@app.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    current_user = get_jwt_identity()
    data = request.get_json()
    user = User.query.filter_by(email=current_user['email']).first()

    if not user:
        return jsonify({"errors": ["User not found"]}), 404

    user.email = data.get('email', user.email)

    try:
        db.session.commit()
        return jsonify({"message": "Profile updated successfully", "user": user.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error updating profile: {str(e)}")
        return jsonify({"errors": ["Internal server error"]}), 500

@app.route('/create_events', methods=['POST'])
@jwt_required()
def create_event():
    current_user = get_jwt_identity()
    data = request.get_json()
    user = User.query.filter_by(email=current_user['email']).first()  # Ensure user exists

    if not user:
        return jsonify({"errors": ["User not found"]}), 404

    new_event = Event(
        title=data['title'],
        description=data['description'],
        date=data['date'],
        user_id=user.id
    )

    try:
        db.session.add(new_event)
        db.session.commit()
        return jsonify({"message": "Event created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Error creating event: {str(e)}")
        return jsonify({"errors": ["Internal server error"]}), 500

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Test route is working"})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
