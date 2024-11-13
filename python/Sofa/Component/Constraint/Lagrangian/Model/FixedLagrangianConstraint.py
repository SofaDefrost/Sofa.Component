# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component FixedLagrangianConstraint

.. autofunction:: FixedLagrangianConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class FixedLagrangianConstraint(Object):
    """Lagrangian-based fixation of DOFs of the model"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,group: Optional[int] = None,constraintIndex: Optional[int] = None,endTime: Optional[float] = None,indices: Optional[SofaArray] = None,fixAll: Optional[bool] = None):
        """Lagrangian-based fixation of DOFs of the model
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           constraintIndex (int):   Constraint index (first index in the right hand term resolution vector)
           endTime (float):   The constraint stops acting after the given value.
Use a negative value for infinite constraints
           fixAll (bool):   If true, fix all points
           group (int):   ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
           indices (SofaArray):   Indices of points to fix
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
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

    group: Data[int] 
    'ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.'

    constraintIndex: Data[int] 
    'Constraint index (first index in the right hand term resolution vector)'

    endTime: Data[float] 
    'The constraint stops acting after the given value.Use a negative value for infinite constraints'

    indices: Data[SofaArray] 
    'Indices of points to fix'

    fixAll: Data[bool] 
    'If true, fix all points'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the FixedLagrangianConstraint component"""

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

        group: Optional[int | LinkPath] = None 
        'ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.'

        constraintIndex: Optional[int | LinkPath] = None 
        'Constraint index (first index in the right hand term resolution vector)'

        endTime: Optional[float | LinkPath] = None 
        'The constraint stops acting after the given value.Use a negative value for infinite constraints'

        indices: Optional[SofaArray | LinkPath] = None 
        'Indices of points to fix'

        fixAll: Optional[bool | LinkPath] = None 
        'If true, fix all points'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return FixedLagrangianConstraint.Parameters()
