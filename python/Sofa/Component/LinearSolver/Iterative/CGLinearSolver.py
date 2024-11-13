# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component CGLinearSolver

.. autofunction:: CGLinearSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class CGLinearSolver(Object):
    """Linear system solver using the conjugate gradient iterative algorithm"""

    def __init__(self, template: Optional[str] = None, iterations: int,tolerance: float,threshold: floatname: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,parallelInverseProduct: Optional[bool] = None,warmStart: Optional[bool] = None,graph: Optional[SofaArray] = None):
        """Linear system solver using the conjugate gradient iterative algorithm
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           graph (SofaArray):   Graph of residuals at each iteration
           iterations (int):   Maximum number of iterations of the Conjugate Gradient solution
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           parallelInverseProduct (bool):   Parallelize the computation of the product J*M^{-1}*J^T where M is the matrix of the linear system and J is any matrix with compatible dimensions
           printLog (bool):   if true, emits extra messages at runtime.
           tags (object):   list of the subsets the objet belongs to
           threshold (float):   Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution
           tolerance (float):   Desired accuracy of the Conjugate Gradient solution evaluating: |r|²/|b|² (ratio of current residual norm over initial residual norm)
           warmStart (bool):   Use previous solution as initial solution
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
    'Maximum number of iterations of the Conjugate Gradient solution'

    tolerance: Data[float] 
    'Desired accuracy of the Conjugate Gradient solution evaluating: |r|²/|b|² (ratio of current residual norm over initial residual norm)'

    threshold: Data[float] 
    'Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution'

    warmStart: Data[bool] 
    'Use previous solution as initial solution'

    graph: Data[SofaArray] 
    'Graph of residuals at each iteration'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the CGLinearSolver component"""

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
        'Maximum number of iterations of the Conjugate Gradient solution'

        tolerance: Optional[float | LinkPath] = None 
        'Desired accuracy of the Conjugate Gradient solution evaluating: |r|²/|b|² (ratio of current residual norm over initial residual norm)'

        threshold: Optional[float | LinkPath] = None 
        'Minimum value of the denominator (pT A p)^ in the conjugate Gradient solution'

        warmStart: Optional[bool | LinkPath] = None 
        'Use previous solution as initial solution'

        graph: Optional[SofaArray | LinkPath] = None 
        'Graph of residuals at each iteration'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return CGLinearSolver.Parameters()
