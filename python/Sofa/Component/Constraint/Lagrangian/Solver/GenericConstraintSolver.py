# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component GenericConstraintSolver

.. autofunction:: GenericConstraintSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class GenericConstraintSolver(Object):
    """A Generic Constraint Solver using the Linear Complementarity Problem formulation to solve Constraint based components"""

    def __init__(self, maxIterations: int,tolerance: floatname: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,resolutionMethod: Optional[object] = None,sor: Optional[float] = None,scaleTolerance: Optional[bool] = None,allVerified: Optional[bool] = None,newtonIterations: Optional[int] = None,multithreading: Optional[bool] = None,computeGraphs: Optional[bool] = None,graphErrors: Optional[SofaArray] = None,graphConstraints: Optional[SofaArray] = None,graphForces: Optional[SofaArray] = None,graphViolations: Optional[SofaArray] = None,currentNumConstraints: Optional[int] = None,currentNumConstraintGroups: Optional[int] = None,currentIterations: Optional[int] = None,currentError: Optional[float] = None,reverseAccumulateOrder: Optional[bool] = None,constraintForces: Optional[SofaArray] = None,computeConstraintForces: Optional[bool] = None):
        """A Generic Constraint Solver using the Linear Complementarity Problem formulation to solve Constraint based components
        
        Args:
           allVerified (bool):   All contraints must be verified (each constraint's error < tolerance)
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           computeConstraintForces (bool):   enable the storage of the constraintForces.
           computeGraphs (bool):   Compute graphs of errors and forces during resolution
           constraintForces (SofaArray):   OUTPUT: constraint forces (stored only if computeConstraintForces=True)
           currentError (float):   OUTPUT: current error
           currentIterations (int):   OUTPUT: current number of constraint groups
           currentNumConstraintGroups (int):   OUTPUT: current number of constraints
           currentNumConstraints (int):   OUTPUT: current number of constraints
           graphConstraints (SofaArray):   Graph of each constraint's error at the end of the resolution
           graphErrors (SofaArray):   Sum of the constraints' errors at each iteration
           graphForces (SofaArray):   Graph of each constraint's force at each step of the resolution
           graphViolations (SofaArray):   Graph of each constraint's violation at each step of the resolution
           listening (bool):   if true, handle the events, otherwise ignore the events
           maxIterations (int):   maximal number of iterations of the Gauss-Seidel algorithm
           multithreading (bool):   Build compliances concurrently
           name (str):   object name
           newtonIterations (int):   Maximum iteration number of Newton (for the NonsmoothNonlinearConjugateGradient solver only)
           printLog (bool):   if true, emits extra messages at runtime.
           resolutionMethod (object):   Method used to solve the constraint problem, among: "ProjectedGaussSeidel", "UnbuiltGaussSeidel" or "for NonsmoothNonlinearConjugateGradient"
           reverseAccumulateOrder (bool):   True to accumulate constraints from nodes in reversed order (can be necessary when using multi-mappings or interaction constraints not following the node hierarchy)
           scaleTolerance (bool):   Scale the error tolerance with the number of constraints
           sor (float):   Successive Over Relaxation parameter (0-2)
           tags (object):   list of the subsets the objet belongs to
           tolerance (float):   residual error threshold for termination of the Gauss-Seidel algorithm
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

    resolutionMethod: Data[object] 
    'Method used to solve the constraint problem, among: "ProjectedGaussSeidel", "UnbuiltGaussSeidel" or "for NonsmoothNonlinearConjugateGradient"'

    maxIterations: Data[int] 
    'maximal number of iterations of the Gauss-Seidel algorithm'

    tolerance: Data[float] 
    'residual error threshold for termination of the Gauss-Seidel algorithm'

    sor: Data[float] 
    'Successive Over Relaxation parameter (0-2)'

    scaleTolerance: Data[bool] 
    'Scale the error tolerance with the number of constraints'

    allVerified: Data[bool] 
    'All contraints must be verified (each constraints error < tolerance)'

    newtonIterations: Data[int] 
    'Maximum iteration number of Newton (for the NonsmoothNonlinearConjugateGradient solver only)'

    multithreading: Data[bool] 
    'Build compliances concurrently'

    computeGraphs: Data[bool] 
    'Compute graphs of errors and forces during resolution'

    graphErrors: Data[SofaArray] 
    'Sum of the constraints errors at each iteration'

    graphConstraints: Data[SofaArray] 
    'Graph of each constraints error at the end of the resolution'

    graphForces: Data[SofaArray] 
    'Graph of each constraints force at each step of the resolution'

    graphViolations: Data[SofaArray] 
    'Graph of each constraints violation at each step of the resolution'

    currentNumConstraints: Data[int] 
    'OUTPUT: current number of constraints'

    currentNumConstraintGroups: Data[int] 
    'OUTPUT: current number of constraints'

    currentIterations: Data[int] 
    'OUTPUT: current number of constraint groups'

    currentError: Data[float] 
    'OUTPUT: current error'

    reverseAccumulateOrder: Data[bool] 
    'True to accumulate constraints from nodes in reversed order (can be necessary when using multi-mappings or interaction constraints not following the node hierarchy)'

    constraintForces: Data[SofaArray] 
    'OUTPUT: constraint forces (stored only if computeConstraintForces=True)'

    computeConstraintForces: Data[bool] 
    'enable the storage of the constraintForces.'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the GenericConstraintSolver component"""

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

        resolutionMethod: Optional[object | LinkPath] = None 
        'Method used to solve the constraint problem, among: "ProjectedGaussSeidel", "UnbuiltGaussSeidel" or "for NonsmoothNonlinearConjugateGradient"'

        maxIterations: Optional[int | LinkPath] = None 
        'maximal number of iterations of the Gauss-Seidel algorithm'

        tolerance: Optional[float | LinkPath] = None 
        'residual error threshold for termination of the Gauss-Seidel algorithm'

        sor: Optional[float | LinkPath] = None 
        'Successive Over Relaxation parameter (0-2)'

        scaleTolerance: Optional[bool | LinkPath] = None 
        'Scale the error tolerance with the number of constraints'

        allVerified: Optional[bool | LinkPath] = None 
        'All contraints must be verified (each constraints error < tolerance)'

        newtonIterations: Optional[int | LinkPath] = None 
        'Maximum iteration number of Newton (for the NonsmoothNonlinearConjugateGradient solver only)'

        multithreading: Optional[bool | LinkPath] = None 
        'Build compliances concurrently'

        computeGraphs: Optional[bool | LinkPath] = None 
        'Compute graphs of errors and forces during resolution'

        graphErrors: Optional[SofaArray | LinkPath] = None 
        'Sum of the constraints errors at each iteration'

        graphConstraints: Optional[SofaArray | LinkPath] = None 
        'Graph of each constraints error at the end of the resolution'

        graphForces: Optional[SofaArray | LinkPath] = None 
        'Graph of each constraints force at each step of the resolution'

        graphViolations: Optional[SofaArray | LinkPath] = None 
        'Graph of each constraints violation at each step of the resolution'

        currentNumConstraints: Optional[int | LinkPath] = None 
        'OUTPUT: current number of constraints'

        currentNumConstraintGroups: Optional[int | LinkPath] = None 
        'OUTPUT: current number of constraints'

        currentIterations: Optional[int | LinkPath] = None 
        'OUTPUT: current number of constraint groups'

        currentError: Optional[float | LinkPath] = None 
        'OUTPUT: current error'

        reverseAccumulateOrder: Optional[bool | LinkPath] = None 
        'True to accumulate constraints from nodes in reversed order (can be necessary when using multi-mappings or interaction constraints not following the node hierarchy)'

        constraintForces: Optional[SofaArray | LinkPath] = None 
        'OUTPUT: constraint forces (stored only if computeConstraintForces=True)'

        computeConstraintForces: Optional[bool | LinkPath] = None 
        'enable the storage of the constraintForces.'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return GenericConstraintSolver.Parameters()
