from event_loop import EventManager, OneEvent


class Test_event(object):
    def setup_class(self):
        self.manager = EventManager()

    def teardown_class(self):
        self.manager.stop()

    def handler(self, event):
        print("handler process!!!:", event.event_type)

    def test_one(self):
        event = OneEvent() 
        self.manager.sent_event(event)
        self.manager.add_event_handler(event.event_type, self.handler)
        self.manager.start()
