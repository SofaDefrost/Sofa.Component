# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component VisualModelImpl

.. autofunction:: VisualModelImpl

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class VisualModelImpl(Object):
    """Generic visual model. If a viewer is active it will replace the VisualModel alias, otherwise nothing will be displayed."""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,enable: Optional[bool] = None,position: Optional[SofaArray] = None,restPosition: Optional[SofaArray] = None,normal: Optional[SofaArray] = None,initRestPositions: Optional[bool] = None,useNormals: Optional[bool] = None,updateNormals: Optional[bool] = None,computeTangents: Optional[bool] = None,updateTangents: Optional[bool] = None,handleDynamicTopology: Optional[bool] = None,fixMergedUVSeams: Optional[bool] = None,keepLines: Optional[bool] = None,vertices: Optional[SofaArray] = None,texcoords: Optional[SofaArray] = None,tangents: Optional[SofaArray] = None,bitangents: Optional[SofaArray] = None,edges: Optional[SofaArray] = None,triangles: Optional[SofaArray] = None,quads: Optional[SofaArray] = None,vertPosIdx: Optional[SofaArray] = None,vertNormIdx: Optional[SofaArray] = None,filename: Optional[str] = None,texturename: Optional[str] = None,translation: Optional[SofaArray] = None,rotation: Optional[SofaArray] = None,scale3d: Optional[SofaArray] = None,scaleTex: Optional[SofaArray] = None,translationTex: Optional[SofaArray] = None,material: Optional[object] = None,putOnlyTexCoords: Optional[bool] = None,srgbTexturing: Optional[bool] = None,materials: Optional[SofaArray] = None,groups: Optional[SofaArray] = None):
        """Generic visual model. If a viewer is active it will replace the VisualModel alias, otherwise nothing will be displayed.
        
        Args:
           bbox (object):   this object bounding box
           bitangents (SofaArray):   tangents for normal mapping
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           computeTangents (bool):   True if tangents should be computed at startup
           edges (SofaArray):   edges of the model
           enable (bool):   Display the object or not
           filename (str):    Path to an ogl model
           fixMergedUVSeams (bool):   True if UV seams should be handled even when duplicate UVs are merged
           groups (SofaArray):   Groups of triangles and quads using a given material
           handleDynamicTopology (bool):   True if topological changes should be handled
           initRestPositions (bool):   True if rest positions must be initialized with initial positions
           keepLines (bool):   keep and draw lines (false by default)
           listening (bool):   if true, handle the events, otherwise ignore the events
           material (object):   Material
           materials (SofaArray):   List of materials
           name (str):   object name
           normal (SofaArray):   Normals of the model
           position (SofaArray):   Vertices coordinates
           printLog (bool):   if true, emits extra messages at runtime.
           putOnlyTexCoords (bool):   Give Texture Coordinates without the texture binding
           quads (SofaArray):   quads of the model
           restPosition (SofaArray):   Vertices rest coordinates
           rotation (SofaArray):   Initial Rotation of the object
           scale3d (SofaArray):   Initial Scale of the object
           scaleTex (SofaArray):   Scale of the texture
           srgbTexturing (bool):   When sRGB rendering is enabled, is the texture in sRGB colorspace?
           tags (object):   list of the subsets the objet belongs to
           tangents (SofaArray):   tangents for normal mapping
           texcoords (SofaArray):   coordinates of the texture
           texturename (str):   Name of the Texture
           translation (SofaArray):   Initial Translation of the object
           translationTex (SofaArray):   Translation of the texture
           triangles (SofaArray):   triangles of the model
           updateNormals (bool):   True if normals should be updated at each iteration
           updateTangents (bool):   True if tangents should be updated at each iteration
           useNormals (bool):   True if normal smoothing groups should be read from file
           vertNormIdx (SofaArray):   If vertices have multiple normals/texcoords stores vertices normal indices
           vertPosIdx (SofaArray):   If vertices have multiple normals/texcoords stores vertices position indices
           vertices (SofaArray):   vertices of the model (only if vertices have multiple normals/texcoords, otherwise positions are used)
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

    position: Data[SofaArray] 
    'Vertices coordinates'

    restPosition: Data[SofaArray] 
    'Vertices rest coordinates'

    normal: Data[SofaArray] 
    'Normals of the model'

    initRestPositions: Data[bool] 
    'True if rest positions must be initialized with initial positions'

    useNormals: Data[bool] 
    'True if normal smoothing groups should be read from file'

    updateNormals: Data[bool] 
    'True if normals should be updated at each iteration'

    computeTangents: Data[bool] 
    'True if tangents should be computed at startup'

    updateTangents: Data[bool] 
    'True if tangents should be updated at each iteration'

    handleDynamicTopology: Data[bool] 
    'True if topological changes should be handled'

    fixMergedUVSeams: Data[bool] 
    'True if UV seams should be handled even when duplicate UVs are merged'

    keepLines: Data[bool] 
    'keep and draw lines (false by default)'

    vertices: Data[SofaArray] 
    'vertices of the model (only if vertices have multiple normals/texcoords, otherwise positions are used)'

    texcoords: Data[SofaArray] 
    'coordinates of the texture'

    tangents: Data[SofaArray] 
    'tangents for normal mapping'

    bitangents: Data[SofaArray] 
    'tangents for normal mapping'

    edges: Data[SofaArray] 
    'edges of the model'

    triangles: Data[SofaArray] 
    'triangles of the model'

    quads: Data[SofaArray] 
    'quads of the model'

    vertPosIdx: Data[SofaArray] 
    'If vertices have multiple normals/texcoords stores vertices position indices'

    vertNormIdx: Data[SofaArray] 
    'If vertices have multiple normals/texcoords stores vertices normal indices'

    filename: Data[str] 
    ' Path to an ogl model'

    texturename: Data[str] 
    'Name of the Texture'

    translation: Data[SofaArray] 
    'Initial Translation of the object'

    rotation: Data[SofaArray] 
    'Initial Rotation of the object'

    scale3d: Data[SofaArray] 
    'Initial Scale of the object'

    scaleTex: Data[SofaArray] 
    'Scale of the texture'

    translationTex: Data[SofaArray] 
    'Translation of the texture'

    material: Data[object] 
    'Material'

    putOnlyTexCoords: Data[bool] 
    'Give Texture Coordinates without the texture binding'

    srgbTexturing: Data[bool] 
    'When sRGB rendering is enabled, is the texture in sRGB colorspace?'

    materials: Data[SofaArray] 
    'List of materials'

    groups: Data[SofaArray] 
    'Groups of triangles and quads using a given material'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the VisualModelImpl component"""

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

        position: Optional[SofaArray | LinkPath] = None 
        'Vertices coordinates'

        restPosition: Optional[SofaArray | LinkPath] = None 
        'Vertices rest coordinates'

        normal: Optional[SofaArray | LinkPath] = None 
        'Normals of the model'

        initRestPositions: Optional[bool | LinkPath] = None 
        'True if rest positions must be initialized with initial positions'

        useNormals: Optional[bool | LinkPath] = None 
        'True if normal smoothing groups should be read from file'

        updateNormals: Optional[bool | LinkPath] = None 
        'True if normals should be updated at each iteration'

        computeTangents: Optional[bool | LinkPath] = None 
        'True if tangents should be computed at startup'

        updateTangents: Optional[bool | LinkPath] = None 
        'True if tangents should be updated at each iteration'

        handleDynamicTopology: Optional[bool | LinkPath] = None 
        'True if topological changes should be handled'

        fixMergedUVSeams: Optional[bool | LinkPath] = None 
        'True if UV seams should be handled even when duplicate UVs are merged'

        keepLines: Optional[bool | LinkPath] = None 
        'keep and draw lines (false by default)'

        vertices: Optional[SofaArray | LinkPath] = None 
        'vertices of the model (only if vertices have multiple normals/texcoords, otherwise positions are used)'

        texcoords: Optional[SofaArray | LinkPath] = None 
        'coordinates of the texture'

        tangents: Optional[SofaArray | LinkPath] = None 
        'tangents for normal mapping'

        bitangents: Optional[SofaArray | LinkPath] = None 
        'tangents for normal mapping'

        edges: Optional[SofaArray | LinkPath] = None 
        'edges of the model'

        triangles: Optional[SofaArray | LinkPath] = None 
        'triangles of the model'

        quads: Optional[SofaArray | LinkPath] = None 
        'quads of the model'

        vertPosIdx: Optional[SofaArray | LinkPath] = None 
        'If vertices have multiple normals/texcoords stores vertices position indices'

        vertNormIdx: Optional[SofaArray | LinkPath] = None 
        'If vertices have multiple normals/texcoords stores vertices normal indices'

        filename: Optional[str | LinkPath] = None 
        ' Path to an ogl model'

        texturename: Optional[str | LinkPath] = None 
        'Name of the Texture'

        translation: Optional[SofaArray | LinkPath] = None 
        'Initial Translation of the object'

        rotation: Optional[SofaArray | LinkPath] = None 
        'Initial Rotation of the object'

        scale3d: Optional[SofaArray | LinkPath] = None 
        'Initial Scale of the object'

        scaleTex: Optional[SofaArray | LinkPath] = None 
        'Scale of the texture'

        translationTex: Optional[SofaArray | LinkPath] = None 
        'Translation of the texture'

        material: Optional[object | LinkPath] = None 
        'Material'

        putOnlyTexCoords: Optional[bool | LinkPath] = None 
        'Give Texture Coordinates without the texture binding'

        srgbTexturing: Optional[bool | LinkPath] = None 
        'When sRGB rendering is enabled, is the texture in sRGB colorspace?'

        materials: Optional[SofaArray | LinkPath] = None 
        'List of materials'

        groups: Optional[SofaArray | LinkPath] = None 
        'Groups of triangles and quads using a given material'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return VisualModelImpl.Parameters()
