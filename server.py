import os

import cherrypy

"""
This is a simple Battlesnake server written in Python.
"""


class Battlesnake(object):
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        
        return {
            "apiversion": "1",
            "author": "DONALD G",
            "color": "#3E338F",
            "head": "shac-gamer",
            "tail": "shac-mouse",
        }

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def start(self):
        
        data = cherrypy.request.json

        print("START")
        return "ok"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        
        data = cherrypy.request.json
        
        move = "left"

        if data["you"]["head"]["x"] == 0:
            move = "up"
        if data["you"]["head"]["y"] == 10:
            move = "right"
        if data["you"]["head"]["x"] == 10:
            move = "down"
        if data["you"]["head"]["y"] == 0:
            move = "left"

        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        
        data = cherrypy.request.json

        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8080")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)
