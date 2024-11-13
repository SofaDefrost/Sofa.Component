# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component QuadularBendingSprings

.. autofunction:: QuadularBendingSprings

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class QuadularBendingSprings(Object):
    """Springs added to a quad mesh to prevent bending"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,stiffness: Optional[float] = None,damping: Optional[float] = None,edgeInfo: Optional[SofaArray] = None):
        """Springs added to a quad mesh to prevent bending
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           damping (float):   uniform damping for the all springs
           edgeInfo (SofaArray):   Internal edge data
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           stiffness (float):   uniform stiffness for the all springs
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

    stiffness: Data[float] 
    'uniform stiffness for the all springs'

    damping: Data[float] 
    'uniform damping for the all springs'

    edgeInfo: Data[SofaArray] 
    'Internal edge data'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the QuadularBendingSprings component"""

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

        stiffness: Optional[float | LinkPath] = None 
        'uniform stiffness for the all springs'

        damping: Optional[float | LinkPath] = None 
        'uniform damping for the all springs'

        edgeInfo: Optional[SofaArray | LinkPath] = None 
        'Internal edge data'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return QuadularBendingSprings.Parameters()
