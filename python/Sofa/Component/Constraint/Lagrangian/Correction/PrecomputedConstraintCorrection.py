# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component PrecomputedConstraintCorrection

.. autofunction:: PrecomputedConstraintCorrection

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class PrecomputedConstraintCorrection(Object):
    """Component computing constraint forces within a simulated body using the compliance method."""

    def __init__(self, template: Optional[str] = None, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,rotations: Optional[bool] = None,restDeformations: Optional[bool] = None,recompute: Optional[bool] = None,debugViewFrameScale: Optional[float] = None,fileCompliance: Optional[str] = None,fileDir: Optional[str] = None):
        """Component computing constraint forces within a simulated body using the compliance method.
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           debugViewFrameScale (float):   Scale on computed node's frame
           fileCompliance (str):   Precomputed compliance matrix data file
           fileDir (str):   If not empty, the compliance will be saved in this repertory
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           recompute (bool):   if true, always recompute the compliance
           restDeformations (bool):   
           rotations (bool):   
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

    rotations: Data[bool] 
    ''

    restDeformations: Data[bool] 
    ''

    recompute: Data[bool] 
    'if true, always recompute the compliance'

    debugViewFrameScale: Data[float] 
    'Scale on computed nodes frame'

    fileCompliance: Data[str] 
    'Precomputed compliance matrix data file'

    fileDir: Data[str] 
    'If not empty, the compliance will be saved in this repertory'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the PrecomputedConstraintCorrection component"""

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

        rotations: Optional[bool | LinkPath] = None 
        ''

        restDeformations: Optional[bool | LinkPath] = None 
        ''

        recompute: Optional[bool | LinkPath] = None 
        'if true, always recompute the compliance'

        debugViewFrameScale: Optional[float | LinkPath] = None 
        'Scale on computed nodes frame'

        fileCompliance: Optional[str | LinkPath] = None 
        'Precomputed compliance matrix data file'

        fileDir: Optional[str | LinkPath] = None 
        'If not empty, the compliance will be saved in this repertory'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return PrecomputedConstraintCorrection.Parameters()
