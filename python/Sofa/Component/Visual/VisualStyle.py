# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component VisualStyle

.. autofunction:: VisualStyle

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class VisualStyle(Object):
    """Edit the visual style.
 Allowed values for displayFlags data are a combination of the following:
showAll, hideAll,
    showVisual, hideVisual,
        showVisualModels, hideVisualModels,
    showBehavior, hideBehavior,
        showBehaviorModels, hideBehaviorModels,
        showForceFields, hideForceFields,
        showInteractionForceFields, hideInteractionForceFields
    showMapping, hideMapping
        showMappings, hideMappings
        showMechanicalMappings, hideMechanicalMappings
    showCollision, hideCollision
        showCollisionModels, hideCollisionModels
        showBoundingCollisionModels, hideBoundingCollisionModels
    showOptions hideOptions
        showRendering hideRendering
        showNormals hideNormals
        showWireframe hideWireframe"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,enable: Optional[bool] = None,displayFlags: Optional[object] = None):
        """Edit the visual style.
 Allowed values for displayFlags data are a combination of the following:
showAll, hideAll,
    showVisual, hideVisual,
        showVisualModels, hideVisualModels,
    showBehavior, hideBehavior,
        showBehaviorModels, hideBehaviorModels,
        showForceFields, hideForceFields,
        showInteractionForceFields, hideInteractionForceFields
    showMapping, hideMapping
        showMappings, hideMappings
        showMechanicalMappings, hideMechanicalMappings
    showCollision, hideCollision
        showCollisionModels, hideCollisionModels
        showBoundingCollisionModels, hideBoundingCollisionModels
    showOptions hideOptions
        showRendering hideRendering
        showNormals hideNormals
        showWireframe hideWireframe
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           displayFlags (object):   Display Flags
           enable (bool):   Display the object or not
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
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

    enable: Data[bool] 
    'Display the object or not'

    displayFlags: Data[object] 
    'Display Flags'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the VisualStyle component"""

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

        enable: Optional[bool | LinkPath] = None 
        'Display the object or not'

        displayFlags: Optional[object | LinkPath] = None 
        'Display Flags'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return VisualStyle.Parameters()
