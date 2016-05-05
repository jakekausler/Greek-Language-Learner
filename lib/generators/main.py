'''
Created on Nov 18, 2014

@author: Jake Kausler

Main class of the program. Start a GUI that allows the user to
generate and translate sentences
'''

from Tkinter import *
import ttk
import tkFileDialog, tkMessageBox
import SemanticGenerator, SentenceGenerator
import os


class Window(Frame):
    '''
    Main Program Window. Contains a title, translation and text textboxes, and a contol panel.
    '''
    SEMANTIC = 0 #Constant denoting the semantic input method
    MODELLED = 1 #Constant denoting the modelled input method
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent = parent
        self.sentences = []
        self.answers = []
        self.currentQuestion = 0
        self.inputMethod = IntVar()
        self.weighted = BooleanVar()
        self.initUI()
        parent.protocol('WM_DELETE_WINDOW',self.onClose)

    def initUI(self):
        '''
        Initializes the User Interface
        '''
        self.parent.title("Greek Translation Practice")

        self.createTitlePanel()
        self.createTextPanel()
        self.createControlPanel()

        # self.columnconfigure(0,pad=3)
        # self.columnconfigure(1,pad=3)
        # self.columnconfigure(2,pad=3)

        # self.rowconfigure(0,pad=3)
        # self.rowconfigure(1,pad=3)
        # self.rowconfigure(2,pad=3)
        # self.rowconfigure(3,pad=3)
        # self.rowconfigure(4,pad=3)
        # self.rowconfigure(5,pad=3)
        # self.rowconfigure(6,pad=3)
        # self.rowconfigure(7,pad=3)
        # self.rowconfigure(8,pad=3)

        # self.textLabel = Label(self,text="Text:")
        # self.textLabel.grid(row=0,column=0,columnspan=3,sticky=W)
        # self.translationLabel = Label(self,text="Translation:")
        # self.translationLabel.grid(row=4,column=0,columnspan=3,sticky=W)
        # self.textBox = Text(self,height=5,width=50)
        # self.textBox.grid(row=1,column=0,rowspan=3,columnspan=3,sticky=W+E)
        # self.translationBox = Text(self,height=5,width=50)
        # self.translationBox.grid(row=5,column=0,rowspan=3,columnspan=3,sticky=W+E)
        # self.previousButton = Button(self,text="Previous",command=self.previousQuestion)
        # self.previousButton.grid(row=8,column=0,sticky=W+E)
        # self.nextButton = Button(self,text="Next",command=self.nextQuestion)
        # self.nextButton.grid(row=8,column=1,sticky=W+E)
        # self.newButton = Button(self,text="New",command=self.getNewQuestions)
        # self.newButton.grid(row=8,column=2,sticky=W+E)

        self.pack(fill='both',expand=True)

    def createTitlePanel(self):
        '''
        Creates the Title Frame
        '''
        self.titleFrame = Frame(self)
        self.titleLabel = Label(self.titleFrame,text='Greek Grammar Generator')
        self.titleLabel.pack(fill=BOTH)
        self.titleFrame.pack(fill=BOTH)

    def createTextPanel(self):
        '''
        Creates the Text Frame, consisting of the text and translation textboxs
        '''
        self.textFrame = Frame(self)
        self.textLabel = Label(self.textFrame,text="Text:")
        self.textLabel.pack(fill=BOTH)

        self.textBoxFrame = Frame(self.textFrame)
        self.textBox = Text(self.textBoxFrame,state=DISABLED,height=5)
        self.textBox.pack(fill=BOTH,side=LEFT,expand=True)
        self.textScroll = Scrollbar(self.textBoxFrame)
        self.textScroll.pack(fill=Y,side=RIGHT,expand=False)
        self.textBox.config(yscrollcommand=self.textScroll.set)
        self.textBoxFrame.pack(fill=BOTH,expand=True)

        self.translationLabel = Label(self.textFrame,text="Translation:")
        self.translationLabel.pack(fill=BOTH)

        self.translationBoxFrame = Frame(self.textFrame)
        self.translationBox = Text(self.translationBoxFrame,height=5)
        self.translationBox.pack(fill=BOTH,side=LEFT,expand=True)
        self.translationScroll = Scrollbar(self.translationBoxFrame)
        self.translationScroll.pack(fill=Y,side=RIGHT,expand=False)
        self.translationBox.config(yscrollcommand=self.translationScroll.set)
        self.translationBoxFrame.pack(fill=BOTH,expand=True)

        self.textFrame.pack(fill=BOTH,expand=True)

    def createControlPanel(self):
        '''
        Creates the control frame, which allows the user to switch questions and generate new questions
        '''
        self.controlFrame = Frame(self)
        
        #Configure the columns and rows of the control frame
        self.controlFrame.rowconfigure(0,pad=3,weight=1)
        self.controlFrame.rowconfigure(1,pad=3,weight=1)
        self.controlFrame.columnconfigure(0,pad=3,weight=1)
        self.controlFrame.columnconfigure(1,pad=3,weight=1)
        self.controlFrame.columnconfigure(2,pad=3,weight=1)

        #Add the navigation buttons
        self.previousButton = Button(self.controlFrame,text="Previous",command=self.previousQuestion)
        self.previousButton.grid(row=0,column=0,sticky=W+E)
        self.nextButton = Button(self.controlFrame,text="Next",command=self.nextQuestion)
        self.nextButton.grid(row=0,column=1,sticky=W+E)

        #Add the save/open buttons
        self.saveButton = Button(self.controlFrame,text="Save",command=self.saveSession)
        self.saveButton.grid(row=1,column=0,sticky=W+E)
        self.openButton = Button(self.controlFrame,text="Open",command=self.openSession)
        self.openButton.grid(row=1,column=1,sticky=W+E)

        #Create the config frame, which holds the options and button for creating new sentences
        self.configFrame = Frame(self.controlFrame)
        self.configFrame.grid(row=0,column=2,sticky=W+E,rowspan=2)

        #Configure the config frame rows and columns
        self.configFrame.rowconfigure(0,pad=3,weight=1)
        self.configFrame.rowconfigure(1,pad=3,weight=1)
        self.configFrame.rowconfigure(2,pad=3,weight=1)
        self.configFrame.columnconfigure(0,pad=3,weight=1)
        self.configFrame.columnconfigure(1,pad=3,weight=1)
        self.configFrame.columnconfigure(2,pad=3,weight=1)
        self.configFrame.columnconfigure(3,pad=3,weight=1)

        #Add the contols to the config frame
        self.newButton = Button(self.configFrame,text="New",command=self.getNewQuestions)
        self.newButton.grid(row=0,column=3,rowspan=3,sticky=W+E)
        self.numberLabel = Label(self.configFrame,text='Number:')
        self.numberLabel.grid(row=0,column=0,sticky=W+E)
        self.complexityLabel = Label(self.configFrame,text='Complexity:')
        self.complexityLabel.grid(row=1,column=0,sticky=W+E)
        self.numberSlider = Scale(self.configFrame,from_=1,to=20,orient=HORIZONTAL)
        self.numberSlider.grid(row=0,column=1,columnspan=2,sticky=W+E)
        self.numberSlider.set(5)
        self.complexitySlider = Scale(self.configFrame,from_=1,to=20,orient=HORIZONTAL)
        self.complexitySlider.grid(row=1,column=1,columnspan=2,sticky=W+E)
        self.complexitySlider.set(5)
        self.weightedCheckBox = Checkbutton(self.configFrame,text='Weighted',variable=self.weighted)
        self.weightedCheckBox.grid(row=2,column=0,sticky=W+E)
        self.semanticRadioButton = Radiobutton(self.configFrame,text='Semantic Mode',variable=self.inputMethod,value=self.SEMANTIC)
        self.semanticRadioButton.grid(row=2,column=1,sticky=W+E)
        self.modelledRadioButton = Radiobutton(self.configFrame,text='Modelled Mode',variable=self.inputMethod,value=self.MODELLED)
        self.modelledRadioButton.grid(row=2,column=2,sticky=W+E)

        self.controlFrame.pack(fill=BOTH,expand=True)

    def getNewQuestions(self):
        '''
        Generate new sentences based on the input method.
        '''
        if not self.sentences: # if list is empty
            prompt = self.promptSave()
            if prompt == None:
                return
            elif prompt == True:
                saved = self.saveSession()
                if saved == -1:
                    return
        if self.inputMethod.get() == self.SEMANTIC:
            self.sentences = generateSentencesSemantic(self.numberSlider.get(),self.complexitySlider.get())
        elif self.inputMethod.get() == self.MODELLED:
            self.sentences = generateSentencesModelled(self.numberSlider.get(),self.weighted.get())
        self.currentQuestion=0
        self.updateText()
        self.clearAnswers()

    def updateText(self):
        '''
        Change the text in the textBox (the Greek box) to the current sentence
        '''
        self.textBox.config(state=NORMAL)
        self.textBox.delete(1.0, END)
        if self.inputMethod.get() == self.SEMANTIC:
            if len(self.sentences) > 0:
                for w in self.sentences[self.currentQuestion]:
                    self.textBox.insert(END,w+' ')
        else:
            if len(self.sentences) > 0:
                for w in self.sentences[self.currentQuestion][0]:
                    self.textBox.insert(END,w+' ')
        self.textBox.config(state=DISABLED)

    def updateTranslation(self):
        '''
        Change the text in the translationBox (the English box) to the current sentence
        '''
        self.translationBox.delete("1.0", END)
        if len(self.sentences) > 0:
            self.translationBox.insert(END,self.answers[self.currentQuestion])

    def clearAnswers(self):
        '''
        Remove all user answers from memory
        '''
        self.answers = []
        for i in range(len(self.sentences)):
            self.answers.append('')

    def saveAnswer(self):
        '''
        Save the current answer to memory
        '''
        self.answers[self.currentQuestion] = self.translationBox.get("1.0",END)

    def nextQuestion(self):
        '''
        Go to the next question (allows for looping)
        '''
        if len(self.sentences) > 0:
            self.saveAnswer()
            if self.currentQuestion == len(self.sentences)-1:
                self.currentQuestion = 0
            else:
                self.currentQuestion += 1
            self.updateText()
            self.updateTranslation()
            self.autosave()

    def previousQuestion(self):
        '''
        Go to the previous question (allows for looping)
        '''
        if len(self.sentences) > 0:
            self.saveAnswer()
            if self.currentQuestion == 0:
                self.currentQuestion = len(self.sentences)-1
            else:
                self.currentQuestion -= 1
            self.updateText()
            self.updateTranslation()
            self.autosave()

    def saveSession(self,f=None):
        '''
        Saves the current session to a file.

        Keyword Arguments:
        f - file to which save (used when saving the backup)

        Returns:
        1 if the session saves
        -1 if not (error or cancellation)
        '''
        if f == None: #File needs to be filled
            f = tkFileDialog.asksaveasfilename(defaultextension='.fll',filetypes=[('Foreign Language Learning Files','.fll')])
        if f == '': #Error or cancellation
            return -1
        else:
            self.saveAnswer()
            f = open(f,'w+')
            f.write(self.formatSaveFile())
            f.close()
            return 1

    def formatSaveFile(self):
        '''
        Creates and returns a string representing the current user session
        '''
        s = ''
        s += 'Greek\n' #to be used in future versions
        for sent in self.sentences:
            for w in sent:
                print type(w), w
                s += w + ','
            s = s[:-1] + '\n'
        s += '\n'
        for ans in self.answers:
            s += ans[:-1] + '\n'
        return s

    def autosave(self,f='../../Autosave/autosave.fll'):
        '''Autosaves the current session

        Keyword Arguments:
        f - Autosave file
        '''
        self.saveSession(f)

    def openSession(self,f=None):
        '''
        Opens a new session from a file.

        Keyword Arguments:
        f - file to open (used when opening an autosaved file)

        Returns:
        1 if the session saves
        -1 if not (error or cancellation)
        '''
        if f == None: #File needs to be filled
            f = tkFileDialog.askopenfilename(defaultextension='.fll',filetypes=[('Foreign Language Learning Files','.fll')])
        if f == None: #Error or cancellation
            return -1
        else:
            if not self.sentences: # if list is empty
                prompt = self.promptSave()
                if prompt == None:
                    return -1
                elif prompt == True:
                    saved = self.saveSession()
                    if saved == -1:
                        return -1
            f = open(f)
            lines = f.readlines()
            f.close()
            self.readSessionFile(lines)
            return 1

    def readSessionFile(self,lines):
        '''
        Reads and opens the lines of a session file.

        Keyword Arguments:
        lines - the lines of the session file
        '''
        language = lines[0] #to be used in future versions
        self.sentences = []
        self.answers = []
        self.currentQuestion = 0
        readingSentences = True
        for line in lines[1:]:
            if line == '\n' and readingSentences:
                readingSentences = False
            else:
                if readingSentences:
                    self.sentences.append([])
                    for word in line[:-1].split(','):
                        self.sentences[len(self.sentences)-1].append(word)
                elif len(self.answers) < len(self.sentences):
                    self.answers.append(line)
        self.updateText()
        self.updateTranslation()


    def promptSave(self):
        '''
        Tells the user that they are about to delete the current
        session, and asks them if they want to save. Returns a value
        based on the user's choice to the prompt.

        Returns:
        None: Cancel
        False: Don't Save
        True: Save
        '''
        return tkMessageBox.askyesnocancel(default=tkMessageBox.YES,icon=tkMessageBox.QUESTION,message='This will end your current session.\nWould you like to save your current session?',title='Save?')

    def onClose(self):
        '''
        Prompts the user to save on closing the program
        '''
        if not self.sentences: # if list is empty
            prompt = self.promptSave()
            if prompt == None:
                return
            elif prompt == True:
                saved = self.saveSession()
                if saved == -1:
                    return
        self.parent.quit()

def main():
    '''
    Start the program.
    '''
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    root = Tk()
    root.geometry('500x350+300+300')
    app = Window(root)
    root.mainloop()

def generateSentencesSemantic(number,minLength):
    '''
    Generate sentences by the semantic method
    '''
    return SemanticGenerator.makeSentences(number,minLength)

def generateSentencesModelled(number,weighted):
    '''
    Generate sentences by the modelled method
    '''
    return SentenceGenerator.autogenerateSentencesFromModelFile(number,weighted)

#Run the program
if __name__ == '__main__':
    main()