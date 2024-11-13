# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component RecordedCamera

.. autofunction:: RecordedCamera

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class RecordedCamera(Object):
    """A camera that is moving along a predetermined path."""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,position: Optional[SofaArray] = None,orientation: Optional[SofaArray] = None,lookAt: Optional[SofaArray] = None,distance: Optional[float] = None,fieldOfView: Optional[float] = None,zNear: Optional[float] = None,zFar: Optional[float] = None,computeZClip: Optional[bool] = None,minBBox: Optional[SofaArray] = None,maxBBox: Optional[SofaArray] = None,widthViewport: Optional[int] = None,heightViewport: Optional[int] = None,projectionType: Optional[object] = None,activated: Optional[bool] = None,fixedLookAt: Optional[bool] = None,modelViewMatrix: Optional[SofaArray] = None,projectionMatrix: Optional[SofaArray] = None,zoomSpeed: Optional[float] = None,panSpeed: Optional[float] = None,pivot: Optional[int] = None,startTime: Optional[float] = None,endTime: Optional[float] = None,rotationMode: Optional[bool] = None,translationMode: Optional[bool] = None,navigationMode: Optional[bool] = None,rotationSpeed: Optional[float] = None,rotationCenter: Optional[SofaArray] = None,rotationStartPoint: Optional[SofaArray] = None,rotationLookAt: Optional[SofaArray] = None,rotationAxis: Optional[SofaArray] = None,cameraUp: Optional[SofaArray] = None,drawRotation: Optional[bool] = None,drawTranslation: Optional[bool] = None,cameraPositions: Optional[SofaArray] = None,cameraOrientations: Optional[SofaArray] = None):
        """A camera that is moving along a predetermined path.
        
        Args:
           activated (bool):   Camera activated ?
           bbox (object):   this object bounding box
           cameraOrientations (SofaArray):   Intermediate camera's orientations
           cameraPositions (SofaArray):   Intermediate camera's positions
           cameraUp (SofaArray):   Camera Up axis
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           computeZClip (bool):   Compute Z clip planes (Near and Far) according to the bounding box
           distance (float):   Distance between camera and look at
           drawRotation (bool):   If true, will draw the rotation path
           drawTranslation (bool):   If true, will draw the translation path
           endTime (float):   Time when the camera moves will end (or loop)
           fieldOfView (float):   Camera's FOV
           fixedLookAt (bool):   keep the lookAt point always fixed
           heightViewport (int):   heightViewport
           listening (bool):   if true, handle the events, otherwise ignore the events
           lookAt (SofaArray):   Camera's look at
           maxBBox (SofaArray):   maxBBox
           minBBox (SofaArray):   minBBox
           modelViewMatrix (SofaArray):   ModelView Matrix
           name (str):   object name
           navigationMode (bool):   If true, navigation will be performed
           orientation (SofaArray):   Camera's orientation
           panSpeed (float):   Pan Speed
           pivot (int):   Pivot (0 => Scene center, 1 => World Center
           position (SofaArray):   Camera's position
           printLog (bool):   if true, emits extra messages at runtime.
           projectionMatrix (SofaArray):   Projection Matrix
           projectionType (object):   Camera Type (0 = Perspective, 1 = Orthographic)
           rotationAxis (SofaArray):   Rotation axis
           rotationCenter (SofaArray):   Rotation center coordinates
           rotationLookAt (SofaArray):   Position to be focused during rotation
           rotationMode (bool):   If true, rotation will be performed
           rotationSpeed (float):   rotation Speed
           rotationStartPoint (SofaArray):   Rotation start position coordinates
           startTime (float):   Time when the camera moves will start
           tags (object):   list of the subsets the objet belongs to
           translationMode (bool):   If true, translation will be performed
           widthViewport (int):   widthViewport
           zFar (float):   Camera's zFar
           zNear (float):   Camera's zNear
           zoomSpeed (float):   Zoom Speed
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

    zoomSpeed: Data[float] 
    'Zoom Speed'

    panSpeed: Data[float] 
    'Pan Speed'

    pivot: Data[int] 
    'Pivot (0 => Scene center, 1 => World Center'

    startTime: Data[float] 
    'Time when the camera moves will start'

    endTime: Data[float] 
    'Time when the camera moves will end (or loop)'

    rotationMode: Data[bool] 
    'If true, rotation will be performed'

    translationMode: Data[bool] 
    'If true, translation will be performed'

    navigationMode: Data[bool] 
    'If true, navigation will be performed'

    rotationSpeed: Data[float] 
    'rotation Speed'

    rotationCenter: Data[SofaArray] 
    'Rotation center coordinates'

    rotationStartPoint: Data[SofaArray] 
    'Rotation start position coordinates'

    rotationLookAt: Data[SofaArray] 
    'Position to be focused during rotation'

    rotationAxis: Data[SofaArray] 
    'Rotation axis'

    cameraUp: Data[SofaArray] 
    'Camera Up axis'

    drawRotation: Data[bool] 
    'If true, will draw the rotation path'

    drawTranslation: Data[bool] 
    'If true, will draw the translation path'

    cameraPositions: Data[SofaArray] 
    'Intermediate cameras positions'

    cameraOrientations: Data[SofaArray] 
    'Intermediate cameras orientations'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the RecordedCamera component"""

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

        zoomSpeed: Optional[float | LinkPath] = None 
        'Zoom Speed'

        panSpeed: Optional[float | LinkPath] = None 
        'Pan Speed'

        pivot: Optional[int | LinkPath] = None 
        'Pivot (0 => Scene center, 1 => World Center'

        startTime: Optional[float | LinkPath] = None 
        'Time when the camera moves will start'

        endTime: Optional[float | LinkPath] = None 
        'Time when the camera moves will end (or loop)'

        rotationMode: Optional[bool | LinkPath] = None 
        'If true, rotation will be performed'

        translationMode: Optional[bool | LinkPath] = None 
        'If true, translation will be performed'

        navigationMode: Optional[bool | LinkPath] = None 
        'If true, navigation will be performed'

        rotationSpeed: Optional[float | LinkPath] = None 
        'rotation Speed'

        rotationCenter: Optional[SofaArray | LinkPath] = None 
        'Rotation center coordinates'

        rotationStartPoint: Optional[SofaArray | LinkPath] = None 
        'Rotation start position coordinates'

        rotationLookAt: Optional[SofaArray | LinkPath] = None 
        'Position to be focused during rotation'

        rotationAxis: Optional[SofaArray | LinkPath] = None 
        'Rotation axis'

        cameraUp: Optional[SofaArray | LinkPath] = None 
        'Camera Up axis'

        drawRotation: Optional[bool | LinkPath] = None 
        'If true, will draw the rotation path'

        drawTranslation: Optional[bool | LinkPath] = None 
        'If true, will draw the translation path'

        cameraPositions: Optional[SofaArray | LinkPath] = None 
        'Intermediate cameras positions'

        cameraOrientations: Optional[SofaArray | LinkPath] = None 
        'Intermediate cameras orientations'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return RecordedCamera.Parameters()
