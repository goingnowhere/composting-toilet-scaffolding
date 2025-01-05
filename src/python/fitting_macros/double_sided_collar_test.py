# This FreeCAD macro script makes a double fixing pad objects
# for advanced positioning and rotation testing as well as to
# indicate how these fittings can be used to fix boards to scafolding.

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Arch

from parameters import *
from fittings import Double_Sided_Collar, make_pole

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a a set of double fixing pad objects rotated in all directions
# connected by scaffolding poles and a panel
panel_sides = 600
second_row_height = panel_sides - Double_Sided_Collar.length
centre_1 = App.Vector(0, 0 ,0)
centre_2 = App.Vector(0, panel_sides, 0)
centre_3 = App.Vector(panel_sides, panel_sides , 0)
centre_4 = App.Vector(0, 0 , second_row_height)
centre_5 = App.Vector(0, panel_sides, second_row_height)
centre_6 = App.Vector(panel_sides, panel_sides, second_row_height)
double_side_collar_1 = Double_Sided_Collar(freecad_document = document,
                    fitting_label = "Double_Sided_Collar_1",
                    centre = centre_1,
                    rotation = App.Rotation(90, 0, 0))
double_side_collar_2 = Double_Sided_Collar(freecad_document = document,
                    fitting_label = "Double_Sided_Collar_2",
                    centre = centre_2,
                    rotation = App.Rotation(0, 0, 0))
double_side_collar_3 = Double_Sided_Collar(freecad_document = document,
                    fitting_label = "Double_Sided_Collar_3",
                    centre = centre_3,
                    rotation = App.Rotation(270, 0, 0))
double_side_collar_4 = Double_Sided_Collar(freecad_document = document,
                    fitting_label = "Double_Sided_Collar_4",
                    centre = centre_4,
                    rotation = App.Rotation(90, 0, 0))
double_side_collar_5 = Double_Sided_Collar(freecad_document = document,
                    fitting_label = "Double_Sided_Collar_5",
                    centre = centre_5,
                    rotation = App.Rotation(0, 0, 0))
double_side_collar_6 = Double_Sided_Collar(freecad_document = document,
                    fitting_label = "Double_Sided_Collar_6",
                    centre = centre_6,
                    rotation = App.Rotation(270, 0, 0))


# Offsets for double fixing pad
offset = Double_Sided_Collar.length
# Make Connection poles.
line_1_4 = Draft.make_line(
    centre_1 + App.Vector(0, 0, 0),
    centre_4 + App.Vector(0, 0, offset))
make_pole(line_1_4, "Pole_1_4")
line_2_5 = Draft.make_line(
    centre_2 + App.Vector(0, 0, 0),
    centre_5 + App.Vector(0, 0, offset))
make_pole(line_2_5, "Pole_2_5")
line_3_6 = Draft.make_line(
    centre_3 + App.Vector(0, 0, 0),
    centre_6 + App.Vector(0, 0, offset))
make_pole(line_3_6, "Pole_3_6")


# Add Panels
panel_thickness = 12
x_panel_offset = pole_diameter / 2 
rect_1 = Draft.makeRectangle(panel_sides, panel_sides)
panel_1 = Arch.makePanel(rect_1, thickness = panel_thickness)
panel_1.Placement = App.Placement(
        App.Vector(0, 0, 0),
        App.Rotation(0, 270, 0),
        App.Vector(0, 0, 0))
Draft.move(panel_1, App.Vector(-x_panel_offset, 0, 0))
rect_2 = Draft.makeRectangle(panel_sides, panel_sides)
panel_2 = Arch.makePanel(rect_2, thickness = panel_thickness)
panel_2.Placement = App.Placement(
        App.Vector(0, 0, 0),
        App.Rotation(0, 0, 90),
        App.Vector(0, 0, 0))
y_panel_offset = pole_diameter / 2 + panel_sides + panel_thickness
Draft.move(panel_2, App.Vector(0, y_panel_offset, 0))
