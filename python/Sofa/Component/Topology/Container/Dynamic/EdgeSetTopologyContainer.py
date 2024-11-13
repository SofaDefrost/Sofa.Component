# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component EdgeSetTopologyContainer

.. autofunction:: EdgeSetTopologyContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class EdgeSetTopologyContainer(Object):
    """Edge set topology container"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,filename: Optional[str] = None,position: Optional[SofaArray] = None,checkTopology: Optional[bool] = None,nbPoints: Optional[int] = None,edges: Optional[SofaArray] = None,checkConnexity: Optional[bool] = None):
        """Edge set topology container
        
        Args:
           bbox (object):   this object bounding box
           checkConnexity (bool):   It true, will check the connexity of the mesh.
           checkTopology (bool):   Parameter to activate internal topology checks (might slow down the simulation)
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           edges (SofaArray):   List of edge indices
           filename (str):   Filename of the mesh
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           nbPoints (int):   Number of points
           position (SofaArray):   Initial position of points
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

    filename: Data[str] 
    'Filename of the mesh'

    position: Data[SofaArray] 
    'Initial position of points'

    checkTopology: Data[bool] 
    'Parameter to activate internal topology checks (might slow down the simulation)'

    nbPoints: Data[int] 
    'Number of points'

    edges: Data[SofaArray] 
    'List of edge indices'

    checkConnexity: Data[bool] 
    'It true, will check the connexity of the mesh.'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the EdgeSetTopologyContainer component"""

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

        filename: Optional[str | LinkPath] = None 
        'Filename of the mesh'

        position: Optional[SofaArray | LinkPath] = None 
        'Initial position of points'

        checkTopology: Optional[bool | LinkPath] = None 
        'Parameter to activate internal topology checks (might slow down the simulation)'

        nbPoints: Optional[int | LinkPath] = None 
        'Number of points'

        edges: Optional[SofaArray | LinkPath] = None 
        'List of edge indices'

        checkConnexity: Optional[bool | LinkPath] = None 
        'It true, will check the connexity of the mesh.'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return EdgeSetTopologyContainer.Parameters()
