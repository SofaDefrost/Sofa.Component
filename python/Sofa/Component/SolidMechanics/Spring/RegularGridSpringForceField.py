# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component RegularGridSpringForceField

.. autofunction:: RegularGridSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class RegularGridSpringForceField(Object):
    """Spring acting on the edges and faces of a regular grid"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,stiffness: Optional[float] = None,damping: Optional[float] = None,showArrowSize: Optional[float] = None,drawMode: Optional[int] = None,spring: Optional[SofaArray] = None,springsIndices1: Optional[SofaArray] = None,springsIndices2: Optional[SofaArray] = None,indices1: Optional[SofaArray] = None,indices2: Optional[SofaArray] = None,lengths: Optional[SofaArray] = None,linesStiffness: Optional[float] = None,linesDamping: Optional[float] = None,quadsStiffness: Optional[float] = None,quadsDamping: Optional[float] = None,cubesStiffness: Optional[float] = None,cubesDamping: Optional[float] = None):
        """Spring acting on the edges and faces of a regular grid
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           cubesDamping (float):   Cubes Damping
           cubesStiffness (float):   Cubes Stiffness
           damping (float):   uniform damping for the all springs
           drawMode (int):   The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow
           indices1 (SofaArray):   Indices of the source points on the first model
           indices2 (SofaArray):   Indices of the fixed points on the second model
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           lengths (SofaArray):   List of lengths to create the springs. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, 0 will be applied everywhere
           linesDamping (float):   Lines Damping
           linesStiffness (float):   Lines Stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           quadsDamping (float):   Quads Damping
           quadsStiffness (float):   Quads Stiffness
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           showArrowSize (float):   size of the axis
           spring (SofaArray):   pairs of indices, stiffness, damping, rest length
           springsIndices1 (SofaArray):   List of indices in springs from the first mstate
           springsIndices2 (SofaArray):   List of indices in springs from the second mstate
           stiffness (float):   uniform stiffness for the all springs
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

    stiffness: Data[float] 
    'uniform stiffness for the all springs'

    damping: Data[float] 
    'uniform damping for the all springs'

    showArrowSize: Data[float] 
    'size of the axis'

    drawMode: Data[int] 
    'The way springs will be drawn:- 0: Line- 1:Cylinder- 2: Arrow'

    spring: Data[SofaArray] 
    'pairs of indices, stiffness, damping, rest length'

    springsIndices1: Data[SofaArray] 
    'List of indices in springs from the first mstate'

    springsIndices2: Data[SofaArray] 
    'List of indices in springs from the second mstate'

    indices1: Data[SofaArray] 
    'Indices of the source points on the first model'

    indices2: Data[SofaArray] 
    'Indices of the fixed points on the second model'

    lengths: Data[SofaArray] 
    'List of lengths to create the springs. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, 0 will be applied everywhere'

    linesStiffness: Data[float] 
    'Lines Stiffness'

    linesDamping: Data[float] 
    'Lines Damping'

    quadsStiffness: Data[float] 
    'Quads Stiffness'

    quadsDamping: Data[float] 
    'Quads Damping'

    cubesStiffness: Data[float] 
    'Cubes Stiffness'

    cubesDamping: Data[float] 
    'Cubes Damping'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the RegularGridSpringForceField component"""

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

        stiffness: Optional[float | LinkPath] = None 
        'uniform stiffness for the all springs'

        damping: Optional[float | LinkPath] = None 
        'uniform damping for the all springs'

        showArrowSize: Optional[float | LinkPath] = None 
        'size of the axis'

        drawMode: Optional[int | LinkPath] = None 
        'The way springs will be drawn:- 0: Line- 1:Cylinder- 2: Arrow'

        spring: Optional[SofaArray | LinkPath] = None 
        'pairs of indices, stiffness, damping, rest length'

        springsIndices1: Optional[SofaArray | LinkPath] = None 
        'List of indices in springs from the first mstate'

        springsIndices2: Optional[SofaArray | LinkPath] = None 
        'List of indices in springs from the second mstate'

        indices1: Optional[SofaArray | LinkPath] = None 
        'Indices of the source points on the first model'

        indices2: Optional[SofaArray | LinkPath] = None 
        'Indices of the fixed points on the second model'

        lengths: Optional[SofaArray | LinkPath] = None 
        'List of lengths to create the springs. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, 0 will be applied everywhere'

        linesStiffness: Optional[float | LinkPath] = None 
        'Lines Stiffness'

        linesDamping: Optional[float | LinkPath] = None 
        'Lines Damping'

        quadsStiffness: Optional[float | LinkPath] = None 
        'Quads Stiffness'

        quadsDamping: Optional[float | LinkPath] = None 
        'Quads Damping'

        cubesStiffness: Optional[float | LinkPath] = None 
        'Cubes Stiffness'

        cubesDamping: Optional[float | LinkPath] = None 
        'Cubes Damping'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return RegularGridSpringForceField.Parameters()