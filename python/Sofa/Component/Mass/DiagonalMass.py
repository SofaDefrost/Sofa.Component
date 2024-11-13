# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component DiagonalMass

.. autofunction:: DiagonalMass

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class DiagonalMass(Object):
    """Define a specific mass for each particle"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,separateGravity: Optional[bool] = None,rayleighMass: Optional[float] = None,vertexMass: Optional[SofaArray] = None,massDensity: Optional[float] = None,totalMass: Optional[float] = None,computeMassOnRest: Optional[bool] = None,showGravityCenter: Optional[bool] = None,showAxisSizeFactor: Optional[float] = None,filename: Optional[str] = None):
        """Define a specific mass for each particle
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           computeMassOnRest (bool):   If true, the mass of every element is computed based on the rest position rather than the position
           filename (str):   Xsp3.0 file to specify the mass parameters
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           massDensity (float):   Specify one single real and positive value for the mass density. 
If unspecified or wrongly set, the totalMass information is used.
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighMass (float):   Rayleigh damping - mass matrix coefficient
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           separateGravity (bool):   add separately gravity to velocity computation
           showAxisSizeFactor (float):   Factor length of the axis displayed (only used for rigids)
           showGravityCenter (bool):   Display the center of gravity of the system
           tags (object):   list of the subsets the objet belongs to
           totalMass (float):   Specify the total mass resulting from all particles. 
If unspecified or wrongly set, the default value is used: totalMass = 1.0
           vertexMass (SofaArray):   Specify a vector giving the mass of each vertex. 
If unspecified or wrongly set, the massDensity or totalMass information is used.
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

    vertexMass: Data[SofaArray] 
    'Specify a vector giving the mass of each vertex. If unspecified or wrongly set, the massDensity or totalMass information is used.'

    massDensity: Data[float] 
    'Specify one single real and positive value for the mass density. If unspecified or wrongly set, the totalMass information is used.'

    totalMass: Data[float] 
    'Specify the total mass resulting from all particles. If unspecified or wrongly set, the default value is used: totalMass = 1.0'

    computeMassOnRest: Data[bool] 
    'If true, the mass of every element is computed based on the rest position rather than the position'

    showGravityCenter: Data[bool] 
    'Display the center of gravity of the system'

    showAxisSizeFactor: Data[float] 
    'Factor length of the axis displayed (only used for rigids)'

    filename: Data[str] 
    'Xsp3.0 file to specify the mass parameters'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the DiagonalMass component"""

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

        vertexMass: Optional[SofaArray | LinkPath] = None 
        'Specify a vector giving the mass of each vertex. If unspecified or wrongly set, the massDensity or totalMass information is used.'

        massDensity: Optional[float | LinkPath] = None 
        'Specify one single real and positive value for the mass density. If unspecified or wrongly set, the totalMass information is used.'

        totalMass: Optional[float | LinkPath] = None 
        'Specify the total mass resulting from all particles. If unspecified or wrongly set, the default value is used: totalMass = 1.0'

        computeMassOnRest: Optional[bool | LinkPath] = None 
        'If true, the mass of every element is computed based on the rest position rather than the position'

        showGravityCenter: Optional[bool | LinkPath] = None 
        'Display the center of gravity of the system'

        showAxisSizeFactor: Optional[float | LinkPath] = None 
        'Factor length of the axis displayed (only used for rigids)'

        filename: Optional[str | LinkPath] = None 
        'Xsp3.0 file to specify the mass parameters'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return DiagonalMass.Parameters()
