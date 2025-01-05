# This FreeCAD macro script makes tests all structures developed
# for correct combination with other strucvtures as well as 
# change of centre.

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
                          location = App.Vector(side_panel_seperation_x, 0, 0))
side_panel_3 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_3",
                          location =  App.Vector(2 * side_panel_seperation_x, 0, 0))
side_panel_4 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_4",
                          location =  App.Vector(3 * side_panel_seperation_x, 0, 0))



# Make Left Cabin
cabin_ground = Cabin_Ground(freecad_document = document, 
                          structure_label = "Cabin_Ground")
cabin_floor = Cabin_Floor(freecad_document = document, 
                          structure_label = "Cabin_Floor")
cabin_back = Cabin_Back(freecad_document = document, 
                          structure_label = "Cabin_Back")
cabin_partition = Cabin_Partition(freecad_document = document, 
                          structure_label = "Cabin_Partition",
                          location =  App.Vector(left_third_x, 
                                                0,
                                                0))
cabin_partition = Cabin_Partition(freecad_document = document, 
                          structure_label = "Cabin_Partition",
                          location =  App.Vector(right_third_x, 
                                                0,
                                                0))

# Make Middle Urinal
urinal_floor = Urinal_Floor(freecad_document = document, 
                          structure_label = "Urinal_Floor",
                          location =  App.Vector(side_panel_seperation_x, 0, 0))
urinal_back = Urinal_Back(freecad_document = document, 
                          structure_label = "Urinal_Back",
                          location =  App.Vector(side_panel_seperation_x, 0, 0))

# Make Right Cabin
cabin_ground = Cabin_Ground(freecad_document = document, 
                          structure_label = "Cabin_Ground",
                          location =  App.Vector(side_panel_seperation_x * 2, 0, 0))
cabin_floor = Cabin_Floor(freecad_document = document, 
                          structure_label = "Cabin_Floor",
                          location =  App.Vector(side_panel_seperation_x * 2, 0, 0))
cabin_back = Cabin_Back(freecad_document = document, 
                          structure_label = "Cabin_Back",
                          location =  App.Vector(side_panel_seperation_x * 2, 0, 0))
cabin_partition = Cabin_Partition(freecad_document = document, 
                          structure_label = "Cabin_Partition",
                          location =  App.Vector(side_panel_seperation_x * 2 + left_third_x, 
                                                0,
                                                0))
cabin_partition = Cabin_Partition(freecad_document = document, 
                          structure_label = "Cabin_Partition",
                          location =  App.Vector(side_panel_seperation_x * 2 + right_third_x, 
                                                0,
                                                0))