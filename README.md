# TranquiList
Springboard Software Engineering BootCamp - Cohort Jan 2022
Started: June 2022

## Access at
https://tranquilist.herokuapp.com/

Note: This app is still in development and is not accessible to users who have not been preapproved by the developer.

## About
Written task lists often get misplaced, outdated and messy. Other task management apps often come with cluttered displays, annoying alerts and reminders as well as strict timelines that I find impractical and annoying for everyday tasks.

Being obsessed with organization and task lists yet often irritated by constant reminders and alerts, I’ve reimagined my task list to provide a place to store everyday tasks while still utilizing the Google Calendar for events that require exact timing.

This app allows users to register, create/edit/delete task and connect their account to google calendar api.

You can view the upcoming weeks calendar events and holidays beside your created tasks. You can click calendar events to follow links and edit your calendar events at google calendars webpage.

## Assignment
**Capstone Project 1**

We were given the opportunity to create a simple functioning app utilizing an api of choice.

This task manager calls Google Calendar API to display upcoming events and holidays using Oauth2.0 and a smaller simple API for motivational quotes.

Google Calendar API: https://developers.google.com/calendar/api

Currently the google calendar api key is set for development. As the result, utilizing this app requires preapproval of the developer. The scope of this app is set to "readonly" and will not modify events stored in the users google calendar.

Motivational Quote API: https://rapidapi.com/bitbiscuit-bitbiscuit-default/api/motivational-quotes1/details


## To Do
- At a later date I plan to introduce more features like editing, completing, deleting subtasks. Additional features needed include editing the users username, password, email, etc.
- More tests and error handling are needed to improve user experience.
