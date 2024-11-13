# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component PolynomialSpringsForceField

.. autofunction:: PolynomialSpringsForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class PolynomialSpringsForceField(Object):
    """Simple elastic springs applied to given degrees of freedom between their current and rest shape position"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,firstObjectPoints: Optional[SofaArray] = None,secondObjectPoints: Optional[SofaArray] = None,polynomialStiffness: Optional[SofaArray] = None,polynomialDegree: Optional[SofaArray] = None,computeZeroLength: Optional[int] = None,zeroLength: Optional[SofaArray] = None,recompute_indices: Optional[bool] = None,compressible: Optional[bool] = None,drawMode: Optional[int] = None,showArrowSize: Optional[float] = None,springColor: Optional[object] = None,showIndicesScale: Optional[float] = None):
        """Simple elastic springs applied to given degrees of freedom between their current and rest shape position
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           compressible (bool):   Indicates if object compresses without reactio force
           computeZeroLength (int):   flag to compute initial length for springs
           drawMode (int):   The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow
           firstObjectPoints (SofaArray):   points related to the first object
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           polynomialDegree (SofaArray):   vector of values that show polynomials degrees
           polynomialStiffness (SofaArray):   coefficients for all spring polynomials
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           recompute_indices (bool):   Recompute indices (should be false for BBOX)
           secondObjectPoints (SofaArray):   points related to the second object
           showArrowSize (float):   size of the axis
           showIndicesScale (float):   Scale for indices display. (default=0.02)
           springColor (object):   spring color
           tags (object):   list of the subsets the objet belongs to
           zeroLength (SofaArray):   initial length for springs
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

    isCompliance: Data[bool] 
    'Consider the component as a compliance, else as a stiffness'

    rayleighStiffness: Data[float] 
    'Rayleigh damping - stiffness matrix coefficient'

    firstObjectPoints: Data[SofaArray] 
    'points related to the first object'

    secondObjectPoints: Data[SofaArray] 
    'points related to the second object'

    polynomialStiffness: Data[SofaArray] 
    'coefficients for all spring polynomials'

    polynomialDegree: Data[SofaArray] 
    'vector of values that show polynomials degrees'

    computeZeroLength: Data[int] 
    'flag to compute initial length for springs'

    zeroLength: Data[SofaArray] 
    'initial length for springs'

    recompute_indices: Data[bool] 
    'Recompute indices (should be false for BBOX)'

    compressible: Data[bool] 
    'Indicates if object compresses without reactio force'

    drawMode: Data[int] 
    'The way springs will be drawn:- 0: Line- 1:Cylinder- 2: Arrow'

    showArrowSize: Data[float] 
    'size of the axis'

    springColor: Data[object] 
    'spring color'

    showIndicesScale: Data[float] 
    'Scale for indices display. (default=0.02)'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the PolynomialSpringsForceField component"""

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

        isCompliance: Optional[bool | LinkPath] = None 
        'Consider the component as a compliance, else as a stiffness'

        rayleighStiffness: Optional[float | LinkPath] = None 
        'Rayleigh damping - stiffness matrix coefficient'

        firstObjectPoints: Optional[SofaArray | LinkPath] = None 
        'points related to the first object'

        secondObjectPoints: Optional[SofaArray | LinkPath] = None 
        'points related to the second object'

        polynomialStiffness: Optional[SofaArray | LinkPath] = None 
        'coefficients for all spring polynomials'

        polynomialDegree: Optional[SofaArray | LinkPath] = None 
        'vector of values that show polynomials degrees'

        computeZeroLength: Optional[int | LinkPath] = None 
        'flag to compute initial length for springs'

        zeroLength: Optional[SofaArray | LinkPath] = None 
        'initial length for springs'

        recompute_indices: Optional[bool | LinkPath] = None 
        'Recompute indices (should be false for BBOX)'

        compressible: Optional[bool | LinkPath] = None 
        'Indicates if object compresses without reactio force'

        drawMode: Optional[int | LinkPath] = None 
        'The way springs will be drawn:- 0: Line- 1:Cylinder- 2: Arrow'

        showArrowSize: Optional[float | LinkPath] = None 
        'size of the axis'

        springColor: Optional[object | LinkPath] = None 
        'spring color'

        showIndicesScale: Optional[float | LinkPath] = None 
        'Scale for indices display. (default=0.02)'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return PolynomialSpringsForceField.Parameters()
