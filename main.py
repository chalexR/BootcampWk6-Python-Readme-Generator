from InquirerPy import inquirer
from InquirerPy.separator import Separator
from rich.style import Style
from rich.console import Console
import os
import pathlib

class fItem:
    def __init__(self, tMess = ""):
        self.tMess = tMess
        self.result = ""
            
    def results(self):
        return self.result
    
    def __str__(self):
        return f"{self.result}"

class tMulti(fItem):
    def __init__(self, tMess = ""):
        self.result = inquirer.text(
            message=tMess, 
            multiline=True).execute()

class text(fItem):
    def __init__(self, tMess = ""):
        self.result = inquirer.text(
            message=tMess
            ).execute()

class checkbox(fItem):
    def __init__(self, tMess = "", checkChoice = ""):
        self.result = inquirer.checkbox(
            message = tMess,
            choices = checkChoice,
            validate = lambda result: len (result) >= 1,
            invalid_message = "At least 1 items must be selected"
            ).execute()

class dropdown(fItem):
    def __init__(self, tMess, dropChoice = ""):
        self.result = inquirer.select(
            message = tMess,
            choices = dropChoice,
            default = None
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

def instruction_cont(instr, repoURL = False):
    customCheck = False
    funcResponse = "# Installation Instructions \n\n"
    if not repoURL:
        repoURL = "https://github.com/your-username/your-repo-name.git"
    for data in instr:

        if data == "Clone the repository":
            funcResponse += f"### Clone the repository\n\n"
            funcResponse += f"To get a local copy of this project up and running, clone the repository using:\n\n"
            funcResponse += f"```git clone {repoURL}```"
            funcResponse += f"\n\n"
            customCheck = True #use this to make sure the script knows you have edited the response

        if data == "Navigate into the project directory":
            funcResponse += f"### Navigate into the project directory\n\n"
            funcResponse += f"Then navigate into the project directory:\n\n"
            funcResponse += f"```cd your-repo-name```"
            funcResponse += f"\n\n"
            customCheck = True #use this to make sure the script knows you have edited the response

        if data == "Install dependencies":
            funcResponse += f"### Install Dependencies\n\n"
            funcResponse += f"## Python (with pip)"
            funcResponse += f"If you’re using Python, make sure your virtual environment is activated, then run:\n\n"
            funcResponse += f"```pip install -r requirements.txt```"
            funcResponse += f"\n\n"
            customCheck = True #use this to make sure the script knows you have edited the response

        if data == "Create and activate a virtual environment":
            funcResponse += f"### Create and Activate a Virtual Environment\n\n"
            funcResponse += f"It is recommended to use a virtual environment to manage dependencies. To create and activate one:"
            funcResponse += f"## macOS / Linux"
            funcResponse += f"```python3 -m venv venv\nsource venv/bin/activate```"
            funcResponse += f"## Windows"
            funcResponse += f"```python -m venv venv\nvenv\Scripts\activate```"
            funcResponse += f"Once activated, your terminal prompt should change (e.g., (venv)), and you can proceed to install dependencies."
            funcResponse += f"\n\n"
            customCheck = True #use this to make sure the script knows you have edited the response
        
        if data == "Start the Python application":
            funcResponse += f"### Start the Python Application\n\n"
            funcResponse += f"After activating your virtual environment and installing dependencies, you can run the application with:"
            funcResponse += f"```python main.py```"
            funcResponse += f"* *Replace main.py with your actual entry-point file name if different.* *"
            funcResponse += f"If your project requires environment variables or setup steps before running, make sure those are completed first."
            funcResponse += f"\n\n"
            customCheck = True #use this to make sure the script knows you have edited the response

        if not customCheck:
            funcResponse += f"{data}\n"
    return funcResponse

def license_cont(license, name):
    if license == "MIT License":
        return f'# MIT License\n\nCopyright (c) 2025 [your name]\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, subject to the following conditions:\n[Full license: https://opensource.org/licenses/MIT]'
    else:
        return license

## Function to define and return the available coding languages
def language_choice():
    return [
        "HTML/CSS",
        "JavaScript",
        "Python"
    ]

## Function to take the selected coding languages and give the user back options for a chockbox
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
            "Create and activate a virtual environment",
            "Install dependencies with pip",
            "Install via requirements.txt",
            "Set environment variables",
            "Run a setup script",
            "Run initial database migrations (Django/Flask/etc)",
            "Start the Python application"
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

## Function to return Options for license options
def license_opt():
    return [
        "MIT License",
        "Apache License 2.0",
        "GNU General Public License (GPL v3)",
        "GNU Lesser General Public License (LGPL v3)",
        "BSD 2-Clause / 3-Clause License",
        "Mozilla Public License 2.0 (MPL 2.0)",
        Separator("Not for Code Projects"),
        "Creative Commons (CC) Licenses"
    ]

# TODO: Add in a response for adding a custom set up instruction if the user chooses Other.
# Then we need to populate a text string based on the options selected

### BUILD THE FORM

# Must be laid out in order of how you wish for the to appear in form.
console = Console()
## General Project Information
console.print("Add basic info for the project (project title, description, repoURL etc", style="bold green")
# Title
titleQ = text("What Title would you like to give your project?")
# Project Repo URL
urlQ = text("What is the GitHub Repo Url for the proejct?")
# GitHub Deployment URL
deployQ = text("Is there a deployment URL for this project?")
# Project Description
descriptionQ = tMulti("Please add your description here:")

## Installation Instructions
console.print("Add Installation Instructions, this will give you multiple choices, simply add the ones that apply to the project.", style="bold green")
# Specify which languages our project uses
language_check = checkbox("Select which languages you are using", language_choice())
# Use the languages we choose to display the installation options
instruction_check = checkbox("Select the instruction options from below:", lang_choice_gen(language_check.results()))

## Usage Instructions
console.print("This section is for usage instructions. You will be asked for each step in using the application, you will then be asked if you wish to add a code snippet for that step", style="bold green")
usageQ = usage_steps() 

console.print("Add Licensing and Author Info", style="bold green")
## License Info
licenseQ = dropdown("Select the license for the project:", license_opt())

## Author Info
# Name
nameQ = text("Author Name:")
emailQ = text("Author Email:")
webQ = text("Website Address:")

### BUILD OUT VARIABLES

pTitle = titleQ.results()
pRepoURL = urlQ.results()
pDeplURL = deployQ.results()
pDesc = descriptionQ.results()
pInstr = instruction_check.results()
pHowTo = usageQ
pLicense = licenseQ.results()
pName = nameQ.results()
pEmail = emailQ.results()
pWebsite = webQ.results()

### File Formatting & Save

## Save
file_path = str(pathlib.Path(__file__).parent.resolve() )+ "/README.md"
# TITLE
file_cont = f"# {pTitle} \n \n"
# Description
file_cont += f"{pDesc}"
# Install Instructions Here
file_cont += instruction_cont(pInstr)
# Usage Instructions
file_cont += f"{pHowTo}"
file_cont += f"{instruction_cont(pInstr)}"
# Usage Instructions
file_cont += f"{license_cont(pLicense, pName)}"
# Build Author Section
file_cont += f"### Author Information"
# Usage Instructions
file_cont += f"Name: {pName}"
# Usage Instructions
file_cont += f"Email: {pEmail}"
# Usage Instructions
file_cont += f"Website: {pWebsite}"

with open(str(file_path), 'w') as file:
    file.write(file_cont)

console.print("FILE CREATED!")