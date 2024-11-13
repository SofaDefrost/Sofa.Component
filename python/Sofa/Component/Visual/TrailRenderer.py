# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component TrailRenderer

.. autofunction:: TrailRenderer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class TrailRenderer(Object):
    """Render a trail behind particles"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,enable: Optional[bool] = None,position: Optional[SofaArray] = None,nbSteps: Optional[int] = None,color: Optional[object] = None,thickness: Optional[float] = None):
        """Render a trail behind particles
        
        Args:
           bbox (object):   this object bounding box
           color (object):   Color of the trail
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           enable (bool):   Display the object or not
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           nbSteps (int):   Number of time steps to use to render the trail
           position (SofaArray):   Position of the particles behind which a trail is rendered
           printLog (bool):   if true, emits extra messages at runtime.
           tags (object):   list of the subsets the objet belongs to
           thickness (float):   Thickness of the trail
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

    enable: Data[bool] 
    'Display the object or not'

    position: Data[SofaArray] 
    'Position of the particles behind which a trail is rendered'

    nbSteps: Data[int] 
    'Number of time steps to use to render the trail'

    color: Data[object] 
    'Color of the trail'

    thickness: Data[float] 
    'Thickness of the trail'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the TrailRenderer component"""

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

        enable: Optional[bool | LinkPath] = None 
        'Display the object or not'

        position: Optional[SofaArray | LinkPath] = None 
        'Position of the particles behind which a trail is rendered'

        nbSteps: Optional[int | LinkPath] = None 
        'Number of time steps to use to render the trail'

        color: Optional[object | LinkPath] = None 
        'Color of the trail'

        thickness: Optional[float | LinkPath] = None 
        'Thickness of the trail'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return TrailRenderer.Parameters()
