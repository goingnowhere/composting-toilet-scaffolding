# This FreeCAD macro script makes Urinal Back objects
# for advanced positioning and rotation testing as well as to
# indicate how these panels can be connected together to.

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD as App
import FreeCADGui as Gui

from parameters import *
from structures import Urinal_Back
from structures import Urinal_Floor
from structures import Side_Panel

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Make 3 side panels a board length apart.
side_panel_1 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_1")
side_panel_2 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_2",
                          centre = App.Vector(side_panel_seperation_x, 0, 0))
side_panel_3 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_3",
                          centre =  App.Vector(2 * side_panel_seperation_x, 0, 0))

# Make Urinal Floors
urinal_floor_1 = Urinal_Floor(freecad_document = document, 
                          structure_label = "Urinal_Floor_1")
urinal_floor_2 = Urinal_Floor(freecad_document = document, 
                          structure_label = "Urinal_Floor_2",
                          centre =  App.Vector(side_panel_seperation_x, 0, 0))
# Make Urinal Backs
urinal_back_1 = Urinal_Back(freecad_document = document, 
                          structure_label = "Urinal_Back_1")
urinal_back_2 = Urinal_Back(freecad_document = document, 
                          structure_label = "Urinal_Back_2",
                          centre =  App.Vector(side_panel_seperation_x, 0, 0))





