# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component AngularSpringForceField

.. autofunction:: AngularSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class AngularSpringForceField(Object):
    """Angular springs applied to rotational degrees of freedom of a rigid body or frame"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,indices: Optional[SofaArray] = None,angularStiffness: Optional[SofaArray] = None,limit: Optional[SofaArray] = None,drawSpring: Optional[bool] = None,springColor: Optional[object] = None):
        """Angular springs applied to rotational degrees of freedom of a rigid body or frame
        
        Args:
           angularStiffness (SofaArray):   angular stiffness for the controlled nodes
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           drawSpring (bool):   draw Spring
           indices (SofaArray):   index of nodes controlled by the angular springs
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           limit (SofaArray):   angular limit (max; min) values where the force applies
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           springColor (object):   spring color
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

    indices: Data[SofaArray] 
    'index of nodes controlled by the angular springs'

    angularStiffness: Data[SofaArray] 
    'angular stiffness for the controlled nodes'

    limit: Data[SofaArray] 
    'angular limit (max; min) values where the force applies'

    drawSpring: Data[bool] 
    'draw Spring'

    springColor: Data[object] 
    'spring color'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the AngularSpringForceField component"""

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

        indices: Optional[SofaArray | LinkPath] = None 
        'index of nodes controlled by the angular springs'

        angularStiffness: Optional[SofaArray | LinkPath] = None 
        'angular stiffness for the controlled nodes'

        limit: Optional[SofaArray | LinkPath] = None 
        'angular limit (max; min) values where the force applies'

        drawSpring: Optional[bool | LinkPath] = None 
        'draw Spring'

        springColor: Optional[object | LinkPath] = None 
        'spring color'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return AngularSpringForceField.Parameters()
