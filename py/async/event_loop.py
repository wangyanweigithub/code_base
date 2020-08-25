from queue import Queue, Empty
from threading import *

class EventManager:

    def __init__(self):
        self._eventQueue = Queue()
        self._active = False
        self._thread = Thread(target=self._Run)
        self._handlers = {}

    def _Run(self):
        while self._active == True:
            try:
                event = self._eventQueue.get(block=True, timeout=1)
                self._EventProcess(event)
            except Empty:
                pass

    def _EventProcess(self, event):
        if event.type_ in self._handlers:
            for handler in self._handlers[event.type_]:
                handler(event)

    def Start(self):
        self._active = True
        self._thread.start()

    def Stop(self):
        self._active = False
        self._thread.join()

    def AddEventListener(self, type_, handler):
        handlerList = self._handlers.setdefault(type_,[])
        if handler not in handlerList:
            handlerList.append(handler)

    def RemoveEventListener(self, type_, handler):
        pass

    def SendEvent(self, event):
        self._eventQueue.put(event)

class NewEvent:
    def __init__(self, type_=None):
        self.type_ = type_
        self.dict = {}
