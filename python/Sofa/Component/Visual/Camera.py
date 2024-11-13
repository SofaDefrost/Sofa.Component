# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component Camera

.. autofunction:: Camera

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class Camera(Object):
    """A Camera that render the scene from a given location & orientation."""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,position: Optional[SofaArray] = None,orientation: Optional[SofaArray] = None,lookAt: Optional[SofaArray] = None,distance: Optional[float] = None,fieldOfView: Optional[float] = None,zNear: Optional[float] = None,zFar: Optional[float] = None,computeZClip: Optional[bool] = None,minBBox: Optional[SofaArray] = None,maxBBox: Optional[SofaArray] = None,widthViewport: Optional[int] = None,heightViewport: Optional[int] = None,projectionType: Optional[object] = None,activated: Optional[bool] = None,fixedLookAt: Optional[bool] = None,modelViewMatrix: Optional[SofaArray] = None,projectionMatrix: Optional[SofaArray] = None):
        """A Camera that render the scene from a given location & orientation.
        
        Args:
           activated (bool):   Camera activated ?
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           computeZClip (bool):   Compute Z clip planes (Near and Far) according to the bounding box
           distance (float):   Distance between camera and look at
           fieldOfView (float):   Camera's FOV
           fixedLookAt (bool):   keep the lookAt point always fixed
           heightViewport (int):   heightViewport
           listening (bool):   if true, handle the events, otherwise ignore the events
           lookAt (SofaArray):   Camera's look at
           maxBBox (SofaArray):   maxBBox
           minBBox (SofaArray):   minBBox
           modelViewMatrix (SofaArray):   ModelView Matrix
           name (str):   object name
           orientation (SofaArray):   Camera's orientation
           position (SofaArray):   Camera's position
           printLog (bool):   if true, emits extra messages at runtime.
           projectionMatrix (SofaArray):   Projection Matrix
           projectionType (object):   Camera Type (0 = Perspective, 1 = Orthographic)
           tags (object):   list of the subsets the objet belongs to
           widthViewport (int):   widthViewport
           zFar (float):   Camera's zFar
           zNear (float):   Camera's zNear
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

    position: Data[SofaArray] 
    'Cameras position'

    orientation: Data[SofaArray] 
    'Cameras orientation'

    lookAt: Data[SofaArray] 
    'Cameras look at'

    distance: Data[float] 
    'Distance between camera and look at'

    fieldOfView: Data[float] 
    'Cameras FOV'

    zNear: Data[float] 
    'Cameras zNear'

    zFar: Data[float] 
    'Cameras zFar'

    computeZClip: Data[bool] 
    'Compute Z clip planes (Near and Far) according to the bounding box'

    minBBox: Data[SofaArray] 
    'minBBox'

    maxBBox: Data[SofaArray] 
    'maxBBox'

    widthViewport: Data[int] 
    'widthViewport'

    heightViewport: Data[int] 
    'heightViewport'

    projectionType: Data[object] 
    'Camera Type (0 = Perspective, 1 = Orthographic)'

    activated: Data[bool] 
    'Camera activated ?'

    fixedLookAt: Data[bool] 
    'keep the lookAt point always fixed'

    modelViewMatrix: Data[SofaArray] 
    'ModelView Matrix'

    projectionMatrix: Data[SofaArray] 
    'Projection Matrix'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the Camera component"""

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

        position: Optional[SofaArray | LinkPath] = None 
        'Cameras position'

        orientation: Optional[SofaArray | LinkPath] = None 
        'Cameras orientation'

        lookAt: Optional[SofaArray | LinkPath] = None 
        'Cameras look at'

        distance: Optional[float | LinkPath] = None 
        'Distance between camera and look at'

        fieldOfView: Optional[float | LinkPath] = None 
        'Cameras FOV'

        zNear: Optional[float | LinkPath] = None 
        'Cameras zNear'

        zFar: Optional[float | LinkPath] = None 
        'Cameras zFar'

        computeZClip: Optional[bool | LinkPath] = None 
        'Compute Z clip planes (Near and Far) according to the bounding box'

        minBBox: Optional[SofaArray | LinkPath] = None 
        'minBBox'

        maxBBox: Optional[SofaArray | LinkPath] = None 
        'maxBBox'

        widthViewport: Optional[int | LinkPath] = None 
        'widthViewport'

        heightViewport: Optional[int | LinkPath] = None 
        'heightViewport'

        projectionType: Optional[object | LinkPath] = None 
        'Camera Type (0 = Perspective, 1 = Orthographic)'

        activated: Optional[bool | LinkPath] = None 
        'Camera activated ?'

        fixedLookAt: Optional[bool | LinkPath] = None 
        'keep the lookAt point always fixed'

        modelViewMatrix: Optional[SofaArray | LinkPath] = None 
        'ModelView Matrix'

        projectionMatrix: Optional[SofaArray | LinkPath] = None 
        'Projection Matrix'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return Camera.Parameters()
