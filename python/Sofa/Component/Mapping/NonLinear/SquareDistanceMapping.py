# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component SquareDistanceMapping

.. autofunction:: SquareDistanceMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class SquareDistanceMapping(Object):
    """Compute square edge extensions"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,mapForces: Optional[bool] = None,mapConstraints: Optional[bool] = None,mapMasses: Optional[bool] = None,mapMatrices: Optional[bool] = None,applyRestPosition: Optional[bool] = None,geometricStiffness: Optional[object] = None,showObjectScale: Optional[float] = None,showColor: Optional[object] = None):
        """Compute square edge extensions
        
        Args:
           applyRestPosition (bool):   set to true to apply this mapping to restPosition at init
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           geometricStiffness (object):   Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
-Stabilized: the exact geometric stiffness is approximated in order to improve stability
           listening (bool):   if true, handle the events, otherwise ignore the events
           mapConstraints (bool):   Are constraints mapped ?
           mapForces (bool):   Are forces mapped ?
           mapMasses (bool):   Are masses mapped ?
           mapMatrices (bool):   Are matrix explicit mapped?
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           showColor (object):   Color for object display. (default=[1.0,1.0,0.0,1.0])
           showObjectScale (float):   Scale for object display
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

    geometricStiffness: Data[object] 
    'Method used to compute the geometric stiffness:-None: geometric stiffness is not computed-Exact: the exact geometric stiffness is computed-Stabilized: the exact geometric stiffness is approximated in order to improve stability'

    showObjectScale: Data[float] 
    'Scale for object display'

    showColor: Data[object] 
    'Color for object display. (default=[1.0,1.0,0.0,1.0])'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the SquareDistanceMapping component"""

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

        geometricStiffness: Optional[object | LinkPath] = None 
        'Method used to compute the geometric stiffness:-None: geometric stiffness is not computed-Exact: the exact geometric stiffness is computed-Stabilized: the exact geometric stiffness is approximated in order to improve stability'

        showObjectScale: Optional[float | LinkPath] = None 
        'Scale for object display'

        showColor: Optional[object | LinkPath] = None 
        'Color for object display. (default=[1.0,1.0,0.0,1.0])'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return SquareDistanceMapping.Parameters()
