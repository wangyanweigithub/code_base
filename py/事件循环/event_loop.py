from queue import Queue, Empty
from threading import *


class EventManager(object):
    def __init__(self):
        self.event_queue = Queue()
        self.active = False
        self.handlers = {}
        self.thread = Thread(target=self.run)

    def run(self):
        while self.active:
            try:
                event = self.event_queue.get(block=True, timeout=1)
                self.event_process(event)
            except Empty:
                print("timeout 1 seconds")

    def event_process(self, event):
        if event.event_type in self.handlers:
            for handler in self.handlers[event.event_type]:
                handler(event)

    def start(self):
        self.active = True
        self.thread.start()

    def stop(self):
        self.active = False
        self.thread.join()

    def add_event_handler(self, event_type, handler):
        handlers = self.handlers.setdefault(event_type, [])
        if handler not in handlers:
            handlers.append(handler)

    def remove_event_handler(self, event, handler):
        if handler in self.handlers.get(event.event_type, []):
            self.handlers[event.event_type].remove(handler)

    def sent_event(self, event):
        self.event_queue.put(event)


class OneEvent(object):
    def __init__(self, event_type="one"):
        self.event_type = event_type
        self.data = {}
