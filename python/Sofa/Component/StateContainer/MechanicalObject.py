# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component MechanicalObject

.. autofunction:: MechanicalObject

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class MechanicalObject(Object):
    """The main component of a simulation in SOFA is the MechanicalObject. It inherits from MechanicalState, itself inheriting from State.

These state vectors correspond to the degrees of freedom (DOFs) and their first time derivative. The vector size is the number of nodes, and the size of each vector entry depends on the template (see below).

The state vectors can contain different type of data depending on the degrees of freedom (DOFs). In order to provide generic implementation, components (C++ classes) in SOFA will be templated on DataTypes.

Example of use: 
```python
	import Sofa.Core
	from Sofa.Component.StateContainer.MechanicalObject import MechanicalObject
	
	r = Sofa.Core.Node("root")
	r.addObject("MechanicalObject", template="vec3", position=[[1,0,0], [2,0,0]]
```

SOFA supports several DataTypes corresponding to the DOFs:
	- Vec1f or Vec1d: 1 DOF per node is used. For instance, this can be used for thermodynamics (temperature field). Vec1f denotes vectors of float and Vec1d denotes the use of doubles.
	- Vec2f or Vec2d: 2 DOFs per node are used. For instance, this can be used for cardiac electrophysiology.
	- Vec3f or Vec3d: 3 DOFs per node are used. For instance, this can be used for mechanics.
	- Vec6f or Vec6d: 6 DOFs per node are used. For instance, this can be used for beam simulations (3 translations and 3 rotations).
	- Rigid3d: this DataType corresponds to 7 DOFs per node, this can be used to simulate rigid bodies (3 positions and 1 quaternion).

In the MechanicalObject, each of these state vectors can be accessed using (scattered) state vectors, called multi-vectors or MultiVec. 

*Note: the SOFA framework being historically focused on soft tissue mechanics, the semantic is strongly related to mechanics. The state vectors (DOFs) are stored in the field named position, their first derivatives in the velocity field and their second derivatives in the acceleration field.
Templates*    
    """

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,position: Optional[SofaArray] = None,velocity: Optional[SofaArray] = None,force: Optional[SofaArray] = None,rest_position: Optional[SofaArray] = None,externalForce: Optional[SofaArray] = None,derivX: Optional[SofaArray] = None,free_position: Optional[SofaArray] = None,free_velocity: Optional[SofaArray] = None,constraint: Optional[SofaArray] = None,mappingJacobian: Optional[SofaArray] = None,reset_position: Optional[SofaArray] = None,reset_velocity: Optional[SofaArray] = None,restScale: Optional[float] = None,useTopology: Optional[bool] = None,showObject: Optional[bool] = None,showObjectScale: Optional[float] = None,showIndices: Optional[bool] = None,showIndicesScale: Optional[float] = None,showVectors: Optional[bool] = None,showVectorsScale: Optional[float] = None,drawMode: Optional[int] = None,showColor: Optional[object] = None,translation: Optional[SofaArray] = None,rotation: Optional[SofaArray] = None,scale3d: Optional[SofaArray] = None,translation2: Optional[SofaArray] = None,rotation2: Optional[SofaArray] = None,size: Optional[int] = None,reserve: Optional[int] = None):
        """mechanical state vectors
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           constraint (SofaArray):   constraints applied to the degrees of freedom
           derivX (SofaArray):   dx vector of the degrees of freedom
           drawMode (int):   The way vectors will be drawn:
- 0: Line
- 1:Cylinder
- 2: Arrow.

The DOFS will be drawn:
- 0: point
- >1: sphere. (default=0)
           externalForce (SofaArray):   externalForces vector of the degrees of freedom
           force (SofaArray):   force vector of the degrees of freedom
           free_position (SofaArray):   free position coordinates of the degrees of freedom
           free_velocity (SofaArray):   free velocity coordinates of the degrees of freedom
           listening (bool):   if true, handle the events, otherwise ignore the events
           mappingJacobian (SofaArray):   mappingJacobian applied to the degrees of freedom
           name (str):   object name
           position (SofaArray):   position coordinates of the degrees of freedom
           printLog (bool):   if true, emits extra messages at runtime.
           reserve (int):   Size to reserve when creating vectors. (default=0)
           reset_position (SofaArray):   reset position coordinates of the degrees of freedom
           reset_velocity (SofaArray):   reset velocity coordinates of the degrees of freedom
           restScale (float):   optional scaling of rest position coordinates (to simulated pre-existing internal tension).(default = 1.0)
           rest_position (SofaArray):   rest position coordinates of the degrees of freedom
           rotation (SofaArray):   Rotation of the DOFs
           rotation2 (SofaArray):   Rotation of the DOFs, applied the after the rest position has been computed
           scale3d (SofaArray):   Scale of the DOFs in 3 dimensions
           showColor (object):   Color for object display. (default=[1 1 1 1])
           showIndices (bool):   Show indices. (default=false)
           showIndicesScale (float):   Scale for indices display. (default=0.02)
           showObject (bool):   Show objects. (default=false)
           showObjectScale (float):   Scale for object display. (default=0.1)
           showVectors (bool):   Show velocity. (default=false)
           showVectorsScale (float):   Scale for vectors display. (default=0.0001)
           size (int):   Size of the vectors
           tags (object):   list of the subsets the objet belongs to
           translation (SofaArray):   Translation of the DOFs
           translation2 (SofaArray):   Translation of the DOFs, applied after the rest position has been computed
           useTopology (bool):   Shall this object rely on any active topology to initialize its size and positions
           velocity (SofaArray):   velocity coordinates of the degrees of freedom
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
    'position coordinates of the degrees of freedom'

    velocity: Data[SofaArray] 
    'velocity coordinates of the degrees of freedom'

    force: Data[SofaArray] 
    'force vector of the degrees of freedom'

    rest_position: Data[SofaArray] 
    'rest position coordinates of the degrees of freedom'

    externalForce: Data[SofaArray] 
    'externalForces vector of the degrees of freedom'

    derivX: Data[SofaArray] 
    'dx vector of the degrees of freedom'

    free_position: Data[SofaArray] 
    'free position coordinates of the degrees of freedom'

    free_velocity: Data[SofaArray] 
    'free velocity coordinates of the degrees of freedom'

    constraint: Data[SofaArray] 
    'constraints applied to the degrees of freedom'

    mappingJacobian: Data[SofaArray] 
    'mappingJacobian applied to the degrees of freedom'

    reset_position: Data[SofaArray] 
    'reset position coordinates of the degrees of freedom'

    reset_velocity: Data[SofaArray] 
    'reset velocity coordinates of the degrees of freedom'

    restScale: Data[float] 
    'optional scaling of rest position coordinates (to simulated pre-existing internal tension).(default = 1.0)'

    useTopology: Data[bool] 
    'Shall this object rely on any active topology to initialize its size and positions'

    showObject: Data[bool] 
    'Show objects. (default=false)'

    showObjectScale: Data[float] 
    'Scale for object display. (default=0.1)'

    showIndices: Data[bool] 
    'Show indices. (default=false)'

    showIndicesScale: Data[float] 
    'Scale for indices display. (default=0.02)'

    showVectors: Data[bool] 
    'Show velocity. (default=false)'

    showVectorsScale: Data[float] 
    'Scale for vectors display. (default=0.0001)'

    drawMode: Data[int] 
    'The way vectors will be drawn:- 0: Line- 1:Cylinder- 2: Arrow.The DOFS will be drawn:- 0: point- >1: sphere. (default=0)'

    showColor: Data[object] 
    'Color for object display. (default=[1 1 1 1])'

    translation: Data[SofaArray] 
    'Translation of the DOFs'

    rotation: Data[SofaArray] 
    'Rotation of the DOFs'

    scale3d: Data[SofaArray] 
    'Scale of the DOFs in 3 dimensions'

    translation2: Data[SofaArray] 
    'Translation of the DOFs, applied after the rest position has been computed'

    rotation2: Data[SofaArray] 
    'Rotation of the DOFs, applied the after the rest position has been computed'

    size: Data[int] 
    'Size of the vectors'

    reserve: Data[int] 
    'Size to reserve when creating vectors. (default=0)'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the MechanicalObject component"""

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
        'position coordinates of the degrees of freedom'

        velocity: Optional[SofaArray | LinkPath] = None 
        'velocity coordinates of the degrees of freedom'

        force: Optional[SofaArray | LinkPath] = None 
        'force vector of the degrees of freedom'

        rest_position: Optional[SofaArray | LinkPath] = None 
        'rest position coordinates of the degrees of freedom'

        externalForce: Optional[SofaArray | LinkPath] = None 
        'externalForces vector of the degrees of freedom'

        derivX: Optional[SofaArray | LinkPath] = None 
        'dx vector of the degrees of freedom'

        free_position: Optional[SofaArray | LinkPath] = None 
        'free position coordinates of the degrees of freedom'

        free_velocity: Optional[SofaArray | LinkPath] = None 
        'free velocity coordinates of the degrees of freedom'

        constraint: Optional[SofaArray | LinkPath] = None 
        'constraints applied to the degrees of freedom'

        mappingJacobian: Optional[SofaArray | LinkPath] = None 
        'mappingJacobian applied to the degrees of freedom'

        reset_position: Optional[SofaArray | LinkPath] = None 
        'reset position coordinates of the degrees of freedom'

        reset_velocity: Optional[SofaArray | LinkPath] = None 
        'reset velocity coordinates of the degrees of freedom'

        restScale: Optional[float | LinkPath] = None 
        'optional scaling of rest position coordinates (to simulated pre-existing internal tension).(default = 1.0)'

        useTopology: Optional[bool | LinkPath] = None 
        'Shall this object rely on any active topology to initialize its size and positions'

        showObject: Optional[bool | LinkPath] = None 
        'Show objects. (default=false)'

        showObjectScale: Optional[float | LinkPath] = None 
        'Scale for object display. (default=0.1)'

        showIndices: Optional[bool | LinkPath] = None 
        'Show indices. (default=false)'

        showIndicesScale: Optional[float | LinkPath] = None 
        'Scale for indices display. (default=0.02)'

        showVectors: Optional[bool | LinkPath] = None 
        'Show velocity. (default=false)'

        showVectorsScale: Optional[float | LinkPath] = None 
        'Scale for vectors display. (default=0.0001)'

        drawMode: Optional[int | LinkPath] = None 
        'The way vectors will be drawn:- 0: Line- 1:Cylinder- 2: Arrow.The DOFS will be drawn:- 0: point- >1: sphere. (default=0)'

        showColor: Optional[object | LinkPath] = None 
        'Color for object display. (default=[1 1 1 1])'

        translation: Optional[SofaArray | LinkPath] = None 
        'Translation of the DOFs'

        rotation: Optional[SofaArray | LinkPath] = None 
        'Rotation of the DOFs'

        scale3d: Optional[SofaArray | LinkPath] = None 
        'Scale of the DOFs in 3 dimensions'

        translation2: Optional[SofaArray | LinkPath] = None 
        'Translation of the DOFs, applied after the rest position has been computed'

        rotation2: Optional[SofaArray | LinkPath] = None 
        'Rotation of the DOFs, applied the after the rest position has been computed'

        size: Optional[int | LinkPath] = None 
        'Size of the vectors'

        reserve: Optional[int | LinkPath] = None 
        'Size to reserve when creating vectors. (default=0)'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return MechanicalObject.Parameters()
