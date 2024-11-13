# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component TriangularBiquadraticSpringsForceField

.. autofunction:: TriangularBiquadraticSpringsForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class TriangularBiquadraticSpringsForceField(Object):
    """Biquadratic Springs on a Triangular Mesh"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,triangleInfo: Optional[SofaArray] = None,edgeInfo: Optional[SofaArray] = None,initialPoints: Optional[SofaArray] = None,poissonRatio: Optional[float] = None,youngModulus: Optional[float] = None,dampingRatio: Optional[float] = None,useAngularSprings: Optional[bool] = None,compressible: Optional[bool] = None,matrixRegularization: Optional[float] = None):
        """Biquadratic Springs on a Triangular Mesh
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           compressible (bool):   If additional energy penalizing compressibility should be used
           dampingRatio (float):   Ratio damping/stiffness
           edgeInfo (SofaArray):   Internal edge data
           initialPoints (SofaArray):   Initial Position
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           matrixRegularization (float):   Regularization of the Stiffnes Matrix (between 0 and 1)
           name (str):   object name
           poissonRatio (float):   Poisson ratio in Hooke's law
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           tags (object):   list of the subsets the objet belongs to
           triangleInfo (SofaArray):   Internal triangle data
           useAngularSprings (bool):   If Angular Springs should be used or not
           youngModulus (float):   Young modulus in Hooke's law
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

    triangleInfo: Data[SofaArray] 
    'Internal triangle data'

    edgeInfo: Data[SofaArray] 
    'Internal edge data'

    initialPoints: Data[SofaArray] 
    'Initial Position'

    poissonRatio: Data[float] 
    'Poisson ratio in Hookes law'

    youngModulus: Data[float] 
    'Young modulus in Hookes law'

    dampingRatio: Data[float] 
    'Ratio damping/stiffness'

    useAngularSprings: Data[bool] 
    'If Angular Springs should be used or not'

    compressible: Data[bool] 
    'If additional energy penalizing compressibility should be used'

    matrixRegularization: Data[float] 
    'Regularization of the Stiffnes Matrix (between 0 and 1)'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the TriangularBiquadraticSpringsForceField component"""

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

        triangleInfo: Optional[SofaArray | LinkPath] = None 
        'Internal triangle data'

        edgeInfo: Optional[SofaArray | LinkPath] = None 
        'Internal edge data'

        initialPoints: Optional[SofaArray | LinkPath] = None 
        'Initial Position'

        poissonRatio: Optional[float | LinkPath] = None 
        'Poisson ratio in Hookes law'

        youngModulus: Optional[float | LinkPath] = None 
        'Young modulus in Hookes law'

        dampingRatio: Optional[float | LinkPath] = None 
        'Ratio damping/stiffness'

        useAngularSprings: Optional[bool | LinkPath] = None 
        'If Angular Springs should be used or not'

        compressible: Optional[bool | LinkPath] = None 
        'If additional energy penalizing compressibility should be used'

        matrixRegularization: Optional[float | LinkPath] = None 
        'Regularization of the Stiffnes Matrix (between 0 and 1)'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return TriangularBiquadraticSpringsForceField.Parameters()
