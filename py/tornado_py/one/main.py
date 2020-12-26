from tornado import web
from tornado import ioloop
from tornado import log


class MainHandler(web.RequestHandler):
    def initialize(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def get(self):
        print("get argums", self.get_argument("name", None))

        print("get path args", self.path_args)

    def post(self):
        print("post body:", self.get_body_arguments('name'))


class NumHandler(web.RequestHandler):
    def get():
        pass


def main():
    handlers = [(r"/.*", MainHandler), (r"/(\d*)", NumHandler)]
    setting = dict(debug=True)
    app = web.Application(handlers, **setting)
    app.listen(8888)
    ioloop.IOLoop.current().start()


main()
