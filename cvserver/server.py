# CV Server

from http.server import HTTPServer, BaseHTTPRequestHandler
from imgproc import detect_objects, convert_coord

class wserver(BaseHTTPRequestHandler):
    def do_GET(self):
        # GET request (unused)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

    def do_POST(self):
        # recieve image data
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # save recieved image to disk
        # print(post_data)
        # f = open('received.jpeg', 'wb')
        # f.write(post_data)
        # f.close()
        label, obj_coord = detect_objects(post_data, False)
        self.send_response(200)
        self.end_headers()
        if label == "":
            # reply no object found
            print("No object detected")
            self.wfile.write(bytes("none", 'utf-8'))
        else:
            # reply to request with object and coord
            print(label)
            self.wfile.write(bytes(label + " " + "".join(map(lambda x: str(x) + " ", convert_coord(obj_coord))), 'utf-8'))



httpd = HTTPServer(('your computers ip address', 8000), wserver)
httpd.serve_forever()