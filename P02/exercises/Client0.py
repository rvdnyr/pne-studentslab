# Client and Seq classes modules
# Class for sending messages to a server

import socket
from pathlib import Path

class Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def ping(self):
        print("OK!")

    def __str__(self):
        return f"Connection to SERVER at {self.ip}, PORT: {self.port}"

    def talk(self, msg):

        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data
        s.send(str.encode(msg))

        # Receive data
        response = s.recv(2048).decode("utf-8")

        # Close the socket
        s.close()

        # Return the response
        return response


class Seq:

    def __init__(self, strbases=None):
        self.strbases = strbases
        if strbases is not None:
            is_valid = False
            for i in strbases:
                if i in ["A", "C", "G", "T"]:
                    is_valid = True
                else:
                    is_valid = False
            if is_valid:
                print("New sequence created!")
            else:
                print("INVALID sequence")
        else:
            print("NULL sequence created")

    def __str__(self):
        return self.strbases

    def read_fasta(self, filename):
        lines = filename.split('\n')
        sequence = ""
        for line in lines:
            if not line.startswith('>'):
                sequence += line.strip()
        return sequence
