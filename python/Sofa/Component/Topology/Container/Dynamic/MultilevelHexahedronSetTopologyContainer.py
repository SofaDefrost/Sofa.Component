# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component MultilevelHexahedronSetTopologyContainer

.. autofunction:: MultilevelHexahedronSetTopologyContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class MultilevelHexahedronSetTopologyContainer(Object):
    """Hexahedron set topology container"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,filename: Optional[str] = None,position: Optional[SofaArray] = None,checkTopology: Optional[bool] = None,nbPoints: Optional[int] = None,edges: Optional[SofaArray] = None,checkConnexity: Optional[bool] = None,quads: Optional[SofaArray] = None,createQuadArray: Optional[bool] = None,hexahedra: Optional[SofaArray] = None,level: Optional[int] = None,resolution: Optional[SofaArray] = None,idxInRegularGrid: Optional[SofaArray] = None,coarseComponents: Optional[SofaArray] = None,fineComponents: Optional[SofaArray] = None):
        """Hexahedron set topology container
        
        Args:
           bbox (object):   this object bounding box
           checkConnexity (bool):   It true, will check the connexity of the mesh.
           checkTopology (bool):   Parameter to activate internal topology checks (might slow down the simulation)
           coarseComponents (SofaArray):   map between hexahedra and components - coarse
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           createQuadArray (bool):   Force the creation of a set of quads associated with the hexahedra
           edges (SofaArray):   List of edge indices
           filename (str):   Filename of the mesh
           fineComponents (SofaArray):   map between hexahedra and components - fine
           hexahedra (SofaArray):   List of hexahedron indices
           idxInRegularGrid (SofaArray):   indices of the hexa in the grid.
           level (int):   Number of resolution levels between the fine and coarse mesh
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           nbPoints (int):   Number of points
           position (SofaArray):   Initial position of points
           printLog (bool):   if true, emits extra messages at runtime.
           quads (SofaArray):   List of quad indices
           resolution (SofaArray):   fine resolution
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

    quads: Data[SofaArray] 
    'List of quad indices'

    createQuadArray: Data[bool] 
    'Force the creation of a set of quads associated with the hexahedra'

    hexahedra: Data[SofaArray] 
    'List of hexahedron indices'

    level: Data[int] 
    'Number of resolution levels between the fine and coarse mesh'

    resolution: Data[SofaArray] 
    'fine resolution'

    idxInRegularGrid: Data[SofaArray] 
    'indices of the hexa in the grid.'

    coarseComponents: Data[SofaArray] 
    'map between hexahedra and components - coarse'

    fineComponents: Data[SofaArray] 
    'map between hexahedra and components - fine'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the MultilevelHexahedronSetTopologyContainer component"""

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

        quads: Optional[SofaArray | LinkPath] = None 
        'List of quad indices'

        createQuadArray: Optional[bool | LinkPath] = None 
        'Force the creation of a set of quads associated with the hexahedra'

        hexahedra: Optional[SofaArray | LinkPath] = None 
        'List of hexahedron indices'

        level: Optional[int | LinkPath] = None 
        'Number of resolution levels between the fine and coarse mesh'

        resolution: Optional[SofaArray | LinkPath] = None 
        'fine resolution'

        idxInRegularGrid: Optional[SofaArray | LinkPath] = None 
        'indices of the hexa in the grid.'

        coarseComponents: Optional[SofaArray | LinkPath] = None 
        'map between hexahedra and components - coarse'

        fineComponents: Optional[SofaArray | LinkPath] = None 
        'map between hexahedra and components - fine'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return MultilevelHexahedronSetTopologyContainer.Parameters()
