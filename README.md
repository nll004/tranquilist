![tranquilist-logo3](https://user-images.githubusercontent.com/96667141/223807066-085c52ed-3b45-4822-9245-cf48e3c184ea.png)

Written task lists often get misplaced, outdated and messy. Other task management apps often come with cluttered displays, annoying alerts and reminders as well as strict timelines that many find impractical and annoying for everyday tasks.

I’ve reimagined the task list to provide a place to store everyday tasks while utilizing the [Google Calendar API](https://developers.google.com/calendar/api) to retrieve events stored in a users calendar.

[![HitCount](https://hits.dwyl.com/nll004/tranquilist.svg?style=flat-square)](http://hits.dwyl.com/nll004/tranquilist)
## Table of Contents
- [Features](#features)
  - [Register User](#register-new-user)
  - [User Authentication](#user-authentication)
  - [Create Tasks](#create-tasks-and-subtasks)
  - [Modify Tasks](#modify-tasks-and-subtasks)
  - [Complete Tasks](#complete-tasks-and-subtasks)
- [Technologies Used](#technologies-used)
- [Future Direction](#future-direction-for-project)

## Features

### Register New User
Create an account and authorize Tranquilist to retrieve Google Calendar events. 


https://user-images.githubusercontent.com/96667141/223791510-6cd5614a-49c4-4d9a-8988-ded74dba6ad1.mp4


### User Authentication
Login in using username and password to display personalized tasks and calendar events.


https://user-images.githubusercontent.com/96667141/223791562-3471c2f6-dcc6-4049-a0d7-0a867a775a66.mp4


### Create Tasks and Subtasks
Create new tasks/subtasks and collapse displays.


https://user-images.githubusercontent.com/96667141/223797521-0856942e-56fb-4d63-8672-1d89629c9f47.mp4


### Modify Tasks and Subtasks
Modify tasks and the list the timeline you want them to belong to.


https://user-images.githubusercontent.com/96667141/223800958-cd486dd5-0e98-4743-892c-c76b918ded05.mp4


### Complete Tasks and Subtasks
Complete and delete tasks and subtasks


https://user-images.githubusercontent.com/96667141/223799211-ce249b1f-ce03-4039-a491-569a278a68cf.mp4


### View Calendar 
Navigate to google calendar to edit, view or add calendar event with a simple click.


https://user-images.githubusercontent.com/96667141/223803796-85a9f775-c48e-408a-bc21-00a4fdf8d99a.mp4


## Technologies Used
- [Motivational Quote API](https://rapidapi.com/ipworld/api/quotes-inspirational-quotes-motivational-quotes)
- [Google Calendar API](https://developers.google.com/calendar/api)
- Python 3 
- Flask.py
- Jinja templating
- Oauth2.0
- HTML/CSS
- jQuery
- PostgreSQL
- SQLAlchemy(ORM)

## Future Direction For Project
- Recreate front end with React.js
- Editing users password, email and other information
- Drag and drop editing tasks
- Allow user to save favorite quotes
- Allow user to name their timelines and add additional timelines if desired
- Allow user to add a google calendar event without going to google calendar
- Muted styling for calendar events that occur today to help distinguish from other events


