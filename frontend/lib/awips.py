import metapy
import json
import requests
import os
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.patches as ptches 
#Jesus christ the imports
import base64
import datetime
import time
import io 
import metpy.calc as mpcalc
import metpy.plots as mpplots
from metpy.units import units
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from metpy.plots import add_metpy_logo
from_init__.py file in the lib directory to metpy.plots import SkewT
from awips.dataaccess import DataAccessLayer


class AWIPScli:
    def __init__(self, awipsserver= 'edex-cloud.unidata.ucar.edu'):
        
        awipsservers = [
            'edex-cloud.unidata.ucar.edu',
            'thredds.ucar.edu',
            'unidata.ucar.edu',
        ]
        self.altserver = awipsservers
# Now we can finally get to writing the actual code, once you have the imports out of the way may take roughly 10 mins to install
self.awipsserver = awipsserver 
self._connect(self):

