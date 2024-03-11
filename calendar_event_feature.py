from datetime import datetime
import os.path
from colorama import Fore
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]


def authenticate_calendar_api():
    creds = None
    if os.path.exists("Ctoken.json"):
        creds = Credentials.from_authorized_user_file("Ctoken.json")

    from google.auth.exceptions import RefreshError

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError as e:
                print(Fore.RED+"Error while refreshing token")
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("Ctoken.json", "w") as token:
            token.write(creds.to_json())

    return creds


def events_calendar(print_event_details: bool):
    try:
        creds = authenticate_calendar_api()
        service = build("calendar", "v3", credentials=creds)

        now = datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        # *print("Getting the upcoming 10 events")
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=10,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
        c = 0
        if not events:
            print("No upcoming events found.")
            return c

        # Prints the start and name of the next 10 events

        for event in events:
            location = event.get("location", "not given")
            start = event["start"].get("dateTime", event["start"].get("date"))
            start_datetime = datetime.fromisoformat(start)
            e_time = start_datetime.strftime("%d/%b/%Y %I:%M %p")
            if print_event_details:
                print(f"Event Name: {event['summary']}")
                print(f"Description: {event.get('description', 'No description')}")
                print(f"Start Time: {e_time}")
                print(f"Event Location: {location}")
                print(f"Event Link: {event.get('htmlLink', 'No link available')}\n\n")
            c += 1

    except HttpError as error:
        print(f"An error occurred: {error}")
    return c


def get_events_for_current_date(print_event_details: bool):
    creds = authenticate_calendar_api()
    service = build("calendar", "v3", credentials=creds)

    now = datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    # *print("Getting today's upcoming events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    c = 0
    # Prints the start and name of the next 10 events
    for event in events:
        # Get the current date in the format YYYY-MM-DD

        current_date = datetime.now().date()
        start = event["start"].get("dateTime", event["start"].get("date"))
        start_datetime = datetime.fromisoformat(start)
        e_time1 = start_datetime.strftime("%d/%b/%Y %I:%M %p")
        e_time = start_datetime.strftime("%Y-%m-%d")

        if str(current_date) == e_time:
            if print_event_details:
                location = event.get("location", "not given")
                print(f"Event Name: {event['summary']}")
                print(f"Description: {event.get('description', 'No description')}")
                print(f"Start Time: {e_time1}")
                print(f"Event Location: {location}")
                print(f"Event Link: {event.get('htmlLink', 'No link available')}\n\n")
            c += 1

        else:
            print("No upcoming event's for Today.")
    return c


def eventpop_date():
    creds = authenticate_calendar_api()
    service = build("calendar", "v3", credentials=creds)

    now = datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    # *print("Getting today's upcoming events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    return events
