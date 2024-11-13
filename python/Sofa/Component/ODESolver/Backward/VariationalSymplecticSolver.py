# -*- coding: utf-8 -*-


import Sofa
from Sofa.Core import Object, LinkPath
from Sofa.Component.TypeHints import Data, Optional, SofaArray
import dataclasses
"""
Component VariationalSymplecticSolver

.. autofunction:: VariationalSymplecticSolver

Indices and tables
******************

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""
    
class VariationalSymplecticSolver(Object):
    """Implicit time integrator which conserves linear momentum and mechanical energy"""

    def __init__(self, name: Optional[str] = None,printLog: Optional[bool] = None,tags: Optional[object] = None,bbox: Optional[object] = None,componentState: Optional[object] = None,listening: Optional[bool] = None,newtonError: Optional[float] = None,steps: Optional[int] = None,rayleighStiffness: Optional[float] = None,rayleighMass: Optional[float] = None,saveEnergyInFile: Optional[bool] = None,explicitIntegration: Optional[bool] = None,file: Optional[str] = None,computeHamiltonian: Optional[bool] = None,hamiltonianEnergy: Optional[float] = None,useIncrementalPotentialEnergy: Optional[bool] = None,threadSafeVisitor: Optional[bool] = None):
        """Implicit time integrator which conserves linear momentum and mechanical energy
        
        Args:
           bbox (object):   this object bounding box
           componentState (object):   The state of the component among (Dirty, Valid, Undefined, Loading, Invalid).
           computeHamiltonian (bool):   Compute hamiltonian
           explicitIntegration (bool):   Use explicit integration scheme
           file (str):   File name where kinetic and potential energies are saved in a CSV file
           hamiltonianEnergy (float):   hamiltonian energy
           listening (bool):   if true, handle the events, otherwise ignore the events
           name (str):   object name
           newtonError (float):   Error tolerance for Newton iterations
           printLog (bool):   if true, emits extra messages at runtime.
           rayleighMass (float):   Rayleigh damping coefficient related to mass, > 0
           rayleighStiffness (float):   Rayleigh damping coefficient related to stiffness, > 0
           saveEnergyInFile (bool):   If kinetic and potential energies should be dumped in a CSV file at each iteration
           steps (int):   Maximum number of Newton steps
           tags (object):   list of the subsets the objet belongs to
           threadSafeVisitor (bool):   If true, do not use realloc and free visitors in fwdInteractionForceField.
           useIncrementalPotentialEnergy (bool):   use real potential energy, if false use approximate potential energy
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

    newtonError: Data[float] 
    'Error tolerance for Newton iterations'

    steps: Data[int] 
    'Maximum number of Newton steps'

    rayleighStiffness: Data[float] 
    'Rayleigh damping coefficient related to stiffness, > 0'

    rayleighMass: Data[float] 
    'Rayleigh damping coefficient related to mass, > 0'

    saveEnergyInFile: Data[bool] 
    'If kinetic and potential energies should be dumped in a CSV file at each iteration'

    explicitIntegration: Data[bool] 
    'Use explicit integration scheme'

    file: Data[str] 
    'File name where kinetic and potential energies are saved in a CSV file'

    computeHamiltonian: Data[bool] 
    'Compute hamiltonian'

    hamiltonianEnergy: Data[float] 
    'hamiltonian energy'

    useIncrementalPotentialEnergy: Data[bool] 
    'use real potential energy, if false use approximate potential energy'

    threadSafeVisitor: Data[bool] 
    'If true, do not use realloc and free visitors in fwdInteractionForceField.'



    @dataclasses.dataclass
    class Parameters:
        """Parameter for the construction of the VariationalSymplecticSolver component"""

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

        newtonError: Optional[float | LinkPath] = None 
        'Error tolerance for Newton iterations'

        steps: Optional[int | LinkPath] = None 
        'Maximum number of Newton steps'

        rayleighStiffness: Optional[float | LinkPath] = None 
        'Rayleigh damping coefficient related to stiffness, > 0'

        rayleighMass: Optional[float | LinkPath] = None 
        'Rayleigh damping coefficient related to mass, > 0'

        saveEnergyInFile: Optional[bool | LinkPath] = None 
        'If kinetic and potential energies should be dumped in a CSV file at each iteration'

        explicitIntegration: Optional[bool | LinkPath] = None 
        'Use explicit integration scheme'

        file: Optional[str | LinkPath] = None 
        'File name where kinetic and potential energies are saved in a CSV file'

        computeHamiltonian: Optional[bool | LinkPath] = None 
        'Compute hamiltonian'

        hamiltonianEnergy: Optional[float | LinkPath] = None 
        'hamiltonian energy'

        useIncrementalPotentialEnergy: Optional[bool | LinkPath] = None 
        'use real potential energy, if false use approximate potential energy'

        threadSafeVisitor: Optional[bool | LinkPath] = None 
        'If true, do not use realloc and free visitors in fwdInteractionForceField.'

 

        def to_dict(self): 
            return dataclasses.asdict(self)

    @staticmethod
    def new_parameters() -> Parameters: 
        return VariationalSymplecticSolver.Parameters()
