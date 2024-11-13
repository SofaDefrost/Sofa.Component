# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component TubularMapping

.. autofunction:: TubularMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class TubularMapping(Object):
    """Create a Tube around rigid points"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,mapForces: Optional[bool] = None,mapConstraints: Optional[bool] = None,mapMasses: Optional[bool] = None,mapMatrices: Optional[bool] = None,applyRestPosition: Optional[bool] = None,nbPointsOnEachCircle: Optional[int] = None,radius: Optional[float] = None,peak: Optional[int] = None):
        """Create a Tube around rigid points
        
        Args:
           applyRestPosition (bool):   set to true to apply this mapping to restPosition at init
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           listening (bool):   if true, handle the events, otherwise ignore the events
           mapConstraints (bool):   Are constraints mapped ?
           mapForces (bool):   Are forces mapped ?
           mapMasses (bool):   Are masses mapped ?
           mapMatrices (bool):   Are matrix explicit mapped?
           name (str):   object name
           nbPointsOnEachCircle (int):   Discretization of created circles
           peak (int):   =0 no peak, =1 peak on the first segment =2 peak on the two first segment, =-1 peak on the last segment
           printLog (bool):   if true, emits extra messages at runtime.
           radius (float):   Radius of created circles
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

    nbPointsOnEachCircle: Data[int] 
    'Discretization of created circles'

    radius: Data[float] 
    'Radius of created circles'

    peak: Data[int] 
    '=0 no peak, =1 peak on the first segment =2 peak on the two first segment, =-1 peak on the last segment'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the TubularMapping component"""

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

        nbPointsOnEachCircle: Optional[int | LinkPath] = None 
        'Discretization of created circles'

        radius: Optional[float | LinkPath] = None 
        'Radius of created circles'

        peak: Optional[int | LinkPath] = None 
        '=0 no peak, =1 peak on the first segment =2 peak on the two first segment, =-1 peak on the last segment'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return TubularMapping.Parameters()
