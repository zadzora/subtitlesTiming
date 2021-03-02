import os
from tkinter import *
from tkinter import filedialog
import subtitlesTimer as subT


global filename
filename = "default.srt"

timeMove = 0


def timeValue(self):
    global timeMove
    timeMove = int(s1.get())


def changeValues():
    global filename
    subT.Wooble(timeMove, filename)

def browseFiles():
    global filename

    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Srt files", "*.srt*"), ("Text files", "*.txt*"), ("all files", "*.*")))

    label_file_explorer.configure(text="File Opened: " + filename)
    filename = os.path.basename(filename)


if __name__ == '__main__':


    # create window
    window = Tk()
    #window.geometry(str(500) + 'x' + str(300))
    #window.minsize(450,200)
    window.title('Subtitle')
    window.resizable(False, False)

    title_label = Label(window, text='Subtitles Changer', font=('Verdana', 12, 'bold'))


    # Create a File Explorer label
    label_file_explorer = Label(window, text="Choose source file...", font=('Verdana',8), fg="blue")

#
    button_explore = Button(window,
                            text="Browse Files",
                            command=browseFiles)


    timeToMove_label = Label(window, text="Time", font=('Verdana', 10,'bold'))
    timeToMove_field = Entry(window)



    change_button = Button(window, text='Change', font=('Verdana', 10, 'bold'),
                           bg="green",
                           fg="white",
                           command=changeValues)

    v1 = DoubleVar()

    s1 = Scale(window, variable=v1,
               from_=-50, to=50,
               orient=HORIZONTAL,
               command=timeValue)


    title_label.grid(column=1, row=1,pady=8)
    label_file_explorer.grid(column=1, row=2)
    button_explore.grid(column=0, row=3,padx=8)

    timeToMove_label.grid(column=0, row=4)

    s1.grid(column=1, row=4)
    change_button.grid(column=2, row=5,pady=8,padx=8)


    window.mainloop()

