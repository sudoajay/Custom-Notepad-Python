from tkinter.filedialog import *
from tkinter.messagebox import *


class Notepad:
    root = Tk()
    root.configure(bg='black')
    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(root)
    __thisMenuBar = Menu(root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self):

        # # Set icon
        # try:
        #     self.root.wm_iconbitmap("ajay.ico")
        # except:
        #     pass

        # Set window size (the default is 300x300)

        try:
            self.__thisWidth = self.root.winfo_screenwidth()
        except KeyError:
            # self.__thisWidth = 300
            pass

        try:
            self.__thisHeight = self.root.winfo_screenheight()
        except KeyError:
            pass

        # Set the window text
        self.root.title("Untitled - Notepad")

        # Center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # For top and bottom
        self.root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                            self.__thisHeight,
                                            left, top))

        # To make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)
        self.__thisTextArea.bind('<KeyPress>', self.track_change_to_text)

        # To open new file
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)

        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)

        # To save current file
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)

        # To create a line in the dialog
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)

        # To give a feature of cut
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)

        # to give a feature of copy
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)

        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)

        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)

        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)

        self.root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.root.destroy()

    # exit()

    def __showAbout(self):
        showinfo("Notepad", "Minor Project - Akansha")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Text Documents", "*.txt")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            try:
                self.root.title(os.path.dirname(self.__file) + " - Notepad")

                self.__thisTextArea.delete(1.0, END)

                file = open(self.__file, "r")

                self.__thisTextArea.insert(1.0, file.read())

                file.close()
            except:
                pass

    def __newFile(self):
        self.root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Text Documents", "*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                try:
                    # Try to save the file
                    file = open(self.__file, "w")
                    file.write(self.__thisTextArea.get(1.0, END))
                    file.close()

                    # Change the window title
                    self.root.title(os.path.basename(self.__file) + " - Notepad")
                except:
                    pass

        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        # Run main application
        self.root.mainloop()

    # Run main application
    def track_change_to_text(self):
        self.__thisTextArea.tag_add("here", "1.0", "1.4")
        self.__thisTextArea.tag_config("here", background="black", foreground="green")

notepad = Notepad()
notepad.run()
