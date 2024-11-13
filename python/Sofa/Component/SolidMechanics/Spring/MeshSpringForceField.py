# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component MeshSpringForceField

.. autofunction:: MeshSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class MeshSpringForceField(Object):
    """Spring force field acting along the edges of a mesh"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,stiffness: Optional[float] = None,damping: Optional[float] = None,showArrowSize: Optional[float] = None,drawMode: Optional[int] = None,spring: Optional[SofaArray] = None,springsIndices1: Optional[SofaArray] = None,springsIndices2: Optional[SofaArray] = None,indices1: Optional[SofaArray] = None,indices2: Optional[SofaArray] = None,lengths: Optional[SofaArray] = None,linesStiffness: Optional[float] = None,linesDamping: Optional[float] = None,trianglesStiffness: Optional[float] = None,trianglesDamping: Optional[float] = None,quadsStiffness: Optional[float] = None,quadsDamping: Optional[float] = None,tetrahedraStiffness: Optional[float] = None,tetrahedraDamping: Optional[float] = None,cubesStiffness: Optional[float] = None,cubesDamping: Optional[float] = None,noCompression: Optional[bool] = None,drawMinElongationRange: Optional[float] = None,drawMaxElongationRange: Optional[float] = None,drawSpringSize: Optional[float] = None,localRange: Optional[SofaArray] = None):
        """Spring force field acting along the edges of a mesh
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           cubesDamping (float):   Damping for the Cubes
           cubesStiffness (float):   Stiffness for the Cubes
           damping (float):   uniform damping for the all springs
           drawMaxElongationRange (float):   Max range of elongation (red eongation - blue neutral - green compression)
           drawMinElongationRange (float):   Min range of elongation (red eongation - blue neutral - green compression)
           drawMode (int):   The way springs will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow
           drawSpringSize (float):   Size of drawed lines
           indices1 (SofaArray):   Indices of the source points on the first model
           indices2 (SofaArray):   Indices of the fixed points on the second model
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           lengths (SofaArray):   List of lengths to create the springs. Must have the same than indices1 & indices2, or if only one element, it will be applied to all springs. If empty, 0 will be applied everywhere
           linesDamping (float):   Damping for the Lines
           linesStiffness (float):   Stiffness for the Lines
           listening (bool):   if true, handle the events, otherwise ignore the events
           localRange (SofaArray):   optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)
           name (str):   object name
           noCompression (bool):   Only consider elongation
           printLog (bool):   if true, emits extra messages at runtime.
           quadsDamping (float):   Damping for the Quads
           quadsStiffness (float):   Stiffness for the Quads
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           showArrowSize (float):   size of the axis
           spring (SofaArray):   pairs of indices, stiffness, damping, rest length
           springsIndices1 (SofaArray):   List of indices in springs from the first mstate
           springsIndices2 (SofaArray):   List of indices in springs from the second mstate
           stiffness (float):   uniform stiffness for the all springs
           tags (object):   list of the subsets the objet belongs to
           tetrahedraDamping (float):   Damping for the Tetrahedra
           tetrahedraStiffness (float):   Stiffness for the Tetrahedra
           trianglesDamping (float):   Damping for the Triangles
           trianglesStiffness (float):   Stiffness for the Triangles
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
    'Stiffness for the Lines'

    linesDamping: Data[float] 
    'Damping for the Lines'

    trianglesStiffness: Data[float] 
    'Stiffness for the Triangles'

    trianglesDamping: Data[float] 
    'Damping for the Triangles'

    quadsStiffness: Data[float] 
    'Stiffness for the Quads'

    quadsDamping: Data[float] 
    'Damping for the Quads'

    tetrahedraStiffness: Data[float] 
    'Stiffness for the Tetrahedra'

    tetrahedraDamping: Data[float] 
    'Damping for the Tetrahedra'

    cubesStiffness: Data[float] 
    'Stiffness for the Cubes'

    cubesDamping: Data[float] 
    'Damping for the Cubes'

    noCompression: Data[bool] 
    'Only consider elongation'

    drawMinElongationRange: Data[float] 
    'Min range of elongation (red eongation - blue neutral - green compression)'

    drawMaxElongationRange: Data[float] 
    'Max range of elongation (red eongation - blue neutral - green compression)'

    drawSpringSize: Data[float] 
    'Size of drawed lines'

    localRange: Data[SofaArray] 
    'optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the MeshSpringForceField component"""

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
        'Stiffness for the Lines'

        linesDamping: Optional[float | LinkPath] = None 
        'Damping for the Lines'

        trianglesStiffness: Optional[float | LinkPath] = None 
        'Stiffness for the Triangles'

        trianglesDamping: Optional[float | LinkPath] = None 
        'Damping for the Triangles'

        quadsStiffness: Optional[float | LinkPath] = None 
        'Stiffness for the Quads'

        quadsDamping: Optional[float | LinkPath] = None 
        'Damping for the Quads'

        tetrahedraStiffness: Optional[float | LinkPath] = None 
        'Stiffness for the Tetrahedra'

        tetrahedraDamping: Optional[float | LinkPath] = None 
        'Damping for the Tetrahedra'

        cubesStiffness: Optional[float | LinkPath] = None 
        'Stiffness for the Cubes'

        cubesDamping: Optional[float | LinkPath] = None 
        'Damping for the Cubes'

        noCompression: Optional[bool | LinkPath] = None 
        'Only consider elongation'

        drawMinElongationRange: Optional[float | LinkPath] = None 
        'Min range of elongation (red eongation - blue neutral - green compression)'

        drawMaxElongationRange: Optional[float | LinkPath] = None 
        'Max range of elongation (red eongation - blue neutral - green compression)'

        drawSpringSize: Optional[float | LinkPath] = None 
        'Size of drawed lines'

        localRange: Optional[SofaArray | LinkPath] = None 
        'optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return MeshSpringForceField.Parameters()
