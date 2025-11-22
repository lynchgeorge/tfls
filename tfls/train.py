from tfls.line import get_line_by_id
from tfls.custom_api import tfl_get


class Train:
    def __init__(self, from_station, to_station, line):
        self.line = line
        self.from_station = from_station
        self.to_station = to_station
        self.lat = 0
        self.long = 0
        self.set_location()

    def get_train_id(self):
        return self.train_id
    
    def set_train_id(self, train_id):
        self.train_id = train_id

    # Getter and Setter for line
    def get_line(self):
        return self.line

    def set_line(self, line):
        self.line = line

    # Getter and Setter for from_station
    def get_from_station(self):
        return self.from_station

    def set_from_station(self, station):
        self.from_station = station

    # Getter and Setter for to_station
    def get_to_station(self):
        return self.to_station

    def set_to_station(self, station):
        self.to_station = station

    def set_location(self):
        if not (self.from_station == None or self.to_station == None):
            self.lat = (self.from_station.lat + self.to_station.lat) / 2
            self.long = (self.from_station.lon + self.to_station.lon) / 2
        
        elif self.from_station == None and self.to_station != None:
            self.lat = self.to_station.lat
            self.long = self.to_station.lon
        
        elif self.from_station != None and self.to_station == None:
            self.lat = self.from_station.lat
            self.long = self.from_station.lon

def get_trains():
    victoria_trains = tfl_get("/Line/victoria/Arrivals")
    victoria_trains_parsed = []

    for train in victoria_trains:
        current_location = train["currentLocation"].lower()
        if "between" in current_location:
            current_location1 = current_location.replace("between ","")
            position = current_location1.split(" and ", 1)
            if "platform" in position[0]:
                position[0] = position[0].split('platform')[0]
            elif "platform" in position[1]:
                position[1] = position[1].split('platform')[0]
            victoria_trains_parsed.append(position)
        elif 'at platform' in current_location:
            continue
        elif 'at' in current_location:
            position = current_location.split(" ", 1)[1]
            if "platform" in position:
                position = position.split("platform")[0]
            victoria_trains_parsed.append([position, None])
        elif 'approaching' in current_location:
            position = current_location.split(" ", 1)[1]
            if "platform" in position:
                position = position.split("platform")[0]
            victoria_trains_parsed.append([None, position])

    victoria_train_objs = []
    for train in victoria_trains_parsed:
        victoria_line = get_line_by_id('victoria')
        if train[0] != None and train[1] != None:
            victoria_train_objs.append(Train(victoria_line.get_station(train[0]), victoria_line.get_station(train[1]), 'victoria'))
        elif train[0] == None:
            victoria_train_objs.append(Train(None, victoria_line.get_station(train[1]), 'victoria'))
        else:
            victoria_train_objs.append(Train(victoria_line.get_station(train[0]), None, 'victoria'))

    return victoria_train_objs

