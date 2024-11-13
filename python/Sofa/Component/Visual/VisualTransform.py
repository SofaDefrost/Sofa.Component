# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component VisualTransform

.. autofunction:: VisualTransform

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class VisualTransform(Object):
    """TODO"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,enable: Optional[bool] = None,transform: Optional[SofaArray] = None,recursive: Optional[bool] = None):
        """TODO
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           enable (bool):   Display the object or not
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           recursive (bool):   True to apply transform to all nodes below
           tags (object):   list of the subsets the objet belongs to
           transform (SofaArray):   Transformation to apply
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

    transform: Data[SofaArray] 
    'Transformation to apply'

    recursive: Data[bool] 
    'True to apply transform to all nodes below'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the VisualTransform component"""

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

        transform: Optional[SofaArray | LinkPath] = None 
        'Transformation to apply'

        recursive: Optional[bool | LinkPath] = None 
        'True to apply transform to all nodes below'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return VisualTransform.Parameters()
