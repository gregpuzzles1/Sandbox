import tkinter as tk
import time

class StopWatch(tk.Frame):
    """Implements a stopwatch as a tkinter Frame widget."""

    def __init__(self, parent=None, **kwargs):
        try:
            super().__init__(parent, **kwargs)
            self._start = 0.0                # Store the start time
            self._elapsedtime = 0.0          # Store the elapsed time
            self._running = False            # Track whether the stopwatch is running
            self._timer = None               # ID for the after event
            self.timestr = tk.StringVar()    # StringVar to update label text
            self._create_widgets()
        except Exception as e:
            print(f"Error initializing StopWatch: {e}")

    def _create_widgets(self):
        """Create and pack the label widget to display time."""
        try:
            self._set_time(self._elapsedtime)
            label = tk.Label(self, textvariable=self.timestr, font=('Helvetica', 24))
            label.pack(fill=tk.X, expand=False, pady=5, padx=5)
        except Exception as e:
            print(f"Error creating widgets: {e}")

    def _update(self):
        """Update the time display every 50 ms."""
        try:
            self._elapsedtime = time.time() - self._start
            self._set_time(self._elapsedtime)
            self._timer = self.after(50, self._update)
        except Exception as e:
            print(f"Error updating time: {e}")

    def _set_time(self, elap):
        """Format the time and set it to the label (MM:SS:HS)."""
        try:
            minutes = int(elap // 60)
            seconds = int(elap % 60)
            hseconds = int((elap - int(elap)) * 100)
            self.timestr.set(f'{minutes:02d}:{seconds:02d}:{hseconds:02d}')
        except Exception as e:
            print(f"Error formatting time: {e}")

    def start(self):
        """Start the stopwatch if it isn't already running."""
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = True

    def stop(self):
        """Stop the stopwatch if it is currently running."""
        if self._running:
            if self._timer:
                self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._set_time(self._elapsedtime)
            self._running = False

    def reset(self):
        """Reset the stopwatch to zero."""
        if self._running:
            self.stop()
        self._elapsedtime = 0.0
        self._set_time(self._elapsedtime)

def main():
    try:
        root = tk.Tk()
        root.title("Stopwatch")

        stopwatch = StopWatch(root)
        stopwatch.pack(side=tk.TOP)

        # Control Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(side=tk.TOP, pady=10)

        tk.Button(btn_frame, text='Start', command=stopwatch.start).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text='Stop', command=stopwatch.stop).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text='Reset', command=stopwatch.reset).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text='Quit', command=root.destroy).pack(side=tk.LEFT, padx=5)

        root.mainloop()
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == '__main__':
    main()
