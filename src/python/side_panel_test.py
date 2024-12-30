# This FreeCAD macro script makes side panel objects
# for advanced positioning and rotation testing as well as to
# indicate how these panels can be connected together to.

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Arch

from parameters import *
from fittings import make_pole, display_variable
from side_panel import Side_Panel

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# # Make 3 side panels a board length apart.
x_distance_apart = board_length + side_panel_board_thickness
side_panel_1 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_1")
side_panel_2 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_2",
                          centre = App.Vector(x_distance_apart, 0, 0))
side_panel_3 = Side_Panel(freecad_document = document, 
                          structure_label = "Side_Panel_3",
                          centre =  App.Vector(2 * x_distance_apart, 0, 0))

# #Test line
# line = Draft.make_line(
#     side_panel_1.roof_front_right,
#     App.Vector(2000, 0, 2984.0))
# make_pole(line, "Pole")


# display_variable("side_panel_2.roof_front_right", side_panel_2.roof_front_left)


# Make Urinal Connection Poles between Panel 1 and 2
# urinal_roof_front_line = Draft.make_line(
#     side_panel_1.roof_front_right,
#     side_panel_2.roof_front_left)
# make_pole(urinal_roof_front_line, "Urinal_Roof_Front_Pole")
# urinal_roof_back_line = Draft.make_line(
#     side_panel_1.roof_back_right,
#     side_panel_2.roof_back_left)
# make_pole(urinal_roof_back_line, "Urinal_Roof_Back_Pole")


# line_2_5 = Draft.make_line(
#     centre_2 + App.Vector(0, 0, 0),
#     centre_5 + App.Vector(0, 0, offset))
# make_pole(line_2_5, "Pole_2_5")
# line_3_6 = Draft.make_line(
#     centre_3 + App.Vector(0, 0, 0),
#     centre_6 + App.Vector(0, 0, offset))
# make_pole(line_3_6, "Pole_3_6")


# Add Panels
# panel_thickness = 12
# x_panel_offset = pole_diameter / 2 
# rect_1 = Draft.makeRectangle(panel_sides, panel_sides)
# panel_1 = Arch.makePanel(rect_1, thickness = panel_thickness)
# panel_1.Placement = App.Placement(
#         App.Vector(0, 0, 0),
#         App.Rotation(0, 270, 0),
#         App.Vector(0, 0, 0))
# Draft.move(panel_1, App.Vector(-x_panel_offset, 0, 0))
# rect_2 = Draft.makeRectangle(panel_sides, panel_sides)
# panel_2 = Arch.makePanel(rect_2, thickness = panel_thickness)
# panel_2.Placement = App.Placement(
#         App.Vector(0, 0, 0),
#         App.Rotation(0, 0, 90),
#         App.Vector(0, 0, 0))
# y_panel_offset = pole_diameter / 2 + panel_sides + panel_thickness
# Draft.move(panel_2, App.Vector(0, y_panel_offset, 0))
