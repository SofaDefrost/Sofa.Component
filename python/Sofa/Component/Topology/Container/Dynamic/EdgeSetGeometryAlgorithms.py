# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component EdgeSetGeometryAlgorithms

.. autofunction:: EdgeSetGeometryAlgorithms

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class EdgeSetGeometryAlgorithms(Object):
    """Edge set geometry algorithms"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,showIndicesScale: Optional[float] = None,showPointIndices: Optional[bool] = None,tagMechanics: Optional[str] = None,showEdgeIndices: Optional[bool] = None,drawEdges: Optional[bool] = None,drawColorEdges: Optional[object] = None):
        """Edge set geometry algorithms
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           drawColorEdges (object):   RGB code color used to draw edges.
           drawEdges (bool):   if true, draw the edges in the topology.
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           showEdgeIndices (bool):   Debug : view Edge indices.
           showIndicesScale (float):   Debug : scale for view topology indices
           showPointIndices (bool):   Debug : view Point indices
           tagMechanics (str):   Tag of the Mechanical Object
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

    showIndicesScale: Data[float] 
    'Debug : scale for view topology indices'

    showPointIndices: Data[bool] 
    'Debug : view Point indices'

    tagMechanics: Data[str] 
    'Tag of the Mechanical Object'

    showEdgeIndices: Data[bool] 
    'Debug : view Edge indices.'

    drawEdges: Data[bool] 
    'if true, draw the edges in the topology.'

    drawColorEdges: Data[object] 
    'RGB code color used to draw edges.'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the EdgeSetGeometryAlgorithms component"""

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

        showIndicesScale: Optional[float | LinkPath] = None 
        'Debug : scale for view topology indices'

        showPointIndices: Optional[bool | LinkPath] = None 
        'Debug : view Point indices'

        tagMechanics: Optional[str | LinkPath] = None 
        'Tag of the Mechanical Object'

        showEdgeIndices: Optional[bool | LinkPath] = None 
        'Debug : view Edge indices.'

        drawEdges: Optional[bool | LinkPath] = None 
        'if true, draw the edges in the topology.'

        drawColorEdges: Optional[object | LinkPath] = None 
        'RGB code color used to draw edges.'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return EdgeSetGeometryAlgorithms.Parameters()
