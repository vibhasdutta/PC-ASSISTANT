import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file tasktoken.json.
SCOPES = ["https://www.googleapis.com/auth/tasks"]


def authenticate_gmail_api():
    creds = None

    if os.path.exists("taskToken.json"):
        creds = Credentials.from_authorized_user_file("taskToken.json")

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("taskToken.json", "w") as token:
            token.write(creds.to_json())

    return creds

def show_tasks(speak,ttsoutput):
    creds = authenticate_gmail_api()
    service = build("tasks", "v1", credentials=creds)
    results = service.tasklists().list().execute()
    items = results.get("items", [])
    if not items:
        speak("No task lists found.")
    else:
        speak("Here's the Task lists")
        print("Task lists:")
        for item in items:
            print(f"{item['title']}")

    for item in items:
        speak("Which task list tasks do you want to see?")
        tasklist_name=ttsoutput().lower()
        if any (word in tasklist_name for word in (item['title']).lower()):
            tasklist = item['id']
            results = service.tasks().list(tasklist=tasklist).execute()
            items = results.get("items", [])
            if not items:
                speak("No tasks found.")
            else:
                speak("Here's the tasks")
                print("Tasks:")
                for item in items:
                    print(f"{item['title']}")
            break

def create_task(speak,ttsoutput):
    creds = authenticate_gmail_api()
    service = build("tasks", "v1", credentials=creds)
    results = service.tasklists().list().execute()
    items = results.get("items", [])
    if not items:
        speak("No task lists found.")
    else:
        speak("here's the task lists")
        print("Task lists:")
        for item in items:
            print(f"{item['title']}")
    speak("What do you want to add? Task list or Task")
    taskAction=ttsoutput().lower()
    if all (word in taskAction for word in ["add","task","list"]):
        tasklist = input("Enter the task list you want to add: ").lower()
        tasklist = {"title": tasklist}
        service.tasklists().insert(body=tasklist).execute()
        speak("Task list added successfully")

    elif any (word in taskAction for word in ["add","task"]):
        for item in items:
            speak("Enter the task list you want to add the task to")
            tasklist_name = input("Enter the task list you want to add the task to: ").lower()
            if any (word in tasklist_name for word in (item['title']).lower()):
                tasklist = item['id']
                results = service.tasks().list(tasklist=tasklist).execute()
                items = results.get("items", [])
                if not items:
                    speak("No tasks found.")
                else:
                    speak("Here's the tasks")
                    print("Tasks:")
                    for item in items:
                        print(f"{item['title']}")
                break
        
        speak("Enter the task you want to add")
        task = input("Enter the task you want to add: ").lower()
        results = service.tasklists().list().execute()
        items = results.get("items", [])
        for item in items:
            if tasklist == (item['title']).lower():
                tasklist = item['id']
                task = {"title": task}
                service.tasks().insert(tasklist=tasklist, body=task).execute()
                speak("Task added successfully")
                break
def delete_task(speak,ttsoutput):
    creds = authenticate_gmail_api()
    service = build("tasks", "v1", credentials=creds)
    results = service.tasklists().list().execute()
    items = results.get("items", [])
    if not items:
        speak("No task lists found.")
        print("No task lists found.")
    else:
        speak("Here's the task lists")
        print("Task lists:")
        for item in items:
            print(f"{item['title']}")

    speak("What do you want to delete? Task list or Task")
    taskAction=ttsoutput().lower()
    if any (word in taskAction for word in ["delete","task","list"]):
        speak("Enter the task list you want to delete")
        tasklist = input("Enter the task list you want to delete: ").lower()
        results = service.tasklists().list().execute()
        items = results.get("items", [])
        for item in items:
            if tasklist == (item['title']).lower():
                tasklist = item['id']
                service.tasklists().delete(tasklist=tasklist).execute()
                speak("Task list deleted successfully")
                break

    elif any (word in taskAction for word in ["delete","task"]):
        for item in items:
            speak("Enter the task list you want to delete the task from")
            tasklist_name = input("Enter the task list you want to delete the task from: ").lower()
            if any (word in tasklist_name for word in (item['title']).lower()):
                tasklist = item['id']
                results = service.tasks().list(tasklist=tasklist).execute()
                items = results.get("items", [])
                if not items:
                    speak("No tasks found.")
                else:
                    speak("Here's the tasks")
                    print("Tasks:")
                    for item in items:
                        print(f"{item['title']}")
                break
        speak("Enter the task you want to delete")
        task = input("Enter the task you want to delete: ").lower()
        
        results = service.tasklists().list().execute()
        items = results.get("items", [])
        for item in items:
            if tasklist == (item['title']).lower():
                tasklist = item['id']
                results = service.tasks().list(tasklist=tasklist).execute()
                items = results.get("items", [])
                for item in items:
                    if task == (item['title']).lower():
                        task = item['id']
                        service.tasks().delete(tasklist=tasklist, task=task).execute()
                        speak("Task deleted successfully")
                        break
                break
