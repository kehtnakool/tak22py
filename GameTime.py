from datetime import datetime


class GameTime:
    def __init__(self, label_time):
        self.label_time = label_time
        self.counter = 0
        self.running = False

    def update(self):
        if self.running:
            if self.counter == 0:
                display = "00:00:00"
            else:
                tt = datetime.utcfromtimestamp(self.counter)
                string = tt.strftime("%T")  # %M%M%S
                display = string
            self.label_time["text"] = display
            self.label_time.after(1000, self.update)
            self.counter += 1

    def start(self):
        self.running = True
        self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.counter = 0
        self.label_time["text"] = "00:00:00"
