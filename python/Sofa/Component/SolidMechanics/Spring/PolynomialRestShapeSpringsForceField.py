# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component PolynomialRestShapeSpringsForceField

.. autofunction:: PolynomialRestShapeSpringsForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class PolynomialRestShapeSpringsForceField(Object):
    """Simple elastic springs applied to given degrees of freedom between their current and rest shape position"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,points: Optional[SofaArray] = None,external_points: Optional[SofaArray] = None,polynomialStiffness: Optional[SofaArray] = None,polynomialDegree: Optional[SofaArray] = None,recompute_indices: Optional[bool] = None,drawSpring: Optional[bool] = None,springColor: Optional[object] = None,showIndicesScale: Optional[float] = None,initialLength: Optional[SofaArray] = None,smoothShift: Optional[float] = None,smoothScale: Optional[float] = None):
        """Simple elastic springs applied to given degrees of freedom between their current and rest shape position
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           drawSpring (bool):   draw Spring
           external_points (SofaArray):   points from the external Mechancial State that define the rest shape springs
           initialLength (SofaArray):   initial virtual length of the spring
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           points (SofaArray):   points controlled by the rest shape springs
           polynomialDegree (SofaArray):   vector of values that show polynomials degrees
           polynomialStiffness (SofaArray):   coefficients for all spring polynomials
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           recompute_indices (bool):   Recompute indices (should be false for BBOX)
           showIndicesScale (float):   Scale for indices display. (default=0.02)
           smoothScale (float):   denominator correction adding scale
           smoothShift (float):   denominator correction adding shift value
           springColor (object):   spring color
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

    isCompliance: Data[bool] 
    'Consider the component as a compliance, else as a stiffness'

    rayleighStiffness: Data[float] 
    'Rayleigh damping - stiffness matrix coefficient'

    points: Data[SofaArray] 
    'points controlled by the rest shape springs'

    external_points: Data[SofaArray] 
    'points from the external Mechancial State that define the rest shape springs'

    polynomialStiffness: Data[SofaArray] 
    'coefficients for all spring polynomials'

    polynomialDegree: Data[SofaArray] 
    'vector of values that show polynomials degrees'

    recompute_indices: Data[bool] 
    'Recompute indices (should be false for BBOX)'

    drawSpring: Data[bool] 
    'draw Spring'

    springColor: Data[object] 
    'spring color'

    showIndicesScale: Data[float] 
    'Scale for indices display. (default=0.02)'

    initialLength: Data[SofaArray] 
    'initial virtual length of the spring'

    smoothShift: Data[float] 
    'denominator correction adding shift value'

    smoothScale: Data[float] 
    'denominator correction adding scale'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the PolynomialRestShapeSpringsForceField component"""

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

        points: Optional[SofaArray | LinkPath] = None 
        'points controlled by the rest shape springs'

        external_points: Optional[SofaArray | LinkPath] = None 
        'points from the external Mechancial State that define the rest shape springs'

        polynomialStiffness: Optional[SofaArray | LinkPath] = None 
        'coefficients for all spring polynomials'

        polynomialDegree: Optional[SofaArray | LinkPath] = None 
        'vector of values that show polynomials degrees'

        recompute_indices: Optional[bool | LinkPath] = None 
        'Recompute indices (should be false for BBOX)'

        drawSpring: Optional[bool | LinkPath] = None 
        'draw Spring'

        springColor: Optional[object | LinkPath] = None 
        'spring color'

        showIndicesScale: Optional[float | LinkPath] = None 
        'Scale for indices display. (default=0.02)'

        initialLength: Optional[SofaArray | LinkPath] = None 
        'initial virtual length of the spring'

        smoothShift: Optional[float | LinkPath] = None 
        'denominator correction adding shift value'

        smoothScale: Optional[float | LinkPath] = None 
        'denominator correction adding scale'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return PolynomialRestShapeSpringsForceField.Parameters()
