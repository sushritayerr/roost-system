import geopy
from geopy import distance
import numpy as np
from roosts.utils.sunset_util import get_sunrise_time
from roosts.utils.nexrad_util import NEXRAD_LOCATIONS

def euclid_distance(p, q):
    return np.sqrt(np.sum((p - q) * (p - q), axis = 1))

def is_box_nested(box1, box2):
    # check if box1 is nested in box2
    if box1[0] >= box2[0] and box1[1] >= box2[1] and box1[2] <= box2[2] and box1[3] <= box2[3]:
        return True
    return False

def geo_dist_km(coor1, coor2):
    return distance.distance(coor1, coor2).km

def sunrise_time(radar_name):
    station = radar_name[:4]
    year = radar_name[4:8]
    month = radar_name[8:10]
    day = radar_name[10:12]
    date = '{:s}-{:s}-{:s}'.format(year, month, day)
    rising_time = get_sunrise_time(station, date)
    return rising_time

def cart2pol(x, y):
    dis = np.sqrt(x**2 + y**2)
    angle = np.arctan2(y, x)
    return angle, dis

def rad2deg(angle):
    return angle * 180. / np.pi

def pol2cmp(angle):
    bearing = rad2deg(np.pi / 2 - angle)
    bearing = np.mod(bearing, 360)
    return bearing 

def get_roost_coor(roost_xy, station_xy, station_name):
    """ 
        Convert from image coordinates to geographic coordinates

        Args:
            roost_xy: image coordinates of roost center
            station_xy: image coordinates of station 
            station_name: name of station, e.g., KDOX

        Return:
            longitude, latitide of roost center
    """
    station_lat, station_lon = NEXRAD_LOCATIONS[station_name]["lat"], NEXRAD_LOCATIONS[station_name]["lon"]
    angle, dis = cart2pol(roost_xy[0]-station_xy[0], roost_xy[1]-station_xy[1])
    bearing = pol2cmp(angle)
    origin = geopy.Point(station_lat, station_lon)
    des = distance.distance(kilometers=dis / 1000.).destination(origin, bearing) 
    return des[1], des[0] # in order of lon and lat
