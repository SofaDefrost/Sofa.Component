# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component UncoupledConstraintCorrection

.. autofunction:: UncoupledConstraintCorrection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class UncoupledConstraintCorrection(Object):
    """Component computing constraint forces within a simulated body using the compliance method."""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,compliance: Optional[SofaArray] = None,defaultCompliance: Optional[float] = None,verbose: Optional[bool] = None,correctionVelocityFactor: Optional[float] = None,correctionPositionFactor: Optional[float] = None,useOdeSolverIntegrationFactors: Optional[bool] = None):
        """Component computing constraint forces within a simulated body using the compliance method.
        
        Args:
           bbox (object):   this object bounding box
           compliance (SofaArray):   compliance value on each dof. If Rigid compliance (7 values): 1st value for translations, 6 others for upper-triangular part of symmetric 3x3 rotation compliance matrix
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           correctionPositionFactor (float):   Factor applied to the constraint forces when correcting the positions
           correctionVelocityFactor (float):   Factor applied to the constraint forces when correcting the velocities
           defaultCompliance (float):   Default compliance value for new dof or if all should have the same (in which case compliance vector should be empty)
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           tags (object):   list of the subsets the objet belongs to
           useOdeSolverIntegrationFactors (bool):   Use odeSolver integration factors instead of correctionVelocityFactor and correctionPositionFactor
           verbose (bool):   Dump the constraint matrix at each iteration
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

    compliance: Data[SofaArray] 
    'compliance value on each dof. If Rigid compliance (7 values): 1st value for translations, 6 others for upper-triangular part of symmetric 3x3 rotation compliance matrix'

    defaultCompliance: Data[float] 
    'Default compliance value for new dof or if all should have the same (in which case compliance vector should be empty)'

    verbose: Data[bool] 
    'Dump the constraint matrix at each iteration'

    correctionVelocityFactor: Data[float] 
    'Factor applied to the constraint forces when correcting the velocities'

    correctionPositionFactor: Data[float] 
    'Factor applied to the constraint forces when correcting the positions'

    useOdeSolverIntegrationFactors: Data[bool] 
    'Use odeSolver integration factors instead of correctionVelocityFactor and correctionPositionFactor'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the UncoupledConstraintCorrection component"""

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

        compliance: Optional[SofaArray | LinkPath] = None 
        'compliance value on each dof. If Rigid compliance (7 values): 1st value for translations, 6 others for upper-triangular part of symmetric 3x3 rotation compliance matrix'

        defaultCompliance: Optional[float | LinkPath] = None 
        'Default compliance value for new dof or if all should have the same (in which case compliance vector should be empty)'

        verbose: Optional[bool | LinkPath] = None 
        'Dump the constraint matrix at each iteration'

        correctionVelocityFactor: Optional[float | LinkPath] = None 
        'Factor applied to the constraint forces when correcting the velocities'

        correctionPositionFactor: Optional[float | LinkPath] = None 
        'Factor applied to the constraint forces when correcting the positions'

        useOdeSolverIntegrationFactors: Optional[bool | LinkPath] = None 
        'Use odeSolver integration factors instead of correctionVelocityFactor and correctionPositionFactor'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return UncoupledConstraintCorrection.Parameters()
