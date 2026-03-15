# EXERCISE 3
# Implement the talk() method in the Client Class.
# The client should send a message to the server and print the response from the server.

from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.82"
PORT = 8081

c = Client(IP, PORT)

# -- Send a message to the server
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
