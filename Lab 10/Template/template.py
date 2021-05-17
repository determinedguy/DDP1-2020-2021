from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

# TODO: Lengkapi class Application dibawah ini
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()
        self.create_buttons()
        self.create_editor()

    def initUI(self):
        # TODO: Atur judul dan ukuran dari main window,
        # lalu buat sebuah Frame sebagai anchor dari seluruh button
        pass

    def create_buttons(self):
        # TODO: Implementasikan semua button yang dibutuhkan
        pass

    def create_editor(self):
        # TODO: Implementasikan textbox
        pass

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
        # TODO: tampilkan result di textbox

    def save_file_event(self, event):
        self.save_file()

    def save_file(self):
        file_name = asksaveasfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return
        # TODO: ambil isi dari textbox lalu simpan dalam file dengan nama file_name

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
