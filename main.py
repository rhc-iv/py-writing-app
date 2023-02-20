import tkinter as tk


class WritingApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x600')
        self.master.title('Writing App..With A Twist!')

        self.text_input = tk.Text(
            self.master,
            height=30,
            width=80
        )
        self.text_input.pack()

        self.close_button = tk.Button(
            self.master,
            text="CLOSE",
            command=self.close_app
        )
        self.close_button.pack(side=tk.BOTTOM)

        self.text_input.bind("<Key>", self.reset_timer)
        self.timer = None

    def reset_timer(self, event):
        if self.timer is not None:
            self.master.after_cancel(self.timer)
        self.timer = self.master.after(2000, self.clear_text_input)

    def clear_text_input(self):
        self.text_input.delete('1.0', tk.END)

    def close_app(self):
        self.master.destroy()


root = tk.Tk()
app = WritingApp(root)
root.mainloop()