# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component ConstantSparsityPatternSystem

.. autofunction:: ConstantSparsityPatternSystem

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class ConstantSparsityPatternSystem(Object):
    """Linear system taking advantage of the constant sparsity pattern of the global matrix to speed up the matrix assembly. Do not use if sparsity pattern is not constant (topological changes, ...)."""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,matrixSize: Optional[SofaArray] = None,assembleStiffness: Optional[bool] = None,assembleMass: Optional[bool] = None,assembleDamping: Optional[bool] = None,assembleGeometricStiffness: Optional[bool] = None,applyProjectiveConstraints: Optional[bool] = None,applyMappedComponents: Optional[bool] = None,checkIndices: Optional[bool] = None,parallelAssemblyIndependentMatrices: Optional[bool] = None):
        """Linear system taking advantage of the constant sparsity pattern of the global matrix to speed up the matrix assembly. Do not use if sparsity pattern is not constant (topological changes, ...).
        
        Args:
           applyMappedComponents (bool):   If true, mapped components contribute to the global matrix
           applyProjectiveConstraints (bool):   If true, projective constraints are applied on the global matrix
           assembleDamping (bool):   If true, the damping is added to the global matrix
           assembleGeometricStiffness (bool):   If true, the geometric stiffness of mappings is added to the global matrix
           assembleMass (bool):   If true, the mass is added to the global matrix
           assembleStiffness (bool):   If true, the stiffness is added to the global matrix
           bbox (object):   this object bounding box
           checkIndices (bool):   If true, indices are verified before being added in to the global matrix, favoring security over speed
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           listening (bool):   if true, handle the events, otherwise ignore the events
           matrixSize (SofaArray):   Size of the global matrix
           name (str):   object name
           parallelAssemblyIndependentMatrices (bool):   If true, independent matrices (global matrix vs mapped matrices) are assembled in parallel
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

    matrixSize: Data[SofaArray] 
    'Size of the global matrix'

    assembleStiffness: Data[bool] 
    'If true, the stiffness is added to the global matrix'

    assembleMass: Data[bool] 
    'If true, the mass is added to the global matrix'

    assembleDamping: Data[bool] 
    'If true, the damping is added to the global matrix'

    assembleGeometricStiffness: Data[bool] 
    'If true, the geometric stiffness of mappings is added to the global matrix'

    applyProjectiveConstraints: Data[bool] 
    'If true, projective constraints are applied on the global matrix'

    applyMappedComponents: Data[bool] 
    'If true, mapped components contribute to the global matrix'

    checkIndices: Data[bool] 
    'If true, indices are verified before being added in to the global matrix, favoring security over speed'

    parallelAssemblyIndependentMatrices: Data[bool] 
    'If true, independent matrices (global matrix vs mapped matrices) are assembled in parallel'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the ConstantSparsityPatternSystem component"""

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

        matrixSize: Optional[SofaArray | LinkPath] = None 
        'Size of the global matrix'

        assembleStiffness: Optional[bool | LinkPath] = None 
        'If true, the stiffness is added to the global matrix'

        assembleMass: Optional[bool | LinkPath] = None 
        'If true, the mass is added to the global matrix'

        assembleDamping: Optional[bool | LinkPath] = None 
        'If true, the damping is added to the global matrix'

        assembleGeometricStiffness: Optional[bool | LinkPath] = None 
        'If true, the geometric stiffness of mappings is added to the global matrix'

        applyProjectiveConstraints: Optional[bool | LinkPath] = None 
        'If true, projective constraints are applied on the global matrix'

        applyMappedComponents: Optional[bool | LinkPath] = None 
        'If true, mapped components contribute to the global matrix'

        checkIndices: Optional[bool | LinkPath] = None 
        'If true, indices are verified before being added in to the global matrix, favoring security over speed'

        parallelAssemblyIndependentMatrices: Optional[bool | LinkPath] = None 
        'If true, independent matrices (global matrix vs mapped matrices) are assembled in parallel'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return ConstantSparsityPatternSystem.Parameters()
