# This FreeCAD macro script makes side panel objects
# for advanced positioning and rotation testing as well as to
# indicate how these panels can be connected together to.

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD as App
import FreeCADGui as Gui

from parameters import *
from fittings import make_pole, display_variable
from structures import *

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# # Make 3 side panels a board length apart.
side_panel_1 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_1")
side_panel_2 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_2",
                          centre = App.Vector(side_panel_seperation_x, 0, 0))
side_panel_3 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_3",
                          centre =  App.Vector(2 * side_panel_seperation_x, 0, 0))

# Make Urinal Floor
urinal_floor = Urinal_Floor(freecad_document = document, 
                          structure_label = "Urinal_Floor")

# Make Urinal Back
urinal_back = Urinal_Back(freecad_document = document, 
                          structure_label = "Urinal_Back")

# Make Cabin Ground
cabin_ground = Cabin_Ground(freecad_document = document, 
                          structure_label = "Cabin_Ground",
                          centre =  App.Vector(side_panel_seperation_x, 0, 0))
# Make Cabin Floor
cabin_floor = Cabin_Floor(freecad_document = document, 
                          structure_label = "Cabin_Floor",
                          centre =  App.Vector(side_panel_seperation_x, 0, 0))
# Make Cabin Back
cabin_back = Cabin_Back(freecad_document = document, 
                          structure_label = "Cabin_Back",
                          centre =  App.Vector(side_panel_seperation_x, 0, 0))

# Make Cabin Partitions
cabin_partition = Cabin_Partition(freecad_document = document, 
                          structure_label = "Cabin_Partition",
                          centre =  App.Vector(side_panel_seperation_x + left_third_x, 
                                                0,
                                                0))
cabin_partition = Cabin_Partition(freecad_document = document, 
                          structure_label = "Cabin_Partition",
                          centre =  App.Vector(side_panel_seperation_x + right_third_x, 
                                                0,
                                                0))