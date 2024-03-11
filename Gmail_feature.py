import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
from prompt_toolkit import prompt
import os
from respones_data import *
from colorama import Fore

SCOPES = ["https://mail.google.com/"]


def authenticate_gmail_api():
    creds = None

    if os.path.exists("Gmailtoken.json"):
        creds = Credentials.from_authorized_user_file("Gmailtoken.json")

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

        with open("Gmailtoken.json", "w") as token:
            token.write(creds.to_json())

    return creds


def user_info():
    creds = authenticate_gmail_api()
    service = build("gmail", "v1", credentials=creds)

    profile = service.users().getProfile(userId="me").execute()
    print(Fore.CYAN+f"User Profile: {profile}")


def get_unread_email_count():
    creds = authenticate_gmail_api()
    service = build("gmail", "v1", credentials=creds)

    # List unread messages in the inbox
    results = (
        service.users()
        .messages()
        .list(userId="me", labelIds=["INBOX", "UNREAD"])
        .execute()
    )
    messages = results.get("messages", [])
    unread_count = len(messages)
    return unread_count


def create_message_with_attachment(to, msg, subject, body, file_path):
    message = MIMEMultipart()
    message["to"] = to
    message["subject"] = subject

    msg = MIMEText(body)
    message.attach(msg)

    # Attach the file
    content_type, encoding = mimetypes.guess_type(file_path)
    if content_type is None or encoding is not None:
        content_type = "application/octet-stream"
    main_type, sub_type = content_type.split("/", 1)
    with open(file_path, "rb") as file:
        attachment = MIMEBase(main_type, sub_type)
        attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header(
        "Content-Disposition", "attachment", filename=os.path.basename(file_path)
    )
    message.attach(attachment)

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode("utf-8")
    return {"raw": raw_message}


# * send one email at a time
def send_email(email_message, receiver_email, email_subject, attachements,file_path,speak):
    creds = authenticate_gmail_api()
    service = build("gmail", "v1", credentials=creds)

    # Create a MIMEText message
    message = MIMEText(email_message)
    message["to"] = receiver_email
    message["subject"] = email_subject
    try:
        if attachements == "True":
            message = create_message_with_attachment(
                receiver_email, email_message, email_subject, email_message, file_path
            )
            body = message
            sent_message = service.users().messages().send(userId="me", body=body).execute()
        else:

            # Encode the message as bytes and then base64 encode
            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            # Create the body of the message
            body = {"raw": raw_message}

            # Send the message
            sent_message = service.users().messages().send(userId="me", body=body).execute()
    except Exception:
        print(Fore.RED+f"This Email {receiver_email} not found")
    speak ("email send successfully")


def reply_to_email(original_message_id, reply_subject, Reply_message):
    creds = authenticate_gmail_api()
    service = build("gmail", "v1", credentials=creds)

    # Fetch the original message
    original_message = (
        service.users().messages().get(userId="me", id=original_message_id).execute()
    )

    # Get the original recipient email address
    original_recipient = None
    for header in original_message["payload"]["headers"]:
        if header["name"] == "To":
            original_recipient = header["value"]
            break

    if not original_recipient:
        print(Fore.RED+"Error: Could not determine the original recipient.")
        return

    # Create a reply message
    reply_message = MIMEText(Reply_message)
    reply_message["subject"] = reply_subject
    reply_message["to"] = (
        original_recipient  # Set the recipient to the original recipient
    )

    # Encode the reply message as bytes and then base64 encode
    raw_reply_message = base64.urlsafe_b64encode(reply_message.as_bytes()).decode()

    # Create the body of the reply message
    reply_body = {"raw": raw_reply_message, "threadId": original_message["threadId"]}

    # Send the reply
    sent_reply = service.users().messages().send(userId="me", body=reply_body).execute()
    print(Fore.CYAN+sent_reply)


def read_email(message_id, speak):
    creds = authenticate_gmail_api()
    service = build("gmail", "v1", credentials=creds)

    try:
        # Get the details of the specified email message
        message = service.users().messages().get(userId="me", id=message_id).execute()

        # Extract relevant information from the message
        subject = None
        sender = None
        date = None
        body = None

        # Retrieve headers
        headers = message.get("payload", {}).get("headers", [])
        for header in headers:
            if header["name"] == "Subject":
                subject = header["value"]
            elif header["name"] == "From":
                sender = header["value"]
            elif header["name"] == "Date":
                date = header["value"]

        # Get the body of the message
        body_data = message.get("payload", {}).get("body", {}).get("data", "")
        if body_data:
            body = base64.urlsafe_b64decode(body_data).decode("utf-8")

        # Print or use the extracted information
        speak(f"Sender: {sender}")
        print(Fore.CYAN+f"Sender: {sender}")
        speak(f"Subject: {subject}")
        print(Fore.CYAN+f"Subject: {subject}")
        print(Fore.CYAN+f"Date: {date}")
        if body:
            print(Fore.CYAN+f"Body:\n{body}")
        service.users().messages().modify(
            userId="me", id=message_id, body={"removeLabelIds": ["UNREAD"]}
        ).execute()
    except Exception as e:
        print(Fore.RED+f"An error occurred while reading the email")


def mail_read_and_reply(speak, ttsoutput):
    creds = authenticate_gmail_api()
    service = build("gmail", "v1", credentials=creds)

    try:
        # List messages in the inbox
        results = (
            service.users()
            .messages()
            .list(userId="me", labelIds=["INBOX", "UNREAD"])
            .execute()
        )
        messages = results.get("messages", [])
        confirmattion = False
        # Print the message IDs
        for message in messages:
            message_id = message["id"]
            # print(f"Message ID: {message_id}")
            print("\n")
            read_email(message_id, speak)

            print("\n")
            while True:
                try:

                    speak("should i reply or read the next mail")
                    voice_response = ttsoutput()
                    voice_response = voice_response.lower()
                    if (
                        all(word in voice_response for word in ["reply"])
                        and any(word in voice_response for word in yes_words)
                        and any(word in voice_response for word in ["mail"])
                    ):
                        reply_subject = input(Fore.GREEN+"subject:")

                        reply_message = input(Fore.GREEN+"message:")

                        speak("should i send the email")
                        while True:
                            voice2_response = ttsoutput()
                            voice2_response = voice2_response.lower()
                            try:
                                if any(word in voice2_response for word in yes_words):
                                    reply_to_email(
                                        message_id, reply_subject, reply_message
                                    )
                                    break
                                elif any(word in voice2_response for word in no_words):
                                    break
                            except Exception:
                                pass

                    elif any(word in voice_response for word in ["read"]) or any(
                        word in voice_response for word in ["mail"]
                    ):
                        break
                    elif any(word in voice_response for word in ["close"]) and any(
                        word in voice_response for word in ["mail"]
                    ):
                        confirmattion = True
                        break

                except Exception:
                    pass
            if confirmattion == True:  # * main  loop break
                break
            else:
                pass
        speak("that's all for now!")
    except Exception as e:
        print(Fore.RED+f"An error in reading and replying to the email")


# * send same  bulk email at a time
def send_bulk_email(attachements,file_path,speak,suggest_message):
    creds = authenticate_gmail_api()
    service = build("gmail", "v1", credentials=creds)

    speak("how many people you want to send email")
    personnum = input(Fore.GREEN+"Enter the number of people you want to send email to\n")

    email_list = []
    for id in range(0, personnum):
        email_id = input(Fore.GREEN+f"Enter email id of person {id+1}\n")
        email_list.append(email_id)


    speak("Type the subject")
    email_subject = input(Fore.GREEN+"Enter the Email subject\n")

    speak("type the message")
    suggestext=suggest_message("write email body message on topic")
    email_message = prompt("Enter the Email message\n",default=suggestext)

    for receiver_email in email_list:
        # Create a MIMEText message
        message = MIMEText(email_message)
        message["to"] = receiver_email
        message["subject"] = email_subject
        try:
            if attachements == "True" :

                message = create_message_with_attachment(
                    receiver_email, email_message, email_subject, email_message, file_path
                )
                body = message
                sent_message = (
                    service.users().messages().send(userId="me", body=body).execute()
                )
            else:

                # Encode the message as bytes and then base64 encode
                raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
                # Create the body of the message
                body = {"raw": raw_message}

                # Send the message
                sent_message = (
                    service.users().messages().send(userId="me", body=body).execute()
                )
        except  Exception:
            print(Fore.RED+f"This Email {receiver_email} not found")
    speak("all the email send successfully")
