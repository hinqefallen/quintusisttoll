from mcrcon import MCRcon
import sys
import os
import fortune
address = "5.83.169.114"
password = "supersecretpassword"
with MCRcon(address, password, int(26805)) as rcon:
    for i in range (6000):
      text = fortune.get_random_fortune("/dadjokes")
      response = rcon.command(f"say DOFTD: {text}")
      print(f"{text} Nr: {i}")