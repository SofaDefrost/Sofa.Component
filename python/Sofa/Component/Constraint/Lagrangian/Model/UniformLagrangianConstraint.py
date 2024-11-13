# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component UniformLagrangianConstraint

.. autofunction:: UniformLagrangianConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class UniformLagrangianConstraint(Object):
    """A constraint equation applied on all dofs."""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,group: Optional[int] = None,constraintIndex: Optional[int] = None,endTime: Optional[float] = None,iterative: Optional[bool] = None,constrainToRestPos: Optional[bool] = None):
        """A constraint equation applied on all dofs.
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           constrainToRestPos (bool):   if false, constrains the pos to be zero / if true constraint the current position to stay at rest position
           constraintIndex (int):   Constraint index (first index in the right hand term resolution vector)
           endTime (float):   The constraint stops acting after the given value.
Use a negative value for infinite constraints
           group (int):   ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
           iterative (bool):   Iterate over the bilateral constraints, otherwise a block factorisation is computed.
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

    iterative: Data[bool] 
    'Iterate over the bilateral constraints, otherwise a block factorisation is computed.'

    constrainToRestPos: Data[bool] 
    'if false, constrains the pos to be zero / if true constraint the current position to stay at rest position'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the UniformLagrangianConstraint component"""

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

        iterative: Optional[bool | LinkPath] = None 
        'Iterate over the bilateral constraints, otherwise a block factorisation is computed.'

        constrainToRestPos: Optional[bool | LinkPath] = None 
        'if false, constrains the pos to be zero / if true constraint the current position to stay at rest position'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return UniformLagrangianConstraint.Parameters()
