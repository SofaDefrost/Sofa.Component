# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component BilateralLagrangianConstraint

.. autofunction:: BilateralLagrangianConstraint

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class BilateralLagrangianConstraint(Object):
    """BilateralLagrangianConstraint defining an holonomic equality constraint (attachment)"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,group: Optional[int] = None,constraintIndex: Optional[int] = None,endTime: Optional[float] = None,first_point: Optional[SofaArray] = None,second_point: Optional[SofaArray] = None,rest_vector: Optional[SofaArray] = None,numericalTolerance: Optional[float] = None,activate: Optional[bool] = None,keepOrientationDifference: Optional[bool] = None):
        """BilateralLagrangianConstraint defining an holonomic equality constraint (attachment)
        
        Args:
           activate (bool):   control constraint activation (true by default)
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           constraintIndex (int):   Constraint index (first index in the right hand term resolution vector)
           endTime (float):   The constraint stops acting after the given value.
Use a negative value for infinite constraints
           first_point (SofaArray):   index of the constraint on the first model
           group (int):   ID of the group containing this constraint. This ID is used to specify which constraints are solved by which solver, by specifying in each solver which groups of constraints it should handle.
           keepOrientationDifference (bool):   keep the initial difference in orientation (only for rigids)
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           numericalTolerance (float):   a real value specifying the tolerance during the constraint solving. (optional, default=0.0001)
           printLog (bool):   if true, emits extra messages at runtime.
           rest_vector (SofaArray):   Relative position to maintain between attached points (optional)
           second_point (SofaArray):   index of the constraint on the second model
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

    first_point: Data[SofaArray] 
    'index of the constraint on the first model'

    second_point: Data[SofaArray] 
    'index of the constraint on the second model'

    rest_vector: Data[SofaArray] 
    'Relative position to maintain between attached points (optional)'

    numericalTolerance: Data[float] 
    'a real value specifying the tolerance during the constraint solving. (optional, default=0.0001)'

    activate: Data[bool] 
    'control constraint activation (true by default)'

    keepOrientationDifference: Data[bool] 
    'keep the initial difference in orientation (only for rigids)'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the BilateralLagrangianConstraint component"""

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

        first_point: Optional[SofaArray | LinkPath] = None 
        'index of the constraint on the first model'

        second_point: Optional[SofaArray | LinkPath] = None 
        'index of the constraint on the second model'

        rest_vector: Optional[SofaArray | LinkPath] = None 
        'Relative position to maintain between attached points (optional)'

        numericalTolerance: Optional[float | LinkPath] = None 
        'a real value specifying the tolerance during the constraint solving. (optional, default=0.0001)'

        activate: Optional[bool | LinkPath] = None 
        'control constraint activation (true by default)'

        keepOrientationDifference: Optional[bool | LinkPath] = None 
        'keep the initial difference in orientation (only for rigids)'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return BilateralLagrangianConstraint.Parameters()
