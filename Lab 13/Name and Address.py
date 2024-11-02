import tkinter
import tkinter.messagebox

class MyGUI: 
  def __init__(self):
    self.main_window = tkinter.Tk()
    #Show Info: display name and address when button clicked
    self.show_info_button = tkinter.Button(self.main_window, text = 'Show Info', command = self.execute)
    #Quit: undo Show Info
    self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)
    
    self.show_info_button.pack(side = 'left')
    self.quit_button.pack(side = 'right')
    tkinter.mainloop()
  #display box of name and address
  def execute(self):
      tkinter.messagebox.showinfo('My Information', 'My name is Nandini Patel and I live in Spartanburg, SC.')
my_gui = MyGUI()
