
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from pathlib import Path
import subprocess, sys, os


def run_cli(input_path: Path):
    # Simple wrapper to call CLI script
    cmd = [sys.executable, 'book_price_finder.py', str(input_path)]
    subprocess.run(cmd, check=False)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Book Price Finder')
        self.configure(bg='#1e1e1e')
        self.geometry('500x250')
        self.input_path: Path | None = None
        self.report_dir = Path('output')
        self._build()

    def _build(self):
        lbl = tk.Label(self, text='Book Price Finder', bg='#1e1e1e', fg='#ffffff', font=('Segoe UI', 16, 'bold'))
        lbl.pack(pady=10)
        self.file_label = tk.Label(self, text='No file selected', bg='#1e1e1e', fg='#e0e0e0')
        self.file_label.pack(pady=5)
        tk.Button(self, text='Browse...', command=self.browse).pack(pady=5)
        tk.Button(self, text='Search Prices', command=self.run).pack(pady=10)
        tk.Button(self, text='Open Output Folder', command=self.open_folder).pack(pady=5)

    def browse(self):
        fname = filedialog.askopenfilename(filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
        if fname:
            self.input_path = Path(fname)
            self.file_label.config(text=self.input_path.name)

    def run(self):
        if not self.input_path:
            messagebox.showerror('Error', 'Select an input file first.')
            return
        run_cli(self.input_path)
        messagebox.showinfo('Done', 'Search complete. Check the output folder.')

    def open_folder(self):
        self.report_dir.mkdir(exist_ok=True)
        os.startfile(self.report_dir)


if __name__ == '__main__':
    App().mainloop()
