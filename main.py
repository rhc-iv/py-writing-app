import tkinter as tk


class WritingApp:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='#3E4451')
        self.master.columnconfigure(0, weight=3)
        self.master.geometry('1000x800')
        self.master.resizable(0, 0)
        self.master.rowconfigure(0, weight=4)
        self.master.title('Writing App..With A Twist!')

        self.app_name = tk.Label(
            bg='#3E4451',
            fg='#98C379',
            font=(
                'SF Pro Display',
                32,
                'bold',
            ),
            text=('Tkinter Devious Writing App'),
        )
        self.app_name.grid(
            row=0,
            column=0,
            columnspan=3,
        )

        self.text_input = tk.Text(
            self.master,
            bg='gray',
            fg='white',
            font=(
                'SF Pro Display',
                16,
                'normal',
            ),
            height=30,
            padx=10,
            pady=10,
            width=80
        )
        self.text_input.grid(
            column=0,
            columnspan=3,
            padx=10,
            pady=5,
            row=1,
        )

        self.close_button = tk.Button(
            self.master,
            borderwidth=1.5,
            cursor='pirate',
            default=tk.NORMAL,
            font=(
                'SF Pro Display',
                18,
                'bold',
            ),
            highlightcolor='#E06C75',
            highlightbackground='#ABB2BF',
            padx=30,
            pady=5,
            relief='groove',
            text="CLOSE",
            command=self.close_app
        )
        self.close_button.grid(
            column=0,
            pady=10,
            row=2,
        )

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