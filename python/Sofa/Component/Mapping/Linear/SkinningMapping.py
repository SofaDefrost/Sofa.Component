# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component SkinningMapping

.. autofunction:: SkinningMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class SkinningMapping(Object):
    """skin a model from a set of rigid dofs"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,mapForces: Optional[bool] = None,mapConstraints: Optional[bool] = None,mapMasses: Optional[bool] = None,mapMatrices: Optional[bool] = None,applyRestPosition: Optional[bool] = None,initPos: Optional[SofaArray] = None,nbRef: Optional[SofaArray] = None,indices: Optional[SofaArray] = None,weight: Optional[SofaArray] = None,showFromIndex: Optional[int] = None,showWeights: Optional[bool] = None):
        """skin a model from a set of rigid dofs
        
        Args:
           applyRestPosition (bool):   set to true to apply this mapping to restPosition at init
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           indices (SofaArray):   parent indices for each child.
           initPos (SofaArray):   initial child coordinates in the world reference frame.
           listening (bool):   if true, handle the events, otherwise ignore the events
           mapConstraints (bool):   Are constraints mapped ?
           mapForces (bool):   Are forces mapped ?
           mapMasses (bool):   Are masses mapped ?
           mapMatrices (bool):   Are matrix explicit mapped?
           name (str):   object name
           nbRef (SofaArray):   Number of primitives influencing each point.
           printLog (bool):   if true, emits extra messages at runtime.
           showFromIndex (int):   Displayed From Index.
           showWeights (bool):   Show influence.
           tags (object):   list of the subsets the objet belongs to
           weight (SofaArray):   influence weights of the Dofs.
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

    initPos: Data[SofaArray] 
    'initial child coordinates in the world reference frame.'

    nbRef: Data[SofaArray] 
    'Number of primitives influencing each point.'

    indices: Data[SofaArray] 
    'parent indices for each child.'

    weight: Data[SofaArray] 
    'influence weights of the Dofs.'

    showFromIndex: Data[int] 
    'Displayed From Index.'

    showWeights: Data[bool] 
    'Show influence.'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the SkinningMapping component"""

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

        initPos: Optional[SofaArray | LinkPath] = None 
        'initial child coordinates in the world reference frame.'

        nbRef: Optional[SofaArray | LinkPath] = None 
        'Number of primitives influencing each point.'

        indices: Optional[SofaArray | LinkPath] = None 
        'parent indices for each child.'

        weight: Optional[SofaArray | LinkPath] = None 
        'influence weights of the Dofs.'

        showFromIndex: Optional[int | LinkPath] = None 
        'Displayed From Index.'

        showWeights: Optional[bool | LinkPath] = None 
        'Show influence.'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return SkinningMapping.Parameters()
