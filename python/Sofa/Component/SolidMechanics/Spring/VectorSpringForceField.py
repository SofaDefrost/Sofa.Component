# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component VectorSpringForceField

.. autofunction:: VectorSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class VectorSpringForceField(Object):
    """Spring force field acting along the edges of a mesh"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,springs: Optional[SofaArray] = None,filename: Optional[str] = None,stiffness: Optional[float] = None,viscosity: Optional[float] = None,useTopology: Optional[bool] = None):
        """Spring force field acting along the edges of a mesh
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           filename (str):   File name from which the spring informations are loaded
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           springs (SofaArray):   springs data
           stiffness (float):   Default edge stiffness used in absence of file information
           tags (object):   list of the subsets the objet belongs to
           useTopology (bool):   Activate/Desactivate topology mode of the component (springs on each edge)
           viscosity (float):   Default edge viscosity used in absence of file information
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

    springs: Data[SofaArray] 
    'springs data'

    filename: Data[str] 
    'File name from which the spring informations are loaded'

    stiffness: Data[float] 
    'Default edge stiffness used in absence of file information'

    viscosity: Data[float] 
    'Default edge viscosity used in absence of file information'

    useTopology: Data[bool] 
    'Activate/Desactivate topology mode of the component (springs on each edge)'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the VectorSpringForceField component"""

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

        springs: Optional[SofaArray | LinkPath] = None 
        'springs data'

        filename: Optional[str | LinkPath] = None 
        'File name from which the spring informations are loaded'

        stiffness: Optional[float | LinkPath] = None 
        'Default edge stiffness used in absence of file information'

        viscosity: Optional[float | LinkPath] = None 
        'Default edge viscosity used in absence of file information'

        useTopology: Optional[bool | LinkPath] = None 
        'Activate/Desactivate topology mode of the component (springs on each edge)'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return VectorSpringForceField.Parameters()
