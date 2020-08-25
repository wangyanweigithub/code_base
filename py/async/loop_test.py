#!/usr/bin/python
# coding: utf-8
import sys
from datetime import datetime
from threading import Thread, Timer
from event_loop import EventManager, NewEvent

EVENT_ARTICAL = "Event_Article"

class PublicAccout:
    def __init__(self, eventManager):
        self._eventManager = eventManager

    def WriteNewAritcal(self):
        event = NewEvent(type_=EVENT_ARTICAL)
        event.dict["artical"] = "how to write more pythonic code"
        self._eventManager.SendEvent(event)
        print("!!! New papers")

class Listener:
    def __init__(self, username):
        self._username = username

    def ReadArtical(self, event):
        print("%s recive new artical" % self._username)
        print("now reading the new artical: %s" % event.dict["artical"])

def test():
    listener1 = Listener("wang")
    listener2 = Listener("yan")
    eventManager = EventManager()

    eventManager.AddEventListener(EVENT_ARTICAL, listener1.ReadArtical)
    eventManager.AddEventListener(EVENT_ARTICAL, listener2.ReadArtical)
    eventManager.Start()

    putlicAcc = PublicAccout(eventManager)
    timer = Timer(2, putlicAcc.WriteNewAritcal)
    timer.start()
if __name__ == "__main__":
    test()
