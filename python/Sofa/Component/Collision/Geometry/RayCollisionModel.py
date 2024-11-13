# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component RayCollisionModel

.. autofunction:: RayCollisionModel

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class RayCollisionModel(Object):
    """Collision model representing a ray in space, e.g. a mouse click"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,active: Optional[bool] = None,moving: Optional[bool] = None,simulated: Optional[bool] = None,selfCollision: Optional[bool] = None,proximity: Optional[float] = None,contactStiffness: Optional[float] = None,contactFriction: Optional[float] = None,contactRestitution: Optional[float] = None,contactResponse: Optional[str] = None,color: Optional[object] = None,group: Optional[SofaArray] = None,numberOfContacts: Optional[int] = None,defaultLength: Optional[float] = None):
        """Collision model representing a ray in space, e.g. a mouse click
        
        Args:
           active (bool):   flag indicating if this collision model is active and should be included in default collision detections
           bbox (object):   this object bounding box
           color (object):   color used to display the collision model if requested
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           contactFriction (float):   Contact friction coefficient (dry or viscous or unused depending on the contact method)
           contactResponse (str):   if set, indicate to the ContactManager that this model should use the given class of contacts.
Note that this is only indicative, and in particular if both collision models specify a different class it is up to the manager to choose.
           contactRestitution (float):   Contact coefficient of restitution
           contactStiffness (float):   Contact stiffness
           defaultLength (float):   The default length for all rays in this collision model
           group (SofaArray):   IDs of the groups containing this model. No collision can occur between collision models included in a common group (e.g. allowing the same object to have multiple collision models)
           listening (bool):   if true, handle the events, otherwise ignore the events
           moving (bool):   flag indicating if this object is changing position between iterations
           name (str):   object name
           numberOfContacts (int):   Number of collision models this collision model is currently attached to
           printLog (bool):   if true, emits extra messages at runtime.
           proximity (float):   Distance to the actual (visual) surface
           selfCollision (bool):   flag indication if the object can self collide
           simulated (bool):   flag indicating if this object is controlled by a simulation
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

    active: Data[bool] 
    'flag indicating if this collision model is active and should be included in default collision detections'

    moving: Data[bool] 
    'flag indicating if this object is changing position between iterations'

    simulated: Data[bool] 
    'flag indicating if this object is controlled by a simulation'

    selfCollision: Data[bool] 
    'flag indication if the object can self collide'

    proximity: Data[float] 
    'Distance to the actual (visual) surface'

    contactStiffness: Data[float] 
    'Contact stiffness'

    contactFriction: Data[float] 
    'Contact friction coefficient (dry or viscous or unused depending on the contact method)'

    contactRestitution: Data[float] 
    'Contact coefficient of restitution'

    contactResponse: Data[str] 
    'if set, indicate to the ContactManager that this model should use the given class of contacts.Note that this is only indicative, and in particular if both collision models specify a different class it is up to the manager to choose.'

    color: Data[object] 
    'color used to display the collision model if requested'

    group: Data[SofaArray] 
    'IDs of the groups containing this model. No collision can occur between collision models included in a common group (e.g. allowing the same object to have multiple collision models)'

    numberOfContacts: Data[int] 
    'Number of collision models this collision model is currently attached to'

    defaultLength: Data[float] 
    'The default length for all rays in this collision model'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the RayCollisionModel component"""

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

        active: Optional[bool | LinkPath] = None 
        'flag indicating if this collision model is active and should be included in default collision detections'

        moving: Optional[bool | LinkPath] = None 
        'flag indicating if this object is changing position between iterations'

        simulated: Optional[bool | LinkPath] = None 
        'flag indicating if this object is controlled by a simulation'

        selfCollision: Optional[bool | LinkPath] = None 
        'flag indication if the object can self collide'

        proximity: Optional[float | LinkPath] = None 
        'Distance to the actual (visual) surface'

        contactStiffness: Optional[float | LinkPath] = None 
        'Contact stiffness'

        contactFriction: Optional[float | LinkPath] = None 
        'Contact friction coefficient (dry or viscous or unused depending on the contact method)'

        contactRestitution: Optional[float | LinkPath] = None 
        'Contact coefficient of restitution'

        contactResponse: Optional[str | LinkPath] = None 
        'if set, indicate to the ContactManager that this model should use the given class of contacts.Note that this is only indicative, and in particular if both collision models specify a different class it is up to the manager to choose.'

        color: Optional[object | LinkPath] = None 
        'color used to display the collision model if requested'

        group: Optional[SofaArray | LinkPath] = None 
        'IDs of the groups containing this model. No collision can occur between collision models included in a common group (e.g. allowing the same object to have multiple collision models)'

        numberOfContacts: Optional[int | LinkPath] = None 
        'Number of collision models this collision model is currently attached to'

        defaultLength: Optional[float | LinkPath] = None 
        'The default length for all rays in this collision model'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return RayCollisionModel.Parameters()
