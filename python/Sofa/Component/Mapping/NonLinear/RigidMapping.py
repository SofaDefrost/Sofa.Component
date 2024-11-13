# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component RigidMapping

.. autofunction:: RigidMapping

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class RigidMapping(Object):
    """Set the positions and velocities of points attached to a rigid parent"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,mapForces: Optional[bool] = None,mapConstraints: Optional[bool] = None,mapMasses: Optional[bool] = None,mapMatrices: Optional[bool] = None,applyRestPosition: Optional[bool] = None,geometricStiffness: Optional[object] = None,initialPoints: Optional[SofaArray] = None,index: Optional[int] = None,filename: Optional[str] = None,useX0: Optional[bool] = None,indexFromEnd: Optional[bool] = None,rigidIndexPerPoint: Optional[SofaArray] = None,globalToLocalCoords: Optional[bool] = None):
        """Set the positions and velocities of points attached to a rigid parent
        
        Args:
           applyRestPosition (bool):   set to true to apply this mapping to restPosition at init
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           filename (str):   Xsp file where rigid mapping information can be loaded from.
           geometricStiffness (object):   Method used to compute the geometric stiffness:
-None: geometric stiffness is not computed
-Exact: the exact geometric stiffness is computed
-Stabilized: the exact geometric stiffness is approximated in order to improve stability
           globalToLocalCoords (bool):   are the output DOFs initially expressed in global coordinates
           index (int):   input DOF index
           indexFromEnd (bool):   input DOF index starts from the end of input DOFs vector
           initialPoints (SofaArray):   Local Coordinates of the points
           listening (bool):   if true, handle the events, otherwise ignore the events
           mapConstraints (bool):   Are constraints mapped ?
           mapForces (bool):   Are forces mapped ?
           mapMasses (bool):   Are masses mapped ?
           mapMatrices (bool):   Are matrix explicit mapped?
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           rigidIndexPerPoint (SofaArray):   For each mapped point, the index of the Rigid it is mapped from
           tags (object):   list of the subsets the objet belongs to
           useX0 (bool):   Use x0 instead of local copy of initial positions (to support topo changes)
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

    geometricStiffness: Data[object] 
    'Method used to compute the geometric stiffness:-None: geometric stiffness is not computed-Exact: the exact geometric stiffness is computed-Stabilized: the exact geometric stiffness is approximated in order to improve stability'

    initialPoints: Data[SofaArray] 
    'Local Coordinates of the points'

    index: Data[int] 
    'input DOF index'

    filename: Data[str] 
    'Xsp file where rigid mapping information can be loaded from.'

    useX0: Data[bool] 
    'Use x0 instead of local copy of initial positions (to support topo changes)'

    indexFromEnd: Data[bool] 
    'input DOF index starts from the end of input DOFs vector'

    rigidIndexPerPoint: Data[SofaArray] 
    'For each mapped point, the index of the Rigid it is mapped from'

    globalToLocalCoords: Data[bool] 
    'are the output DOFs initially expressed in global coordinates'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the RigidMapping component"""

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

        geometricStiffness: Optional[object | LinkPath] = None 
        'Method used to compute the geometric stiffness:-None: geometric stiffness is not computed-Exact: the exact geometric stiffness is computed-Stabilized: the exact geometric stiffness is approximated in order to improve stability'

        initialPoints: Optional[SofaArray | LinkPath] = None 
        'Local Coordinates of the points'

        index: Optional[int | LinkPath] = None 
        'input DOF index'

        filename: Optional[str | LinkPath] = None 
        'Xsp file where rigid mapping information can be loaded from.'

        useX0: Optional[bool | LinkPath] = None 
        'Use x0 instead of local copy of initial positions (to support topo changes)'

        indexFromEnd: Optional[bool | LinkPath] = None 
        'input DOF index starts from the end of input DOFs vector'

        rigidIndexPerPoint: Optional[SofaArray | LinkPath] = None 
        'For each mapped point, the index of the Rigid it is mapped from'

        globalToLocalCoords: Optional[bool | LinkPath] = None 
        'are the output DOFs initially expressed in global coordinates'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return RigidMapping.Parameters()
