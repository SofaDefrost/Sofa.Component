# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component JointSpringForceField

.. autofunction:: JointSpringForceField

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class JointSpringForceField(Object):
    """Springs for Rigids"""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,isCompliance: Optional[bool] = None,rayleighStiffness: Optional[float] = None,outfile: Optional[str] = None,infile: Optional[str] = None,period: Optional[float] = None,reinit: Optional[bool] = None,spring: Optional[SofaArray] = None,showLawfulTorsion: Optional[bool] = None,showExtraTorsion: Optional[bool] = None,showFactorSize: Optional[float] = None):
        """Springs for Rigids
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           infile (str):   input file containing constant joint force
           isCompliance (bool):   Consider the component as a compliance, else as a stiffness
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           outfile (str):   output file name
           period (float):   period between outputs
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighStiffness (float):   Rayleigh damping - stiffness matrix coefficient
           reinit (bool):   flag enabling reinitialization of the output file at each timestep
           showExtraTorsion (bool):   display the illicit part of the joint rotation
           showFactorSize (float):   modify the size of the debug information of a given factor
           showLawfulTorsion (bool):   display the lawful part of the joint rotation
           spring (SofaArray):   pairs of indices, stiffness, damping, rest length
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

    isCompliance: Data[bool] 
    'Consider the component as a compliance, else as a stiffness'

    rayleighStiffness: Data[float] 
    'Rayleigh damping - stiffness matrix coefficient'

    outfile: Data[str] 
    'output file name'

    infile: Data[str] 
    'input file containing constant joint force'

    period: Data[float] 
    'period between outputs'

    reinit: Data[bool] 
    'flag enabling reinitialization of the output file at each timestep'

    spring: Data[SofaArray] 
    'pairs of indices, stiffness, damping, rest length'

    showLawfulTorsion: Data[bool] 
    'display the lawful part of the joint rotation'

    showExtraTorsion: Data[bool] 
    'display the illicit part of the joint rotation'

    showFactorSize: Data[float] 
    'modify the size of the debug information of a given factor'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the JointSpringForceField component"""

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

        outfile: Optional[str | LinkPath] = None 
        'output file name'

        infile: Optional[str | LinkPath] = None 
        'input file containing constant joint force'

        period: Optional[float | LinkPath] = None 
        'period between outputs'

        reinit: Optional[bool | LinkPath] = None 
        'flag enabling reinitialization of the output file at each timestep'

        spring: Optional[SofaArray | LinkPath] = None 
        'pairs of indices, stiffness, damping, rest length'

        showLawfulTorsion: Optional[bool | LinkPath] = None 
        'display the lawful part of the joint rotation'

        showExtraTorsion: Optional[bool | LinkPath] = None 
        'display the illicit part of the joint rotation'

        showFactorSize: Optional[float | LinkPath] = None 
        'modify the size of the debug information of a given factor'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return JointSpringForceField.Parameters()
