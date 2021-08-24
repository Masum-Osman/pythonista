import tornado.ioloop
import tornado.web
import sys
import os

class MainHandler (tornado.web.RequestHandler):
    def get(self):
        self.write(f"Served from {os.getpid()}")

def make_app():
    return tornado.web.Application([
        (r"/balance", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()