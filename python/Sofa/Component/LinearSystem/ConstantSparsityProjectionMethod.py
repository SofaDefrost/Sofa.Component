# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component ConstantSparsityProjectionMethod

.. autofunction:: ConstantSparsityProjectionMethod

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class ConstantSparsityProjectionMethod(Object):
    """Matrix mapping computing the matrix projection taking advantage of the constant sparsity pattern"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,areJacobiansConstant: Optional[bool] = None,parallelProduct: Optional[bool] = None):
        """Matrix mapping computing the matrix projection taking advantage of the constant sparsity pattern
        
        Args:
           areJacobiansConstant (bool):   True if mapping jacobians are considered constant over time. They are computed only the first time.
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           parallelProduct (bool):   Compute the matrix product in parallel
           printLog (bool):   if true, emits extra messages at runtime.
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

    areJacobiansConstant: Data[bool] 
    'True if mapping jacobians are considered constant over time. They are computed only the first time.'

    parallelProduct: Data[bool] 
    'Compute the matrix product in parallel'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the ConstantSparsityProjectionMethod component"""

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

        areJacobiansConstant: Optional[bool | LinkPath] = None 
        'True if mapping jacobians are considered constant over time. They are computed only the first time.'

        parallelProduct: Optional[bool | LinkPath] = None 
        'Compute the matrix product in parallel'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return ConstantSparsityProjectionMethod.Parameters()