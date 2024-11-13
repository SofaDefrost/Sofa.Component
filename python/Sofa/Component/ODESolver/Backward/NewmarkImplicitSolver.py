# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component NewmarkImplicitSolver

.. autofunction:: NewmarkImplicitSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class NewmarkImplicitSolver(Object):
    """Implicit time integrator using Newmark scheme"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,rayleighStiffness: Optional[float] = None,rayleighMass: Optional[float] = None,vdamping: Optional[float] = None,gamma: Optional[float] = None,beta: Optional[float] = None,threadSafeVisitor: Optional[bool] = None):
        """Implicit time integrator using Newmark scheme
        
        Args:
           bbox (object):   this object bounding box
           beta (float):   Newmark scheme beta coefficient
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           gamma (float):   Newmark scheme gamma coefficient
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighMass (float):   Rayleigh damping coefficient related to mass
           rayleighStiffness (float):   Rayleigh damping coefficient related to stiffness
           tags (object):   list of the subsets the objet belongs to
           threadSafeVisitor (bool):   If true, do not use realloc and free visitors in fwdInteractionForceField.
           vdamping (float):   Velocity decay coefficient (no decay if null)
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

    rayleighStiffness: Data[float] 
    'Rayleigh damping coefficient related to stiffness'

    rayleighMass: Data[float] 
    'Rayleigh damping coefficient related to mass'

    vdamping: Data[float] 
    'Velocity decay coefficient (no decay if null)'

    gamma: Data[float] 
    'Newmark scheme gamma coefficient'

    beta: Data[float] 
    'Newmark scheme beta coefficient'

    threadSafeVisitor: Data[bool] 
    'If true, do not use realloc and free visitors in fwdInteractionForceField.'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the NewmarkImplicitSolver component"""

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

        rayleighStiffness: Optional[float | LinkPath] = None 
        'Rayleigh damping coefficient related to stiffness'

        rayleighMass: Optional[float | LinkPath] = None 
        'Rayleigh damping coefficient related to mass'

        vdamping: Optional[float | LinkPath] = None 
        'Velocity decay coefficient (no decay if null)'

        gamma: Optional[float | LinkPath] = None 
        'Newmark scheme gamma coefficient'

        beta: Optional[float | LinkPath] = None 
        'Newmark scheme beta coefficient'

        threadSafeVisitor: Optional[bool | LinkPath] = None 
        'If true, do not use realloc and free visitors in fwdInteractionForceField.'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return NewmarkImplicitSolver.Parameters()
