#unit m/s
import math
CONST_SPEED_OF_LIGHT=299792458

class SpaceObject(object):
    """Objects contained in our universe including blackholes, galaxies,star,planets etc."""
    def __init__(self,objid,ra,dec,redshift=None):
        self.objid=objid
        self.ra=ra
        self.dec=dec
        self.redshift=redshift

    #+going away ,-for moving closer

    def velocityOfObject(self):
        return ((math.pow(self.redshift,2)+2*self.redshift)/\
                (math.pow(self.redshift,2)+2*self.redshift+2))*CONST_SPEED_OF_LIGHT