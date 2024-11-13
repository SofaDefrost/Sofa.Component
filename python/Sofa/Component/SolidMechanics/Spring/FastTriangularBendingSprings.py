# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component FastTriangularBendingSprings

.. autofunction:: FastTriangularBendingSprings

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class FastTriangularBendingSprings(Object):
    """Springs added to a triangular mesh to prevent bending"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,bendingStiffness: Optional[float] = None,minDistValidity: Optional[float] = None,edgeInfo: Optional[SofaArray] = None):
        """Springs added to a triangular mesh to prevent bending
        
        Args:
           bbox (object):   this object bounding box
           bendingStiffness (float):   bending stiffness of the material
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           edgeInfo (SofaArray):   Internal edge data
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           minDistValidity (float):   Distance under which a spring is not valid
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
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

    isCompliance: Data[bool] 
    'Consider the component as a compliance, else as a stiffness'

    rayleighStiffness: Data[float] 
    'Rayleigh damping - stiffness matrix coefficient'

    bendingStiffness: Data[float] 
    'bending stiffness of the material'

    minDistValidity: Data[float] 
    'Distance under which a spring is not valid'

    edgeInfo: Data[SofaArray] 
    'Internal edge data'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the FastTriangularBendingSprings component"""

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

        isCompliance: Optional[bool | LinkPath] = None 
        'Consider the component as a compliance, else as a stiffness'

        rayleighStiffness: Optional[float | LinkPath] = None 
        'Rayleigh damping - stiffness matrix coefficient'

        bendingStiffness: Optional[float | LinkPath] = None 
        'bending stiffness of the material'

        minDistValidity: Optional[float | LinkPath] = None 
        'Distance under which a spring is not valid'

        edgeInfo: Optional[SofaArray | LinkPath] = None 
        'Internal edge data'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return FastTriangularBendingSprings.Parameters()
