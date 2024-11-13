# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component Visual3DText

.. autofunction:: Visual3DText

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class Visual3DText(Object):
    """Display 3D camera-oriented text"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,enable: Optional[bool] = None,text: Optional[str] = None,position: Optional[SofaArray] = None,scale: Optional[float] = None,color: Optional[object] = None,depthTest: Optional[bool] = None):
        """Display 3D camera-oriented text
        
        Args:
           bbox (object):   this object bounding box
           color (object):   text color. (default=[1.0,1.0,1.0,1.0])
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           depthTest (bool):   perform depth test
           enable (bool):   Display the object or not
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           position (SofaArray):   3d position
           printLog (bool):   if true, emits extra messages at runtime.
           scale (float):   text scale
           tags (object):   list of the subsets the objet belongs to
           text (str):   Test to display
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

    text: Data[str] 
    'Test to display'

    position: Data[SofaArray] 
    '3d position'

    scale: Data[float] 
    'text scale'

    color: Data[object] 
    'text color. (default=[1.0,1.0,1.0,1.0])'

    depthTest: Data[bool] 
    'perform depth test'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the Visual3DText component"""

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

        text: Optional[str | LinkPath] = None 
        'Test to display'

        position: Optional[SofaArray | LinkPath] = None 
        '3d position'

        scale: Optional[float | LinkPath] = None 
        'text scale'

        color: Optional[object | LinkPath] = None 
        'text color. (default=[1.0,1.0,1.0,1.0])'

        depthTest: Optional[bool | LinkPath] = None 
        'perform depth test'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return Visual3DText.Parameters()
