# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component SubsetMapping

.. autofunction:: SubsetMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class SubsetMapping(Object):
    """TODO-SubsetMappingClass"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,mapForces: Optional[bool] = None,mapConstraints: Optional[bool] = None,mapMasses: Optional[bool] = None,mapMatrices: Optional[bool] = None,applyRestPosition: Optional[bool] = None,indices: Optional[SofaArray] = None,first: Optional[int] = None,last: Optional[int] = None,radius: Optional[float] = None,handleTopologyChange: Optional[bool] = None,ignoreNotFound: Optional[bool] = None,resizeToModel: Optional[bool] = None):
        """TODO-SubsetMappingClass
        
        Args:
           applyRestPosition (bool):   set to true to apply this mapping to restPosition at init
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           first (int):   first index (use if indices are sequential)
           handleTopologyChange (bool):   Enable support of topological changes for indices (disable if it is linked from SubsetTopologicalMapping::pointD2S)
           ignoreNotFound (bool):   True to ignore points that are not found in the input model, they will be treated as fixed points
           indices (SofaArray):   list of input indices
           last (int):   last index (use if indices are sequential)
           listening (bool):   if true, handle the events, otherwise ignore the events
           mapConstraints (bool):   Are constraints mapped ?
           mapForces (bool):   Are forces mapped ?
           mapMasses (bool):   Are masses mapped ?
           mapMatrices (bool):   Are matrix explicit mapped?
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           radius (float):   search radius to find corresponding points in case no indices are given
           resizeToModel (bool):   True to resize the output MechanicalState to match the size of indices
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

    mapForces: Data[bool] 
    'Are forces mapped ?'

    mapConstraints: Data[bool] 
    'Are constraints mapped ?'

    mapMasses: Data[bool] 
    'Are masses mapped ?'

    mapMatrices: Data[bool] 
    'Are matrix explicit mapped?'

    applyRestPosition: Data[bool] 
    'set to true to apply this mapping to restPosition at init'

    indices: Data[SofaArray] 
    'list of input indices'

    first: Data[int] 
    'first index (use if indices are sequential)'

    last: Data[int] 
    'last index (use if indices are sequential)'

    radius: Data[float] 
    'search radius to find corresponding points in case no indices are given'

    handleTopologyChange: Data[bool] 
    'Enable support of topological changes for indices (disable if it is linked from SubsetTopologicalMapping::pointD2S)'

    ignoreNotFound: Data[bool] 
    'True to ignore points that are not found in the input model, they will be treated as fixed points'

    resizeToModel: Data[bool] 
    'True to resize the output MechanicalState to match the size of indices'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the SubsetMapping component"""

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

        mapForces: Optional[bool | LinkPath] = None 
        'Are forces mapped ?'

        mapConstraints: Optional[bool | LinkPath] = None 
        'Are constraints mapped ?'

        mapMasses: Optional[bool | LinkPath] = None 
        'Are masses mapped ?'

        mapMatrices: Optional[bool | LinkPath] = None 
        'Are matrix explicit mapped?'

        applyRestPosition: Optional[bool | LinkPath] = None 
        'set to true to apply this mapping to restPosition at init'

        indices: Optional[SofaArray | LinkPath] = None 
        'list of input indices'

        first: Optional[int | LinkPath] = None 
        'first index (use if indices are sequential)'

        last: Optional[int | LinkPath] = None 
        'last index (use if indices are sequential)'

        radius: Optional[float | LinkPath] = None 
        'search radius to find corresponding points in case no indices are given'

        handleTopologyChange: Optional[bool | LinkPath] = None 
        'Enable support of topological changes for indices (disable if it is linked from SubsetTopologicalMapping::pointD2S)'

        ignoreNotFound: Optional[bool | LinkPath] = None 
        'True to ignore points that are not found in the input model, they will be treated as fixed points'

        resizeToModel: Optional[bool | LinkPath] = None 
        'True to resize the output MechanicalState to match the size of indices'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return SubsetMapping.Parameters()
