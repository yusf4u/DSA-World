import tkinter as tk
import time

class QueueGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Queue Game")

        # Canvas full screen
        self.canvas = tk.Canvas(root, width=900, height=500, bg="#1e1e2e")
        self.canvas.pack()

        # Queue data
        self.queue = []
        self.box_size = 60
        self.gap = 15
        self.y = 150

        # UI Elements (centered)
        self.entry = tk.Entry(root, font=('Consolas', 14), width=10)
        self.canvas.create_window(350, 300, window=self.entry)

        self.enqueue_button = tk.Button(root, text="Enqueue", font=('Consolas', 12),
                                        bg="#89b4fa", command=self.enqueue)
        self.canvas.create_window(470, 300, window=self.enqueue_button)

        self.dequeue_button = tk.Button(root, text="Dequeue", font=('Consolas', 12),
                                        bg="#f38ba8", command=self.dequeue, state=tk.DISABLED)
        self.canvas.create_window(590, 300, window=self.dequeue_button)

        self.canvas.create_text(450, 40, text="Queue Visualizer", font=("Consolas", 18, "bold"), fill="white")

    def draw_queue(self):
        self.canvas.delete("queue")

        total_width = len(self.queue) * (self.box_size + self.gap) - self.gap
        start_x = (900 - total_width) // 2

        for i, value in enumerate(self.queue):
            x = start_x + i * (self.box_size + self.gap)
            self.canvas.create_rectangle(x, self.y, x + self.box_size, self.y + self.box_size,
                                         fill="#a6e3a1", outline="#94e2d5", width=3, tags="queue")
            self.canvas.create_text(x + self.box_size / 2, self.y + self.box_size / 2,
                                    text=value, font=('Consolas', 16), fill="black", tags="queue")

            if i == 0:
                self.canvas.create_line(x + self.box_size / 2, self.y - 30,
                                        x + self.box_size / 2, self.y,
                                        arrow=tk.LAST, width=3, fill="#f38ba8", tags="queue")
                self.canvas.create_text(x + self.box_size / 2, self.y - 40,
                                        text="FRONT", fill="#f38ba8", font=("Consolas", 12, "bold"), tags="queue")

            if i == len(self.queue) - 1:
                self.canvas.create_line(x + self.box_size / 2, self.y + self.box_size,
                                        x + self.box_size / 2, self.y + self.box_size + 30,
                                        arrow=tk.LAST, width=3, fill="#89b4fa", tags="queue")
                self.canvas.create_text(x + self.box_size / 2, self.y + self.box_size + 40,
                                        text="REAR", fill="#89b4fa", font=("Consolas", 12, "bold"), tags="queue")

    def animate_enqueue(self, value, target_index):
        total_width = (target_index + 1) * (self.box_size + self.gap) - self.gap
        target_x = (900 - total_width) // 2 + target_index * (self.box_size + self.gap)
        x = 10
        y = self.y
        box = self.canvas.create_rectangle(x, y, x + self.box_size, y + self.box_size,
                                           fill="#fab387", outline="#f9e2af", width=3, tags="queue")
        text = self.canvas.create_text(x + self.box_size / 2, y + self.box_size / 2,
                                       text=value, font=('Consolas', 16), fill="black", tags="queue")

        while x < target_x:
            self.canvas.move(box, 5, 0)
            self.canvas.move(text, 5, 0)
            self.canvas.update()
            x += 5
            time.sleep(0.01)

    def enqueue(self):
        value = self.entry.get().strip()
        if not value:
            return
        self.entry.delete(0, tk.END)
        self.animate_enqueue(value, len(self.queue))
        self.queue.append(value)
        self.draw_queue()
        self.update_buttons()

    def dequeue(self):
        if not self.queue:
            return
        self.draw_queue()

        total_width = len(self.queue) * (self.box_size + self.gap) - self.gap
        start_x = (900 - total_width) // 2
        x = start_x
        y = self.y
        box = self.canvas.create_rectangle(x, y, x + self.box_size, y + self.box_size,
                                           fill="#f38ba8", outline="#eba0ac", width=3, tags="queue")
        text = self.canvas.create_text(x + self.box_size / 2, y + self.box_size / 2,
                                       text=self.queue[0], font=('Consolas', 16), fill="black", tags="queue")

        for _ in range(20):
            self.canvas.move(box, -5, 0)
            self.canvas.move(text, -5, 0)
            self.canvas.update()
            time.sleep(0.01)

        self.queue.pop(0)
        self.draw_queue()
        self.update_buttons()

    def update_buttons(self):
        # Disable the Dequeue button if the queue is empty
        if len(self.queue) == 0:
            self.dequeue_button.config(state=tk.DISABLED)
        else:
            self.dequeue_button.config(state=tk.NORMAL)

