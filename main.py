import os
import time

from queue import Queue
from threading import Thread

class TerminalFrame:
    # Made by Kaenova, https://github.com/kaenova
    def __init__(self, fps=None):
        self.base = """"""
        self.max_cols = os.get_terminal_size().columns
        self.max_lines = os.get_terminal_size().lines
        self.current_lines = 0 
        self.fps = fps
        self.data = []
        
        # Start print tick
        if self.fps != None:
            self.queue_stop = Queue()
            self.print_tick = Thread(target=self._tick_time, args=(self.data, self.queue_stop, fps))
            self.print_tick.start()
        
        
    def _update_screen_meta(self) -> int:
        if (self.max_lines < os.get_terminal_size().lines) or \
            (self.max_cols < os.get_terminal_size().columns):
            print("[ERROR] The Number of lines or columns for the latest " +
                  "saved line were not met the current size of terminal. "+
                  "Please make terminal screen larger")
            return 0 
        
        self.max_cols = os.get_terminal_size().columns
        self.max_lines = os.get_terminal_size().lines
        return 1
    
    def _clear(self):
        print(chr(27) + "[2J")
        # print("\033[H\033[J", end="")
        
    def _tick_time(self,stack:list, stop_q: Queue, fps:int):
        run = True
        last_out = """"""
        while run:
            start = time.time()
            time.sleep(1/fps)
            if len(stack) != 0:
                last_out = stack.pop()
            self._clear()  
            print(last_out)
            print("fps:", 1/(time.time() - start))
            print("Make sure to not change the winodw size")
            if not stop_q.empty():
                run = False 
        
    def print(self):
        if self.fps != None:
            for _ in range(self.max_lines - self.current_lines -3):
                self.base += "\n"
            self.data.append(self.base)
            return
        self._clear()
        print(self.base)
        
    def add_line(self, input: str):
        if not self._update_screen_meta():
            return
        if self.max_lines < self.current_lines:
            print("[ERROR] Reached the maximum line on terminal, please make "+
                  "terminal window longer.")
        if len(input) > self.max_cols:
            print("[ERROR] The length of input is more than the terminal width")
            return
        if type(input) != str:
            raise TypeError("Not a valid type, must a string")
        if self.current_lines != 0: self.base += "\n"
        self.base += input
        self.current_lines += 1
        
    def reset(self):
        self.base = """"""
        self.current_lines = 0
        
        
    # Stop print tick
    def stop(self):
        self.queue_stop.put(True)