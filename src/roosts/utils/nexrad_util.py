# https://github.com/darkecology/cajun/blob/master/aws/nexrad_util.py commit 7863f13

NEXRAD_LOCATIONS = {
    "KABR": {'lat': 45.45583,  'lon': -98.41306,   'elev': 1302,   'tz': 'America/Chicago'},
    "KABX": {'lat': 35.14972,  'lon': -106.82333,  'elev': 5870,   'tz': 'America/Denver'},
    "KAKQ": {'lat': 36.98389,  'lon': -77.0075,    'elev': 112,    'tz': 'America/New_York'},
    "KAMA": {'lat': 35.23333,  'lon': -101.70889,  'elev': 3587,   'tz': 'America/Chicago'},
    "KAMX": {'lat': 25.61056,  'lon': -80.41306,   'elev': 14,     'tz': 'America/New_York'},
    "KAPX": {'lat': 44.90722,  'lon': -84.71972,   'elev': 1464,   'tz': 'America/Detroit'},
    "KARX": {'lat': 43.82278,  'lon': -91.19111,   'elev': 1276,   'tz': 'America/Chicago'},
    "KATX": {'lat': 48.19472,  'lon': -122.49444,  'elev': 494,    'tz': 'America/Los_Angeles'},
    "KBBX": {'lat': 39.49611,  'lon': -121.63167,  'elev': 173,    'tz': 'America/Los_Angeles'},
    "KBGM": {'lat': 42.19972,  'lon': -75.985,     'elev': 1606,   'tz': 'America/New_York'},
    "KBHX": {'lat': 40.49833,  'lon': -124.29194,  'elev': 2402,   'tz': 'America/Los_Angeles'},
    "KBIS": {'lat': 46.77083,  'lon': -100.76028,  'elev': 1658,   'tz': 'America/Chicago'},
    "KBLX": {'lat': 45.85389,  'lon': -108.60611,  'elev': 3598,   'tz': 'America/Denver'},
    "KBMX": {'lat': 33.17194,  'lon': -86.76972,   'elev': 645,    'tz': 'America/Chicago'},
    "KBOX": {'lat': 41.95583,  'lon': -71.1375,    'elev': 118,    'tz': 'America/New_York'},
    "KBRO": {'lat': 25.91556,  'lon': -97.41861,   'elev': 23,     'tz': 'America/Chicago'},
    "KBUF": {'lat': 42.94861,  'lon': -78.73694,   'elev': 693,    'tz': 'America/New_York'},
    "KBYX": {'lat': 24.59694,  'lon': -81.70333,   'elev': 8,      'tz': 'America/New_York'},
    "KCAE": {'lat': 33.94861,  'lon': -81.11861,   'elev': 231,    'tz': 'America/New_York'},
    "KCBW": {'lat': 46.03917,  'lon': -67.80694,   'elev': 746,    'tz': 'America/New_York'},
    "KCBX": {'lat': 43.49083,  'lon': -116.23444,  'elev': 3061,   'tz': 'America/Boise'},
    "KCCX": {'lat': 40.92306,  'lon': -78.00389,   'elev': 2405,   'tz': 'America/New_York'},
    "KCLE": {'lat': 41.41306,  'lon': -81.86,      'elev': 763,    'tz': 'America/New_York'},
    "KCLX": {'lat': 32.65556,  'lon': -81.04222,   'elev': 97,     'tz': 'America/New_York'},
    "KCRI": {'lat': 35.2383,   'lon': -97.4602,    'elev': 1201,   'tz': 'America/Chicago'},
    "KCRP": {'lat': 27.78389,  'lon': -97.51083,   'elev': 45,     'tz': 'America/Chicago'},
    "KCXX": {'lat': 44.51111,  'lon': -73.16639,   'elev': 317,    'tz': 'America/New_York'},
    "KCYS": {'lat': 41.15194,  'lon': -104.80611,  'elev': 6128,   'tz': 'America/Denver'},
    "KDAX": {'lat': 38.50111,  'lon': -121.67667,  'elev': 30,     'tz': 'America/Los_Angeles'},
    "KDDC": {'lat': 37.76083,  'lon': -99.96833,   'elev': 2590,   'tz': 'America/Chicago'},
    "KDFX": {'lat': 29.2725,   'lon': -100.28028,  'elev': 1131,   'tz': 'America/Chicago'},
    "KDGX": {'lat': 32.28,     'lon': -89.98444,   'elev': -99999, 'tz': 'America/Chicago'},
    "KDIX": {'lat': 39.94694,  'lon': -74.41111,   'elev': 149,    'tz': 'America/New_York'},
    "KDLH": {'lat': 46.83694,  'lon': -92.20972,   'elev': 1428,   'tz': 'America/Chicago'},
    "KDMX": {'lat': 41.73111,  'lon': -93.72278,   'elev': 981,    'tz': 'America/Chicago'},
    "KDOX": {'lat': 38.82556,  'lon': -75.44,      'elev': 50,     'tz': 'America/New_York'},
    "KDTX": {'lat': 42.69972,  'lon': -83.47167,   'elev': 1072,   'tz': 'America/Detroit'},
    "KDVN": {'lat': 41.61167,  'lon': -90.58083,   'elev': 754,    'tz': 'America/Chicago'},
    "KDYX": {'lat': 32.53833,  'lon': -99.25417,   'elev': 1517,   'tz': 'America/Chicago'},
    "KEAX": {'lat': 38.81028,  'lon': -94.26417,   'elev': 995,    'tz': 'America/Chicago'},
    "KEMX": {'lat': 31.89361,  'lon': -110.63028,  'elev': 5202,   'tz': 'America/Phoenix'},
    "KENX": {'lat': 42.58639,  'lon': -74.06444,   'elev': 1826,   'tz': 'America/New_York'},
    "KEOX": {'lat': 31.46028,  'lon': -85.45944,   'elev': 434,    'tz': 'America/Chicago'},
    "KEPZ": {'lat': 31.87306,  'lon': -106.6975,   'elev': 4104,   'tz': 'America/Denver'},
    "KESX": {'lat': 35.70111,  'lon': -114.89139,  'elev': 4867,   'tz': 'America/Los_Angeles'},
    "KEVX": {'lat': 30.56417,  'lon': -85.92139,   'elev': 140,    'tz': 'America/Chicago'},
    "KEWX": {'lat': 29.70361,  'lon': -98.02806,   'elev': 633,    'tz': 'America/Chicago'},
    "KEYX": {'lat': 35.09778,  'lon': -117.56,     'elev': 2757,   'tz': 'America/Los_Angeles'},
    "KFCX": {'lat': 37.02417,  'lon': -80.27417,   'elev': 2868,   'tz': 'America/New_York'},
    "KFDR": {'lat': 34.36222,  'lon': -98.97611,   'elev': 1267,   'tz': 'America/Chicago'},
    "KFDX": {'lat': 34.63528,  'lon': -103.62944,  'elev': 4650,   'tz': 'America/Denver'},
    "KFFC": {'lat': 33.36333,  'lon': -84.56583,   'elev': 858,    'tz': 'America/New_York'},
    "KFSD": {'lat': 43.58778,  'lon': -96.72889,   'elev': 1430,   'tz': 'America/Chicago'},
    "KFSX": {'lat': 34.57444,  'lon': -111.19833,  'elev': -99999, 'tz': 'America/Phoenix'},
    "KFTG": {'lat': 39.78667,  'lon': -104.54528,  'elev': 5497,   'tz': 'America/Denver'},
    "KFWS": {'lat': 32.57278,  'lon': -97.30278,   'elev': 683,    'tz': 'America/Chicago'},
    "KGGW": {'lat': 48.20639,  'lon': -106.62417,  'elev': 2276,   'tz': 'America/Denver'},
    "KGJX": {'lat': 39.06222,  'lon': -108.21306,  'elev': 9992,   'tz': 'America/Denver'},
    "KGLD": {'lat': 39.36694,  'lon': -101.7,      'elev': 3651,   'tz': 'America/Denver'},
    "KGRB": {'lat': 44.49833,  'lon': -88.11111,   'elev': 682,    'tz': 'America/Chicago'},
    "KGRK": {'lat': 30.72167,  'lon': -97.38278,   'elev': 538,    'tz': 'America/Chicago'},
    "KGRR": {'lat': 42.89389,  'lon': -85.54472,   'elev': 778,    'tz': 'America/Detroit'},
    "KGSP": {'lat': 34.88306,  'lon': -82.22028,   'elev': 940,    'tz': 'America/New_York'},
    "KGWX": {'lat': 33.89667,  'lon': -88.32889,   'elev': 476,    'tz': 'America/Chicago'},
    "KGYX": {'lat': 43.89139,  'lon': -70.25694,   'elev': 409,    'tz': 'America/New_York'},
    "KHDX": {'lat': 33.07639,  'lon': -106.12222,  'elev': 4222,   'tz': 'America/Denver'},
    "KHGX": {'lat': 29.47194,  'lon': -95.07889,   'elev': 18,     'tz': 'America/Chicago'},
    "KHNX": {'lat': 36.31417,  'lon': -119.63111,  'elev': 243,    'tz': 'America/Los_Angeles'},
    "KHPX": {'lat': 36.73667,  'lon': -87.285,     'elev': 576,    'tz': 'America/Chicago'},
    "KHTX": {'lat': 34.93056,  'lon': -86.08361,   'elev': 1760,   'tz': 'America/Chicago'},
    "KICT": {'lat': 37.65444,  'lon': -97.4425,    'elev': 1335,   'tz': 'America/Chicago'},
    "KICX": {'lat': 37.59083,  'lon': -112.86222,  'elev': 10600,  'tz': 'America/Denver'},
    "KILN": {'lat': 39.42028,  'lon': -83.82167,   'elev': 1056,   'tz': 'America/New_York'},
    "KILX": {'lat': 40.15056,  'lon': -89.33667,   'elev': 582,    'tz': 'America/Chicago'},
    "KIND": {'lat': 39.7075,   'lon': -86.28028,   'elev': 790,    'tz': 'America/Indiana/Indianapolis'},
    "KINX": {'lat': 36.175,    'lon': -95.56444,   'elev': 668,    'tz': 'America/Chicago'},
    "KIWA": {'lat': 33.28917,  'lon': -111.66917,  'elev': 1353,   'tz': 'America/Phoenix'},
    "KIWX": {'lat': 41.40861,  'lon': -85.7,       'elev': 960,    'tz': 'America/Indiana/Indianapolis'},
    "KJAN": {'lat': 32.3205,   'lon': -90.0777,    'elev': 330,    'tz': 'America/Chicago'},
    "KJAX": {'lat': 30.48444,  'lon': -81.70194,   'elev': 33,     'tz': 'America/New_York'},
    "KJGX": {'lat': 32.675,    'lon': -83.35111,   'elev': 521,    'tz': 'America/New_York'},
    "KJKL": {'lat': 37.59083,  'lon': -83.31306,   'elev': 1364,   'tz': 'America/New_York'},
    "KLBB": {'lat': 33.65417,  'lon': -101.81361,  'elev': 3259,   'tz': 'America/Chicago'},
    "KLCH": {'lat': 30.125,    'lon': -93.21583,   'elev': 13,     'tz': 'America/Chicago'},
    "KLGX": {'lat': 47.1158,   'lon': -124.1069,   'elev': 252,    'tz': 'America/Los_Angeles'},
    "KLIX": {'lat': 30.33667,  'lon': -89.82528,   'elev': 24,     'tz': 'America/Chicago'},
    "KLNX": {'lat': 41.95778,  'lon': -100.57583,  'elev': 2970,   'tz': 'America/Chicago'},
    "KLOT": {'lat': 41.60444,  'lon': -88.08472,   'elev': 663,    'tz': 'America/Chicago'},
    "KLRX": {'lat': 40.73972,  'lon': -116.80278,  'elev': 6744,   'tz': 'America/Los_Angeles'},
    "KLSX": {'lat': 38.69889,  'lon': -90.68278,   'elev': 608,    'tz': 'America/Chicago'},
    "KLTX": {'lat': 33.98917,  'lon': -78.42917,   'elev': 64,     'tz': 'America/New_York'},
    "KLVX": {'lat': 37.97528,  'lon': -85.94389,   'elev': 719,    'tz': 'America/New_York'},
    "KLWX": {'lat': 38.97628,  'lon': -77.48751,   'elev': -99999, 'tz': 'America/New_York'},
    "KLZK": {'lat': 34.83639,  'lon': -92.26194,   'elev': 568,    'tz': 'America/Chicago'},
    "KMAF": {'lat': 31.94333,  'lon': -102.18889,  'elev': 2868,   'tz': 'America/Chicago'},
    "KMAX": {'lat': 42.08111,  'lon': -122.71611,  'elev': 7513,   'tz': 'America/Los_Angeles'},
    "KMBX": {'lat': 48.3925,   'lon': -100.86444,  'elev': 1493,   'tz': 'America/Chicago'},
    "KMHX": {'lat': 34.77583,  'lon': -76.87639,   'elev': 31,     'tz': 'America/New_York'},
    "KMKX": {'lat': 42.96778,  'lon': -88.55056,   'elev': 958,    'tz': 'America/Chicago'},
    "KMLB": {'lat': 28.11306,  'lon': -80.65444,   'elev': 99,     'tz': 'America/New_York'},
    "KMOB": {'lat': 30.67944,  'lon': -88.23972,   'elev': 208,    'tz': 'America/Chicago'},
    "KMPX": {'lat': 44.84889,  'lon': -93.56528,   'elev': 946,    'tz': 'America/Chicago'},
    "KMQT": {'lat': 46.53111,  'lon': -87.54833,   'elev': 1411,   'tz': 'America/Detroit'},
    "KMRX": {'lat': 36.16833,  'lon': -83.40194,   'elev': 1337,   'tz': 'America/New_York'},
    "KMSX": {'lat': 47.04111,  'lon': -113.98611,  'elev': 7855,   'tz': 'America/Denver'},
    "KMTX": {'lat': 41.26278,  'lon': -112.44694,  'elev': 6460,   'tz': 'America/Denver'},
    "KMUX": {'lat': 37.15528,  'lon': -121.8975,   'elev': 3469,   'tz': 'America/Los_Angeles'},
    "KMVX": {'lat': 47.52806,  'lon': -97.325,     'elev': 986,    'tz': 'America/Chicago'},
    "KMXX": {'lat': 32.53667,  'lon': -85.78972,   'elev': 400,    'tz': 'America/Chicago'},
    "KNKX": {'lat': 32.91889,  'lon': -117.04194,  'elev': 955,    'tz': 'America/Los_Angeles'},
    "KNQA": {'lat': 35.34472,  'lon': -89.87333,   'elev': 282,    'tz': 'America/Chicago'},
    "KOAX": {'lat': 41.32028,  'lon': -96.36639,   'elev': 1148,   'tz': 'America/Chicago'},
    "KOHX": {'lat': 36.24722,  'lon': -86.5625,    'elev': 579,    'tz': 'America/Chicago'},
    "KOKX": {'lat': 40.86556,  'lon': -72.86444,   'elev': 85,     'tz': 'America/New_York'},
    "KOTX": {'lat': 47.68056,  'lon': -117.62583,  'elev': 2384,   'tz': 'America/Los_Angeles'},
    "KPAH": {'lat': 37.06833,  'lon': -88.77194,   'elev': 392,    'tz': 'America/Chicago'},
    "KPBZ": {'lat': 40.53167,  'lon': -80.21833,   'elev': 1185,   'tz': 'America/New_York'},
    "KPDT": {'lat': 45.69056,  'lon': -118.85278,  'elev': 1515,   'tz': 'America/Los_Angeles'},
    "KPOE": {'lat': 31.15528,  'lon': -92.97583,   'elev': 408,    'tz': 'America/Chicago'},
    "KPUX": {'lat': 38.45944,  'lon': -104.18139,  'elev': 5249,   'tz': 'America/Denver'},
    "KRAX": {'lat': 35.66528,  'lon': -78.49,      'elev': 348,    'tz': 'America/New_York'},
    "KRGX": {'lat': 39.75417,  'lon': -119.46111,  'elev': 8299,   'tz': 'America/Los_Angeles'},
    "KRIW": {'lat': 43.06611,  'lon': -108.47667,  'elev': 5568,   'tz': 'America/Denver'},
    "KRLX": {'lat': 38.31194,  'lon': -81.72389,   'elev': 1080,   'tz': 'America/New_York'},
    "KRTX": {'lat': 45.715,    'lon': -122.96417,  'elev': -99999, 'tz': 'America/Los_Angeles'},
    "KSFX": {'lat': 43.10583,  'lon': -112.68528,  'elev': 4474,   'tz': 'America/Boise'},
    "KSGF": {'lat': 37.23528,  'lon': -93.40028,   'elev': 1278,   'tz': 'America/Chicago'},
    "KSHV": {'lat': 32.45056,  'lon': -93.84111,   'elev': 273,    'tz': 'America/Chicago'},
    "KSJT": {'lat': 31.37111,  'lon': -100.49222,  'elev': 1890,   'tz': 'America/Chicago'},
    "KSOX": {'lat': 33.81778,  'lon': -117.635,    'elev': 3027,   'tz': 'America/Los_Angeles'},
    "KSRX": {'lat': 35.29056,  'lon': -94.36167,   'elev': -99999, 'tz': 'America/Chicago'},
    "KTBW": {'lat': 27.70528,  'lon': -82.40194,   'elev': 41,     'tz': 'America/New_York'},
    "KTFX": {'lat': 47.45972,  'lon': -111.38444,  'elev': 3714,   'tz': 'America/Denver'},
    "KTLH": {'lat': 30.3975,   'lon': -84.32889,   'elev': 63,     'tz': 'America/New_York'},
    "KTLX": {'lat': 35.33306,  'lon': -97.2775,    'elev': 1213,   'tz': 'America/Chicago'},
    "KTWX": {'lat': 38.99694,  'lon': -96.2325,    'elev': 1367,   'tz': 'America/Chicago'},
    "KTYX": {'lat': 43.75583,  'lon': -75.68,      'elev': 1846,   'tz': 'America/New_York'},
    "KUDX": {'lat': 44.125,    'lon': -102.82944,  'elev': 3016,   'tz': 'America/Denver'},
    "KUEX": {'lat': 40.32083,  'lon': -98.44167,   'elev': 1976,   'tz': 'America/Chicago'},
    "2023": {'lat': 30.89,     'lon': -83.00194,   'elev': 178,    'tz': 'America/New_York'},
    "KVBX": {'lat': 34.83806,  'lon': -120.39583,  'elev': 1233,   'tz': 'America/Los_Angeles'},
    "KVNX": {'lat': 36.74083,  'lon': -98.1275,    'elev': 1210,   'tz': 'America/Chicago'},
    "KVTX": {'lat': 34.41167,  'lon': -119.17861,  'elev': 2726,   'tz': 'America/Los_Angeles'},
    "KVWX": {'lat': 38.26,     'lon': -87.7247,    'elev': -99999, 'tz': 'America/Chicago'},
    "KYUX": {'lat': 32.49528,  'lon': -114.65583,  'elev': 174,    'tz': 'America/Phoenix'},
    "LPLA": {'lat': 38.73028,  'lon': -27.32167,   'elev': 3334,   'tz': 'Atlantic/Azores'},
    "PABC": {'lat': 60.79278,  'lon': -161.87417,  'elev': 162,    'tz': 'America/Anchorage'},
    "PACG": {'lat': 56.85278,  'lon': -135.52917,  'elev': 270,    'tz': 'America/Sitka'},
    "PAEC": {'lat': 64.51139,  'lon': -165.295,    'elev': 54,     'tz': 'America/Nome'},
    "PAHG": {'lat': 60.725914, 'lon': -151.35146,  'elev': 243,    'tz': 'America/Anchorage'},
    "PAIH": {'lat': 59.46194,  'lon': -146.30111,  'elev': 67,     'tz': 'America/Anchorage'},
    "PAKC": {'lat': 58.67944,  'lon': -156.62944,  'elev': 63,     'tz': 'America/Anchorage'},
    "PAPD": {'lat': 65.03556,  'lon': -147.49917,  'elev': 2593,   'tz': 'America/Anchorage'},
    "PGUA": {'lat': 13.45444,  'lon': 144.80833,   'elev': 264,    'tz': 'Pacific/Guam'},
    "PHKI": {'lat': 21.89417,  'lon': -159.55222,  'elev': 179,    'tz': 'Pacific/Honolulu'},
    "PHKM": {'lat': 20.12556,  'lon': -155.77778,  'elev': 3812,   'tz': 'Pacific/Honolulu'},
    "PHMO": {'lat': 21.13278,  'lon': -157.18,     'elev': 1363,   'tz': 'Pacific/Honolulu'},
    "PHWA": {'lat': 19.095,    'lon': -155.56889,  'elev': 1370,   'tz': 'Pacific/Honolulu'},
    "RKJK": {'lat': 35.92417,  'lon': 126.62222,   'elev': 78,     'tz': 'Asia/Seoul'},
    "RKSG": {'lat': 36.95972,  'lon': 127.01833,   'elev': 52,     'tz': 'Asia/Seoul'},
    "RODN": {'lat': 26.30194,  'lon': 127.90972,   'elev': 218,    'tz': 'Asia/Tokyo'},
    "TJUA": {'lat': 18.1175,   'lon': -66.07861,   'elev': 2794,   'tz': 'America/Puerto_Rico'},
}

# Regions Dictionary, To Be Filled with list of stations by region.
STATION_REGIONS = {
    "Birdcast"      : ["KCLE", "KBUF", "KTYX"],
    "my_region"     : ["KDOX", "KLIX", "KBGM", "KLCH"],
    "north_east"    : [
        "KBGM", "KBOX", "KBUF", "KCBW", "KCCX", "KCXX", "KDIX", "KDOX", "KENX", "KGYX", "KLWX", "KOKX", "KTYX"
    ],
    "east"          : [
        "KILX", "KLCH", "KMXX", "KHTX", "KJKL", "KLSX", "KCXX", "KDTX", "KMQT", "KSHV",
        "KFSD", "KCAE", "KBYX", "KDLH", "KNQA", "KRAX", "KBRO", "KLTX", "KMPX", "KICT",
        "KTLX", "KVAX", "KTLH", "KMHX", "KTBW", "KILN", "KTYX", "KLZK", "KMRX", "KOKX",
        "KIND", "KDIX", "KBMX", "KMKX", "KEVX", "KGWX", "KEOX", "KLIX", "KPAH", "KINX",
        "KSRX", "KAMX", "KGYX", "KPBZ", "KENX", "KFCX", "KTWX", "KLOT", "KAPX", "KJGX",
        "KHPX", "KDGX", "KLWX", "KBOX", "KFWS", "KDOX", "KARX", "KIWX", "KOHX", "KMLB",
        "KCLX", "KRLX", "KOAX", "KBUF", "KCLE", "KCRP", "KVWX", "KGRK", "KJAX", "KFFC",
        "KDVN", "KMOB", "KSGF", "KCCX", "KGSP", "KDMX", "KBGM", "KPOE", "KEAX", "KGRB",
        "KHGX", "KMVX", "KLVX", "KGRR", "KAKQ", "KCBW"
    ],
    "all"           : NEXRAD_LOCATIONS.keys(),
    "korea"         : ["RKSG", "RKJK"],
    "japan"         : ["RODN"],
    "alaska"        : ["PAEC", "PAPD", "PABC", "PAHG", "PAKC", "PAIH", "PACG"],
    "guam"          : ["PGUA"],
    "hawaii"        : ["PHKI", "PHMO", "PHKM", "PHWA"],
    "puerto_rico"   : ["TJUA"],
    "azores"        : ["LPLA"],
    "continental"   : [key for key in NEXRAD_LOCATIONS.keys() if key[0] == 'K']
}

def get_stations(region):
    stations = STATION_REGIONS.get(region)
    if stations is None:
        if region in NEXRAD_LOCATIONS:
            return [region]
        else:
            raise ValueError
    else:
        return stations