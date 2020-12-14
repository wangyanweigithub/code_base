from tornado.web import Application, RequestHandler
from tornado import ioloop


class Handler(RequestHandler):
    def get(self,*args):
        self.render("index.html")


def run():
    setting = [(r"/", Handler),debug=True]
    app = Application(*setting)
