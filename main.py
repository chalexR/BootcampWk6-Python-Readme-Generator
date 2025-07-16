from InquirerPy import inquirer
from InquirerPy.separator import Separator

class fItem:
    def __init__(self, tMess = ""):
        self.tMess = tMess
            
    def results(self):
        return self.result

class tMulti(fItem):
    def __init__(self, tMess = ""):
        self.result = inquirer.text(message=tMess, multiline=True).execute()

    def __str__(self):
        return f"{self.result}"

class text(fItem):
    def __init__(self, tMess = ""):
        self.result = inquirer.text(message=tMess).execute()

class checkbox(fItem):
    def __init__(self, tMess = "", checkChoice = ""):
        self.result = inquirer.checkbox(
            message = tMess,
            choices = checkChoice,
            validate = lambda result: len (result) >= 1,
            invalid_message = "At least 1 items must be selected"
            ).execute()

def usage_steps():
    # create a response array
    responseArr = []
    stepCount = 1
    # Loop until we say stop
    while True:
        stepResponse = ""
        codeResponse = ""
        # Run a new multi-line text field
        stepResponse = f"{tMulti(f"Step {stepCount}:")}"
        # ask if the user wants to add code
        codePrompt = inquirer.confirm(message="Would you like to add code to this step?", default=False).execute()
        if codePrompt:
            codeResponse = tMulti(f"Code: ")
            codeResponse = f"```{ codeResponse }```"
        # add response to array
        responseArr.append(stepResponse)
        responseArr.append(codeResponse)
        stepCount += 1
        # ask if the user wants to add another step
        stepPrompt = inquirer.confirm(message="Would you like to add another step?", default=True).execute()
        if not stepPrompt: break
    return responseArr



def language_choice():
    return [
        "HTML/CSS",
        "JavaScript",
        "Python"
    ]

def lang_choice_gen(lang_choices):
    def general_choice(): 
        return [
            Separator("General Setup"),
            "Clone the repository",
            "Navigate into the project directory",
            "Install dependencies",
            "Other (manually enter custom instructions)",

            Separator("GitHub Pages/Hosting"),
            "Deploy with GitHub Pages",
            "Deploy with Netlify or Vercel",
            "Push to GitHub to trigger CI/CD deployment"
        ]
    def html_choice():
        return[
            Separator("HTML/CSS"),
            "Open index.html in your browser",
            "Ensure assets (images, fonts, etc.) are in the correct folders",
            "Link CSS and JS files correctly in HTML",
            "Check browser compatibility (optional)"
        ]
    def js_choice():
        return[
            Separator("Javascript"),
            "Install Node.js dependencies with npm",
            "Install Node.js dependencies with yarn",
            "Build the project with npm/yarn",
            "Run the development server (e.g., npm start)",
            "Run tests with npm/yarn",
            "Configure environment variables (.env file)"
        ]
    def python_choice():
        return[
            Separator("Python"),
            "Create and activate a virtual environment (Python)",
            "Install dependencies with pip",
            "Install via requirements.txt",
            "Set environment variables",
            "Run a setup script",
            "Run initial database migrations (Django/Flask/etc)",
            "Start the Python application (e.g., python app.py)"
        ]

    def adv_choice():
        return[
            Separator("Advanced Options"),
            "Install a CSS preprocessor (e.g., Sass, Less)",
            "Run a bundler (e.g., Webpack, Parcel)",
            "Start a local development server (e.g., Live Server, BrowserSync)",
            "Install Python/Node.js version managers (pyenv/nvm)"
        ]
    response = general_choice()
    for lang in lang_choices:
        if lang == "HTML/CSS":
            response.extend(html_choice())
        if lang == "JavaScript":
            response.extend(js_choice())
        if lang == "Python":
            response.extend(python_choice())

    return response

# TODO: Add in a response for adding a custom set up instruction if the user chooses Other.
# Then we need to populate a text string based on the options selected

# Must be laid out in order of how you wish for the to appear in form.
print("This section is for usage instructions. You will be asked for each step in using the application, you will then be asked if you wish to add a code snippet for that step")
usageQ = usage_steps() 

# Title
#titleQ = text("What Title would you like to give your project?")
# Project Repo URL
#urlQ = text("What is the GitHub Repo Url for the proejct?")
# GitHub Deployment URL
#deployQ = text("Is there a deployment URL for this project?")
# Project Description
#descriptionQ = tMulti("Please add your description here:")

## Installation Instructions
# Specify which languages our project uses
#language_check = checkbox("Select which languages you are using", language_choice())
# Use the languages we choose to display the installation options
#instruction_check = checkbox("Select the instruction options from below:", lang_choice_gen(language_check.results()))

#print(titleQ.results())
#print(descriptionQ.results())
#print(language_check.results())
#print(instruction_check.results())
print(usageQ)
