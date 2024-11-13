# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component MeshMatrixMass

.. autofunction:: MeshMatrixMass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class MeshMatrixMass(Object):
    """Define a specific mass for each particle"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,separateGravity: Optional[bool] = None,rayleighMass: Optional[float] = None,massDensity: Optional[SofaArray] = None,totalMass: Optional[float] = None,vertexMass: Optional[SofaArray] = None,edgeMass: Optional[SofaArray] = None,computeMassOnRest: Optional[bool] = None,showGravityCenter: Optional[bool] = None,showAxisSizeFactor: Optional[float] = None,lumping: Optional[bool] = None,printMass: Optional[bool] = None,graph: Optional[SofaArray] = None):
        """Define a specific mass for each particle
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           computeMassOnRest (bool):   If true, the mass of every element is computed based on the rest position rather than the position
           edgeMass (SofaArray):   internal values of the particles masses on edges, supporting topological changes
           graph (SofaArray):   Graph of the controlled potential
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           lumping (bool):   boolean if you need to use a lumped mass matrix
           massDensity (SofaArray):   Specify real and strictly positive value(s) for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           printMass (bool):   boolean if you want to check the mass conservation
           rayleighMass (float):   Rayleigh damping - mass matrix coefficient
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           separateGravity (bool):   add separately gravity to velocity computation
           showAxisSizeFactor (float):   factor length of the axis displayed (only used for rigids)
           showGravityCenter (bool):   display the center of gravity of the system
           tags (object):   list of the subsets the objet belongs to
           totalMass (float):   Specify the total mass resulting from all particles. 
If unspecified or wrongly set, the default value is used: totalMass = 1.0
           vertexMass (SofaArray):   internal values of the particles masses on vertices, supporting topological changes
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

    isCompliance: Data[bool] 
    'Consider the component as a compliance, else as a stiffness'

    rayleighStiffness: Data[float] 
    'Rayleigh damping - stiffness matrix coefficient'

    separateGravity: Data[bool] 
    'add separately gravity to velocity computation'

    rayleighMass: Data[float] 
    'Rayleigh damping - mass matrix coefficient'

    massDensity: Data[SofaArray] 
    'Specify real and strictly positive value(s) for the mass density. If unspecified or wrongly set, the totalMass information is used.'

    totalMass: Data[float] 
    'Specify the total mass resulting from all particles. If unspecified or wrongly set, the default value is used: totalMass = 1.0'

    vertexMass: Data[SofaArray] 
    'internal values of the particles masses on vertices, supporting topological changes'

    edgeMass: Data[SofaArray] 
    'internal values of the particles masses on edges, supporting topological changes'

    computeMassOnRest: Data[bool] 
    'If true, the mass of every element is computed based on the rest position rather than the position'

    showGravityCenter: Data[bool] 
    'display the center of gravity of the system'

    showAxisSizeFactor: Data[float] 
    'factor length of the axis displayed (only used for rigids)'

    lumping: Data[bool] 
    'boolean if you need to use a lumped mass matrix'

    printMass: Data[bool] 
    'boolean if you want to check the mass conservation'

    graph: Data[SofaArray] 
    'Graph of the controlled potential'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the MeshMatrixMass component"""

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

        isCompliance: Optional[bool | LinkPath] = None 
        'Consider the component as a compliance, else as a stiffness'

        rayleighStiffness: Optional[float | LinkPath] = None 
        'Rayleigh damping - stiffness matrix coefficient'

        separateGravity: Optional[bool | LinkPath] = None 
        'add separately gravity to velocity computation'

        rayleighMass: Optional[float | LinkPath] = None 
        'Rayleigh damping - mass matrix coefficient'

        massDensity: Optional[SofaArray | LinkPath] = None 
        'Specify real and strictly positive value(s) for the mass density. If unspecified or wrongly set, the totalMass information is used.'

        totalMass: Optional[float | LinkPath] = None 
        'Specify the total mass resulting from all particles. If unspecified or wrongly set, the default value is used: totalMass = 1.0'

        vertexMass: Optional[SofaArray | LinkPath] = None 
        'internal values of the particles masses on vertices, supporting topological changes'

        edgeMass: Optional[SofaArray | LinkPath] = None 
        'internal values of the particles masses on edges, supporting topological changes'

        computeMassOnRest: Optional[bool | LinkPath] = None 
        'If true, the mass of every element is computed based on the rest position rather than the position'

        showGravityCenter: Optional[bool | LinkPath] = None 
        'display the center of gravity of the system'

        showAxisSizeFactor: Optional[float | LinkPath] = None 
        'factor length of the axis displayed (only used for rigids)'

        lumping: Optional[bool | LinkPath] = None 
        'boolean if you need to use a lumped mass matrix'

        printMass: Optional[bool | LinkPath] = None 
        'boolean if you want to check the mass conservation'

        graph: Optional[SofaArray | LinkPath] = None 
        'Graph of the controlled potential'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return MeshMatrixMass.Parameters()
