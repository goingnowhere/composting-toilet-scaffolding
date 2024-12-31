# This FreeCAD macro script makes Cabin Floor objects
# for advanced positioning and rotation testing as well as to
# indicate how these panels can be connected together to.

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD as App
import FreeCADGui as Gui

from parameters import *
from structures import Cabin_Ground
from structures import Cabin_Floor
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

# Make Cabin Grounds
cabin_ground_1 = Cabin_Ground(freecad_document = document, 
                          structure_label = "Cabin_Ground_1")
cabin_ground_2 = Cabin_Ground(freecad_document = document, 
                          structure_label = "Cabin_Ground_2",
                          centre =  App.Vector(side_panel_seperation_x, 0, 0))
# Make Cabin Floors
cabin_floor_1 = Cabin_Floor(freecad_document = document, 
                          structure_label = "Cabin_Floor_1")
cabin_floor_2 = Cabin_Floor(freecad_document = document, 
                          structure_label = "Cabin_Floor_2",
                          centre =  App.Vector(side_panel_seperation_x, 0, 0))





