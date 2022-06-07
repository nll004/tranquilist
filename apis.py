from requests import request
from keys import quote_API_key

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Code retrieved on 5/29/22 from GOOGLE API docs https://developers.google.com/calendar/api/quickstart/python.
# Adapted to adjust parameters and results

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def get_events():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Set start and endate (now and one week from now) to use as parameters in Calendar API
        now = datetime.datetime.utcnow()
        one_week = datetime.timedelta(days = 7)
        next_week = now + one_week

        # Convert both dates to strings
        now_str = now.isoformat() + 'Z'  # 'Z' indicates UTC time
        next_week_str = next_week.isoformat() + 'Z'

        # Call the Calendar API for personal events in the next 7 days
        next_page_token = None
        all_events = []
        while True:
            user_events = service.events().list(calendarId='primary', timeMin=now_str, timeMax=next_week_str,
                                                singleEvents=True, orderBy='startTime', pageToken=next_page_token).execute()
            for event in user_events['items']:
                all_events.append(event)
            next_page_token = user_events.get('nextPageToken')
            if not next_page_token:
                break

        # API Call 2 - Google holiday calendar for public holidays in the next 7 days
        public_events = service.events().list(calendarId='en.usa#holiday@group.v.calendar.google.com',
                                                timeMin=now_str, timeMax=next_week_str,
                                                singleEvents=True, orderBy='startTime').execute()
        if public_events:
            for event in public_events['items']:
                # added holiday to object to help distinguish it from other events
                # event['holiday'] = True
                # print(event)
                all_events.append(event)
        else:
            return

        return all_events

    except HttpError as error:
        print('An error occurred: %s' % error)


# 5/26/22. Code retrieved from: https://rapidapi.com/bitbiscuit-bitbiscuit-default/api/motivational-quotes1/
def get_quote():
    '''Get quote from rapidapi'''

    base_url = "https://motivational-quotes1.p.rapidapi.com/motivation"

    payload = {
		"key1": "value",
		"key2": "value"
	}

    headers = {
		"content-type": "application/json",
		"X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com",
        "X-RapidAPI-Key": quote_API_key
	}

    response = request("POST", base_url, json=payload, headers=headers)

    return response


if __name__ == '__main__':
    get_events()
    get_quote()
