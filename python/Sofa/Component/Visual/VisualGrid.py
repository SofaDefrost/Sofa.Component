# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component VisualGrid

.. autofunction:: VisualGrid

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class VisualGrid(Object):
    """Display a simple grid"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,enable: Optional[bool] = None,plane: Optional[str] = None,size: Optional[float] = None,nbSubdiv: Optional[int] = None,color: Optional[object] = None,thickness: Optional[float] = None):
        """Display a simple grid
        
        Args:
           bbox (object):   this object bounding box
           color (object):   Color of the lines in the grid. default=(0.34,0.34,0.34,1.0)
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           enable (bool):   Display the object or not
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           nbSubdiv (int):   Number of subdivisions
           plane (str):   Plane of the grid
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

    plane: Data[str] 
    'Plane of the grid'

    size: Data[float] 
    'Size of the squared grid'

    nbSubdiv: Data[int] 
    'Number of subdivisions'

    color: Data[object] 
    'Color of the lines in the grid. default=(0.34,0.34,0.34,1.0)'

    thickness: Data[float] 
    'Thickness of the lines in the grid'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the VisualGrid component"""

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

        plane: Optional[str | LinkPath] = None 
        'Plane of the grid'

        size: Optional[float | LinkPath] = None 
        'Size of the squared grid'

        nbSubdiv: Optional[int | LinkPath] = None 
        'Number of subdivisions'

        color: Optional[object | LinkPath] = None 
        'Color of the lines in the grid. default=(0.34,0.34,0.34,1.0)'

        thickness: Optional[float | LinkPath] = None 
        'Thickness of the lines in the grid'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return VisualGrid.Parameters()
