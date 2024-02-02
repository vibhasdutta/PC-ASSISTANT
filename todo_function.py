import json
import speech_recognition as sr

TODO_JSON_FILE = "TOdo_database.json"  # *json file


def is_dict_empty_excluding_first_key(json_file_path):
    try:
        # Load data from the JSON file
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        # Check if the dictionary is empty excluding the key at index 0
        return bool(data and len(list(data.keys())[1:]) == 0)
    except FileNotFoundError:
        # Handle the case where the file is not found
        return True
    except Exception as e:
        # Handle other exceptions
        print(f"Error: {e}")
        return True


def ttsoutput():  # * recognizing function
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, 0.2)
        recognizer.pause_threshold = 250

        audio = recognizer.listen(mic, phrase_time_limit=5)
        text = recognizer.recognize_google(audio)
        print(f"usersaid: {text} ")
    return text.lower()


def load_todo_list():  # * loading todolist function
    try:
        with open(TODO_JSON_FILE, "r") as json_file:
            todo_list = json.load(json_file)
    except FileNotFoundError:
        todo_list = {}
    return todo_list


def save_todo_list(todo_list):  # * Saving todolist function
    try:
        with open(TODO_JSON_FILE, "w") as json_file:
            json.dump(todo_list, json_file, indent=2)
        print("Successfully saved to todo_list.json")
    except Exception as e:
        print(f"Error saving to todo_list.json: {e}")


def todo_add_function(speak):  # * adding todolist function
    speak("What should I name the note to save it")
    while True:
        try:
            toname = ttsoutput()
            toname = toname.lower()

            speak("What is the message to save it")
            while True:
                try:
                    todo_audio = ttsoutput()
                    todo_audio = todo_audio.lower()
                    break
                except Exception:
                    speak("Please say it again")
                    continue

            todo_list = load_todo_list()
            todo_list[toname] = todo_audio
            save_todo_list(todo_list)

            print("Adding a new note")
            print(f"Note name: {toname}\nMessage: {todo_audio}")
            speak(f"Successfully added {toname} note")
            break
        except Exception:
            speak("Please say it again")

        print("Adding a new note")
        print(f"Note name: {toname}\nMessage: {todo_audio}")
        speak(f"Successfully added {toname} note")


def todo_remove_function(speak):  # * removing todolist function
    todo_list = load_todo_list()

    speak("Here is the list of saved notes")
    for note_name, note_message in todo_list.items():
        print(f"Note name: {note_name}\nMessage: {note_message}")

    speak("Which note should I remove")
    while True:
        try:
            todo_audio = ttsoutput()
            todo_audio = todo_audio.lower()
            if todo_audio in todo_list:
                del todo_list[todo_audio]
                save_todo_list(todo_list)
            break
        except Exception:
            speak("Please say it again")
            continue

    print(f"Deleting {todo_audio}")
    speak("Updated the list")
    for note_name, note_message in todo_list.items():
        print(f"Note name: {note_name}\nMessage: {note_message}")


def todo_view_function(speak):  # * printing todo list function
    todo_list = load_todo_list()
    if not todo_list:
        print("The notepad is empty")
        speak("The notepad is empty")
    else:
        for note_name, note_message in todo_list.items():
            print(f"Note name: {note_name}\nMessage: {note_message}")


def todo_update_function(speak):  # *updating todo list function
    speak("What should I update")

    while True:
        try:
            todo_audio = ttsoutput()
            break
        except Exception:
            speak("Please say it again")
            continue

    todo_list = load_todo_list()

    if "note name" in todo_audio:  # *updating todo list note name function
        for note_name, note_message in todo_list.items():
            print(f"Note name: {note_name}\nMessage: {note_message}")

        speak("Which note name should I change")
        while True:
            try:
                note_name_to_change = ttsoutput()
                speak("What should I name it")
                if note_name_to_change in todo_list:
                    new_note_name = ttsoutput()
                    todo_list[new_note_name] = todo_list.pop(note_name_to_change)
                    save_todo_list(todo_list)
                break
            except Exception:
                speak("Please say it again")
                continue

    elif "note message" in todo_audio:  # *updating todo list note message function
        for note_name, note_message in todo_list.items():
            print(f"Note name: {note_name}\nMessage: {note_message}")

        speak("Which note message should I change")
        while True:
            try:
                note_name_to_change = ttsoutput()
                speak("Please say the new message")
                new_note_message = ttsoutput()
                todo_list[note_name_to_change] = new_note_message
                save_todo_list(todo_list)
                break
            except Exception:
                speak("Please say it again")
                continue

    else:  # * function for changing both note   name and message
        for note_name, note_message in todo_list.items():
            print(f"Note name: {note_name}\nMessage: {note_message}")

            speak("Which note name should I change")
            while True:
                try:
                    note_name_to_change = ttsoutput()
                    speak("What should I name it")
                    if note_name_to_change in todo_list:
                        new_note_name = ttsoutput()
                        todo_list[new_note_name] = todo_list.pop(note_name_to_change)
                    break
                except Exception:
                    speak("Please say it again")
                    continue

            for note_name, note_message in todo_list.items():
                print(f"Note name: {note_name}\nMessage: {note_message}")
                speak("Which note message should I change")
                while True:
                    try:
                        note_name_to_change = ttsoutput()
                        speak("Please say the new message")
                        new_note_message = ttsoutput()
                        todo_list[note_name_to_change] = new_note_message
                        save_todo_list(todo_list)
                        break
                    except Exception:
                        speak("Please say it again")
                        continue
