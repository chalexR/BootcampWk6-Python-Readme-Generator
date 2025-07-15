from InquirerPy import inquirer

class fItem:
    def __init__(self, tMess = ""):
        self.tMess = tMess
            
    def results(self):
        return self.result

class tMulti(fItem):
    def __init__(self, tMess = ""):
        self.result = inquirer.text(message=tMess, multiline=True).execute()

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

def language_choice():
    return [
        "HTML/CSS",
        "JavaScript",
        "Python"
    ]

def lang_choice_gen(lang_choices):
    def general_choice(): 
        return [
            # General
            "Clone the repository",
            "Navigate into the project directory",
            "Install dependencies",
            "Other (manually enter custom instructions)",

            # GitHub Pages / Hosting
            "Deploy with GitHub Pages",
            "Deploy with Netlify or Vercel",
            "Push to GitHub to trigger CI/CD deployment"
        ]

    def python_choice():
        return[
            "Create and activate a virtual environment (Python)",
            "Install dependencies with pip",
            "Install via requirements.txt",
            "Set environment variables",
            "Run a setup script",
            "Run initial database migrations (Django/Flask/etc)",
            "Start the Python application (e.g., python app.py)"
        ]

    def js_choice():
        return[
            "Install Node.js dependencies with npm",
            "Install Node.js dependencies with yarn",
            "Build the project with npm/yarn",
            "Run the development server (e.g., npm start)",
            "Run tests with npm/yarn",
            "Configure environment variables (.env file)"
        ]

    def html_choice():
        return[
            "Open index.html in your browser",
            "Ensure assets (images, fonts, etc.) are in the correct folders",
            "Link CSS and JS files correctly in HTML",
            "Check browser compatibility (optional)"
        ]

    def adv_choice():
        return[
            "Install a CSS preprocessor (e.g., Sass, Less)",
            "Run a bundler (e.g., Webpack, Parcel)",
            "Start a local development server (e.g., Live Server, BrowserSync)",
            "Install Python/Node.js version managers (pyenv/nvm)"
        ]
    response = general_choice()
    for lang in lang_choices:
        if lang == "HTML/CSS":
            response.extend(html_choice())

    return response

# Must be laid out in order of how you wish for the to appear in form.

language_check = checkbox("Select which languages you are using", language_choice())

instruction_opts = lang_choice_gen(language_check.results())

#instruction_check = checkbox("Select the instruction options from below:", instruction_opts)
# Title
titleQ = text("What Title would you like to give your project?")
# Description
descriptionQ = tMulti("Please add your description here:")
#Installation Instructions
print(titleQ.results())
print(descriptionQ.results())
print(language_check.results())
print(instruction_opts)