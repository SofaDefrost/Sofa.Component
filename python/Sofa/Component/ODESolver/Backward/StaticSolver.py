# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component StaticSolver

.. autofunction:: StaticSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class StaticSolver(Object):
    """Static ODE Solver"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,newton_iterations: Optional[int] = None,absolute_correction_tolerance_threshold: Optional[float] = None,relative_correction_tolerance_threshold: Optional[float] = None,absolute_residual_tolerance_threshold: Optional[float] = None,relative_residual_tolerance_threshold: Optional[float] = None,should_diverge_when_residual_is_growing: Optional[bool] = None):
        """Static ODE Solver
        
        Args:
           absolute_correction_tolerance_threshold (float):   Convergence criterion: The newton iterations will stop when the norm |du| is smaller than this threshold.
           absolute_residual_tolerance_threshold (float):   Convergence criterion: The newton iterations will stop when the norm |R| is smaller than this threshold. Use a negative value to disable this criterion.
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           newton_iterations (int):   Number of newton iterations between each load increments (normally, one load increment per simulation time-step.
           printLog (bool):   if true, emits extra messages at runtime.
           relative_correction_tolerance_threshold (float):   Convergence criterion: The newton iterations will stop when the ratio |du| / |U| is smaller than this threshold.
           relative_residual_tolerance_threshold (float):   Convergence criterion: The newton iterations will stop when the ratio |R|/|R0| is smaller than this threshold. Use a negative value to disable this criterion.
           should_diverge_when_residual_is_growing (bool):   Divergence criterion: The newton iterations will stop when the residual is greater than the one from the previous iteration.
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

    newton_iterations: Data[int] 
    'Number of newton iterations between each load increments (normally, one load increment per simulation time-step.'

    absolute_correction_tolerance_threshold: Data[float] 
    'Convergence criterion: The newton iterations will stop when the norm |du| is smaller than this threshold.'

    relative_correction_tolerance_threshold: Data[float] 
    'Convergence criterion: The newton iterations will stop when the ratio |du| / |U| is smaller than this threshold.'

    absolute_residual_tolerance_threshold: Data[float] 
    'Convergence criterion: The newton iterations will stop when the norm |R| is smaller than this threshold. Use a negative value to disable this criterion.'

    relative_residual_tolerance_threshold: Data[float] 
    'Convergence criterion: The newton iterations will stop when the ratio |R|/|R0| is smaller than this threshold. Use a negative value to disable this criterion.'

    should_diverge_when_residual_is_growing: Data[bool] 
    'Divergence criterion: The newton iterations will stop when the residual is greater than the one from the previous iteration.'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the StaticSolver component"""

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

        newton_iterations: Optional[int | LinkPath] = None 
        'Number of newton iterations between each load increments (normally, one load increment per simulation time-step.'

        absolute_correction_tolerance_threshold: Optional[float | LinkPath] = None 
        'Convergence criterion: The newton iterations will stop when the norm |du| is smaller than this threshold.'

        relative_correction_tolerance_threshold: Optional[float | LinkPath] = None 
        'Convergence criterion: The newton iterations will stop when the ratio |du| / |U| is smaller than this threshold.'

        absolute_residual_tolerance_threshold: Optional[float | LinkPath] = None 
        'Convergence criterion: The newton iterations will stop when the norm |R| is smaller than this threshold. Use a negative value to disable this criterion.'

        relative_residual_tolerance_threshold: Optional[float | LinkPath] = None 
        'Convergence criterion: The newton iterations will stop when the ratio |R|/|R0| is smaller than this threshold. Use a negative value to disable this criterion.'

        should_diverge_when_residual_is_growing: Optional[bool | LinkPath] = None 
        'Divergence criterion: The newton iterations will stop when the residual is greater than the one from the previous iteration.'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return StaticSolver.Parameters()
