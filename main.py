import tkinter as tk
from tkinter import ttk
import logic

class Application(tk.Frame):
    def __init__(self, master: tk.Tk = None):
        super().__init__(master)
        self.master: tk.Tk = master

        self.settings()
        self.widgets()
        self.pack()

    def settings(self):
        self.master.title("Analizador Léxico")
        # self.master.geometry("600x400")
        self.master.resizable(False, False)

    def final_area(self):
        self.middle = tk.Frame(self)

        self.text_area = tk.Text(self.middle, width=60, height=15)
        self.v_scrollbar = tk.Scrollbar(self.middle, command=self.text_area.yview, orient=tk.VERTICAL)
        self.text_area.configure(yscrollcommand=self.v_scrollbar.set)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.middle.pack(fill=tk.BOTH, expand=tk.YES, pady=5, padx=10)

    def widgets(self):
        self.cadena_lbl = tk.Label(self)
        self.cadena_lbl['text'] = "Ingresa cadena"
        self.cadena_lbl.pack()


        self.text_field = tk.Entry(self)
        self.text_field.focus_set()
        self.text_field.pack(pady=5)

        self.button = tk.Button(self, command=self.analizar)
        self.button['text'] = "Analizar"
        self.button.pack(expand=tk.YES, pady=5)

        self.final_area()

    def analizar(self):
        self.text_area['state'] = tk.NORMAL
        self.text_area.delete(1.0, tk.END)

        texto = self.text_field.get()
        tokens = logic.run(texto)

        for i in range(len(tokens)):
            self.text_area.insert(tk.INSERT, f'{tokens[i]}\n')
        
        self.text_area['state'] = tk.DISABLED
    
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()