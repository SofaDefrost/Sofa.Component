# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component BeamLinearMapping

.. autofunction:: BeamLinearMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class BeamLinearMapping(Object):
    """Set the positions and velocities of points attached to a beam using linear interpolation between DOFs"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,mapForces: Optional[bool] = None,mapConstraints: Optional[bool] = None,mapMasses: Optional[bool] = None,mapMatrices: Optional[bool] = None,applyRestPosition: Optional[bool] = None,localCoord: Optional[bool] = None):
        """Set the positions and velocities of points attached to a beam using linear interpolation between DOFs
        
        Args:
           applyRestPosition (bool):   set to true to apply this mapping to restPosition at init
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           listening (bool):   if true, handle the events, otherwise ignore the events
           localCoord (bool):   true if initial coordinates are in the beam local coordinate system (i.e. a point at (10,0,0) is on the DOF number 10, whereas if this is false it is at whatever position on the beam where the distance from the initial DOF is 10)
           mapConstraints (bool):   Are constraints mapped ?
           mapForces (bool):   Are forces mapped ?
           mapMasses (bool):   Are masses mapped ?
           mapMatrices (bool):   Are matrix explicit mapped?
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           tags (object):   list of the subsets the objet belongs to
           template (str): the type of degree of freedom
        """
        ...

    name: Data[str] 
    'object name'

    printLog: Data[bool] 
    'if true, emits extra messages at runtime.'

    tags: Data[object] 
    'list of the subsets the objet belongs to'

    bbox: Data[object] 
    'this object bounding box'

    componentState: Data[object] 
    'The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).'

    listening: Data[bool] 
    'if true, handle the events, otherwise ignore the events'

    mapForces: Data[bool] 
    'Are forces mapped ?'

    mapConstraints: Data[bool] 
    'Are constraints mapped ?'

    mapMasses: Data[bool] 
    'Are masses mapped ?'

    mapMatrices: Data[bool] 
    'Are matrix explicit mapped?'

    applyRestPosition: Data[bool] 
    'set to true to apply this mapping to restPosition at init'

    localCoord: Data[bool] 
    'true if initial coordinates are in the beam local coordinate system (i.e. a point at (10,0,0) is on the DOF number 10, whereas if this is false it is at whatever position on the beam where the distance from the initial DOF is 10)'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the BeamLinearMapping component"""

        name: Optional[str | LinkPath] = None 
        'object name'

        printLog: Optional[bool | LinkPath] = None 
        'if true, emits extra messages at runtime.'

        tags: Optional[object | LinkPath] = None 
        'list of the subsets the objet belongs to'

        bbox: Optional[object | LinkPath] = None 
        'this object bounding box'

        componentState: Optional[object | LinkPath] = None 
        'The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).'

        listening: Optional[bool | LinkPath] = None 
        'if true, handle the events, otherwise ignore the events'

        mapForces: Optional[bool | LinkPath] = None 
        'Are forces mapped ?'

        mapConstraints: Optional[bool | LinkPath] = None 
        'Are constraints mapped ?'

        mapMasses: Optional[bool | LinkPath] = None 
        'Are masses mapped ?'

        mapMatrices: Optional[bool | LinkPath] = None 
        'Are matrix explicit mapped?'

        applyRestPosition: Optional[bool | LinkPath] = None 
        'set to true to apply this mapping to restPosition at init'

        localCoord: Optional[bool | LinkPath] = None 
        'true if initial coordinates are in the beam local coordinate system (i.e. a point at (10,0,0) is on the DOF number 10, whereas if this is false it is at whatever position on the beam where the distance from the initial DOF is 10)'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return BeamLinearMapping.Parameters()
