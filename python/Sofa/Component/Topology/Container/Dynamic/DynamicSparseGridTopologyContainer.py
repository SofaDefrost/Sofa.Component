# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component DynamicSparseGridTopologyContainer

.. autofunction:: DynamicSparseGridTopologyContainer

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class DynamicSparseGridTopologyContainer(Object):
    """Hexahedron set topology container"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,filename: Optional[str] = None,position: Optional[SofaArray] = None,checkTopology: Optional[bool] = None,nbPoints: Optional[int] = None,edges: Optional[SofaArray] = None,checkConnexity: Optional[bool] = None,quads: Optional[SofaArray] = None,createQuadArray: Optional[bool] = None,hexahedra: Optional[SofaArray] = None,resolution: Optional[SofaArray] = None,valuesIndexedInRegularGrid: Optional[SofaArray] = None,valuesIndexedInTopology: Optional[SofaArray] = None,idxInRegularGrid: Optional[SofaArray] = None,idInRegularGrid2IndexInTopo: Optional[object] = None,voxelSize: Optional[SofaArray] = None):
        """Hexahedron set topology container
        
        Args:
           bbox (object):   this object bounding box
           checkConnexity (bool):   It true, will check the connexity of the mesh.
           checkTopology (bool):   Parameter to activate internal topology checks (might slow down the simulation)
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           createQuadArray (bool):   Force the creation of a set of quads associated with the hexahedra
           edges (SofaArray):   List of edge indices
           filename (str):   Filename of the mesh
           hexahedra (SofaArray):   List of hexahedron indices
           idInRegularGrid2IndexInTopo (object):   map between id in the Regular Grid and index in the topology
           idxInRegularGrid (SofaArray):   indices in the Regular Grid
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           nbPoints (int):   Number of points
           position (SofaArray):   Initial position of points
           printLog (bool):   if true, emits extra messages at runtime.
           quads (SofaArray):   List of quad indices
           resolution (SofaArray):   voxel grid resolution
           tags (object):   list of the subsets the objet belongs to
           valuesIndexedInRegularGrid (SofaArray):   values indexed in the Regular Grid
           valuesIndexedInTopology (SofaArray):   values indexed in the topology
           voxelSize (SofaArray):   Size of the Voxels
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

    resolution: Data[SofaArray] 
    'voxel grid resolution'

    valuesIndexedInRegularGrid: Data[SofaArray] 
    'values indexed in the Regular Grid'

    valuesIndexedInTopology: Data[SofaArray] 
    'values indexed in the topology'

    idxInRegularGrid: Data[SofaArray] 
    'indices in the Regular Grid'

    idInRegularGrid2IndexInTopo: Data[object] 
    'map between id in the Regular Grid and index in the topology'

    voxelSize: Data[SofaArray] 
    'Size of the Voxels'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the DynamicSparseGridTopologyContainer component"""

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

        resolution: Optional[SofaArray | LinkPath] = None 
        'voxel grid resolution'

        valuesIndexedInRegularGrid: Optional[SofaArray | LinkPath] = None 
        'values indexed in the Regular Grid'

        valuesIndexedInTopology: Optional[SofaArray | LinkPath] = None 
        'values indexed in the topology'

        idxInRegularGrid: Optional[SofaArray | LinkPath] = None 
        'indices in the Regular Grid'

        idInRegularGrid2IndexInTopo: Optional[object | LinkPath] = None 
        'map between id in the Regular Grid and index in the topology'

        voxelSize: Optional[SofaArray | LinkPath] = None 
        'Size of the Voxels'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return DynamicSparseGridTopologyContainer.Parameters()
