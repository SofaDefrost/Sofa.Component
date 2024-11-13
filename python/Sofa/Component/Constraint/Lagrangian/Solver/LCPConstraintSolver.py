# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component LCPConstraintSolver

.. autofunction:: LCPConstraintSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class LCPConstraintSolver(Object):
    """A Constraint Solver using the Linear Complementarity Problem formulation to solve BaseConstraint based components"""

    def __init__(self, tolerance: float,maxIt: intname: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,displayDebug: Optional[bool] = None,initial_guess: Optional[bool] = None,build_lcp: Optional[bool] = None,mu: Optional[float] = None,minW: Optional[float] = None,maxF: Optional[float] = None,multi_grid: Optional[bool] = None,multi_grid_levels: Optional[int] = None,merge_method: Optional[int] = None,merge_spatial_step: Optional[int] = None,merge_local_levels: Optional[int] = None,constraintForces: Optional[SofaArray] = None,computeConstraintForces: Optional[bool] = None,group: Optional[SofaArray] = None,graph: Optional[SofaArray] = None,showLevels: Optional[int] = None,showCellWidth: Optional[float] = None,showTranslation: Optional[SofaArray] = None,showLevelTranslation: Optional[SofaArray] = None):
        """A Constraint Solver using the Linear Complementarity Problem formulation to solve BaseConstraint based components
        
        Args:
           bbox (object):   this object bounding box
           build_lcp (bool):   LCP is not fully built to increase performance in some case.
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           computeConstraintForces (bool):   enable the storage of the constraintForces.
           constraintForces (SofaArray):   OUTPUT: constraint forces (stored only if computeConstraintForces=True)
           displayDebug (bool):   Display debug information.
           graph (SofaArray):   Graph of residuals at each iteration
           group (SofaArray):   list of ID of groups of constraints to be handled by this solver.
           initial_guess (bool):   activate LCP results history to improve its resolution performances.
           listening (bool):   if true, handle the events, otherwise ignore the events
           maxF (float):   If not zero, constraints whose response force becomes larger than this threshold will be ignored
           maxIt (int):   maximal number of iterations of the Gauss-Seidel algorithm
           merge_local_levels (int):   if merge_method is 1: up to the specified level of the multigrid, constraints are grouped locally, i.e. separately within each contact pairs, while on upper levels they are grouped globally independently of contact pairs.
           merge_method (int):   if multi_grid is active: which method to use to merge constraints (0 = compliance-based, 1 = spatial coordinates)
           merge_spatial_step (int):   if merge_method is 1: grid size reduction between multigrid levels
           minW (float):   If not zero, constraints whose self-compliance (i.e. the corresponding value on the diagonal of W) is smaller than this threshold will be ignored
           mu (float):   Friction coefficient
           multi_grid (bool):   activate multi_grid resolution (NOT STABLE YET)
           multi_grid_levels (int):   if multi_grid is active: how many levels to create (>=2)
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           showCellWidth (float):   Distance between each constraint cells
           showLevelTranslation (SofaArray):   Translation between levels
           showLevels (int):   Number of constraint levels to display
           showTranslation (SofaArray):   Position of the first cell
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

    displayDebug: Data[bool] 
    'Display debug information.'

    initial_guess: Data[bool] 
    'activate LCP results history to improve its resolution performances.'

    build_lcp: Data[bool] 
    'LCP is not fully built to increase performance in some case.'

    tolerance: Data[float] 
    'residual error threshold for termination of the Gauss-Seidel algorithm'

    maxIt: Data[int] 
    'maximal number of iterations of the Gauss-Seidel algorithm'

    mu: Data[float] 
    'Friction coefficient'

    minW: Data[float] 
    'If not zero, constraints whose self-compliance (i.e. the corresponding value on the diagonal of W) is smaller than this threshold will be ignored'

    maxF: Data[float] 
    'If not zero, constraints whose response force becomes larger than this threshold will be ignored'

    multi_grid: Data[bool] 
    'activate multi_grid resolution (NOT STABLE YET)'

    multi_grid_levels: Data[int] 
    'if multi_grid is active: how many levels to create (>=2)'

    merge_method: Data[int] 
    'if multi_grid is active: which method to use to merge constraints (0 = compliance-based, 1 = spatial coordinates)'

    merge_spatial_step: Data[int] 
    'if merge_method is 1: grid size reduction between multigrid levels'

    merge_local_levels: Data[int] 
    'if merge_method is 1: up to the specified level of the multigrid, constraints are grouped locally, i.e. separately within each contact pairs, while on upper levels they are grouped globally independently of contact pairs.'

    constraintForces: Data[SofaArray] 
    'OUTPUT: constraint forces (stored only if computeConstraintForces=True)'

    computeConstraintForces: Data[bool] 
    'enable the storage of the constraintForces.'

    group: Data[SofaArray] 
    'list of ID of groups of constraints to be handled by this solver.'

    graph: Data[SofaArray] 
    'Graph of residuals at each iteration'

    showLevels: Data[int] 
    'Number of constraint levels to display'

    showCellWidth: Data[float] 
    'Distance between each constraint cells'

    showTranslation: Data[SofaArray] 
    'Position of the first cell'

    showLevelTranslation: Data[SofaArray] 
    'Translation between levels'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the LCPConstraintSolver component"""

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

        displayDebug: Optional[bool | LinkPath] = None 
        'Display debug information.'

        initial_guess: Optional[bool | LinkPath] = None 
        'activate LCP results history to improve its resolution performances.'

        build_lcp: Optional[bool | LinkPath] = None 
        'LCP is not fully built to increase performance in some case.'

        tolerance: Optional[float | LinkPath] = None 
        'residual error threshold for termination of the Gauss-Seidel algorithm'

        maxIt: Optional[int | LinkPath] = None 
        'maximal number of iterations of the Gauss-Seidel algorithm'

        mu: Optional[float | LinkPath] = None 
        'Friction coefficient'

        minW: Optional[float | LinkPath] = None 
        'If not zero, constraints whose self-compliance (i.e. the corresponding value on the diagonal of W) is smaller than this threshold will be ignored'

        maxF: Optional[float | LinkPath] = None 
        'If not zero, constraints whose response force becomes larger than this threshold will be ignored'

        multi_grid: Optional[bool | LinkPath] = None 
        'activate multi_grid resolution (NOT STABLE YET)'

        multi_grid_levels: Optional[int | LinkPath] = None 
        'if multi_grid is active: how many levels to create (>=2)'

        merge_method: Optional[int | LinkPath] = None 
        'if multi_grid is active: which method to use to merge constraints (0 = compliance-based, 1 = spatial coordinates)'

        merge_spatial_step: Optional[int | LinkPath] = None 
        'if merge_method is 1: grid size reduction between multigrid levels'

        merge_local_levels: Optional[int | LinkPath] = None 
        'if merge_method is 1: up to the specified level of the multigrid, constraints are grouped locally, i.e. separately within each contact pairs, while on upper levels they are grouped globally independently of contact pairs.'

        constraintForces: Optional[SofaArray | LinkPath] = None 
        'OUTPUT: constraint forces (stored only if computeConstraintForces=True)'

        computeConstraintForces: Optional[bool | LinkPath] = None 
        'enable the storage of the constraintForces.'

        group: Optional[SofaArray | LinkPath] = None 
        'list of ID of groups of constraints to be handled by this solver.'

        graph: Optional[SofaArray | LinkPath] = None 
        'Graph of residuals at each iteration'

        showLevels: Optional[int | LinkPath] = None 
        'Number of constraint levels to display'

        showCellWidth: Optional[float | LinkPath] = None 
        'Distance between each constraint cells'

        showTranslation: Optional[SofaArray | LinkPath] = None 
        'Position of the first cell'

        showLevelTranslation: Optional[SofaArray | LinkPath] = None 
        'Translation between levels'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return LCPConstraintSolver.Parameters()
