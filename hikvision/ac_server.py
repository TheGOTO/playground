import socketserver
import http.server
import logging
import cgi
import requests
import json

PORT = 9000

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.debug(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.debug(item)

        http.server.SimpleHTTPRequestHandler.do_GET(self)


        input_from_door=form.getvalue("AccessControllerEvent")
        input_as_json = json.loads(input_from_door)
        event=input_as_json["eventType"]

        print (event)

        if event=="heartBeat":
            x = requests.get('http://dom-iob:8087/set/0_userdata.0.Door.isOnline?value=true')
            logging.debug(x)
        #elif event == "AccessControllerEvent":
        else:
            logging.debug(input_as_json)

            with open("data.txt", "w") as file:
                for key in form.keys():
                   file.write(str(form.getvalue(str(key))) + ",")



Handler = ServerHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
