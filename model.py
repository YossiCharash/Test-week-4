from db import *

class Mission:
    def __init__(self, mission_date,name):
        self.mission_date = mission_date
        self.name = name

    def __str__(self):
        return self.name,self.mission_date


