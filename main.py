from InquirerPy import inquirer

class fItem:
    def __init__(self, tMess = ""):
        self.tMess = tMess
            
    def results(self):
        print(self.result)

class tMulti(fItem):
    def __init__(self, tMess = ""):
        self.result = inquirer.text(message=tMess, multiline=True).execute()

class text(fItem):
    def __init__(self, tMess = ""):
        self.result = inquirer.text(message=tMess).execute()

titleQ = text("What Ttitle would you like to give your project?")
descriptionQ = tMulti("Please add your description here:")
titleQ.results()
descriptionQ.results()