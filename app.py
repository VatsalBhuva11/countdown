import tkinter as tk

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")

        self.time_left = 0
        self.timer_running = False

        # create and place widgets
        self.time_label = tk.Label(master, font=("Helvetica", 36))
        self.time_label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer, state="disabled")
        self.stop_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer, state="disabled")
        self.reset_button.pack()

        self.set_button = tk.Button(master, text="Set Time", command=self.set_time)
        self.set_button.pack()

    def set_time(self):
        self.time_left = int(input("Enter time in seconds: "))

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
            self.reset_button.config(state="normal")
            self.countdown()

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")

    def reset_timer(self):
        self.timer_running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.time_left = 0
        self.update_time()

    def countdown(self):
        if self.time_left <= 0:
            self.time_label.config(text="Time's up!")
            self.timer_running = False
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            self.reset_button.config(state="normal")
        else:
            if self.timer_running:
                self.update_time()
                self.master.after(1000, self.countdown)

    def update_time(self):
        minutes, seconds = divmod(self.time_left, 60)
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.time_label.config(text=time_str)
        self.time_left -= 1

root = tk.Tk()
countdown_timer = CountdownTimer(root)
root.mainloop()
