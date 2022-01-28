from main import TerminalFrame
import time
import os


terminal  = TerminalFrame(fps=60)
for i in range(10000):
    time.sleep(0.01)
    terminal.add_line("Hello")
    terminal.add_line("Bruh")

    terminal.add_line("=" * (i%(os.get_terminal_size().columns) - 20))
    terminal.add_line("=" * (i%(os.get_terminal_size().columns) - 40))
    terminal.add_line("=" * (i%(os.get_terminal_size().columns) - 50))
    terminal.add_line(f"{i}")
    terminal.print()
    terminal.reset()
terminal.stop()
del terminal