# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component EulerImplicitSolver

.. autofunction:: EulerImplicitSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class EulerImplicitSolver(Object):
    """Time integrator using implicit backward Euler scheme"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,rayleighStiffness: Optional[float] = None,rayleighMass: Optional[float] = None,vdamping: Optional[float] = None,firstOrder: Optional[bool] = None,trapezoidalScheme: Optional[bool] = None,solveConstraint: Optional[bool] = None,threadSafeVisitor: Optional[bool] = None):
        """Time integrator using implicit backward Euler scheme
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           firstOrder (bool):   Use backward Euler scheme for first order ode system.
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighMass (float):   Rayleigh damping coefficient related to mass, > 0
           rayleighStiffness (float):   Rayleigh damping coefficient related to stiffness, > 0
           solveConstraint (bool):   Apply ConstraintSolver (requires a ConstraintSolver in the same node as this solver, disabled by by default for now)
           tags (object):   list of the subsets the objet belongs to
           threadSafeVisitor (bool):   If true, do not use realloc and free visitors in fwdInteractionForceField.
           trapezoidalScheme (bool):   Optional: use the trapezoidal scheme instead of the implicit Euler scheme and get second order accuracy in time
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
    'Rayleigh damping coefficient related to stiffness, > 0'

    rayleighMass: Data[float] 
    'Rayleigh damping coefficient related to mass, > 0'

    vdamping: Data[float] 
    'Velocity decay coefficient (no decay if null)'

    firstOrder: Data[bool] 
    'Use backward Euler scheme for first order ode system.'

    trapezoidalScheme: Data[bool] 
    'Optional: use the trapezoidal scheme instead of the implicit Euler scheme and get second order accuracy in time'

    solveConstraint: Data[bool] 
    'Apply ConstraintSolver (requires a ConstraintSolver in the same node as this solver, disabled by by default for now)'

    threadSafeVisitor: Data[bool] 
    'If true, do not use realloc and free visitors in fwdInteractionForceField.'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the EulerImplicitSolver component"""

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
        'Rayleigh damping coefficient related to stiffness, > 0'

        rayleighMass: Optional[float | LinkPath] = None 
        'Rayleigh damping coefficient related to mass, > 0'

        vdamping: Optional[float | LinkPath] = None 
        'Velocity decay coefficient (no decay if null)'

        firstOrder: Optional[bool | LinkPath] = None 
        'Use backward Euler scheme for first order ode system.'

        trapezoidalScheme: Optional[bool | LinkPath] = None 
        'Optional: use the trapezoidal scheme instead of the implicit Euler scheme and get second order accuracy in time'

        solveConstraint: Optional[bool | LinkPath] = None 
        'Apply ConstraintSolver (requires a ConstraintSolver in the same node as this solver, disabled by by default for now)'

        threadSafeVisitor: Optional[bool | LinkPath] = None 
        'If true, do not use realloc and free visitors in fwdInteractionForceField.'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return EulerImplicitSolver.Parameters()
