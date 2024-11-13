# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component RuleBasedContactManager

.. autofunction:: RuleBasedContactManager

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class RuleBasedContactManager(Object):
    """Create different response to the collisions based on a set of rules"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,response: Optional[object] = None,responseParams: Optional[str] = None,variables: Optional[str] = None,rules: Optional[SofaArray] = None):
        """Create different response to the collisions based on a set of rules
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           printLog (bool):   if true, emits extra messages at runtime.
           response (object):   contact response class
           responseParams (str):   contact response parameters (syntax: name1=value1&name2=value2&...)
           rules (SofaArray):   Ordered list of rules, each with a triplet of strings.
The first two define either the name of the collision model, its group number, or * meaning any model.
The last string define the response algorithm to use for contacts matched by this rule.
Rules are applied in the order they are specified. If none match a given contact, the default response is used.

           tags (object):   list of the subsets the objet belongs to
           variables (str):   Define a list of variables to be used inside the rules
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

    response: Data[object] 
    'contact response class'

    responseParams: Data[str] 
    'contact response parameters (syntax: name1=value1&name2=value2&...)'

    variables: Data[str] 
    'Define a list of variables to be used inside the rules'

    rules: Data[SofaArray] 
    'Ordered list of rules, each with a triplet of strings.The first two define either the name of the collision model, its group number, or * meaning any model.The last string define the response algorithm to use for contacts matched by this rule.Rules are applied in the order they are specified. If none match a given contact, the default response is used.'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the RuleBasedContactManager component"""

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

        response: Optional[object | LinkPath] = None 
        'contact response class'

        responseParams: Optional[str | LinkPath] = None 
        'contact response parameters (syntax: name1=value1&name2=value2&...)'

        variables: Optional[str | LinkPath] = None 
        'Define a list of variables to be used inside the rules'

        rules: Optional[SofaArray | LinkPath] = None 
        'Ordered list of rules, each with a triplet of strings.The first two define either the name of the collision model, its group number, or * meaning any model.The last string define the response algorithm to use for contacts matched by this rule.Rules are applied in the order they are specified. If none match a given contact, the default response is used.'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return RuleBasedContactManager.Parameters()
