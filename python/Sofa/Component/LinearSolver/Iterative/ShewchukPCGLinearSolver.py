# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component ShewchukPCGLinearSolver

.. autofunction:: ShewchukPCGLinearSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class ShewchukPCGLinearSolver(Object):
    """Linear system solver using the conjugate gradient iterative algorithm"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,parallelInverseProduct: Optional[bool] = None,iterations: Optional[int] = None,tolerance: Optional[float] = None,use_precond: Optional[bool] = None,update_step: Optional[int] = None,build_precond: Optional[bool] = None,graph: Optional[SofaArray] = None):
        """Linear system solver using the conjugate gradient iterative algorithm
        
        Args:
           bbox (object):   this object bounding box
           build_precond (bool):   Build the preconditioners, if false build the preconditioner only at the initial step
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           graph (SofaArray):   Graph of residuals at each iteration
           iterations (int):   maximum number of iterations of the Conjugate Gradient solution
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           parallelInverseProduct (bool):   Parallelize the computation of the product J*M^{-1}*J^T where M is the matrix of the linear system and J is any matrix with compatible dimensions
           printLog (bool):   if true, emits extra messages at runtime.
           tags (object):   list of the subsets the objet belongs to
           tolerance (float):   desired precision of the Conjugate Gradient Solution (ratio of current residual norm over initial residual norm)
           update_step (int):   Number of steps before the next refresh of precondtioners
           use_precond (bool):   Use preconditioner
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

    parallelInverseProduct: Data[bool] 
    'Parallelize the computation of the product J*M^{-1}*J^T where M is the matrix of the linear system and J is any matrix with compatible dimensions'

    iterations: Data[int] 
    'maximum number of iterations of the Conjugate Gradient solution'

    tolerance: Data[float] 
    'desired precision of the Conjugate Gradient Solution (ratio of current residual norm over initial residual norm)'

    use_precond: Data[bool] 
    'Use preconditioner'

    update_step: Data[int] 
    'Number of steps before the next refresh of precondtioners'

    build_precond: Data[bool] 
    'Build the preconditioners, if false build the preconditioner only at the initial step'

    graph: Data[SofaArray] 
    'Graph of residuals at each iteration'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the ShewchukPCGLinearSolver component"""

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

        parallelInverseProduct: Optional[bool | LinkPath] = None 
        'Parallelize the computation of the product J*M^{-1}*J^T where M is the matrix of the linear system and J is any matrix with compatible dimensions'

        iterations: Optional[int | LinkPath] = None 
        'maximum number of iterations of the Conjugate Gradient solution'

        tolerance: Optional[float | LinkPath] = None 
        'desired precision of the Conjugate Gradient Solution (ratio of current residual norm over initial residual norm)'

        use_precond: Optional[bool | LinkPath] = None 
        'Use preconditioner'

        update_step: Optional[int | LinkPath] = None 
        'Number of steps before the next refresh of precondtioners'

        build_precond: Optional[bool | LinkPath] = None 
        'Build the preconditioners, if false build the preconditioner only at the initial step'

        graph: Optional[SofaArray | LinkPath] = None 
        'Graph of residuals at each iteration'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return ShewchukPCGLinearSolver.Parameters()
