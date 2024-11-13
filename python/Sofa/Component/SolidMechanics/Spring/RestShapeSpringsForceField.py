# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component RestShapeSpringsForceField

.. autofunction:: RestShapeSpringsForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class RestShapeSpringsForceField(Object):
    """Elastic springs generating forces on degrees of freedom between their current and rest shape position"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,points: Optional[SofaArray] = None,stiffness: Optional[SofaArray] = None,angularStiffness: Optional[SofaArray] = None,pivot_points: Optional[SofaArray] = None,external_points: Optional[SofaArray] = None,recompute_indices: Optional[bool] = None,drawSpring: Optional[bool] = None,springColor: Optional[object] = None,activeDirections: Optional[SofaArray] = None):
        """Elastic springs generating forces on degrees of freedom between their current and rest shape position
        
        Args:
           activeDirections (SofaArray):   Directions in which the spring is active (default=[1,1,1])
           angularStiffness (SofaArray):   angularStiffness assigned when controlling the rotation of the points
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           drawSpring (bool):   draw Spring
           external_points (SofaArray):   points from the external Mechancial State that define the rest shape springs
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           pivot_points (SofaArray):   global pivot points used when translations instead of the rigid mass centers
           points (SofaArray):   points controlled by the rest shape springs
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           recompute_indices (bool):   Recompute indices (should be false for BBOX)
           springColor (object):   spring color. (default=[0.0,1.0,0.0,1.0])
           stiffness (SofaArray):   stiffness values between the actual position and the rest shape position
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

    points: Data[SofaArray] 
    'points controlled by the rest shape springs'

    stiffness: Data[SofaArray] 
    'stiffness values between the actual position and the rest shape position'

    angularStiffness: Data[SofaArray] 
    'angularStiffness assigned when controlling the rotation of the points'

    pivot_points: Data[SofaArray] 
    'global pivot points used when translations instead of the rigid mass centers'

    external_points: Data[SofaArray] 
    'points from the external Mechancial State that define the rest shape springs'

    recompute_indices: Data[bool] 
    'Recompute indices (should be false for BBOX)'

    drawSpring: Data[bool] 
    'draw Spring'

    springColor: Data[object] 
    'spring color. (default=[0.0,1.0,0.0,1.0])'

    activeDirections: Data[SofaArray] 
    'Directions in which the spring is active (default=[1,1,1])'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the RestShapeSpringsForceField component"""

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

        points: Optional[SofaArray | LinkPath] = None 
        'points controlled by the rest shape springs'

        stiffness: Optional[SofaArray | LinkPath] = None 
        'stiffness values between the actual position and the rest shape position'

        angularStiffness: Optional[SofaArray | LinkPath] = None 
        'angularStiffness assigned when controlling the rotation of the points'

        pivot_points: Optional[SofaArray | LinkPath] = None 
        'global pivot points used when translations instead of the rigid mass centers'

        external_points: Optional[SofaArray | LinkPath] = None 
        'points from the external Mechancial State that define the rest shape springs'

        recompute_indices: Optional[bool | LinkPath] = None 
        'Recompute indices (should be false for BBOX)'

        drawSpring: Optional[bool | LinkPath] = None 
        'draw Spring'

        springColor: Optional[object | LinkPath] = None 
        'spring color. (default=[0.0,1.0,0.0,1.0])'

        activeDirections: Optional[SofaArray | LinkPath] = None 
        'Directions in which the spring is active (default=[1,1,1])'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return RestShapeSpringsForceField.Parameters()
