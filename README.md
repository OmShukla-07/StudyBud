# StudyBud

StudyBud is a collaborative study platform built entirely with Django for the backend, focusing on enabling users to create, join, and participate in topic-based study rooms. This README highlights the backend features, architecture, and ways to get involved.

---

## Project Overview

**This repository contains only the backend implementation of StudyBud.**  
It is ready to serve as the backbone for your frontend applications—whether web, mobile, or desktop. You are encouraged to fork, clone, or build your own frontend to interact with this API-driven platform.

If you're interested in collaborating or integrating this backend with your frontend project, feel free to open an issue or pull request. I welcome contributions and collaboration opportunities!

---

## Backend Features

### 1. User Authentication & Registration
- Secure user login, logout, and registration using Django's built-in authentication system.
- User credentials are handled securely, with forms for both login and registration.
- New users can sign up; existing users can log in and out seamlessly.

### 2. Topic-Based Study Rooms
- **Room Model**: Represents a study group or room.
- Each room is associated with a topic (e.g., Math, Science).
- Users can create new rooms, specifying the topic, description, and name.
- The room host (creator) is tracked, and only the host can edit or delete the room.

### 3. Real-Time Participation & Messaging
- Users can join rooms as participants.
- Each room maintains a list of participants, allowing for collaborative study.
- Inside rooms, users can post messages (chat functionality), which are timestamped and display the sender.

### 4. Room & Message Management
- Create, update, and delete rooms (with permissions: only the host can edit/delete their rooms).
- Users can post messages within rooms; messages can also be deleted.
- Rooms and messages are ordered by update and creation times, ensuring the most recent content is prioritized.

### 5. User Profiles
- Each user has a profile page listing their created rooms and messages.
- Easy navigation to view and interact with a user's contributions across the platform.

### 6. Search & Filtering
- Home page supports searching for rooms by topic, name, or description.
- Efficient filtering allows users to quickly find relevant study sessions.

## Technology Stack

- **Backend Framework**: Django
- **Database**: Django ORM (default: SQLite, easily switchable to others)
- **Authentication**: Django's built-in system
- **Templating**: Django templates for rendering dynamic HTML pages

## Core Models

- **User**: Built-in Django user, extended with relationships.
- **Topic**: Represents categories for rooms.
- **Room**: Study group, linked to a topic, host, and participants.
- **Message**: Posts within rooms, linked to users and rooms.

## API Endpoints

- `/login/` — User login
- `/logout/` — User logout
- `/register/` — User registration
- `/` — Home page with room list and search
- `/room/<id>/` — Room details and messaging
- `/profile/<id>/` — User profile
- `/create-room/`, `/update-room/<id>`, `/delete-room/<id>` — Room management

## Getting Started

1. Clone the repo and install requirements.
2. Run migrations to set up the database.
3. Start the Django server and access StudyBud in your browser.

For more backend code details, browse the source: [StudyBud GitHub Repository](https://github.com/OmShukla-07/StudyBud)

---

## Contributing & Collaboration

This backend project is open for use and collaboration!  
- **Frontend developers:** You can use this backend as an API for your own frontend implementation.
- **Collaborators:** If you have ideas, wish to improve the backend, or want to build an integrated product, feel free to reach out by opening an issue or a pull request.
- **Community:** All contributions and suggestions are welcome.

---

_This summary covers the main backend features. For more details or frontend features, please refer to the repository or contact the maintainer._
