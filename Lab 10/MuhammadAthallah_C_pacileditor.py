from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()
        self.create_buttons()
        self.create_editor()

    def initUI(self):
        # Mengubah judul dari main window
        self.master.title("Pacil Editor")
        # Mengubah ukuran dari main window
        self.master.geometry("500x400")
        # Membuat Frame sebagai anchor dari seluruh button
        self.container = Frame(self.master)
        # Anchor ke sisi atas, northwest
        self.container.pack(side=TOP, anchor=NW)

    def create_buttons(self):
        # Inisiasi tombol
        self.open_button = Button(self.container, text="Open File", command=self.load_file)
        self.save_button = Button(self.container, text="Save File", command=self.save_file)
        self.quit_button = Button(self.container, text="Quit Program", command=self.master.destroy)
        # Tampilkan tombol
        self.open_button.grid(row=0, column=0, padx=5)
        self.save_button.grid(row=0, column=1, padx=5)
        self.quit_button.grid(row=0, column=2, padx=5)
        # Buat shortcut
        self.master.bind('<Control-o>', self.load_file_event)
        self.master.bind('<Control-s>', self.save_file_event)

    def create_editor(self):
        # Insiasi bagian teks
        self.edit = Text(self.master)
        # Tampilkan dengan behavior stretch
        self.edit.pack(padx=5, pady=10, fill=BOTH, expand=YES)
    
    def load_file_event(self, event):
        self.load_file()

    def load_file(self):
        file_name = askopenfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return
        text_file = open(file_name, 'r', encoding="utf-8")
        result = text_file.read()
        # Tampilkan result di textbox
        self.set_text(result)
        # Close file
        text_file.close()

    def save_file_event(self, event):
        self.save_file()

    def save_file(self):
        file_name = asksaveasfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return
        # Ambil teks dari textbox
        result = self.get_text()
        # Simpan dalam file dengan nama file_name
        text_file = open(file_name, 'w', encoding="utf-8")
        text_file.write(result)
        text_file.close()

    def set_text(self, text=''):
        self.edit.delete('1.0', END)
        self.edit.insert('1.0', text)
        self.edit.mark_set(INSERT, '1.0')
        self.edit.focus()

    def get_text(self):
        return self.edit.get('1.0', END+'-1c')


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
