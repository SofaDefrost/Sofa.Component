# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component LineAxis

.. autofunction:: LineAxis

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class LineAxis(Object):
    """Display scene axis"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,enable: Optional[bool] = None,axis: Optional[str] = None,size: Optional[float] = None,thickness: Optional[float] = None):
        """Display scene axis
        
        Args:
           axis (str):   Axis to draw
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           enable (bool):   Display the object or not
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           size (float):   Size of the squared grid
           tags (object):   list of the subsets the objet belongs to
           thickness (float):   Thickness of the lines in the grid
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

    axis: Data[str] 
    'Axis to draw'

    size: Data[float] 
    'Size of the squared grid'

    thickness: Data[float] 
    'Thickness of the lines in the grid'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the LineAxis component"""

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

        axis: Optional[str | LinkPath] = None 
        'Axis to draw'

        size: Optional[float | LinkPath] = None 
        'Size of the squared grid'

        thickness: Optional[float | LinkPath] = None 
        'Thickness of the lines in the grid'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return LineAxis.Parameters()
