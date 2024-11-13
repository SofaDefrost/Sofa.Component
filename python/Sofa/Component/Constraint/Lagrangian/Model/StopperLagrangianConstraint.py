# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component StopperLagrangianConstraint

.. autofunction:: StopperLagrangianConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class StopperLagrangianConstraint(Object):
    """TODO-StopperLagrangianConstraint"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,group: Optional[int] = None,constraintIndex: Optional[int] = None,endTime: Optional[float] = None,index: Optional[int] = None,min: Optional[float] = None,max: Optional[float] = None):
        """TODO-StopperLagrangianConstraint
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           constraintIndex (int):   Constraint index (first index in the right hand term resolution vector)
           endTime (float):   The constraint stops acting after the given value.
Use a negative value for infinite constraints
           group (int):   ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
           index (int):   index of the stop constraint
           listening (bool):   if true, handle the events, otherwise ignore the events
           max (float):   maximum value accepted
           min (float):   minimum value accepted
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

    index: Data[int] 
    'index of the stop constraint'

    min: Data[float] 
    'minimum value accepted'

    max: Data[float] 
    'maximum value accepted'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the StopperLagrangianConstraint component"""

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

        index: Optional[int | LinkPath] = None 
        'index of the stop constraint'

        min: Optional[float | LinkPath] = None 
        'minimum value accepted'

        max: Optional[float | LinkPath] = None 
        'maximum value accepted'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return StopperLagrangianConstraint.Parameters()
