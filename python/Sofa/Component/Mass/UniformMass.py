# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component UniformMass

.. autofunction:: UniformMass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class UniformMass(Object):
    """Define the same mass for all the particles"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,separateGravity: Optional[bool] = None,rayleighMass: Optional[float] = None,vertexMass: Optional[float] = None,totalMass: Optional[float] = None,filename: Optional[str] = None,showGravityCenter: Optional[bool] = None,showAxisSizeFactor: Optional[float] = None,compute_mapping_inertia: Optional[bool] = None,showInitialCenterOfGravity: Optional[bool] = None,showX0: Optional[bool] = None,localRange: Optional[SofaArray] = None,indices: Optional[SofaArray] = None,preserveTotalMass: Optional[bool] = None):
        """Define the same mass for all the particles
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           compute_mapping_inertia (bool):   to be used if the mass is placed under a mapping
           filename (str):   File storing the mass parameters [rigid objects only].
           indices (SofaArray):   optional local DOF indices. Any computation involving only indices outside of this list are discarded
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           localRange (SofaArray):   optional range of local DOF indices. 
Any computation involving only indices outside of this range 
are discarded (useful for parallelization using mesh partitionning)
           name (str):   object name
           preserveTotalMass (bool):   Prevent totalMass from decreasing when removing particles.
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighMass (float):   Rayleigh damping - mass matrix coefficient
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           separateGravity (bool):   add separately gravity to velocity computation
           showAxisSizeFactor (float):   factor length of the axis displayed (only used for rigids)
           showGravityCenter (bool):   display the center of gravity of the system
           showInitialCenterOfGravity (bool):   display the initial center of gravity of the system
           showX0 (bool):   display the rest positions
           tags (object):   list of the subsets the objet belongs to
           totalMass (float):   Specify the total mass resulting from all particles. 
If unspecified or wrongly set, the default value is used: totalMass = 1.0
           vertexMass (float):   Specify one single, positive, real value for the mass of each particle. 
If unspecified or wrongly set, the totalMass information is used.
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

    vertexMass: Data[float] 
    'Specify one single, positive, real value for the mass of each particle. If unspecified or wrongly set, the totalMass information is used.'

    totalMass: Data[float] 
    'Specify the total mass resulting from all particles. If unspecified or wrongly set, the default value is used: totalMass = 1.0'

    filename: Data[str] 
    'File storing the mass parameters [rigid objects only].'

    showGravityCenter: Data[bool] 
    'display the center of gravity of the system'

    showAxisSizeFactor: Data[float] 
    'factor length of the axis displayed (only used for rigids)'

    compute_mapping_inertia: Data[bool] 
    'to be used if the mass is placed under a mapping'

    showInitialCenterOfGravity: Data[bool] 
    'display the initial center of gravity of the system'

    showX0: Data[bool] 
    'display the rest positions'

    localRange: Data[SofaArray] 
    'optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)'

    indices: Data[SofaArray] 
    'optional local DOF indices. Any computation involving only indices outside of this list are discarded'

    preserveTotalMass: Data[bool] 
    'Prevent totalMass from decreasing when removing particles.'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the UniformMass component"""

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

        vertexMass: Optional[float | LinkPath] = None 
        'Specify one single, positive, real value for the mass of each particle. If unspecified or wrongly set, the totalMass information is used.'

        totalMass: Optional[float | LinkPath] = None 
        'Specify the total mass resulting from all particles. If unspecified or wrongly set, the default value is used: totalMass = 1.0'

        filename: Optional[str | LinkPath] = None 
        'File storing the mass parameters [rigid objects only].'

        showGravityCenter: Optional[bool | LinkPath] = None 
        'display the center of gravity of the system'

        showAxisSizeFactor: Optional[float | LinkPath] = None 
        'factor length of the axis displayed (only used for rigids)'

        compute_mapping_inertia: Optional[bool | LinkPath] = None 
        'to be used if the mass is placed under a mapping'

        showInitialCenterOfGravity: Optional[bool | LinkPath] = None 
        'display the initial center of gravity of the system'

        showX0: Optional[bool | LinkPath] = None 
        'display the rest positions'

        localRange: Optional[SofaArray | LinkPath] = None 
        'optional range of local DOF indices. Any computation involving only indices outside of this range are discarded (useful for parallelization using mesh partitionning)'

        indices: Optional[SofaArray | LinkPath] = None 
        'optional local DOF indices. Any computation involving only indices outside of this list are discarded'

        preserveTotalMass: Optional[bool | LinkPath] = None 
        'Prevent totalMass from decreasing when removing particles.'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return UniformMass.Parameters()
