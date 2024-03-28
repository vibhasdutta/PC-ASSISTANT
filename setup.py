import os
import subprocess
import sys
import json
def MENU():
    while True:
        print(Fore.YELLOW+">> MENU <<\n")
        print(Fore.CYAN+"1 > RUN WIN\n")
        print(Fore.CYAN+"2 > CONFIG CREDENTIAL AND API's\n")
        print(Fore.CYAN+"3 > UPDATE PACKAGES\n")
        print(Fore.CYAN+"4 > ABOUT US\n")
        print(Fore.CYAN+"5 > REPORT ISSUES and FEATURE REQUESTs\n")
        print(Fore.CYAN+"6 > EXIT MENU\n")
        
        options  = str(input(Fore.GREEN+"Choose from the menu: "))
        if options == "1":
            try:
                ai_terminal=subprocess.Popen(["start", "cmd", "/k", "python Core_main.py"], shell=True)
                print(Fore.MAGENTA+"AI STARTED...")
            except Exception:
                print(Fore.RED+"Error while Starting the AI. Either the Core_main.py file is missing or some other issuse occured.")
        elif options == "2":
            from dotenv import load_dotenv, set_key
            load_dotenv()
            print(Fore.CYAN+"1 > GEMINI_API: "+os.getenv("GEMINI_API"))
            print(Fore.CYAN+"2 > WEATHER_API: "+os.getenv("WEATHER_API"))
            print(Fore.CYAN+"3 > DEFAULT_CITY_NAME: "+os.getenv("CITY_NAME"))
            try:
                with open('credentials.json') as f:
                    # Load the JSON data from the file
                    data = json.load(f)
                print(Fore.CYAN+"4 > GOOGLE_CREDENTIALS: "+json.dumps(data))
            except Exception :
                print(Fore.RED+"Error occured while reading the credentials.json")
                pass
            print(Fore.CYAN+"5 > Prefix: "+os.getenv("PREFIX"))
            suboptions = str(input(Fore.GREEN+"Choose the config options to modify or just press '6': "))
            if suboptions == "1":
                new_value1=input(Fore.GREEN+"enter the value or paste it.")
                set_key(".env", "GEMINI_API", new_value1)
                print(Fore.MAGENTA+"NEW VALUE SAVED!")
            elif suboptions == "2":
                new_value2=input(Fore.GREEN+"enter the value or paste it.")
                set_key(".env", "WEATHER_API", new_value2)
                print(Fore.MAGENTA+"NEW VALUE SAVED!")
            elif suboptions == "3":
                new_value3=input(Fore.GREEN+"enter the value or paste it.")
                set_key(".env", "CITY_NAME", new_value3)
                print(Fore.MAGENTA+"NEW VALUE SAVED!")
            elif suboptions == "4":
                new_value4=input(Fore.GREEN+"enter the value or paste it.")
                try:
                    with open('credentials.json', 'w') as f:
                        # Write the data to the file
                        json.dump(new_value4, f)
                    print(Fore.MAGENTA+"NEW VALUE SAVED!")
                except Exception:
                    print(Fore.RED+"Error occured while reading the credentials.json")
                    return
            elif suboptions == "5":
                new_value5=input(Fore.GREEN+"enter the value or paste it.")
                set_key(".env", "PREFIX", new_value5)
                print(Fore.MAGENTA+"NEW VALUE SAVED!")
            else:
               pass
            
        elif options == "3":
            try:
                subprocess.run(["pip","install","-U","-r","requirements.txt"])
            except Exception:
                print(Fore.RED+"error while updating either pip or requirements is missing.")
        elif options == "4":
            print(Fore.MAGENTA+"I'm Vibhas, a BTech student passionate about technology. I've created a voice assistant that's intuitive and seamless, making daily tasks easier. My goal is to innovate and simplify technology for everyone.")
            print(Fore.MAGENTA+"For more info please checkout the Github:https://github.com/vibhasdutta/PC-ASSISTANT\nTHANK YOU!")
        elif options == "5":
            print(Fore.MAGENTA+"FOR REPORTING ISSUES :https://github.com/vibhasdutta/PC-ASSISTANT/blob/main/.github/ISSUE_TEMPLATE/bug_report.md")
            print(Fore.MAGENTA+"FOR FEATURE REQUESTS :https://github.com/vibhasdutta/PC-ASSISTANT/blob/main/.github/ISSUE_TEMPLATE/feature_request.md")
        elif options == "6":
            print(Fore.RED+"EXITING MENU...")
            Fore.RESET
            sys.exit(1)
        else:
            print(Fore.GREEN+"Choose form the above options")
            

if __name__=="__main__":
    
    env_name = ".venv"
    try:
        if sys.version_info.major == 3 and sys.version_info.minor == 11:
                # Checking if the virtual environment exists
            if os.path.exists(env_name):
                pass
            else:
                # Creating the virtual environment
                try:
                    subprocess.run(["python", "-m", "venv", env_name])
                except FileNotFoundError:
                    print("Could not find the python executable or venv module.")
                    sys.exit(1)


            if sys.platform == "win32":
                activate_script = os.path.join(env_name, "Scripts", "activate.bat")
                try:
                    print("Activating the virtual environment...")
                    subprocess.run([activate_script])
                except FileNotFoundError:
                    print(f"Could not find the activation script at '{activate_script}'.")
                    sys.exit(1)

                print("Installing the required packages...")
                try:
                    subprocess.run(["pip", "install", "-r", "requirements.txt"]) 
                except FileNotFoundError:
                    print("Could not find the pip executable requirements.txt file or pip.")
                    sys.exit(1)
        else:
            print("Python 3.11 is required to run this project.")
            print("Please install it from https://www.python.org/downloads/release/python-3116/")
            sys.exit(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception as E:
        print("An error occurred while setting up the project.")
        print("Please try again.")
        sys.exit(1)
    print("The project has been set up successfully.")
    from art import *
    from colorama import Fore
    tprint("Welcome To Win AI",font="Doom")
    MENU()