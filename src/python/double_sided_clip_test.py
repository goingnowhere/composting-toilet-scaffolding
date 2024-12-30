# This FreeCAD macro script makes double sided clip objects
# for advanced positioning and rotation testing as well as to
# indicate how these fittings can be used to fix boards to scafolding.

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Arch

from parameters import *
from fittings import Double_Sided_Clip, make_pole

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
swivel_distance = panel_sides + pole_diameter
x_short_distance = swivel_distance / 3
x_long_distance = 2 * swivel_distance / 3
y_short_distance = swivel_distance / 3
y_long_distance = 2 * swivel_distance / 3
centre_1 = App.Vector(x_short_distance, 0 ,0)
centre_2 = App.Vector(x_long_distance, 0, 0)
centre_3 = App.Vector(0, y_short_distance , 0)
centre_4 = App.Vector(0, y_long_distance , 0)
centre_5 = App.Vector(swivel_distance, y_short_distance, 0)
centre_6 = App.Vector(swivel_distance, y_long_distance, 0)
centre_7 = App.Vector(x_short_distance, swivel_distance , 0)
centre_8 = App.Vector(x_long_distance, swivel_distance, 0)
double_sided_clip_1 = Double_Sided_Clip(freecad_document = document,
                    fitting_label = "Double_Sided_Clip_1",
                    centre = centre_1,
                    rotation = App.Rotation(90, 0, 90))
double_sided_clip_2 = Double_Sided_Clip(freecad_document = document,
                    fitting_label = "Double_Sided_Clip_2",
                    centre = centre_2,
                    rotation = App.Rotation(90, 0, 90))
double_sided_clip_3 = Double_Sided_Clip(freecad_document = document,
                    fitting_label = "Double_Sided_Clip_3",
                    centre = centre_3,
                    rotation = App.Rotation(0, 0, 90))
double_sided_clip_4 = Double_Sided_Clip(freecad_document = document,
                    fitting_label = "Double_Sided_Clip_4",
                    centre = centre_4,
                    rotation = App.Rotation(0, 0, 90))
double_sided_clip_5 = Double_Sided_Clip(freecad_document = document,
                    fitting_label = "Double_Sided_Clip_5",
                    centre = centre_5,
                    rotation = App.Rotation(0, 180, 90))
double_sided_clip_6 = Double_Sided_Clip(freecad_document = document,
                    fitting_label = "Double_Sided_Clip_6",
                    centre = centre_6,
                    rotation = App.Rotation(0, 180, 90))
double_sided_clip_7 = Double_Sided_Clip(freecad_document = document,
                    fitting_label = "Double_Sided_Clip_7",
                    centre = centre_7,
                    rotation = App.Rotation(270, 0, 270))
double_sided_clip_8 = Double_Sided_Clip(freecad_document = document,
                    fitting_label = "Double_Sided_Clip_8",
                    centre = centre_8,
                    rotation = App.Rotation(270, 0, 270))

# Offsets for double fixing pad
offset = Double_Sided_Clip.length / 2
# Make Connection poles.
line_1_2 = Draft.make_line(
    centre_1 + App.Vector(-offset, 0, 0),
    centre_2 + App.Vector(offset, 0, 0))
make_pole(line_1_2, "Pole_1_2")
line_3_4 = Draft.make_line(
    centre_3 + App.Vector(0, -offset, 0),
    centre_4 + App.Vector(0, offset, 0))
make_pole(line_3_4, "Pole_3_4")
line_5_6 = Draft.make_line(
    centre_5 + App.Vector(0, -offset, 0),
    centre_6 + App.Vector(0, offset, 0))
make_pole(line_5_6, "Pole_5_6")
line_7_8 = Draft.make_line(
    centre_7 + App.Vector(-offset, 0, 0),
    centre_8 + App.Vector(offset, 0, 0))
make_pole(line_7_8, "Pole_7_8")

# Add Panel
pole_radius = pole_diameter/2
rect = Draft.makeRectangle(panel_sides, panel_sides)
panel = Arch.makePanel(rect, thickness = side_panel_board_thickness)
Draft.move(panel, App.Vector(pole_radius, pole_radius, - side_panel_board_thickness / 2))